# Ghostline Speaker Embeddings

These cached Qwen3-TTS x-vectors are shared authoring inputs for consistent
voices across quests.

| Speaker | SafeTensors | SHA-256 |
| --- | --- | --- |
| Patch | [`embeddings/patch.safetensors`](embeddings/patch.safetensors) | `8B8D1F0635C18E6E70B4878F3A6FB727491DFBA0D262F8BE8CAA1FD2015E52DB` |
| V | [`embeddings/v.safetensors`](embeddings/v.safetensors) | `FB153E4CB99A1FD492046CA323B0F84187B8DAA92187ED7089078CB5097834AC` |

Each file contains one `bfloat16` tensor with shape `[2048]` under the key
`embedding`:

```python
from safetensors.torch import load_file

embedding = load_file("embeddings/patch.safetensors")["embedding"]
```

Conversion from the original PyTorch tensors preserved the dtype, shape, and
tensor values exactly. The unsafe pickle-backed `.pt` copies are intentionally
not retained.

Iris's earlier audition pipeline kept its generated x-vector in memory and did
not save it. A future replacement should be stored here as
`embeddings/iris.safetensors` with its reference audio, exact transcript,
model identifier, and hash recorded alongside it.
