//! Speaker-embedding loading across canonical and `DinoML` asset formats.

use std::fs;
use std::path::Path;

use dinoml_qwen3_tts::{SpeakerEmbedding, read_speaker_embedding, write_speaker_embedding};
use half::{bf16, f16};
use safetensors::{Dtype, SafeTensors};

use crate::{Error, Result};

/// Loads a `DinoML` JSON or canonical `SafeTensors` speaker embedding.
///
/// `SafeTensors` inputs must contain a single rank-one tensor named
/// `embedding` with F32, BF16, or F16 values.
///
/// # Errors
///
/// Returns an error for an unknown extension, malformed asset, missing tensor,
/// unsupported dtype/shape, or invalid embedding values.
pub fn load_embedding(path: impl AsRef<Path>) -> Result<SpeakerEmbedding> {
    let path = path.as_ref();
    match path
        .extension()
        .and_then(|extension| extension.to_str())
        .map(str::to_ascii_lowercase)
        .as_deref()
    {
        Some("json") => read_speaker_embedding(path).map_err(Error::from),
        Some("safetensors") => read_safetensors_embedding(path),
        _ => Err(Error::Embedding(format!(
            "{} must use .json or .safetensors",
            path.display()
        ))),
    }
}

/// Converts any supported speaker embedding to `DinoML`'s versioned JSON asset.
///
/// # Errors
///
/// Returns the same errors as [`load_embedding`] plus output I/O errors.
pub fn convert_embedding(input: impl AsRef<Path>, output: impl AsRef<Path>) -> Result<()> {
    let embedding = load_embedding(input)?;
    write_speaker_embedding(output, &embedding).map_err(Error::from)
}

/// Writes a canonical rank-one F32 `SafeTensors` embedding.
///
/// # Errors
///
/// Returns an error for an unsupported extension, serialization, or output I/O.
pub fn save_embedding(path: impl AsRef<Path>, embedding: &SpeakerEmbedding) -> Result<()> {
    let path = path.as_ref();
    if path.extension().and_then(|value| value.to_str()) != Some("safetensors") {
        return Err(Error::Embedding(
            "extracted embeddings require .safetensors".to_owned(),
        ));
    }
    let bytes = embedding
        .values()
        .iter()
        .flat_map(|value| value.to_le_bytes())
        .collect::<Vec<_>>();
    let view = safetensors::tensor::TensorView::new(Dtype::F32, vec![embedding.len()], &bytes)?;
    let encoded = safetensors::tensor::serialize(
        std::collections::HashMap::from([("embedding", view)]),
        None,
    )?;
    if let Some(parent) = path
        .parent()
        .filter(|parent| !parent.as_os_str().is_empty())
    {
        fs::create_dir_all(parent).map_err(|source| Error::io(parent, source))?;
    }
    fs::write(path, encoded).map_err(|source| Error::io(path, source))
}

/// Computes an equal-weight arithmetic mean of same-speaker embeddings.
///
/// Inputs retain their learned scale; no unit-length normalization is applied.
///
/// # Errors
///
/// Returns an error for an empty input set, differing widths, or invalid values.
pub fn mean_embeddings(embeddings: &[SpeakerEmbedding]) -> Result<SpeakerEmbedding> {
    let first = embeddings
        .first()
        .ok_or_else(|| Error::Embedding("at least one embedding is required".to_owned()))?;
    let mut sums = vec![0.0_f64; first.len()];
    for embedding in embeddings {
        if embedding.len() != first.len() {
            return Err(Error::Embedding("embedding widths must match".to_owned()));
        }
        for (sum, value) in sums.iter_mut().zip(embedding.values()) {
            *sum += f64::from(*value);
        }
    }
    #[allow(clippy::cast_precision_loss, clippy::cast_possible_truncation)]
    let values = sums
        .into_iter()
        .map(|value| (value / embeddings.len() as f64) as f32)
        .collect::<Vec<_>>();
    SpeakerEmbedding::try_from_values(values).map_err(Error::from)
}

fn read_safetensors_embedding(path: &Path) -> Result<SpeakerEmbedding> {
    if cfg!(target_endian = "big") {
        return Err(Error::Embedding(
            "SafeTensors embeddings are unsupported on big-endian targets".to_owned(),
        ));
    }
    let bytes = fs::read(path).map_err(|source| Error::io(path, source))?;
    let archive = SafeTensors::deserialize(&bytes)?;
    let tensor = archive.tensor("embedding")?;
    if tensor.shape().len() != 1 || tensor.shape()[0] == 0 {
        return Err(Error::Embedding(format!(
            "{} tensor 'embedding' has shape {:?}; expected nonempty rank one",
            path.display(),
            tensor.shape()
        )));
    }
    let values: Vec<f32> = match tensor.dtype() {
        Dtype::F32 => tensor
            .data()
            .chunks_exact(4)
            .map(|bytes| f32::from_le_bytes([bytes[0], bytes[1], bytes[2], bytes[3]]))
            .collect(),
        Dtype::BF16 => tensor
            .data()
            .chunks_exact(2)
            .map(|bytes| bf16::from_bits(u16::from_le_bytes([bytes[0], bytes[1]])).to_f32())
            .collect(),
        Dtype::F16 => tensor
            .data()
            .chunks_exact(2)
            .map(|bytes| f16::from_bits(u16::from_le_bytes([bytes[0], bytes[1]])).to_f32())
            .collect(),
        dtype => {
            return Err(Error::Embedding(format!(
                "{} tensor 'embedding' has dtype {dtype:?}; expected F32, BF16, or F16",
                path.display()
            )));
        }
    };
    SpeakerEmbedding::try_from_values(values).map_err(Error::from)
}

#[cfg(test)]
mod tests {
    use std::collections::HashMap;

    use safetensors::tensor::{TensorView, serialize};

    use super::*;

    #[test]
    fn mean_preserves_scale_and_rejects_incompatible_inputs() -> Result<()> {
        let first = SpeakerEmbedding::try_from_values(vec![2.0, 4.0])?;
        let second = SpeakerEmbedding::try_from_values(vec![4.0, 8.0])?;
        assert_eq!(
            mean_embeddings(&[first.clone(), second])?.values(),
            [3.0, 6.0]
        );
        assert_eq!(mean_embeddings(std::slice::from_ref(&first))?, first);
        assert!(mean_embeddings(&[]).is_err());
        let short = SpeakerEmbedding::try_from_values(vec![1.0])?;
        assert!(mean_embeddings(&[first, short]).is_err());
        Ok(())
    }

    #[test]
    fn extracted_embedding_round_trips_and_converts() -> Result<()> {
        let directory = tempfile::tempdir().map_err(|source| Error::io("temporary", source))?;
        let canonical = directory.path().join("nested/voice.safetensors");
        let json = directory.path().join("voice.json");
        let expected = SpeakerEmbedding::try_from_values(vec![0.25, -0.5, 1.0])?;
        save_embedding(&canonical, &expected)?;
        assert_eq!(load_embedding(&canonical)?, expected);
        convert_embedding(&canonical, &json)?;
        assert_eq!(load_embedding(&json)?, expected);
        assert!(save_embedding(directory.path().join("voice.pt"), &expected).is_err());
        Ok(())
    }

    #[test]
    fn bf16_safetensors_embedding_is_promoted_losslessly() -> Result<()> {
        let values = [bf16::from_f32(0.25), bf16::from_f32(-0.5)];
        let bytes = values
            .iter()
            .flat_map(|value| value.to_bits().to_le_bytes())
            .collect::<Vec<_>>();
        let view = TensorView::new(Dtype::BF16, vec![2], &bytes)?;
        let encoded = serialize(HashMap::from([("embedding", view)]), None)?;
        let directory = tempfile::tempdir().map_err(|source| Error::io("temporary", source))?;
        let path = directory.path().join("voice.safetensors");
        fs::write(&path, encoded).map_err(|source| Error::io(&path, source))?;

        let embedding = load_embedding(&path)?;

        assert_eq!(embedding.values(), [0.25, -0.5]);
        Ok(())
    }
}
