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

## Clone a reference and compare multiple clips

Extract a canonical speaker embedding from a WAV or FLAC using the original
Base checkpoint and a trusted compiled speaker-encoder artifact:

```powershell
cargo run --release --manifest-path .\tools\ghostline-voice\Cargo.toml -- `
  extract-embedding --checkpoint PATH_TO_BASE_MODEL_SAFETENSORS `
  --speaker-artifact PATH_TO_SPEAKER_ARTIFACT `
  --reference reference.wav --output embedding.safetensors

cargo run --release --manifest-path .\tools\ghostline-voice\Cargo.toml -- `
  merge-embeddings --input clip1.safetensors clip2.safetensors clip3.safetensors `
  --output mean.safetensors
```

`merge-embeddings` computes an equal-weight arithmetic mean and preserves the
encoder's learned scale. Only combine embeddings of the same performer.
Use `extract-embeddings --reference clip1.wav clip2.wav --output-dir embeddings`
with the same checkpoint and speaker-artifact arguments to keep one encoder
resident across a batch. Reference basenames must be unique.
For a concatenated reference, join decoded clips before extraction. The
speaker artifact must support the entire reference's mel-frame count: at
24 kHz with a 256-sample hop, a 30-second reference needs about 2,813 frames,
so a 2,048-frame artifact is too small. A 4,096-frame artifact accommodates
references up to about 43 seconds. Extraction rejects an oversized reference.
Compare concatenation, per-clip means, and single-clip baselines by passing
each embedding to `render-local` with the same manifest, seed base, and
sampling settings, using separate output directories.

## Convert a canonical embedding

```powershell
cargo run --release --manifest-path .\tools\ghostline-voice\Cargo.toml -- `
  convert-embedding `
  .\projects\ghostline\quests\shared\voice\embeddings\v.safetensors `
  .\generated-voices\embeddings\v.json
```

## Render with a persistent Base controller

Create a custom character reference through `design-reference` with a trusted
VoiceDesign checkpoint, generation and decoder artifacts, exact `--text`,
separate `--instruction`, explicit `--seed` and `--output`. The output remains
an unreviewed voice candidate and receives a reproducibility sidecar. Extract
its speaker embedding and reference codes, then use full reference conditioning
for repeated dialogue. This operation must not be used to design V.

On Windows, use the activated DinoML toolchain to compile artifacts. Artifacts
must package the matching SDK's `amdhip64_7.dll`, `amd_comgr.dll`, and
`rocm_kpack.dll` alongside their native libraries. The updated DinoML loader
resolves dependencies from the artifact library directory. See DinoML's
`docs/rocm-development.md` for the runtime deployment contract.

For full reference conditioning, encode each clean WAV with `encode-reference`
and a bounded-variable tokenizer encoder. Supply `render-local
--reference-prompts references.json`, where the JSON maps performer names to
`{"text":"exact spoken reference transcript","codes":"reference-codes.json"}`.
Code paths are relative to that JSON file. The encoder preserves each WAV's
actual sample count and resolves the output as `ceil(samples / 1920)` frames;
one artifact covers its whole declared domain.

`python tools/prepare_vanilla_voices.py` prepares three normal-VO references
each for female/male V and ten vanilla NPCs, then renders Full + Instruction
auditions under `generated-voices/vanilla-library`. Its catalog retains exact
transcripts, depot paths, WAV hashes, codec assets, and matching embeddings.
Reference choices await listening review in `comparison.html`. Re-running
reuses cached encoding when the reference and toolchain inputs match; rendering
uses saved codes through `reference-prompts.json`. Existing V embeddings are
retained. The script reuses the established French-twins native artifacts.

`python tools/compare_v_references.py` compares both Vs using six conversational
reference clips each. It preserves the vanilla library's target text and
Reference 1 seed for each performer across four methods: full reference alone,
full reference with V-specific delivery guidance, full reference with the mean
of six embeddings, and full reference with an embedding from 30s+ concatenated
audio. The latter two keep the same single-clip codec/transcript context and
omit instructions so that only the embedding changes. Results, source audio,
phoneme-coverage estimates and provenance live under
`generated-voices/vanilla-library/v-neutral`; listen in its `comparison.html`.

The selected workflow for both Vs is full reference without an instruction,
using conversational text with contractions. Saved canonical performer entries
and prompts are `generated-voices/vanilla-library/selected-voices.json` and
`selected-reference-prompts.json`.

`python tools/prepare_neutral_npcs.py` prepares two new conversational reference
options for each of eleven NPCs, including Placide. Its default auditions use
full reference without instructions. Only Placide and Takemura receive an
additional accent-guidance comparison with the same text and seeds. Codes and
embeddings are cached with reference/checkpoint/artifact input identities;
listening review selects the preferred reference and determines whether accent
guidance helps. Results live in `generated-voices/vanilla-library/npc-neutral`.
The original vanilla-library auditions remain a historical baseline.

`render-local --instruction "Speak with restrained confidence."` uses DinoML's
explicit Base instruction-conditioning API. Instructions stay separate from
spoken text and work with both speaker embeddings and full reference prompts.
Instructions, reference transcripts, and codec content all invalidate cached
renders when changed. Include reference frames, transcript tokens, target text,
and instruction tokens when selecting the generation artifact's prompt capacity.

The local dynamic-tokenizer development checkout is selected through the
ignored `.cargo/config.toml` patch. The published dependency pin includes the
Base instruction API; the dynamic tokenizer changes currently live in the
local DinoML checkout.

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
