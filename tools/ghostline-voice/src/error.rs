//! Pipeline error boundary.

use std::io;
use std::path::{Path, PathBuf};

use thiserror::Error as ThisError;

/// Error produced by Ghostline voice authoring operations.
#[derive(Debug, ThisError)]
pub enum Error {
    /// A filesystem operation failed for a known path.
    #[error("I/O failed for {path}: {source}")]
    Io {
        /// Path involved in the failed operation.
        path: PathBuf,
        /// Underlying filesystem error.
        source: io::Error,
    },
    /// JSON could not be decoded for a known path.
    #[error("JSON parsing failed for {path}: {source}")]
    Json {
        /// Path containing malformed JSON.
        path: PathBuf,
        /// Underlying JSON error.
        source: serde_json::Error,
    },
    /// An authored manifest violated the pipeline contract.
    #[error("invalid voice manifest: {0}")]
    Manifest(String),
    /// A speaker embedding used an unsupported representation.
    #[error("unsupported speaker embedding: {0}")]
    Embedding(String),
    /// `DinoML` rejected a model, prompt, asset, or generation operation.
    #[error("DinoML operation failed: {0}")]
    DinoMl(#[from] dinoml_qwen3_tts::Error),
    /// A `SafeTensors` asset could not be decoded.
    #[error("SafeTensors operation failed: {0}")]
    SafeTensors(#[from] safetensors::SafeTensorError),
    /// RED reflection metadata could not be loaded.
    #[error("RED schema operation failed: {0}")]
    RedSchema(#[from] ghostline_red::schema::SchemaError),
    /// CR2W JSON could not be written to a template-backed binary.
    #[error("CR2W write failed: {0}")]
    RedWriter(#[from] ghostline_red::writer::WriterError),
    /// A generated CR2W binary could not be decoded for verification.
    #[error("CR2W verification failed: {0}")]
    RedCodec(#[from] ghostline_red::codec::CodecError),
}

impl Error {
    /// Creates a path-aware filesystem error.
    pub fn io(path: impl AsRef<Path>, source: io::Error) -> Self {
        Self::Io {
            path: path.as_ref().to_owned(),
            source,
        }
    }

    /// Creates a path-aware JSON error.
    pub fn json(path: impl AsRef<Path>, source: serde_json::Error) -> Self {
        Self::Json {
            path: path.as_ref().to_owned(),
            source,
        }
    }

    /// Creates an authored-manifest contract error.
    pub fn manifest(message: impl Into<String>) -> Self {
        Self::Manifest(message.into())
    }
}

/// Result returned by Ghostline voice authoring operations.
pub type Result<T> = std::result::Result<T, Error>;
