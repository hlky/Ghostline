//! Subtitle and voiceover-map CR2W-JSON generation.

use std::fs;
use std::path::{Path, PathBuf};

use serde::Deserialize;
use serde_json::{Value, json};

use crate::manifest::VoicePlan;
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
        .map(|dialogue| {
            let lines = dialogue
                .manifest
                .spoken_lines
                .iter()
                .map(|line| LocalizationLine {
                    text: line.text.clone(),
                    string_id: line.string_id.clone(),
                    audio_path: line.audio_path.clone(),
                    male_audio_path: line.male_audio_path.clone(),
                })
                .collect::<Vec<_>>();
            generate_dialogue(
                &plan.repo_root,
                &plan.production.quest,
                &dialogue.index.id,
                &lines,
            )
        })
        .collect()
}

/// Returns the canonical raw and packed localization paths for one dialogue.
///
/// # Errors
///
/// Returns an error when the repository project catalog cannot be read.
pub fn dialogue_paths(plan: &VoicePlan, dialogue_id: &str) -> Result<DialogueLocalizationPaths> {
    paths(&plan.repo_root, &plan.production.quest, dialogue_id)
}

fn project_root(repo_root: &Path, quest: &str) -> Result<PathBuf> {
    let catalog_path = repo_root.join("projects/catalog.json");
    if !catalog_path.is_file() {
        return Ok(repo_root.to_owned());
    }
    let content = fs::read(&catalog_path).map_err(|source| Error::io(&catalog_path, source))?;
    let catalog: Value =
        serde_json::from_slice(&content).map_err(|source| Error::json(&catalog_path, source))?;
    let projects = catalog["projects"]
        .as_object()
        .ok_or_else(|| Error::manifest("Project catalog requires a projects object"))?;
    let depot = format!("mod/{quest}/");
    let mut owner = None;
    for relative in projects.values() {
        let relative = relative
            .as_str()
            .ok_or_else(|| Error::manifest("Project catalog paths must be strings"))?;
        if Path::new(relative).is_absolute() || relative.split('/').any(|part| part == "..") {
            return Err(Error::manifest(
                "Project catalog path escapes the repository",
            ));
        }
        let directory = repo_root.join(relative);
        let config_path = directory.join("project.json");
        let content = fs::read(&config_path).map_err(|source| Error::io(&config_path, source))?;
        let config: Value =
            serde_json::from_slice(&content).map_err(|source| Error::json(&config_path, source))?;
        for prefix in config["depot_prefixes"].as_array().into_iter().flatten() {
            let prefix = prefix
                .as_str()
                .ok_or_else(|| Error::manifest("Depot prefixes must be strings"))?;
            if depot.starts_with(prefix) {
                let length = prefix.len();
                match &owner {
                    Some((previous, _)) if *previous == length => {
                        return Err(Error::manifest(format!("Multiple projects own {depot}")));
                    }
                    Some((previous, _)) if *previous > length => {}
                    _ => owner = Some((length, directory.clone())),
                }
            }
        }
    }
    if let Some((_, directory)) = owner {
        return Ok(directory);
    }
    Err(Error::manifest(format!("No project owns quest {quest}")))
}

fn paths(repo_root: &Path, quest: &str, dialogue_id: &str) -> Result<DialogueLocalizationPaths> {
    let project = project_root(repo_root, quest)?;
    let raw = project
        .join("source/raw/mod")
        .join(quest)
        .join("localization/en-us");
    let binary = project
        .join("source/archive/mod")
        .join(quest)
        .join("localization/en-us");
    Ok(DialogueLocalizationPaths {
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
    })
}

#[derive(Deserialize)]
struct LocalizationLine {
    text: String,
    string_id: String,
    audio_path: String,
    #[serde(default)]
    male_audio_path: Option<String>,
}

/// Generates localization from a single manifest without loading a synthesis model.
///
/// # Errors
/// Returns an error for invalid identities, entries, JSON or output I/O.
pub fn generate_manifest(
    repo_root: &Path,
    manifest: &Path,
    quest: &str,
    dialogue: &str,
) -> Result<DialogueLocalizationPaths> {
    #[derive(Deserialize)]
    struct Input {
        spoken_lines: Vec<LocalizationLine>,
    }
    let input: Input =
        serde_json::from_slice(&fs::read(manifest).map_err(|source| Error::io(manifest, source))?)
            .map_err(|source| Error::json(manifest, source))?;
    generate_dialogue(repo_root, quest, dialogue, &input.spoken_lines)
}

fn generate_dialogue(
    repo_root: &Path,
    quest: &str,
    dialogue: &str,
    lines: &[LocalizationLine],
) -> Result<DialogueLocalizationPaths> {
    for atom in [quest, dialogue] {
        if atom.is_empty()
            || !atom
                .bytes()
                .all(|byte| byte.is_ascii_alphanumeric() || b"_-".contains(&byte))
        {
            return Err(Error::manifest(
                "quest and dialogue must be nonempty path atoms",
            ));
        }
    }
    if lines.is_empty() {
        return Err(Error::manifest("manifest has no spoken_lines"));
    }
    let mut ids = std::collections::BTreeSet::new();
    for line in lines {
        let id = line
            .string_id
            .parse::<u64>()
            .map_err(|_| Error::manifest("string_id must be an unsigned 64-bit integer"))?;
        if !ids.insert(id) || line.text.trim().is_empty() {
            return Err(Error::manifest("duplicate string ID or empty spoken text"));
        }
        for audio in [
            Some(line.audio_path.as_str()),
            line.male_audio_path.as_deref(),
        ]
        .into_iter()
        .flatten()
        {
            if !Path::new(audio)
                .extension()
                .is_some_and(|extension| extension.eq_ignore_ascii_case("wem"))
                || audio.starts_with(['/', '\\'])
                || audio.split(['/', '\\']).any(|part| {
                    part.is_empty() || part == ".." || part == "." || part.contains(':')
                })
            {
                return Err(Error::manifest(
                    "audio path must be a relative WEM depot path",
                ));
            }
        }
    }
    let paths = paths(repo_root, quest, dialogue)?;
    let subtitle_entries: Vec<Value> = lines
        .iter()
        .map(|line| {
            json!({
                "$type": "localizationPersistenceSubtitleEntry", "femaleVariant": line.text,
                "maleVariant": line.text, "stringId": line.string_id,
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

    let voiceover_entries: Vec<Value> = lines.iter()
        .map(|line| {
            json!({
                "$type": "locVoLineEntry",
                "femaleResPath": resource_ref(&line.audio_path),
                "maleResPath": resource_ref(line.male_audio_path.as_deref().unwrap_or(&line.audio_path)),
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

    let depot_subtitle = format!("mod\\{quest}\\localization\\en-us\\subtitles\\{dialogue}.json");
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

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn monorepo_localization_targets_only_the_owning_project() {
        let directory = tempfile::tempdir().unwrap();
        let projects = directory.path().join("projects");
        fs::create_dir_all(projects.join("fixture")).unwrap();
        fs::write(
            projects.join("catalog.json"),
            br#"{"projects":{"fixture":"projects/fixture"}}"#,
        )
        .unwrap();
        fs::write(
            projects.join("fixture/project.json"),
            br#"{"depot_prefixes":["mod/q/"]}"#,
        )
        .unwrap();
        let manifest = directory.path().join("manifest.json");
        fs::write(
            &manifest,
            br#"{"spoken_lines":[{"text":"Hello","string_id":"2","audio_path":"mod\\q\\voice.wem"}]}"#,
        ).unwrap();
        let output = generate_manifest(directory.path(), &manifest, "q", "q_01").unwrap();
        assert!(
            output
                .subtitle_raw
                .starts_with(projects.join("fixture/source/raw"))
        );
        assert!(output.voiceover_raw.is_file());
        assert!(!directory.path().join("source").exists());
        assert!(paths(directory.path(), "unregistered", "line").is_err());
    }

    #[test]
    fn single_manifest_preserves_gendered_and_historical_shared_audio() {
        let directory = tempfile::tempdir().unwrap();
        let manifest = directory.path().join("manifest.json");
        fs::write(&manifest, serde_json::to_vec(&json!({"spoken_lines": [
            {"text": "Hello", "string_id": "18446744073709551615", "audio_path": "mod\\q\\f.wem", "male_audio_path": "mod\\q\\m.wem"},
            {"text": "Again", "string_id": "2", "audio_path": "mod\\q\\historical_name.wem"}
        ]})).unwrap()).unwrap();
        let paths = generate_manifest(directory.path(), &manifest, "q", "q_01").unwrap();
        let output: Value =
            serde_json::from_slice(&fs::read(paths.voiceover_raw).unwrap()).unwrap();
        let entries = &output["Data"]["RootChunk"]["root"]["Data"]["entries"];
        assert_eq!(
            entries[0]["maleResPath"]["DepotPath"]["$value"],
            "mod\\q\\m.wem"
        );
        assert_eq!(entries[0]["stringId"], "18446744073709551615");
        assert_eq!(entries[1]["femaleResPath"], entries[1]["maleResPath"]);
    }

    #[test]
    fn invalid_line_does_not_publish_earlier_resources() {
        let directory = tempfile::tempdir().unwrap();
        let manifest = directory.path().join("manifest.json");
        fs::write(
            &manifest,
            br#"{"spoken_lines":[{"text":"Hello","string_id":"2","audio_path":"../outside.wem"}]}"#,
        )
        .unwrap();
        assert!(generate_manifest(directory.path(), &manifest, "q", "q_01").is_err());
        assert!(!directory.path().join("source").exists());
    }
}
