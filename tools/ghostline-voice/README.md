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
  .\projects\ghostline\quests\shared\voice\embeddings\v.safetensors `
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
sidecar and a Ghostline request receipt. Reuse requires matching text,
embedding content, language, sampling, frame cap, seed, backend artifact
content, and output SHA-256. Artifact/checkpoint files are hashed once when
the backend loads. `--force` rerenders every selected candidate, including
valid outputs, and recovers missing or malformed receipts.

`render-report.json` is the candidate inventory for review:

```powershell
py -B tools/build_voice_selection_csv.py --manifest PATH_TO_MANIFEST `
  --report generated-voices/gq003/render-report.json --output generated-voices/review.csv
py -B tools/promote_voice_selections.py --manifest PATH_TO_MANIFEST `
  --csv generated-voices/review.csv --output-dir PATH_TO_QUEST_VOICE_SOURCE
```

Mark the chosen rows in the CSV's `selected` column before promotion. Designs
are consistent per speaker; optional manifest `voice_designs` values or selected
reference rows can pin a particular speaker's design. Promotion checks reviewed
file hashes and WAV readability before copying. Historical `design/line/take-*.wav`
directories remain available through `--auditions PATH --legacy-layout`; a
historical `reference.wav` additionally requires `--reference-speaker NAME`.

## Generate and serialize localization

```powershell
cargo run --release --manifest-path .\tools\ghostline-voice\Cargo.toml -- localize

cargo run --release --manifest-path .\tools\ghostline-voice\Cargo.toml -- serialize
```

Pure validation/localization builds can add `--no-default-features` to omit
the TTS/model runtime. The `render-local` feature is enabled by default for
compatibility. `localize-manifest --manifest PATH --quest QUEST --dialogue ID`
uses the same localization writer for one manifest, supports historical audio
basenames, and honors optional `male_audio_path`. The Python
`tools/generate_dialogue_localization.py` command is a compatibility adapter
for this operation; it uses a current native binary or Cargo's model-free build.

`serialize` uses GQ003's 23-entry `gq003_17` subtitle and VO resources plus
GQ000's one-entry subtitle map as audited templates. WolvenKit was needed once
to bootstrap the two larger inline-array layouts; normal regeneration is then
native. Every result is decoded again and compared with the authored
`Data.RootChunk.root.Data` payload before success is reported.

WEM conversion remains an explicit external Wwise step through
`tools/convert_wavs_to_wem.ps1`. Packing remains a separate reviewed build step.
Each conversion allocates a fresh output directory, verifies its complete WEM
set, and publishes with rollback if replacement fails. `-NoCopy` verifies the
outputs and prints that run's directory without changing active WEMs.
