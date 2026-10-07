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
use serde_json::json;
use sha2::{Digest, Sha256};

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
    /// Optional speaker names to render; empty selects every speaker.
    pub speakers: BTreeSet<String>,
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
    /// Rerender selected candidates, including valid existing candidates.
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
    /// Voice-conditioning identity used to group audition takes.
    #[serde(default)]
    pub design: String,
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
    validate_speakers(&selected, &options.speakers)?;
    let embeddings = resolve_embeddings(
        plan,
        &selected,
        &options.speaker_embeddings,
        &options.speakers,
    )?;
    fs::create_dir_all(&options.output_root)
        .map_err(|source| Error::io(&options.output_root, source))?;
    let mut candidates = Vec::new();

    for dialogue in selected {
        let dialogue_root = options.output_root.join(&dialogue.index.id);
        fs::create_dir_all(&dialogue_root).map_err(|source| Error::io(&dialogue_root, source))?;
        for line in &dialogue.manifest.spoken_lines {
            if !options.speakers.is_empty() && !options.speakers.contains(&line.speaker) {
                continue;
            }
            let embedding = embeddings.get(&line.speaker).ok_or_else(|| {
                Error::manifest(format!(
                    "speaker {:?} has no loaded embedding",
                    line.speaker
                ))
            })?;
            for version in 0..options.versions {
                let mut candidate = render_candidate(
                    backend,
                    options,
                    &dialogue.index.id,
                    line,
                    embedding,
                    version,
                    &dialogue_root,
                )?;
                let bytes = serde_json::to_vec(embedding.values())
                    .map_err(|source| Error::json("speaker embedding", source))?;
                candidate.design = format!("{:x}", Sha256::digest(bytes));
                candidates.push(candidate);
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
    let fingerprint = request_fingerprint(backend.identity(), options, line, embedding, seed)?;
    if output.exists() && !options.force {
        if let Some(hash) = reusable_output(&output, seed, &fingerprint)? {
            return Ok(candidate_report(
                options, dialogue, line, version, seed, &output, hash, true,
            ));
        }
        return Err(Error::manifest(format!(
            "{} exists without a matching reproducibility record; pass --force to replace it",
            output.display()
        )));
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
    fs::rename(&temporary, &output).map_err(|source| Error::io(&output, source))?;
    let publication = write_generation_record(&output, seed)?;
    write_json(
        &request_record_path(&output),
        &json!({"schema_version": 1, "fingerprint": fingerprint}),
    )?;
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
        design: String::new(),
    }
}

fn reusable_output(path: &Path, seed: u64, fingerprint: &str) -> Result<Option<String>> {
    let request_path = request_record_path(path);
    let Ok(bytes) = fs::read(&request_path) else {
        return Ok(None);
    };
    let Ok(request) = serde_json::from_slice::<serde_json::Value>(&bytes) else {
        return Ok(None);
    };
    if request.get("schema_version") != Some(&json!(1))
        || request.get("fingerprint").and_then(|value| value.as_str()) != Some(fingerprint)
    {
        return Ok(None);
    }
    let record_path = generation_record_path(path);
    if !record_path.is_file() {
        return Ok(None);
    }
    let bytes = fs::read(&record_path).map_err(|source| Error::io(&record_path, source))?;
    let Ok(record) = serde_json::from_slice::<GenerationRecord>(&bytes) else {
        return Ok(None);
    };
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

fn request_record_path(path: &Path) -> PathBuf {
    path.with_extension("request.json")
}

fn request_fingerprint(
    backend: &str,
    options: &RenderOptions,
    line: &SpokenLine,
    embedding: &SpeakerEmbedding,
    seed: u64,
) -> Result<String> {
    let sampling = [options.sampling.outer(), options.sampling.code_predictor()].map(|value| {
        json!({
            "sample": value.do_sample(), "temperature": value.temperature(), "top_k": value.top_k(),
            "top_p": value.top_p(), "repetition_penalty": value.repetition_penalty(),
        })
    });
    let request = json!({"schema_version": 1, "backend": backend, "text": line.text,
        "speaker": line.speaker, "embedding": embedding.values(), "seed": seed,
        "language": options.language, "max_frames": options.max_frames, "sampling": sampling});
    let bytes =
        serde_json::to_vec(&request).map_err(|source| Error::json("synthesis request", source))?;
    Ok(format!("{:x}", Sha256::digest(bytes)))
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
    requested_speakers: &BTreeSet<String>,
) -> Result<BTreeMap<String, SpeakerEmbedding>> {
    let speakers = dialogues
        .iter()
        .flat_map(|dialogue| &dialogue.manifest.spoken_lines)
        .map(|line| line.speaker.as_str())
        .filter(|speaker| requested_speakers.is_empty() || requested_speakers.contains(*speaker))
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

fn validate_speakers(
    dialogues: &[&crate::manifest::PlannedDialogue],
    requested: &BTreeSet<String>,
) -> Result<()> {
    if requested.is_empty() {
        return Ok(());
    }
    let available = dialogues
        .iter()
        .flat_map(|dialogue| &dialogue.manifest.spoken_lines)
        .map(|line| line.speaker.as_str())
        .collect::<BTreeSet<_>>();
    for speaker in requested {
        if !available.contains(speaker.as_str()) {
            return Err(Error::manifest(format!(
                "speaker {speaker:?} has no lines in the selected dialogues"
            )));
        }
    }
    Ok(())
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
    use crate::backend::GeneratedAudio;
    use dinoml_qwen3_tts::{SamplingConfig, write_speaker_embedding};

    struct FakeBackend {
        calls: usize,
        identity: String,
    }
    impl VoiceBackend for FakeBackend {
        fn identity(&self) -> &str {
            &self.identity
        }
        fn synthesize(&mut self, request: SynthesisRequest<'_>) -> Result<GeneratedAudio> {
            self.calls += 1;
            Ok(GeneratedAudio {
                wav: format!("fake PCM {} {}", request.text, self.calls).into_bytes(),
            })
        }
    }

    fn fixture() -> (tempfile::TempDir, VoicePlan, RenderOptions, FakeBackend) {
        let directory = tempfile::tempdir().unwrap();
        let root = directory.path();
        let embedding = root.join("voice.json");
        write_speaker_embedding(
            &embedding,
            &SpeakerEmbedding::try_from_values(vec![0.25, -0.5]).unwrap(),
        )
        .unwrap();
        let mut entries = Vec::new();
        for dialogue in ["q_01", "q_02"] {
            let key = format!("{dialogue}_hello");
            let file = format!("{dialogue}.json");
            fs::write(root.join(&file), serde_json::to_vec(&json!({"spoken_lines": [{
                "key": key, "string_id": fnv1a64(&key).to_string(), "speaker": "Iris", "addressee": "V",
                "text": "Hello", "audio_path": format!("mod\\q\\localization\\en-us\\vo\\{key}.wem"), "duration_ms": 500,
            }]})).unwrap()).unwrap();
            entries.push(json!({"id": dialogue, "file": file, "delivery": "scene", "runtime_status": "test", "line_count": 1, "speakers": ["Iris"]}));
        }
        let index = root.join("voice-production.json");
        fs::write(&index, serde_json::to_vec(&json!({"schema_version": 1, "quest": "q", "spoken_line_count": 2,
            "manifests": entries, "voice_sources": {"Iris": {"mode": "speaker_embedding", "source": "voice.json"}}})).unwrap()).unwrap();
        let plan = VoicePlan::load(root, &index).unwrap();
        let sampling = SamplingConfig::new(true, 0.95, 50, 0.98, 1.0).unwrap();
        let options = RenderOptions {
            output_root: root.join("output"),
            dialogues: BTreeSet::new(),
            speakers: BTreeSet::new(),
            speaker_embeddings: BTreeMap::new(),
            versions: 1,
            seed_base: 3000,
            language: "English".to_owned(),
            max_frames: 24,
            sampling: GenerationSamplingConfig::new(sampling, sampling),
            force: false,
        };
        (
            directory,
            plan,
            options,
            FakeBackend {
                calls: 0,
                identity: "fake-v1".to_owned(),
            },
        )
    }

    #[test]
    fn full_and_subset_renders_keep_candidate_identity_and_reuse() {
        let (_directory, plan, mut options, mut backend) = fixture();
        let full = render_plan(&plan, &mut backend, &options).unwrap();
        options.dialogues.insert("q_02".to_owned());
        let subset = render_plan(&plan, &mut backend, &options).unwrap();
        assert_eq!(backend.calls, 2);
        assert!(subset.candidates[0].reused);
        assert_eq!(subset.candidates[0].seed, full.candidates[1].seed);
        assert_eq!(subset.candidates[0].sha256, full.candidates[1].sha256);
    }

    #[test]
    fn changed_request_requires_force_and_force_always_rerenders() {
        let (_directory, mut plan, mut options, mut backend) = fixture();
        render_plan(&plan, &mut backend, &options).unwrap();
        plan.dialogues[0].manifest.spoken_lines[0].text = "Changed".to_owned();
        assert!(render_plan(&plan, &mut backend, &options).is_err());
        options.force = true;
        render_plan(&plan, &mut backend, &options).unwrap();
        render_plan(&plan, &mut backend, &options).unwrap();
        assert_eq!(backend.calls, 6);
    }

    #[test]
    fn all_request_inputs_and_artifacts_invalidate_reuse() {
        let (_directory, plan, options, mut backend) = fixture();
        render_plan(&plan, &mut backend, &options).unwrap();
        let mut changed = options.clone();
        changed.language = "French".to_owned();
        assert!(render_plan(&plan, &mut backend, &changed).is_err());
        changed = options.clone();
        changed.max_frames += 1;
        assert!(render_plan(&plan, &mut backend, &changed).is_err());
        let sampling = SamplingConfig::new(true, 0.5, 20, 0.7, 1.1).unwrap();
        changed = options.clone();
        changed.sampling = GenerationSamplingConfig::new(sampling, sampling);
        assert!(render_plan(&plan, &mut backend, &changed).is_err());
        backend.identity = "fake-v2".to_owned();
        assert!(render_plan(&plan, &mut backend, &options).is_err());
        backend.identity = "fake-v1".to_owned();
        write_speaker_embedding(
            plan.repo_root.join("voice.json"),
            &SpeakerEmbedding::try_from_values(vec![0.2, -0.5]).unwrap(),
        )
        .unwrap();
        assert!(render_plan(&plan, &mut backend, &options).is_err());
        assert_eq!(backend.calls, 2);
    }

    #[test]
    fn corrupt_audio_and_receipts_are_recoverable_with_force() {
        let (_directory, plan, mut options, mut backend) = fixture();
        let report = render_plan(&plan, &mut backend, &options).unwrap();
        let output = options.output_root.join(&report.candidates[0].wav);
        for path in [
            &output,
            &generation_record_path(&output),
            &request_record_path(&output),
        ] {
            fs::write(path, b"corrupt").unwrap();
            options.force = false;
            assert!(render_plan(&plan, &mut backend, &options).is_err());
            options.force = true;
            render_plan(&plan, &mut backend, &options).unwrap();
        }
    }
}
