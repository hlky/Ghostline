# Workspot Rendering And Captioning

Render locally first; provision the captioning GPU only after preview quality
is accepted. The current pipeline produces source-motion mannequin videos,
timestamped contact sheets, source-bound receipts, a review gallery, and
uncaptioned JSONL jobs. It does not call a model or start a Runpod pod.

## Render Pilot

```powershell
py -B tools/workspot_preview.py plan
py -B tools/workspot_preview.py prepare
py -B tools/workspot_preview.py prepare-skin
py -B tools/workspot_preview.py render --seconds 8 `
  --skin-manifest generated/workspots/skinned-assets/skin.json
py -B tools/workspot_catalog.py review
```

The default pilot selects four workspots: phone talk, standing wait, sitting
in a chair, and the Corpo hands-on-knees idle. Up to six unique body clips
per workspot are selected, prioritizing an idle, a variation, an entry, and
an exit before extra variations. The current pilot has 14 jobs. Repeated clips
with the same rig, animation-set registrations and name share one job.

`prepare` extracts only the explicitly registered rig/animation sets from the
vanilla game. WolvenKit is used because the current native JSON reader leaves
animation buffer headers and rig parent arrays opaque. Serialization happens
beside each extracted binary and is copied to mirrored raw paths: WolvenKit's
`-o` folder option flattens filenames and is unsuitable for a depot catalog.

The decoder resolves each name against the selected rig's registered sets,
respecting priority (including the omitted default of 128). It resolves shared
animation chunks and handles WolvenKit's `tempBuffer`, then uses the existing
compressed/SIMD motion decoders. Rig references and joint cardinality must
match after subtracting declared extra synchronization channels, following
WolvenKit's `numJoints - numExtraJoints` body-joint contract. Omitted extra
channel names/counts are retained in the receipt; there is no arbitrary
truncation to a generic 71-joint skeleton. Additive clips
requiring a base pose and unsupported rigs/formats fail explicitly.

The preferred pilot renderer uses the vanilla `man_average` body mesh, its
authored vertex weights, and the 181-bone `man_base_deformations` hierarchy.
Core joint translations, rotations and scales come from the decoded motion,
including finger articulation. Unanimated helper bones retain their rest
offsets beneath animated parents. The source head follows the animated `Head`
transform as a rigid neutral head; facial expressions are not evaluated.
The skinning implementation checks weighted-bone coverage, weight sums and
rest-pose invariance instead of guessing helper-bone mappings.

These meshes use one neutral material to keep the silhouette and movement
legible. Engine muscle/twist corrections, IK, facial performance, props,
furniture, clothing, synchronization partners, scene cameras and workspot
graph blending are not reproduced. A hand near an ear is visible evidence;
the identity of an absent phone is not. Renderer limitations travel with every
caption job. The original ellipsoid mannequin remains available by omitting
`--skin-manifest`, but is not the preferred VLM input.

`prepare-skin` extracts/exports the two vanilla meshes and deformation rig into
ignored `skinned-assets`, records hashes, and sets `withMaterials=false` only
for the child WolvenKit process. It does not change WolvenKit settings or
author a replacement NPC. The current source skin supports `man_base` only;
the renderer rejects a different animation rig rather than silently applying
the wrong body. A female or other body needs its own corresponding mesh/rig
manifest and validation.

Output under ignored `generated/workspots`:

| Path | Purpose |
| --- | --- |
| `preview-plan.json` | Clip jobs and originating workspot entry/role links |
| `preview-assets/{binary,raw}` | Rig-matched dependencies |
| `skinned-assets/skin.json` | Hash-bound source body/head/deformation assets |
| `previews/<id>/decoded.json` | Sampled source joint positions and timestamps |
| `previews/<id>/preview.mp4` | 960×540 mannequin video, default 12 FPS |
| `previews/<id>/contact.png` | Six evenly spaced, timestamped frames |
| `previews/<id>/render.json` | Source, renderer, settings, and output hashes |
| `previews/results.json` | Successful and failed render outcomes |
| `previews/index.html` | Local pilot review gallery |
| `previews/caption-jobs.jsonl` | Media jobs; no model-derived annotations yet |

Default videos show the first eight seconds, or the entire shorter clip.
`--seconds 0` renders a whole clip. Sample timestamps and full source duration
are retained. MP4 playback uses the chosen FPS, not an implicit 30 FPS.
The video frames carry no semantic filename/label overlay, reducing the risk
that captioning merely repeats the asset name. Contact sheets preserve aspect
ratio and label sample times. Resume requires matching source, code, Blender,
settings and output hashes. Per-job failures do not disappear from the report.

The main workspot browser embeds matching previews after `review` is rerun.
It checks media hashes and the originating workspot hash. Copy the `previews`
directory with the HTML when sharing a report containing videos.

To select other resources, pass repeatable full `--workspot` depot paths to
`plan`. `plan --all --max-clips 0` prepares the complete supported human clip
inventory; this can be much larger than the workspot count. Other body rigs,
device/vehicle rigs and full tree execution are outside this first renderer.
`render --limit N` limits a smoke run, while the default processes its plan.
Use a fresh output tree after changing the installed game version.

## Diverse Local Batch

The checked selection in `reference/workspots/render-batches/diversity-v1.json`
selects two representative clips each from twelve further workspots. It covers kneeling, squatting,
lying down, smoking, drinking, eating, tablet/keyboard use, dancing, boxing,
stretching and a wounded ground pose. These category hints come from source
names; they are selection criteria, not reviewed visual annotations.

```powershell
py -B tools/workspot_preview_batch.py expand
py -B tools/workspot_preview_batch.py prepare
py -B tools/workspot_preview_batch.py render --workers 2
py -B tools/workspot_catalog.py review
```

Expansion merges into the existing plan and preserves existing job identities.
Preparation serializes only missing dependencies so cached source hashes remain
stable. Rendering uses the source skin, eight-second excerpts and 12 FPS by
default. The combined plan has 47 clip jobs across 16 workspots, including
earlier samples retained when refining the selection. Failures remain
visible: the chair turn-25 entry and wounded `sit_ground_lean180__rh_on_belly`
name are absent from their respective registered sets.

The batch publisher writes filename-assisted `previews/caption-jobs.jsonl`.
Each job supplies animation name, originating filename, entry role and available
item-action/prop metadata. Its requested JSON separates `observed_motion` from
`inferred_context`, with missing objects and conflicts recorded explicitly.
For example, phone use may be inferred from source metadata without claiming
that a phone is visible. Source hash mismatches reject stale context.

`previews/caption-evaluation-pairs.jsonl` contains both contextual and
`visual_only` inputs for each successful clip, sharing the same media. The
visual-only variant omits semantic names and interaction metadata. Compare
these paired inputs during the model pilot to measure whether filenames improve
usefulness or encourage unsupported details. No captions have been generated.
After updating prompts, `caption-export` refreshes both files without rendering.

## Model Choice (Research: 2026-10-26)

My initial quality candidate is **Qwen/Qwen3.8-27B**. Its official card
documents native image/video input and Transformers compatibility. Use
**Qwen/Qwen3-VL-32B-Instruct** as a comparison candidate because its documented
focus includes spatial perception and video dynamics. For a cheaper throughput
baseline, try **Qwen/Qwen3.5-9B**, which also accepts video. These are candidates,
not measured winners on Ghostline's mannequin renders.

| Candidate | Proposed use | Unquantized weight estimate |
| --- | --- | --- |
| Qwen3.8-27B | First quality pilot | About 54 GB at two bytes/parameter |
| Qwen3-VL-32B-Instruct | Spatial/video comparison | About 64 GB |
| Qwen3.5-9B | Throughput/cost baseline | About 18 GB |

The weight estimates are arithmetic, not total VRAM requirements; vision
processing, activations and KV cache need additional memory. An 80 GB GPU is
a sensible later BF16 pilot target for the larger models. Quantization should
be compared against a BF16 baseline rather than assumed harmless to captions.
Choose actual GPU/price only when rendering is ready and pod creation is
authorized. Use the explicitly requested
[Runpod remote skill](C:/Users/user/.codex/skills/runpod-codex-remote/SKILL.md)
at that boundary.

Run through Transformers with a video-capable processor and conditional
generation model. Pin the actual model revision and tested package versions
on the pod. Start with SDPA for compatibility; investigate specialized kernels
only after correctness and memory use are measured. Model-family-specific
thinking settings and processor classes must follow the pinned model card,
rather than assuming every candidate shares one template.

## Visual Quality Before Captioning

Prefer a continuous skinned human body over the initial segmented mannequin.
Validate hand-to-head contact, seated posture, forward leans and a moving exit
against the decoded joints. Keep the body fully framed at a fixed camera
through each clip; do not re-center each frame and hide displacement.

For occluded actions, add a second body angle and an upper-body/hand view.
Multi-view evidence helps distinguish poses that overlap in a single 2D view;
[VeMo's motion/VLM study](https://proceedings.mlr.press/v306/ji26l.html)
explicitly studies projection ambiguity and rendered-view reliability.
That supports evaluating views, not a claim that any particular mesh guarantees
accurate captions. Compare outputs on the same clips to measure the benefit.

For object use, seated furniture alignment or synchronized actor interactions,
render the referenced props/partners with their placement and animation, or
capture the actual workspot in game if placement verification is needed.
Filename-assisted inference can provide likely interaction context without
rendering furniture, but cannot verify alignment or contact with absent objects.

## Choose Using The Rendered Pilot

Compare models on the same short clips using both filename-assisted and
name-withheld inputs. Include
standing, seated, leaning, crouching, hand-near-face, fidgets, directional
entry/exit motion and failed/ambiguous renders. Supply sampled frame timestamps
and explicit omissions. Use the video for timing/motion and contact sheets for
human inspection; sparse sheets alone can miss brief actions.

Ask for constrained JSON: posture, torso motion, left/right hand position,
leg motion, facing change when visible, displacement, plain-language action,
visible evidence and uncertainties. Require `unknown` where the visual input
cannot support an observation. Keep absent prop identities in the explicitly
inferred field when metadata supports them. Do not request story intent,
emotional state, rig compatibility, engine loop behavior or runtime safety.

Measure agreement with human observations, hallucinated props/actions,
left/right errors, missed movement, valid JSON rate and seconds per clip.
Prefer the smallest candidate that meets the quality threshold. A model's own
confidence is not a calibrated correctness score. Keep raw responses, prompt
version, model revision, media hashes and decoding settings for audit.

Model suggestions belong in a separate annotation layer with a review state.
Do not overwrite `reference/workspots/annotations.json` or promote a proxy
caption to `runtime_verified`. Workspot-level descriptions should aggregate
reviewed clip evidence and explicit tree settings; one eight-second idle
excerpt cannot establish the whole performance.

## Remote Caption Runner

`tools/workspot_caption.py` consumes the exported JSONL and validates video hashes
before loading a model. Use a pinned Hugging Face revision. The initial runner
uses BF16 on one GPU, SDPA, thinking disabled, greedy decoding and 24 sampled
video frames, with a bounded video pixel budget. It saves raw responses, parsed
JSON, full inputs, model/package/code identity, token counts, latency and peak
GPU allocation. Invalid or truncated JSON remains a failed job with its raw
response; accepted suggestions remain `model_suggested_unreviewed`.

The initial remote environment reuses PyTorch 2.9.1+cu128 from the Runpod image
through a virtualenv with system site packages. Tested package installation:
Transformers 5.20.2, Accelerate 1.15.0, matching Torchvision 0.24.1 from the
PyTorch cu128 index, PyAV 16.1.0, Pillow and NumPy. PyAV 19 removes the
`metadata_errors` argument still used by this Torchvision video decoder;
validate decoding before loading the model. Capture the actual installed freeze
alongside a run. An isolated 120 GB workspace accommodates the BF16 checkpoint
and previews; the default 20 GB skill volume does not.

For the fast Gated DeltaNet path install native `flash-linear-attention==0.6.0`,
`fla-core==0.6.0`, `einops`, and `causal-conv1d==1.7.0`. The latter's official
[release](https://github.com/Dao-AILab/causal-conv1d/releases/tag/v1.7.0) has a
CUDA 12 / Torch 2.9 / CPython 3.12 / cxx11 ABI TRUE Linux x86_64 wheel matching
this image, avoiding a source build. Native packages are selected automatically
with the runner's default settings. This is separate from `flash-attn`: SDPA
handles full attention; FLA accelerates recurrent attention. The reference-only
pilot took 128.4 seconds for 363 output tokens and peaked at 52.55 GiB allocated.
Its caption is unreviewed and does not establish accuracy.

The optional `--use-kernels` Hub replacement path is experimental here: it
failed publisher-trust validation for a transitive kernel repository. The
native-package path avoids needing to relax that check. See the
[Transformers architecture notes](https://huggingface.co/docs/transformers/v5.13.0/en/model_doc/qwen3_5)
and [FLA installation instructions](https://github.com/fla-org/flash-linear-attention/blob/main/INSTALL.md).

```bash
HF_HOME=/workspace/hf-cache /workspace/caption-venv/bin/python \
  /workspace/workspot_caption.py \
  --jobs /workspace/workspot-captions/inputs/caption-jobs.jsonl \
  --output /workspace/workspot-captions/pilot.jsonl \
  --revision 1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0 --limit 1
```

Use `--batch-size 4` to process four independent video conversations per
generation call. The tokenizer uses left padding and each video/context stays
in its own conversation; these are padded batches, not packed sequences. Each
output is trimmed at its own EOS before JSON validation, so a shorter answer
cannot inherit another sequence's padding. Receipts record actual batch IDs,
batch wall time, amortized seconds per clip and shared peak GPU allocation.
OOM batches split in half and retry. Resume preserves successful, source-matched
captions across batch-size changes while keeping their original settings.

Runpod allocation check on 2026-10-26: Secure Cloud A100 SXM 80 GB was $1.79/hour
before storage, advertising at least 117 GB RAM. The selected pod received
250 GB RAM, confirmed against its cgroup limit. API listings are minimum offers,
not guarantees that every host has identical RAM. The 55,562,855,904-byte BF16
checkpoint cannot fit entirely in 48 GB VRAM. A 48 GB GPU may use a supported
8-bit method; do not assume the official fine-grained FP8 checkpoint supports
Ampere through the Transformers backend. That path documents compute capability
9+; Q8_0 is a separate GGUF/backend option. CPU offloading is possible but needs
measured end-to-end throughput before selecting it on hourly cost alone.

### vLLM Backend Trial

`tools/workspot_caption_vllm.py` uses offline `LLM.chat` with independent video
conversations and continuous scheduling. It preserves successful inputs from
the Transformers runner, benchmarks the first four videos separately, then
processes remaining jobs in groups of eight. The checkpoint revision, BF16,
24-frame sampling, pixel budget, prompts and 1,024-token cap stay the same.
Benchmark records go to `vllm-benchmark.jsonl`; main results append to
`captions.jsonl`, keeping per-backend settings and raw output.

The trial uses a separate `vllm-venv` with vLLM 0.32.0 and its resolved
PyTorch/CUDA dependencies. On the selected driver (595.91.07), install with
`uv pip install --python /workspace/vllm-venv/bin/python vllm==0.32.0 --torch-backend=auto`,
then run `vllm download-kernels` as documented. Keep the Transformers environment
separate. Count startup compilation and CUDA graph capture separately from
steady-state inference.

```bash
export PATH=/workspace/vllm-venv/bin:/usr/local/cuda/bin:$PATH
HF_HOME=/workspace/hf-cache OMP_NUM_THREADS=1 VLLM_USE_FLASHINFER_SAMPLER=0 \
  /workspace/vllm-venv/bin/python \
  /workspace/workspot_caption_vllm.py \
  --jobs /workspace/workspot-captions/inputs/caption-jobs.jsonl \
  --output /workspace/workspot-captions/captions.jsonl \
  --revision 1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0
```

The runner bounds context at 8,192 tokens, GPU memory utilization at 90%, and
active requests at eight. Local media access is restricted to the input folder;
no HTTP model endpoint is exposed. The official
[Qwen3.8 vLLM recipe](https://recipes.vllm.ai/Qwen/Qwen3.8-27B) covers serving
options and text-serving verification. Video handling follows vLLM's
[multimodal documentation](https://github.com/vllm-project/vllm/blob/main/docs/features/multimodal_inputs.md).
Performance and correctness on these videos require local measurement.

For a larger-batch comparison, `--batch-size 32 --tune-batches 8,16,32 --tune-size 32`
sets engine capacity to 32, warms the engine, and times each request batch size
on the same 32 clips. Prompt-prefix and multimodal caches are reset before each
round. Raw results remain in separate `tuning-batch-*.jsonl` files; the runner
selects the fastest size for which every sample passes caption JSON validation,
records `batch-tuning.json`, then resumes the main caption output. Existing
successful source/model/prompt/frame-matched captions are retained across batch
sizes. Engine/runtime errors still exit for mandatory supervised shutdown.

The streaming supervisor accepts these same tuning options. A `--start-marker`
allows deliberate shutdown-ownership handoff before restarting the engine:
the replacement supervisor must be waiting before terminating the old one,
and its marker is released only after stopping the old GPU process. Never run
two caption engines concurrently on this pod. Archive the previous exact runner,
caption snapshot and log under `history` before replacing them.

The 2026-10-26 cache-isolated comparison on the replacement A100 SXM measured
32 fixed clips: batch 8 took 98.57 seconds (3.08 seconds/clip), batch 16 took
64.82 seconds (2.03 seconds/clip), and batch 32 took 49.63 seconds
(1.55 seconds/clip). All 32 captions passed JSON validation at each size.
The runner selected 32 and resumed main captioning with the prior 80 successes
retained. Report, raw samples and exact runner sources are saved locally under
`generated/workspots/caption-results/full-run/tuning`. Device memory measured
after each round was 74,883 MiB; this is an observed allocation, not a peak claim.

Measured result on 2026-10-26: the vLLM four-clip benchmark took 21.79 seconds.
The remaining 38 clips completed in 114.24 seconds of batch wall time, averaging
3.01 seconds per clip and 143.65 output tokens/second across concurrent requests.
Engine startup took 232.90 seconds separately. Transformers' four-clip batch had
taken 446.77 seconds (111.69 seconds per clip). These are workflow throughput
measurements; processor implementations and generated answer lengths differ.

All 45 main jobs passed JSON validation: seven retained Transformers results and
38 vLLM results. Results, model/package/code identities, logs and media-hash
verification are saved locally in `generated/workspots/caption-results`, with
`completion.json` recording verified pod shutdown. Suggestions remain unreviewed;
valid JSON does not establish factual accuracy or runtime compatibility.

## Full Catalog Batch

```powershell
py -u -B tools/workspot_full_batch.py --workers 2
```

The full batch plans every named body clip for the selected registered base
human rig of each workspot, with no per-workspot clip limit. It prepares source
assets, resolves exact registration priority, and combines jobs only when rig,
resolved animation-set SHA256 and animation name match. The complete source-use
and alias mapping remains in `generated/workspots/full-batch/plan.json`.
This does not render every rig variant: custom/player/prop rigs and workspots
without explicit base-human animation registrations remain explicit coverage gaps.

The initial inventory contains 26,551 registered jobs and 1,478 rig/set resources.
The final number of resolved source renders is measured after preparation.
Missing resources and decode/render failures remain recorded separately.
The existing pilot plan and captions stay available during the expansion.

The matching female source body/head can be prepared independently with
`py -B tools/workspot_full_batch.py --prepare-female-skin`. Source weights,
deformation-bone coverage and rest-pose invariance are checked before publication.
Male pilot assets are reused. Both skins omit facial animation, props, furniture
and partners.

Progress is saved in `full-batch/state.json`, results in `full-batch/results.json`
and the append-only `full-batch/render-results.jsonl`. Each successful clip has a
source/tool-bound `full-batch.json` receipt for resume. Temporary frame PNGs are
removed after successful encoding; videos, contact sheets, decoded inputs and
receipts remain. Preparation requires 30 GiB free and new renders require 15 GiB.
Resume with the same command, ensuring no existing batch runner is active.

Once `full-batch/plan.json` exists, resume without repeating extraction/indexing:

```powershell
py -u -B tools/workspot_full_batch.py --resume-plan --workers 4
```

The throughput update uses four Blender workers with two render threads each,
factory startup and lossless PNG compression level zero. Resolution, 12 FPS,
eight-second excerpts, scene shading and source skinning are unchanged. All 96
frames of a comparison clip were pixel-identical to the earlier renderer.
The same four-clip benchmark took 32.97 seconds with two workers and 17.24 seconds
with four. This is a small local throughput sample, not a full-catalog ETA.
Earlier successful receipts remain reusable; new receipts hash the faster
renderer and wrapper sources. Per-clip frame PNGs are still removed after encoding.

The extent validator measures the largest spatial dimension, so horizontal
lying bodies are accepted while collapsed geometry is rejected. Existing
successful full-batch receipts are admitted across this exact guard-only
change by reconstructing the prior complete decoder source hash. Their original
render identities and media hashes stay intact; an `accepted_identity` and
`validation_migration` record document the compatibility check. Any unrelated
decoder edit produces a different hash and cannot use this migration.

At `ready_for_captioning`, `previews/full-caption-jobs.jsonl` contains only
successful, source-bound renders. Transfer those videos and that job file before
starting the pinned vLLM command above, using `--benchmark-size 0` and a separate
full-run output. The caption runner retains all workspot associations in its
stored input but sends at most four associations/6,000 serialized characters to
the model, avoiding oversized prompts for widely shared clips. Request validation
errors are isolated to their clip; engine errors propagate to the supervisor.

The user subsequently authorized captioning while the final renders finish.
`tools/workspot_caption_stream.py upload --alias SSH_ALIAS` transfers verified
videos in 512-clip TAR batches. Each remote manifest is published atomically
after its media arrives; complete source associations are retained. The uploader
follows the active render results and writes a hash/count-bound `UPLOAD_COMPLETE`
marker only after all successful renders have been uploaded.

`tools/workspot_caption_stream.py supervise --alias SSH_ALIAS --pod-id POD_ID`
waits for the prepared environment and initial upload, then launches the pinned
runner with `--follow --complete-marker ...`. vLLM stays loaded across manifest
updates. It verifies video hashes, processes each input once per run, and exits
after the final manifest is consumed. An exhausted upload queue without a valid
completion marker times out after five minutes, allowing GPU shutdown.

The streaming replacement pod is recorded in `full-batch/caption-session.json`.
The original stopped pod could not restart because its host had no free GPU;
the replacement uses the same A100 SXM 80 GB tier. Uploader and caption supervisor
states are separate (`stream-state.json`, `caption-state.json`). The original
pilot stays intact; full-run results are collected under `caption-results/full-run`
before review publication. Setup uses `tools/workspot_caption_remote_setup.sh`.

On any caption-run exit, including failure, copy results/logs/exact runners and
verify pod shutdown. Do
not delete the pod or retained workspace. The thread heartbeat
`finish-full-workspot-renders-and-vllm-captions` supervises the authorized run and
notifies only on completion or actionable failure.

## Local Caption Review

After a successful full-run collection and verified shutdown, run
`py -B tools/workspot_caption_publish.py`. It checks collected input identities,
video/contact hashes, animation/rig sources and every planned workspot association.
It retains original pilot caption identities, keeps the complete raw run separately,
and publishes the merged review page plus `caption-results/caption-search.sqlite3`.
The database contains captions, all source-bound entry associations and an FTS5
search index; these remain unreviewed model suggestions. Restart the review server
after publication so its in-memory clip map includes the new records. Human notes
and decisions remain in their separate review store.

```powershell
py -B tools/workspot_caption_review.py
```

Open `http://127.0.0.1:8877/caption-results/review.html`. The workspace places
each video beside observed motion, metadata-assisted inference and uncertainties.
Search covers filenames, model descriptions and saved human corrections/notes.
Use the status filter and Previous/Next buttons (or left/right arrows).

Approve, Needs correction and Reject save decisions immediately. Save notes
also stores an optional corrected summary; moving to another clip saves pending
notes first. Reviews persist separately in
`reference/workspots/caption-reviews.json`, with caption identity, media hashes
and originating workspot hashes. Changed captions or previews require re-review;
caption approval never promotes a workspot to runtime verified.

Export reviews downloads a portable JSON copy. `--reviews PATH` selects a
separate review store; `--port` changes the loopback-only server port. A page
served by the earlier static gallery server is read-only: use this review
service to persist decisions. `--build-only` regenerates the page without
starting a server. Building validates caption-to-media and workspot provenance.

## Validation And Sources

```powershell
py -B -m unittest discover -s tests -p 'test_workspot*.py' -v
py -B -m ruff check tools/workspot*.py tests/test_workspot*.py
```

- [Qwen3.8-27B official model card](https://huggingface.co/Qwen/Qwen3.8-27B).
- [Qwen3-VL-32B-Instruct official model card](https://huggingface.co/Qwen/Qwen3-VL-32B-Instruct).
- [Qwen3.5-9B official model card](https://huggingface.co/Qwen/Qwen3.5-9B).
- [Transformers Qwen3.5 architecture and multimodal usage](https://huggingface.co/docs/transformers/main/model_doc/qwen3_5).
- Local `WolvenKit/WolvenKit.RED4/Archive/IO/AnimationReader.cs` for shared
  chunk addresses and temporary buffers; `animAnimSetupEntry.cs` for the
  priority default; `Types/ClassesExt/CustomData/animAnimationBufferCompressed.cs`
  for compressed key layout; `tools/sex_rid_preview.py` for reused decoders.
