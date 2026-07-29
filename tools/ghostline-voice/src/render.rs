//! Deterministic manifest-driven audition rendering.

use std::collections::{BTreeMap, BTreeSet};
use std::fs;
use std::path::{Path, PathBuf};

use dinoml_qwen3_tts::assets::GenerationRecord;
use dinoml_qwen3_tts::{
    GenerationSamplingConfig, SpeakerEmbedding, generation_record_path, sha256_file,
    write_generation_record,
};
use serde::{Deserialize, Serialize};

use crate::backend::{SynthesisRequest, VoiceBackend};
use crate::embedding::load_embedding;
use crate::manifest::{SpokenLine, VoicePlan, fnv1a64};
use crate::{Error, Result};

/// Rendering controls shared by local and HTTP backends.
#[derive(Debug, Clone)]
pub struct RenderOptions {
    /// Candidate output root.
    pub output_root: PathBuf,
    /// Optional dialogue IDs to render; empty selects all dialogues.
    pub dialogues: BTreeSet<String>,
    /// Explicit speaker-to-embedding overrides.
    pub speaker_embeddings: BTreeMap<String, PathBuf>,
    /// Candidates generated per line.
    pub versions: u32,
    /// Stable seed namespace.
    pub seed_base: u64,
    /// Prompt language.
    pub language: String,
    /// Maximum codec frames per candidate.
    pub max_frames: usize,
    /// Sampling configuration.
    pub sampling: GenerationSamplingConfig,
    /// Replace invalid or stale existing candidates.
    pub force: bool,
}

/// Complete deterministic render report.
#[derive(Debug, Clone, Deserialize, Serialize)]
#[serde(deny_unknown_fields)]
pub struct RenderReport {
    /// Report schema version.
    pub schema_version: u32,
    /// Quest identifier.
    pub quest: String,
    /// Candidate results in manifest order.
    pub candidates: Vec<CandidateReport>,
}

/// One generated or reused audition candidate.
#[derive(Debug, Clone, Deserialize, Serialize)]
#[serde(deny_unknown_fields)]
pub struct CandidateReport {
    /// Dialogue manifest ID.
    pub dialogue: String,
    /// Spoken-line key.
    pub line_key: String,
    /// Speaker name.
    pub speaker: String,
    /// Zero-based candidate version.
    pub version: u32,
    /// Deterministic seed.
    pub seed: u64,
    /// Generated WAV path relative to the output root.
    pub wav: String,
    /// Lowercase SHA-256 digest.
    pub sha256: String,
    /// Whether a valid existing candidate was reused.
    pub reused: bool,
}

/// Renders every selected manifest line through one persistent backend.
///
/// # Errors
///
/// Returns an error for invalid options, unresolved speakers, stale existing
/// outputs, synthesis failure, or report publication failure.
pub fn render_plan(
    plan: &VoicePlan,
    backend: &mut impl VoiceBackend,
    options: &RenderOptions,
) -> Result<RenderReport> {
    if options.versions == 0 {
        return Err(Error::manifest("candidate version count must be positive"));
    }
    if options.max_frames == 0 {
        return Err(Error::manifest("maximum frame count must be positive"));
    }
    let selected = selected_dialogues(plan, &options.dialogues)?;
    let embeddings = resolve_embeddings(plan, &selected, &options.speaker_embeddings)?;
    fs::create_dir_all(&options.output_root)
        .map_err(|source| Error::io(&options.output_root, source))?;
    let mut candidates = Vec::new();

    for dialogue in selected {
        let dialogue_root = options.output_root.join(&dialogue.index.id);
        fs::create_dir_all(&dialogue_root).map_err(|source| Error::io(&dialogue_root, source))?;
        for line in &dialogue.manifest.spoken_lines {
            let embedding = embeddings.get(&line.speaker).ok_or_else(|| {
                Error::manifest(format!(
                    "speaker {:?} has no loaded embedding",
                    line.speaker
                ))
            })?;
            for version in 0..options.versions {
                candidates.push(render_candidate(
                    backend,
                    options,
                    &dialogue.index.id,
                    line,
                    embedding,
                    version,
                    &dialogue_root,
                )?);
            }
        }
    }

    let report = RenderReport {
        schema_version: 1,
        quest: plan.production.quest.clone(),
        candidates,
    };
    let report_path = options.output_root.join("render-report.json");
    write_json(&report_path, &report)?;
    Ok(report)
}

fn render_candidate(
    backend: &mut impl VoiceBackend,
    options: &RenderOptions,
    dialogue: &str,
    line: &SpokenLine,
    embedding: &SpeakerEmbedding,
    version: u32,
    dialogue_root: &Path,
) -> Result<CandidateReport> {
    let seed = options
        .seed_base
        .wrapping_add(fnv1a64(&line.key))
        .wrapping_add(u64::from(version));
    let filename = format!("{}-version{version:02}.wav", line.key);
    let output = dialogue_root.join(&filename);
    if output.exists() {
        if let Some(hash) = reusable_output(&output, seed)? {
            return Ok(candidate_report(
                options, dialogue, line, version, seed, &output, hash, true,
            ));
        }
        if !options.force {
            return Err(Error::manifest(format!(
                "{} exists without a matching reproducibility record; pass --force to replace it",
                output.display()
            )));
        }
    }

    let generated = backend.synthesize(SynthesisRequest {
        text: &line.text,
        language: &options.language,
        speaker: embedding,
        max_frames: options.max_frames,
        seed,
        sampling: options.sampling,
    })?;
    let temporary = output.with_extension("wav.partial");
    fs::write(&temporary, generated.wav).map_err(|source| Error::io(&temporary, source))?;
    if output.exists() {
        fs::remove_file(&output).map_err(|source| Error::io(&output, source))?;
    }
    fs::rename(&temporary, &output).map_err(|source| Error::io(&output, source))?;
    let publication = write_generation_record(&output, seed)?;
    Ok(candidate_report(
        options,
        dialogue,
        line,
        version,
        seed,
        &output,
        publication.output_sha256().to_owned(),
        false,
    ))
}

#[expect(
    clippy::too_many_arguments,
    reason = "candidate identity and publication details are intentionally explicit"
)]
fn candidate_report(
    options: &RenderOptions,
    dialogue: &str,
    line: &SpokenLine,
    version: u32,
    seed: u64,
    output: &Path,
    sha256: String,
    reused: bool,
) -> CandidateReport {
    let relative = output
        .strip_prefix(&options.output_root)
        .unwrap_or(output)
        .to_string_lossy()
        .replace('\\', "/");
    CandidateReport {
        dialogue: dialogue.to_owned(),
        line_key: line.key.clone(),
        speaker: line.speaker.clone(),
        version,
        seed,
        wav: relative,
        sha256,
        reused,
    }
}

fn reusable_output(path: &Path, seed: u64) -> Result<Option<String>> {
    let record_path = generation_record_path(path);
    if !record_path.is_file() {
        return Ok(None);
    }
    let bytes = fs::read(&record_path).map_err(|source| Error::io(&record_path, source))?;
    let record: GenerationRecord =
        serde_json::from_slice(&bytes).map_err(|source| Error::json(&record_path, source))?;
    if record.seed != seed {
        return Ok(None);
    }
    let filename = path.file_name().and_then(|value| value.to_str());
    if filename != Some(record.output_file.as_str()) {
        return Ok(None);
    }
    let actual = sha256_file(path)?;
    if actual != record.output_sha256 {
        return Ok(None);
    }
    Ok(Some(actual))
}

fn selected_dialogues<'a>(
    plan: &'a VoicePlan,
    requested: &BTreeSet<String>,
) -> Result<Vec<&'a crate::manifest::PlannedDialogue>> {
    if requested.is_empty() {
        return Ok(plan.dialogues.iter().collect());
    }
    for dialogue in requested {
        if plan.dialogue(dialogue).is_none() {
            return Err(Error::manifest(format!(
                "dialogue {dialogue:?} is not registered in {}",
                plan.index_path.display()
            )));
        }
    }
    Ok(plan
        .dialogues
        .iter()
        .filter(|dialogue| requested.contains(&dialogue.index.id))
        .collect())
}

fn resolve_embeddings(
    plan: &VoicePlan,
    dialogues: &[&crate::manifest::PlannedDialogue],
    overrides: &BTreeMap<String, PathBuf>,
) -> Result<BTreeMap<String, SpeakerEmbedding>> {
    let speakers = dialogues
        .iter()
        .flat_map(|dialogue| &dialogue.manifest.spoken_lines)
        .map(|line| line.speaker.as_str())
        .collect::<BTreeSet<_>>();
    let mut result = BTreeMap::new();
    for speaker in speakers {
        let path = overrides.get(speaker).cloned().or_else(|| {
            plan.production
                .voice_sources
                .get(speaker)
                .and_then(|source| source.source.as_deref())
                .filter(|source| {
                    matches!(
                        Path::new(source)
                            .extension()
                            .and_then(|value| value.to_str()),
                        Some("json" | "safetensors")
                    )
                })
                .map(|source| plan.repo_root.join(source))
        });
        let path = path.ok_or_else(|| {
            Error::manifest(format!(
                "speaker {speaker:?} needs --embedding {speaker}=PATH"
            ))
        })?;
        result.insert(speaker.to_owned(), load_embedding(path)?);
    }
    Ok(result)
}

fn write_json(path: &Path, value: &impl Serialize) -> Result<()> {
    let mut encoded =
        serde_json::to_vec_pretty(value).map_err(|source| Error::json(path, source))?;
    encoded.push(b'\n');
    fs::write(path, encoded).map_err(|source| Error::io(path, source))
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn candidate_seed_is_stable_across_subsets() {
        let key = "gq003_20_iris_intro_01";
        let first = 3_000_u64.wrapping_add(fnv1a64(key));
        let second = 3_000_u64.wrapping_add(fnv1a64(key));
        assert_eq!(first, second);
    }
}
