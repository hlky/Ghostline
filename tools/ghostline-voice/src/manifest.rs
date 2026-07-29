//! Typed Ghostline voice-production manifests and validation.

use std::collections::{BTreeMap, BTreeSet};
use std::fs;
use std::path::{Component, Path, PathBuf};

use serde::{Deserialize, Serialize, de::DeserializeOwned};

use crate::{Error, Result};

const MAX_LINE_DURATION_MS: u64 = 20_000;
const FNV1A64_OFFSET: u64 = 0xcbf2_9ce4_8422_2325;
const FNV1A64_PRIME: u64 = 0x0000_0100_0000_01b3;

/// Quest-level voice-production index.
#[derive(Debug, Clone, Deserialize, Serialize)]
#[serde(deny_unknown_fields)]
pub struct VoiceProduction {
    /// Index schema version.
    pub schema_version: u32,
    /// Quest identifier such as `gq003`.
    pub quest: String,
    /// Total spoken-line count across every indexed manifest.
    pub spoken_line_count: usize,
    /// Ordered dialogue-manifest inventory.
    pub manifests: Vec<DialogueIndexEntry>,
    /// Speaker conditioning sources and production status.
    pub voice_sources: BTreeMap<String, VoiceSource>,
    /// Human-readable production notes.
    #[serde(default)]
    pub notes: Vec<String>,
}

/// One dialogue manifest registered in the production index.
#[derive(Debug, Clone, Deserialize, Serialize)]
#[serde(deny_unknown_fields)]
pub struct DialogueIndexEntry {
    /// Stable dialogue identifier.
    pub id: String,
    /// Manifest filename relative to the production index.
    pub file: String,
    /// Intended runtime delivery form.
    pub delivery: String,
    /// Current runtime-integration status.
    pub runtime_status: String,
    /// Expected spoken-line count.
    pub line_count: usize,
    /// Sorted speaker names expected in the manifest.
    pub speakers: Vec<String>,
}

/// One speaker's authoring source.
#[derive(Debug, Clone, Deserialize, Serialize)]
#[serde(deny_unknown_fields)]
pub struct VoiceSource {
    /// Conditioning mode such as `speaker_embedding` or `designed_reference`.
    pub mode: String,
    /// Optional repository-relative source asset.
    pub source: Option<String>,
    /// Optional unresolved production status.
    pub status: Option<String>,
}

/// Authored dialogue manifest.
#[derive(Debug, Clone, Deserialize, Serialize)]
pub struct DialogueManifest {
    /// Optional sequence identifier used by non-scene delivery sets.
    pub sequence_id: Option<String>,
    /// Optional delivery classification.
    pub delivery: Option<String>,
    /// Optional runtime-integration status.
    pub runtime_status: Option<String>,
    /// Quest stage numbers covered by this dialogue.
    #[serde(default)]
    pub stages: Vec<u32>,
    /// Spoken lines in playback order.
    pub spoken_lines: Vec<SpokenLine>,
    /// Scene choice-label records, retained but not voiced.
    #[serde(default)]
    pub choice_lines: Vec<serde_json::Value>,
    /// Legacy scene duration lookup retained for compatibility.
    #[serde(default)]
    pub audio_durations_ms: BTreeMap<String, u64>,
}

/// One voiced dialogue line.
#[derive(Debug, Clone, Deserialize, Serialize)]
#[serde(deny_unknown_fields)]
pub struct SpokenLine {
    /// Stable authored line key.
    pub key: String,
    /// Unsigned decimal FNV-1a localization ID.
    pub string_id: String,
    /// Speaking performer.
    pub speaker: String,
    /// Intended recipient or audience.
    pub addressee: String,
    /// Spoken and subtitled text.
    pub text: String,
    /// Runtime WEM depot path.
    pub audio_path: String,
    /// Estimated or reviewed performance duration.
    pub duration_ms: u64,
    /// Optional gameplay or scene beat.
    pub beat: Option<String>,
    /// Optional quest-fact delivery condition.
    pub condition: Option<String>,
}

/// Validated dialogue plus its production-index metadata.
#[derive(Debug, Clone)]
pub struct PlannedDialogue {
    /// Production-index entry.
    pub index: DialogueIndexEntry,
    /// Parsed authored manifest.
    pub manifest: DialogueManifest,
    /// Absolute authored manifest path.
    pub path: PathBuf,
}

/// Validated quest voice plan.
#[derive(Debug, Clone)]
pub struct VoicePlan {
    /// Absolute Ghostline repository root.
    pub repo_root: PathBuf,
    /// Absolute production-index path.
    pub index_path: PathBuf,
    /// Parsed production index.
    pub production: VoiceProduction,
    /// Parsed dialogue manifests in index order.
    pub dialogues: Vec<PlannedDialogue>,
}

impl VoicePlan {
    /// Loads and validates a complete voice-production plan.
    ///
    /// # Errors
    ///
    /// Returns an error for inaccessible JSON, unsafe manifest paths, line-ID
    /// mismatches, duplicate identities, invalid WEM paths, or index drift.
    pub fn load(repo_root: impl AsRef<Path>, index_path: impl AsRef<Path>) -> Result<Self> {
        let repo_root = canonical_directory(repo_root.as_ref())?;
        let index_path = absolute_under(&repo_root, index_path.as_ref());
        let production: VoiceProduction = read_json(&index_path)?;
        if production.schema_version != 1 {
            return Err(Error::manifest(format!(
                "{} uses schema version {}; expected 1",
                index_path.display(),
                production.schema_version
            )));
        }
        if production.quest.trim().is_empty() {
            return Err(Error::manifest("production quest must not be empty"));
        }
        validate_path_atom("production quest", &production.quest)?;
        let script_dir = index_path.parent().ok_or_else(|| {
            Error::manifest(format!("{} has no parent directory", index_path.display()))
        })?;
        let mut dialogues = Vec::with_capacity(production.manifests.len());
        let mut dialogue_ids = BTreeSet::new();
        let mut keys = BTreeSet::new();
        let mut string_ids = BTreeSet::new();
        let mut audio_paths = BTreeSet::new();
        let mut total = 0_usize;

        for entry in &production.manifests {
            validate_relative_filename(&entry.file)?;
            validate_path_atom("dialogue ID", &entry.id)?;
            if !dialogue_ids.insert(entry.id.as_str()) {
                return Err(Error::manifest(format!(
                    "dialogue ID {:?} is registered more than once",
                    entry.id
                )));
            }
            let path = script_dir.join(&entry.file);
            let manifest: DialogueManifest = read_json(&path)?;
            validate_dialogue(
                &production.quest,
                entry,
                &manifest,
                &mut keys,
                &mut string_ids,
                &mut audio_paths,
            )?;
            total = total
                .checked_add(manifest.spoken_lines.len())
                .ok_or_else(|| Error::manifest("spoken-line total overflows addressable memory"))?;
            dialogues.push(PlannedDialogue {
                index: entry.clone(),
                manifest,
                path,
            });
        }
        if total != production.spoken_line_count {
            return Err(Error::manifest(format!(
                "production index declares {} spoken lines but manifests contain {total}",
                production.spoken_line_count
            )));
        }

        Ok(Self {
            repo_root,
            index_path,
            production,
            dialogues,
        })
    }

    /// Returns one planned dialogue by stable ID.
    pub fn dialogue(&self, id: &str) -> Option<&PlannedDialogue> {
        self.dialogues
            .iter()
            .find(|dialogue| dialogue.index.id == id)
    }
}

/// Computes the stable unsigned FNV-1a ID used by dialogue manifests.
#[must_use]
pub fn fnv1a64(value: &str) -> u64 {
    value.bytes().fold(FNV1A64_OFFSET, |hash, byte| {
        (hash ^ u64::from(byte)).wrapping_mul(FNV1A64_PRIME)
    })
}

fn validate_dialogue(
    quest: &str,
    entry: &DialogueIndexEntry,
    manifest: &DialogueManifest,
    keys: &mut BTreeSet<String>,
    string_ids: &mut BTreeSet<String>,
    audio_paths: &mut BTreeSet<String>,
) -> Result<()> {
    if manifest.spoken_lines.len() != entry.line_count {
        return Err(Error::manifest(format!(
            "{} declares {} lines but contains {}",
            entry.id,
            entry.line_count,
            manifest.spoken_lines.len()
        )));
    }
    let speakers = manifest
        .spoken_lines
        .iter()
        .map(|line| line.speaker.as_str())
        .collect::<BTreeSet<_>>()
        .into_iter()
        .collect::<Vec<_>>();
    if speakers
        != entry
            .speakers
            .iter()
            .map(String::as_str)
            .collect::<Vec<_>>()
    {
        return Err(Error::manifest(format!(
            "{} speaker inventory does not match its production index",
            entry.id
        )));
    }
    for line in &manifest.spoken_lines {
        validate_path_atom("spoken-line key", &line.key)?;
        if line.text.trim().is_empty() {
            return Err(Error::manifest(format!("{} has empty text", line.key)));
        }
        let expected_id = fnv1a64(&line.key).to_string();
        if line.string_id != expected_id {
            return Err(Error::manifest(format!(
                "{} has string ID {}; expected {expected_id}",
                line.key, line.string_id
            )));
        }
        if line.duration_ms == 0 || line.duration_ms > MAX_LINE_DURATION_MS {
            return Err(Error::manifest(format!(
                "{} duration {} ms is outside 1..={MAX_LINE_DURATION_MS}",
                line.key, line.duration_ms
            )));
        }
        let expected_audio = format!("mod\\{quest}\\localization\\en-us\\vo\\{}.wem", line.key);
        if line.audio_path != expected_audio {
            return Err(Error::manifest(format!(
                "{} has audio path {:?}; expected {:?}",
                line.key, line.audio_path, expected_audio
            )));
        }
        if !keys.insert(line.key.clone()) {
            return Err(Error::manifest(format!(
                "spoken-line key {:?} is duplicated",
                line.key
            )));
        }
        if !string_ids.insert(line.string_id.clone()) {
            return Err(Error::manifest(format!(
                "spoken-line string ID {} is duplicated",
                line.string_id
            )));
        }
        if !audio_paths.insert(line.audio_path.clone()) {
            return Err(Error::manifest(format!(
                "spoken-line audio path {:?} is duplicated",
                line.audio_path
            )));
        }
    }
    Ok(())
}

fn read_json<T: DeserializeOwned>(path: &Path) -> Result<T> {
    let bytes = fs::read(path).map_err(|source| Error::io(path, source))?;
    serde_json::from_slice(&bytes).map_err(|source| Error::json(path, source))
}

fn canonical_directory(path: &Path) -> Result<PathBuf> {
    path.canonicalize()
        .map_err(|source| Error::io(path, source))
}

fn absolute_under(root: &Path, path: &Path) -> PathBuf {
    if path.is_absolute() {
        path.to_owned()
    } else {
        root.join(path)
    }
}

fn validate_relative_filename(value: &str) -> Result<()> {
    let path = Path::new(value);
    let safe = !path.is_absolute()
        && path
            .components()
            .all(|component| matches!(component, Component::Normal(_)))
        && path.file_name().is_some();
    if !safe {
        return Err(Error::manifest(format!(
            "dialogue manifest path {value:?} must be a relative filename"
        )));
    }
    Ok(())
}

fn validate_path_atom(label: &str, value: &str) -> Result<()> {
    let path = Path::new(value);
    let mut components = path.components();
    let safe = !value.is_empty()
        && !path.is_absolute()
        && matches!(components.next(), Some(Component::Normal(_)))
        && components.next().is_none();
    if !safe {
        return Err(Error::manifest(format!(
            "{label} {value:?} must be one safe path component"
        )));
    }
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn fnv_matches_existing_gq003_line_id() {
        assert_eq!(
            fnv1a64("gq003_20_iris_intro_01"),
            10_032_184_471_124_475_610
        );
    }

    #[test]
    fn unsafe_manifest_filename_is_rejected() {
        let error = validate_relative_filename("../outside.json")
            .expect_err("parent traversal must be rejected");
        assert!(error.to_string().contains("relative filename"));
    }

    #[test]
    fn unsafe_path_atom_is_rejected() {
        let error = validate_path_atom("dialogue ID", "../outside")
            .expect_err("parent traversal must be rejected");
        assert!(error.to_string().contains("safe path component"));
    }
}
