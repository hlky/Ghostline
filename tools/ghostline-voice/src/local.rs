//! Persistent in-process `DinoML` synthesis backend.

use std::path::{Path, PathBuf};

use dinoml_qwen3_tts::{BaseSynthesisController, PromptBuilder};
use dinoml_runtime::Device;

use crate::Result;
use crate::backend::{GeneratedAudio, SynthesisRequest, VoiceBackend};

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
        }
    }
}

/// Long-lived local `DinoML` Base synthesis session.
#[derive(Debug)]
pub struct LocalDinoMlBackend {
    builder: PromptBuilder,
    controller: BaseSynthesisController,
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
        })
    }

    /// Returns the compiled generation artifact's frame capacity.
    pub const fn frame_capacity(&self) -> usize {
        self.controller.frame_capacity()
    }
}

impl VoiceBackend for LocalDinoMlBackend {
    fn synthesize(&mut self, request: SynthesisRequest<'_>) -> Result<GeneratedAudio> {
        let prompt = self.builder.base_xvector(request.text, request.language)?;
        let aligned = self.builder.align(&prompt)?;
        let waveform = self.controller.synthesize_embedding_with_sampling(
            &aligned,
            None,
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
