//! Backend-neutral synthesis request boundary.

use dinoml_qwen3_tts::{GenerationSamplingConfig, SpeakerEmbedding};

use crate::Result;

/// One deterministic synthesis request.
#[derive(Debug, Clone, Copy)]
pub struct SynthesisRequest<'a> {
    /// Text to speak.
    pub text: &'a str,
    /// Qwen language identifier.
    pub language: &'a str,
    /// Reusable speaker conditioning.
    pub speaker: &'a SpeakerEmbedding,
    /// Maximum codec-frame count.
    pub max_frames: usize,
    /// Deterministic generation seed.
    pub seed: u64,
    /// Outer and code-predictor sampling controls.
    pub sampling: GenerationSamplingConfig,
}

/// Canonical WAV returned by any synthesis backend.
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct GeneratedAudio {
    /// Mono PCM16 RIFF/WAVE bytes.
    pub wav: Vec<u8>,
}

/// Synchronous single-GPU synthesis backend.
///
/// The interface is intentionally serial. A persistent HTTP implementation
/// can satisfy the same contract without changing the authoring pipeline.
pub trait VoiceBackend {
    /// Synthesizes one request into canonical WAV bytes.
    ///
    /// # Errors
    ///
    /// Returns an error when prompt construction, generation, or audio
    /// encoding fails.
    fn synthesize(&mut self, request: SynthesisRequest<'_>) -> Result<GeneratedAudio>;
}
