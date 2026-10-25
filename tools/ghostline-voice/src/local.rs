//! Persistent in-process `DinoML` synthesis backend.

use std::collections::BTreeMap;
use std::fs;
use std::path::{Path, PathBuf};

use dinoml_qwen3_tts::sha256_file;
use dinoml_qwen3_tts::{BaseSynthesisController, CodecFrames, PromptBuilder, read_codec_frames};
use dinoml_runtime::Device;
use sha2::{Digest, Sha256};

use crate::backend::{GeneratedAudio, SynthesisRequest, VoiceBackend};
use crate::{Error, Result};

/// Exact transcript and codec asset for one reference performance.
#[derive(Debug, Clone, serde::Deserialize)]
#[serde(deny_unknown_fields)]
pub struct ReferencePrompt {
    /// Words spoken in the reference recording.
    pub text: String,
    /// Versioned codec-frame JSON; relative paths use the prompt file's directory.
    pub codes: PathBuf,
}

/// Loads speaker reference prompts, rejecting empty transcripts.
///
/// # Errors
/// Returns an error for malformed JSON, empty transcripts, or unavailable paths.
pub fn load_reference_prompts(path: &Path) -> Result<BTreeMap<String, ReferencePrompt>> {
    let bytes = fs::read(path).map_err(|source| Error::io(path, source))?;
    let mut prompts: BTreeMap<String, ReferencePrompt> =
        serde_json::from_slice(&bytes).map_err(|source| Error::json(path, source))?;
    for (speaker, prompt) in &mut prompts {
        if speaker.trim().is_empty() || prompt.text.trim().is_empty() {
            return Err(Error::manifest(
                "reference speaker and transcript must be nonempty",
            ));
        }
        if !prompt.codes.is_absolute() {
            prompt.codes = path
                .parent()
                .unwrap_or_else(|| Path::new("."))
                .join(&prompt.codes);
        }
    }
    Ok(prompts)
}

/// Trusted local Base-model artifact configuration.
#[derive(Debug, Clone)]
pub struct LocalDinoMlConfig {
    /// Qwen3-TTS Base checkpoint directory.
    pub checkpoint: PathBuf,
    /// Compiled Base generation artifact directory.
    pub generation_artifact: PathBuf,
    /// Compiled tokenizer decoder artifact directory.
    pub decoder_artifact: PathBuf,
    /// Runtime execution device.
    pub device: Device,
    /// Whether artifact graph replay should be enabled.
    pub graph_replay: bool,
    /// Optional full reference conditioning by performer.
    pub references: BTreeMap<String, ReferencePrompt>,
    /// Optional delivery instruction, separate from spoken text.
    pub instruction: Option<String>,
}

impl LocalDinoMlConfig {
    /// Creates a local backend configuration from trusted paths.
    pub fn new(
        checkpoint: impl AsRef<Path>,
        generation_artifact: impl AsRef<Path>,
        decoder_artifact: impl AsRef<Path>,
        device: Device,
    ) -> Self {
        Self {
            checkpoint: checkpoint.as_ref().to_owned(),
            generation_artifact: generation_artifact.as_ref().to_owned(),
            decoder_artifact: decoder_artifact.as_ref().to_owned(),
            device,
            graph_replay: false,
            references: BTreeMap::new(),
            instruction: None,
        }
    }
}

/// Long-lived local `DinoML` Base synthesis session.
#[derive(Debug)]
pub struct LocalDinoMlBackend {
    builder: PromptBuilder,
    controller: BaseSynthesisController,
    identity: String,
    references: BTreeMap<String, (String, CodecFrames)>,
    instruction: Option<String>,
}

impl LocalDinoMlBackend {
    /// Loads one persistent local Base-model synthesis session.
    ///
    /// # Safety
    ///
    /// Compiled artifact libraries execute native code in-process. Every
    /// configured artifact directory and native dependency must be trusted.
    ///
    /// # Errors
    ///
    /// Returns an error for checkpoint, tokenizer, artifact, device, or graph
    /// replay initialization failure.
    pub unsafe fn load(config: &LocalDinoMlConfig) -> Result<Self> {
        let mut digest = Sha256::new();
        digest.update(format!(
            "ghostline-local-v2|{:?}|{}",
            config.device, config.graph_replay
        ));
        fingerprint_conditioning(&mut digest, config)?;
        for directory in [
            &config.checkpoint,
            &config.generation_artifact,
            &config.decoder_artifact,
        ] {
            fingerprint_tree(directory, directory, &mut digest)?;
        }
        let mut references = BTreeMap::new();
        for (speaker, reference) in &config.references {
            references.insert(
                speaker.clone(),
                (reference.text.clone(), read_codec_frames(&reference.codes)?),
            );
        }
        let identity = format!("{:x}", digest.finalize());
        let builder = PromptBuilder::load(&config.checkpoint)?;
        // SAFETY: The caller accepted the documented trust contract for both
        // native artifact directories and their dependencies.
        let mut controller = unsafe {
            BaseSynthesisController::load_precomputed(
                &config.checkpoint,
                &config.generation_artifact,
                &config.decoder_artifact,
                config.device,
            )
        }?;
        controller.set_graph_replay(config.graph_replay)?;
        Ok(Self {
            builder,
            controller,
            identity,
            references,
            instruction: config.instruction.clone(),
        })
    }

    /// Returns the compiled generation artifact's frame capacity.
    pub const fn frame_capacity(&self) -> usize {
        self.controller.frame_capacity()
    }
}

impl VoiceBackend for LocalDinoMlBackend {
    fn identity(&self) -> &str {
        &self.identity
    }

    fn synthesize(&mut self, request: SynthesisRequest<'_>) -> Result<GeneratedAudio> {
        let reference = self.references.get(request.speaker_name);
        let prompt = match reference {
            Some((text, codes)) => self.builder.base_icl_with_instruction(
                request.text,
                text,
                codes.clone(),
                request.language,
                self.instruction.as_deref(),
            )?,
            None => self.builder.base_xvector_with_instruction(
                request.text,
                request.language,
                self.instruction.as_deref(),
            )?,
        };
        let aligned = self.builder.align(&prompt)?;
        let waveform = self.controller.synthesize_embedding_with_sampling(
            &aligned,
            reference.map(|(_, codes)| codes),
            request.speaker,
            request.max_frames,
            request.seed,
            request.sampling,
        )?;
        Ok(GeneratedAudio {
            wav: waveform.to_pcm16_wav()?,
        })
    }
}

fn fingerprint_conditioning(digest: &mut Sha256, config: &LocalDinoMlConfig) -> Result<()> {
    digest.update(
        serde_json::to_vec(&config.instruction)
            .map_err(|source| Error::json("delivery instruction", source))?,
    );
    for (speaker, reference) in &config.references {
        digest.update(
            serde_json::to_vec(&(speaker, &reference.text, sha256_file(&reference.codes)?))
                .map_err(|source| Error::json(&reference.codes, source))?,
        );
    }
    Ok(())
}

fn fingerprint_tree(root: &Path, directory: &Path, digest: &mut Sha256) -> Result<()> {
    let mut entries = fs::read_dir(directory)
        .map_err(|source| Error::io(directory, source))?
        .map(|entry| entry.map(|entry| entry.path()))
        .collect::<std::io::Result<Vec<_>>>()
        .map_err(|source| Error::io(directory, source))?;
    entries.sort();
    for path in entries {
        // Download metadata is not consumed by the model and may change on inspection.
        if path
            .file_name()
            .is_some_and(|name| name == ".cache" || name == ".git")
        {
            continue;
        }
        if path.is_dir() {
            fingerprint_tree(root, &path, digest)?;
        } else {
            digest.update(
                path.strip_prefix(root)
                    .unwrap_or(&path)
                    .to_string_lossy()
                    .as_bytes(),
            );
            digest.update([0]);
            digest.update(sha256_file(&path)?.as_bytes());
        }
    }
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn conditioning_changes_invalidate_backend_identity() -> Result<()> {
        let directory = tempfile::tempdir().map_err(|source| Error::io("temporary", source))?;
        let codes = directory.path().join("codes.json");
        fs::write(&codes, b"first").map_err(|source| Error::io(&codes, source))?;
        let mut config = LocalDinoMlConfig::new("base", "generation", "decoder", Device::cpu());
        config.references.insert(
            "Aurore".to_owned(),
            ReferencePrompt {
                text: "Exact reference words.".to_owned(),
                codes: codes.clone(),
            },
        );
        let fingerprint = |config: &LocalDinoMlConfig| -> Result<Vec<u8>> {
            let mut digest = Sha256::new();
            fingerprint_conditioning(&mut digest, config)?;
            Ok(digest.finalize().to_vec())
        };
        let original = fingerprint(&config)?;
        assert_eq!(fingerprint(&config)?, original);
        config.instruction = Some("Speak calmly.".to_owned());
        assert_ne!(fingerprint(&config)?, original);
        config.instruction = None;
        config.references.get_mut("Aurore").unwrap().text = "Changed reference words.".to_owned();
        assert_ne!(fingerprint(&config)?, original);
        config.references.get_mut("Aurore").unwrap().text = "Exact reference words.".to_owned();
        fs::write(&codes, b"changed").map_err(|source| Error::io(&codes, source))?;
        assert_ne!(fingerprint(&config)?, original);
        Ok(())
    }

    #[test]
    fn reference_map_preserves_transcripts_and_resolves_relative_codes() -> Result<()> {
        let directory = tempfile::tempdir().map_err(|source| Error::io("temporary", source))?;
        let path = directory.path().join("references.json");
        fs::write(
            &path,
            br#"{"Aurore":{"text":"Exact words.","codes":"audio.json"}}"#,
        )
        .map_err(|source| Error::io(&path, source))?;
        let prompts = load_reference_prompts(&path)?;
        assert_eq!(prompts["Aurore"].text, "Exact words.");
        assert_eq!(prompts["Aurore"].codes, directory.path().join("audio.json"));
        fs::write(&path, br#"{"Aurore":{"text":" ","codes":"audio.json"}}"#)
            .map_err(|source| Error::io(&path, source))?;
        assert!(load_reference_prompts(&path).is_err());
        Ok(())
    }
}
