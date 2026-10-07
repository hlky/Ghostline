//! End-to-end Ghostline dialogue voice and localization authoring pipeline.
//!
//! The crate is deliberately downstream of `DinoML`. It consumes only public
//! Qwen3-TTS contracts and keeps model internals outside Ghostline.

#[cfg(feature = "render-local")]
pub mod backend;
pub mod cr2w;
#[cfg(feature = "render-local")]
pub mod embedding;
pub mod error;
#[cfg(feature = "render-local")]
pub mod local;
pub mod localization;
pub mod manifest;
#[cfg(feature = "render-local")]
pub mod render;

#[doc(inline)]
pub use error::{Error, Result};
