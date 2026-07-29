//! Template-backed localization CR2W serialization and semantic verification.

use std::ffi::OsStr;
use std::fs;
use std::path::{Path, PathBuf};

use ghostline_red::codec::decode_wkit_with_red_schema;
use ghostline_red::schema::RedSchema;
use ghostline_red::writer::write_with_red_schema;
use serde::Serialize;
use serde_json::Value;

use crate::localization::{DialogueLocalizationPaths, dialogue_paths};
use crate::manifest::VoicePlan;
use crate::{Error, Result};

/// Compatible CR2W templates for the three localization resource kinds.
#[derive(Debug, Clone)]
pub struct LocalizationTemplates {
    /// Template for `localizationPersistenceSubtitleEntries`.
    pub subtitles: PathBuf,
    /// Template for `localizationPersistenceSubtitleMap`.
    pub subtitle_map: PathBuf,
    /// Template for `locVoiceoverMap`.
    pub voiceover_map: PathBuf,
}

/// One verified CR2W localization output.
#[derive(Debug, Clone, Serialize)]
pub struct SerializedResource {
    /// Dialogue ID.
    pub dialogue: String,
    /// Resource kind.
    pub kind: String,
    /// Output CR2W path.
    pub output: PathBuf,
    /// Output byte length.
    pub bytes: u64,
}

/// Serializes and round-trip verifies every indexed localization resource.
///
/// # Errors
///
/// Returns an error for unreadable schema/JSON, missing templates, unsupported
/// template-backed writes, or semantic differences after binary round trip.
pub fn serialize_all(
    plan: &VoicePlan,
    schema_path: impl AsRef<Path>,
    templates: &LocalizationTemplates,
) -> Result<Vec<SerializedResource>> {
    let schema_path = schema_path.as_ref();
    let schema_bytes = fs::read(schema_path).map_err(|source| Error::io(schema_path, source))?;
    let schema = RedSchema::from_slice(&schema_bytes)?;
    let mut outputs = Vec::with_capacity(plan.dialogues.len() * 3);
    for dialogue in &plan.dialogues {
        let paths = dialogue_paths(plan, &dialogue.index.id);
        outputs.push(serialize_one(
            &dialogue.index.id,
            "subtitles",
            &paths.subtitle_raw,
            &paths.subtitle_binary,
            &templates.subtitles,
            &schema,
        )?);
        outputs.push(serialize_one(
            &dialogue.index.id,
            "subtitle_map",
            &paths.subtitle_map_raw,
            &paths.subtitle_map_binary,
            &templates.subtitle_map,
            &schema,
        )?);
        outputs.push(serialize_one(
            &dialogue.index.id,
            "voiceover_map",
            &paths.voiceover_raw,
            &paths.voiceover_binary,
            &templates.voiceover_map,
            &schema,
        )?);
    }
    Ok(outputs)
}

/// Verifies that all expected raw localization inputs exist.
///
/// # Errors
///
/// Returns an error naming the first absent generated input.
pub fn require_raw_inputs(plan: &VoicePlan) -> Result<Vec<DialogueLocalizationPaths>> {
    plan.dialogues
        .iter()
        .map(|dialogue| {
            let paths = dialogue_paths(plan, &dialogue.index.id);
            for path in [
                &paths.subtitle_raw,
                &paths.subtitle_map_raw,
                &paths.voiceover_raw,
            ] {
                if !path.is_file() {
                    return Err(Error::manifest(format!(
                        "generated localization input is missing: {}",
                        path.display()
                    )));
                }
            }
            Ok(paths)
        })
        .collect()
}

fn serialize_one(
    dialogue: &str,
    kind: &str,
    raw: &Path,
    output: &Path,
    template: &Path,
    schema: &RedSchema,
) -> Result<SerializedResource> {
    if !template.is_file() {
        return Err(Error::manifest(format!(
            "{kind} CR2W template is missing: {}",
            template.display()
        )));
    }
    let parent = output
        .parent()
        .ok_or_else(|| Error::manifest(format!("{} has no parent directory", output.display())))?;
    fs::create_dir_all(parent).map_err(|source| Error::io(parent, source))?;
    write_with_red_schema(raw, template, output, schema, OsStr::new(""))?;
    verify_semantics(raw, output, schema)?;
    let bytes = fs::metadata(output)
        .map_err(|source| Error::io(output, source))?
        .len();
    Ok(SerializedResource {
        dialogue: dialogue.to_owned(),
        kind: kind.to_owned(),
        output: output.to_owned(),
        bytes,
    })
}

fn verify_semantics(raw: &Path, output: &Path, schema: &RedSchema) -> Result<()> {
    let authored: Value =
        serde_json::from_slice(&fs::read(raw).map_err(|source| Error::io(raw, source))?)
            .map_err(|source| Error::json(raw, source))?;
    let decoded = decode_wkit_with_red_schema(output, schema, OsStr::new(""))?;
    let pointer = "/Data/RootChunk/root/Data";
    if authored.pointer(pointer) != decoded.pointer(pointer) {
        return Err(Error::manifest(format!(
            "{} changed semantically during CR2W round trip",
            output.display()
        )));
    }
    Ok(())
}
