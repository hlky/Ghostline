//! Subtitle and voiceover-map CR2W-JSON generation.

use std::fs;
use std::path::{Path, PathBuf};

use serde_json::{Value, json};

use crate::manifest::{PlannedDialogue, VoicePlan};
use crate::{Error, Result};

/// Raw and packed localization paths for one dialogue.
#[derive(Debug, Clone)]
pub struct DialogueLocalizationPaths {
    /// Raw subtitle entries CR2W-JSON.
    pub subtitle_raw: PathBuf,
    /// Packed subtitle entries CR2W.
    pub subtitle_binary: PathBuf,
    /// Raw subtitle-map CR2W-JSON.
    pub subtitle_map_raw: PathBuf,
    /// Packed subtitle-map CR2W.
    pub subtitle_map_binary: PathBuf,
    /// Raw voiceover-map CR2W-JSON.
    pub voiceover_raw: PathBuf,
    /// Packed voiceover-map CR2W.
    pub voiceover_binary: PathBuf,
}

/// Generates every indexed subtitle, subtitle-map, and voiceover-map JSON.
///
/// # Errors
///
/// Returns an error when an output directory or resource cannot be written.
pub fn generate_all(plan: &VoicePlan) -> Result<Vec<DialogueLocalizationPaths>> {
    plan.dialogues
        .iter()
        .map(|dialogue| generate_dialogue(plan, dialogue))
        .collect()
}

/// Returns the canonical raw and packed localization paths for one dialogue.
#[must_use]
pub fn dialogue_paths(plan: &VoicePlan, dialogue_id: &str) -> DialogueLocalizationPaths {
    let raw = plan
        .repo_root
        .join("source/raw/mod")
        .join(&plan.production.quest)
        .join("localization/en-us");
    let binary = plan
        .repo_root
        .join("source/archive/mod")
        .join(&plan.production.quest)
        .join("localization/en-us");
    DialogueLocalizationPaths {
        subtitle_raw: raw
            .join("subtitles")
            .join(format!("{dialogue_id}.json.json")),
        subtitle_binary: binary.join("subtitles").join(format!("{dialogue_id}.json")),
        subtitle_map_raw: raw
            .join("subtitles")
            .join(format!("{dialogue_id}_subtitles_map.json.json")),
        subtitle_map_binary: binary
            .join("subtitles")
            .join(format!("{dialogue_id}_subtitles_map.json")),
        voiceover_raw: raw.join("vo").join(format!("{dialogue_id}.json.json")),
        voiceover_binary: binary.join("vo").join(format!("{dialogue_id}.json")),
    }
}

fn generate_dialogue(
    plan: &VoicePlan,
    dialogue: &PlannedDialogue,
) -> Result<DialogueLocalizationPaths> {
    let paths = dialogue_paths(plan, &dialogue.index.id);
    let subtitle_entries: Vec<Value> = dialogue
        .manifest
        .spoken_lines
        .iter()
        .map(|line| {
            json!({
                "$type": "localizationPersistenceSubtitleEntry",
                "femaleVariant": line.text,
                "maleVariant": line.text,
                "stringId": line.string_id,
            })
        })
        .collect();
    write_json(
        &paths.subtitle_raw,
        &json_resource(
            &paths.subtitle_binary,
            "localizationPersistenceSubtitleEntries",
            &subtitle_entries,
        ),
    )?;

    let voiceover_entries: Vec<Value> = dialogue
        .manifest
        .spoken_lines
        .iter()
        .map(|line| {
            json!({
                "$type": "locVoLineEntry",
                "femaleResPath": resource_ref(&line.audio_path),
                "maleResPath": resource_ref(&line.audio_path),
                "stringId": line.string_id,
            })
        })
        .collect();
    write_json(
        &paths.voiceover_raw,
        &json_resource(
            &paths.voiceover_binary,
            "locVoiceoverMap",
            &voiceover_entries,
        ),
    )?;

    let depot_subtitle = format!(
        "mod\\{}\\localization\\en-us\\subtitles\\{}.json",
        plan.production.quest, dialogue.index.id
    );
    write_json(
        &paths.subtitle_map_raw,
        &json_resource(
            &paths.subtitle_map_binary,
            "localizationPersistenceSubtitleMap",
            &[json!({
                "$type": "localizationPersistenceSubtitleMapEntry",
                "subtitleFile": resource_ref(&depot_subtitle),
                "subtitleGroup": {
                    "$type": "CName",
                    "$storage": "string",
                    "$value": "quest",
                },
            })],
        ),
    )?;
    Ok(paths)
}

fn json_resource(archive_path: &Path, root_type: &str, entries: &[Value]) -> Value {
    let archive_filename = archive_path
        .to_string_lossy()
        .strip_prefix(r"\\?\")
        .unwrap_or(&archive_path.to_string_lossy())
        .to_owned();
    json!({
        "Header": {
            "WolvenKitVersion": "8.17.4",
            "WKitJsonVersion": "0.0.9",
            "GameVersion": 2310,
            "ExportedDateTime": "1970-01-01T00:00:00Z",
            "DataType": "CR2W",
            "ArchiveFileName": archive_filename,
        },
        "Data": {
            "Version": 195,
            "BuildVersion": 0,
            "RootChunk": {
                "$type": "JsonResource",
                "cookingPlatform": "PLATFORM_PC",
                "root": {
                    "HandleId": "0",
                    "Data": {
                        "$type": root_type,
                        "entries": entries,
                    },
                },
            },
            "EmbeddedFiles": [],
        },
    })
}

fn resource_ref(path: &str) -> Value {
    json!({
        "DepotPath": {
            "$type": "ResourcePath",
            "$storage": "string",
            "$value": path,
        },
        "Flags": "Soft",
    })
}

fn write_json(path: &Path, value: &Value) -> Result<()> {
    let parent = path
        .parent()
        .ok_or_else(|| Error::manifest(format!("{} has no parent directory", path.display())))?;
    fs::create_dir_all(parent).map_err(|source| Error::io(parent, source))?;
    let mut encoded =
        serde_json::to_vec_pretty(value).map_err(|source| Error::json(path, source))?;
    encoded.push(b'\n');
    fs::write(path, encoded).map_err(|source| Error::io(path, source))
}
