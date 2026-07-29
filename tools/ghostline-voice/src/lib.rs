//! End-to-end Ghostline dialogue voice and localization authoring pipeline.
//!
//! The crate is deliberately downstream of `DinoML`. It consumes only public
//! Qwen3-TTS contracts and keeps model internals outside Ghostline.

pub mod backend;
pub mod cr2w;
pub mod embedding;
pub mod error;
pub mod local;
pub mod localization;
pub mod manifest;
pub mod render;

#[doc(inline)]
pub use error::{Error, Result};
