# ghostline-voice

`ghostline-voice` is Ghostline's downstream DinoML integration. It consumes
the public `dinoml-qwen3-tts` API, keeps one model controller resident for an
entire render, and owns the deterministic path from dialogue manifests through
localization CR2W resources.

It does not make audition choices automatically. Generated candidates remain
under `generated-voices`; reviewed selections must be promoted to the owning
quest's `voice/source` directory before Wwise conversion.

## Validate GQ003

```powershell
cargo run --release --manifest-path .\tools\ghostline-voice\Cargo.toml -- `
  validate
```

## Convert a canonical embedding

```powershell
cargo run --release --manifest-path .\tools\ghostline-voice\Cargo.toml -- `
  convert-embedding `
  .\quests\story\ghostline\shared\voice\embeddings\v.safetensors `
  .\generated-voices\embeddings\v.json
```

## Render with a persistent Base controller

```powershell
cargo run --release --manifest-path .\tools\ghostline-voice\Cargo.toml -- `
  render-local `
  --checkpoint G:\checkpoints\Qwen\Qwen3-TTS-12Hz-1.7B-Base `
  --generation-artifact H:\dinoml_v2\build\qwen3_tts_ghostline_1_7b_gfx1201\base_generation_p128_f288 `
  --decoder-artifact H:\dinoml_v2\build\qwen3_tts_ghostline_1_7b_gfx1201\tokenizer_decoder_f256 `
  --dialogue gq003_21 `
  --embedding Patch=.\generated-voices\embeddings\patch.json `
  --embedding V=.\generated-voices\embeddings\v.json
```

Use repeated `--speaker NAME` arguments to render only selected performers
from the chosen dialogue manifests.

The checkpoint and artifact libraries are trusted native inputs. `render-local`
loads them in-process once, then serially renders every selected line and
candidate version. Each WAV receives DinoML's versioned reproducibility
sidecar, and reruns reuse only outputs whose seed and SHA-256 still match.

## Generate and serialize localization

```powershell
cargo run --release --manifest-path .\tools\ghostline-voice\Cargo.toml -- localize

cargo run --release --manifest-path .\tools\ghostline-voice\Cargo.toml -- serialize
```

`serialize` uses GQ003's 23-entry `gq003_17` subtitle and VO resources plus
GQ000's one-entry subtitle map as audited templates. WolvenKit was needed once
to bootstrap the two larger inline-array layouts; normal regeneration is then
native. Every result is decoded again and compared with the authored
`Data.RootChunk.root.Data` payload before success is reported.

WEM conversion remains an explicit external Wwise step through
`tools/convert_wavs_to_wem.ps1`. Packing remains a separate reviewed build step.
