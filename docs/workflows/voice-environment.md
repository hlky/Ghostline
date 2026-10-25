# Voice environment

Use `ghostline-voice` for Ghostline voice design, reference encoding, cloning,
and localization. Establish a compatible tool/artifact set before a batch or
rebuild. The GQ004 session found existing full-length artifacts only after
several searches, and a newer DinoML runtime rejected the working decoder's
`ck_conv1d_weight` storage. An artifact's existence does not prove compatibility
or sufficient prompt/frame capacity.

## Preserved project-local bundle

The ignored `.local/voice/artifacts/` directory contains real copies of the
six working compiled model artifact bundles, independent of their original
Facet and generated-voice folders:

- Base and VoiceDesign generation artifacts;
- their respective decoder artifact bundles;
- the static reference encoder and a speaker encoder.

Each artifact retains its own runtime files and `lib` directory. The global
native-library catalogue, checkpoints, reference inputs, executable, and Python
environment continue to use their existing locations in the quest toolchain.
The cache contains about 1.3 GiB of compiled model artifacts.

`tools/voice-artifacts.json` records the original sources, cache destinations,
hardware/runtime compatibility, and excluded regenerable directories.
`tools/voice-artifacts.lock.json` records every copied file's size and SHA-256.
The large payloads remain ignored. These are compiled ROCm/gfx1201 artifacts;
their recorded architecture and compiled layouts still matter on another GPU.

Run from the repository root:

```powershell
.venv/Scripts/python.exe tools/cache_voice_artifacts.py plan
.venv/Scripts/python.exe -u tools/cache_voice_artifacts.py copy
.venv/Scripts/python.exe -u tools/cache_voice_artifacts.py verify
```

`plan` inventories sources and required space; `copy` verifies original and
copied bytes before publishing the lock. Existing differing copies are rejected.
`verify` reads only the cache and lock, so original artifact folders are not
needed for that check. Interrupted `.copying` files require inspection before
retrying. Regenerable artifact debug output is excluded; each bundle's runtime
assets and libraries remain.
The copy preserves input bytes and does not rebuild or transform the artifacts.

The [2026-10-25 cache check](../../projects/ghostline/quests/gq004/voice/artifact-cache-check.json)
records verification of all six bundles and a successful one-line full-reference
synthesis with local artifacts and the existing checkpoint/native libraries.
The smoke candidate was not promoted to reviewed quest audio.

The GQ004 [toolchain](../../projects/ghostline/quests/gq004/voice/toolchain.json)
selects the cached artifacts by repository-relative path. Checkpoint and
native-library paths remain explicit, including `H:/dinoml-native-libraries`.
Candidate audio remains under ignored
`generated-voices/gq004`; approved source WAVs stay beside the quest.

## Preflight and compatibility

Before producing a new batch:

1. Check the cache against the lock. Read artifact metadata for prompt tokens,
   generation frames, encoder sample limits, backend and architecture. GQ004's
   generation profile is p256/f288; the decoder supports f256 and its static
   reference encoder takes exactly 190048 samples. Tiny qualification artifacts
   are unsuitable for full reference performances.
2. Establish the environment from the recorded workstation setup. The cache
   preserves compiled artifact bundles; it does not copy checkpoints, the
   global native libraries, executable, PyTorch venv, system GPU driver or SDK.
   GQ004 records the PowerShell profile
   and alignment Python in its toolchain. Source that profile explicitly when
   the shell has not already initialized the ROCm runtime.
3. Use each performer's reviewed conditioning method. Full reference requires
   the exact transcript, codec data, and embedding; preserve those together.
   Design a custom character reference first. V uses reviewed cloning inputs.
4. Render and listen to a short candidate using the intended tool,
   checkpoint, cached artifacts, and reference before a full batch. Keep it outside
   approved source and record the recipe/result. File hashes establish copy
   integrity; playback establishes that the combination actually runs.

Treat the preserved bundle as a compatibility baseline. For a new runtime,
create a separately named bundle and prove it before switching the recipe.
GQ004's build wrapper still requires the recorded compatible DinoML source
checkout/commit and existing native libraries for rebuilding. Check that pairing
before replacing a working executable. Python/SDK/source availability for a
rebuild remains separate from cached inference artifacts.

See [GQ004 voice production](../../projects/ghostline/quests/gq004/voice/README.md)
for the selected reference, audition approvals, and lipsync/WEM workflow.
