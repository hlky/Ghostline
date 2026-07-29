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
