---
name: ghostline-localization-audio
description: Use for Ghostline subtitle and voiceover map alignment, voice design or cloning, WAV/WEM handling, localization JSON resources, and gq000_01 dialogue localization maintenance.
---

# Ghostline Localization And Audio Workflow

## Alignment Rules

- Read `projects/ghostline/quests/gq000/implementation/runtime-flow.md` for the three distinct journal/UI, spoken
  dialogue, and embedded choice-label lookup paths.
- Spoken scene-line `locstringIds`, subtitle entries, and voiceover map entries
  must stay aligned.
- The subtitle String ID is the stable link between on-screen dialogue text and
  the voiceover resource.
- Choice labels do not resolve through the subtitle or VO maps and
  `scnChoiceNodeOption.caption` is not authoritative display text. They resolve
  through `screenplayStore.options` and the scene's embedded `locStore`.
- Embedded choice descriptors must be grouped into configured locale blocks
  and sorted inside each block by unsigned numeric `locstringId`. Preserve the
  two adjacent `db_db` variants per choice: blank fallback first, source text
  second.
- Keep scene event and locStore variant RUIDs as full unsigned 64-bit values;
  do not apply a signed-63-bit mask.
- Use `py .\tools\explore_localization.py check` to verify subtitle/VO map
  coverage before packaging dialogue changes.

Current `gq000_01` dialogue localization files:

- subtitles raw:
  `projects/shared/ghostline-runtime/source/raw/mod/gq000/localization/en-us/subtitles/gq000_01.json.json`
- subtitles packed:
  `projects/shared/ghostline-runtime/source/archive/mod/gq000/localization/en-us/subtitles/gq000_01.json`
- ArchiveXL subtitle map raw:
  `projects/shared/ghostline-runtime/source/raw/mod/gq000/localization/en-us/subtitles/gq000_01_subtitles_map.json.json`
- ArchiveXL subtitle map packed:
  `projects/shared/ghostline-runtime/source/archive/mod/gq000/localization/en-us/subtitles/gq000_01_subtitles_map.json`
- VO raw:
  `projects/shared/ghostline-runtime/source/raw/mod/gq000/localization/en-us/vo/gq000_01.json.json`
- VO packed:
  `projects/shared/ghostline-runtime/source/archive/mod/gq000/localization/en-us/vo/gq000_01.json`

Quest-specific onscreens should live under
`projects/shared/ghostline-runtime/source/archive/mod/gq000/localization/en-us/onscreens` and be registered in
`projects/shared/ghostline-runtime/source/resources/Ghostline_Runtime.archive.xl`.

## Scene And Localization Generation

Review the final staged onscreen resource after all generators and staging
steps. A stale source copy can overwrite newly generated objective strings
while both individual files remain valid. Verify the final journal's referenced
secondary keys against that staged resource, not only the generator output.

The removed root-level scene/localization generator and scene template are not
part of the current workflow. Regenerate `gq000_patch_meet.scene` through
`tools/generate_scene.py` and
`projects/ghostline/quests/gq000/implementation/scenes/patch-meet.scene-spec.json`, checked by its validator and
`tests/test_generate_scene.py`.

For spoken dialogue text or audio changes, keep subtitle entries, VO map
entries, `projects/ghostline/quests/gq000/script/gq000_01_manifest.json`, and spoken scene-line
`locstringIds` aligned, regenerate the scene through the current spec, then
convert changed raw CR2W-JSON with the WolvenKit workflow in
`agent/skills/ghostline-wolvenkit-cr2w/SKILL.md`.

## Voice Generation And WEM Conversion

- Follow [voice environment](../../../docs/workflows/voice-environment.md) before
  rebuilding tools or rendering a batch. Use `ghostline-voice`, preserve the
  working artifact/runtime pairing, and check a short synthesis first. The
  project-local cache is ignored; its inventory and recipes are tracked.
- Review the full player-facing dialogue flow before bulk VO. Record the
  required action/read state and speaker readiness; use the performer's
  reviewed conditioning recipe rather than silently switching to embedding-only.
- Shared Patch and V speaker embeddings live under
  `projects/ghostline/quests/shared/voice/embeddings`. SafeTensors files are
  canonical; do not reintroduce pickle-backed PyTorch copies.
- Voice audition generation is an explicit external authoring step, not a
  repository build command. Audition candidates and record the selected file
  in the quest-owned voice-selection manifest.
- For the Player Character, V, use voice clone only.
- For custom characters, design a voice first, then clone it for repeated use.
- Extract reference WAV/FLAC speaker embeddings through `ghostline-voice
  extract-embedding`, using the Base checkpoint's `model.safetensors` and a
  trusted speaker-encoder artifact. Store canonical `.safetensors` outputs;
  `convert-embedding` can produce DinoML JSON when required.
- For multi-reference auditions, compare concatenated audio against
  `ghostline-voice merge-embeddings` (equal-weight arithmetic mean of
  same-speaker embeddings) using identical text, seeds, and sampling settings.
  Keep a single-reference baseline and separate candidate output directories.
  A 30-second reference exceeds a 2,048-mel-frame speaker artifact; use a
  sufficiently large artifact (4,096 frames supports about 43 seconds).
- Cyberpunk stores voiceovers as Wwise `.wem` resources in archives.
- Full reference-conditioned cloning uses `ghostline-voice encode-reference`
  with a bounded-variable speech-tokenizer artifact, then `render-local
  --reference-prompts` with exact transcripts and codec assets by speaker.
  Keep normal VO and `vo_holocall` depot folders separate when preparing WAVs.
  Normal `vo` does not guarantee an unfiltered or healthy performance. Inspect
  scene provenance as well as the expression tag: Songbird's coffee line is in
  normal `vo` but belongs to `q301_00_holocall_hook.scene`; her spaceport ride
  dialogue is also unsuitable for a healthy neutral reference. Prefer physical,
  calm conversations and audition the source; compare original exported audio
  with the resampled model reference when filtering is suspected.
- `render-local --instruction` uses DinoML's explicit Base delivery instruction
  API. Keep instructions separate from the words to speak. Reference context
  and instructions both consume generation prompt capacity.
- Voiceover `.json` resources map subtitle String IDs to voice files.
- Generate localization CR2W-JSON through `ghostline-voice localize` or its
  `localize-manifest` command. `tools/generate_dialogue_localization.py` is a
  compatibility adapter to that same writer. Both shared and explicit
  male/female audio paths are preserved. Pure localization supports Cargo's
  `--no-default-features` option; convert and validate before use.

Use `tools/convert_wavs_to_wem.ps1` to convert quest WAV voiceover files into
Wwise `.wem` files. Authored selections live in each quest's `voice/source`
directory; audition candidates and other generated outputs do not belong
there. By default the script reads
`projects/ghostline/quests/gq000/voice/source` and
`projects/ghostline/quests/gq000/script/gq000_01_manifest.json`, selects only its
13 referenced basenames, normalizes them into a run directory below
`wwise_conversion\ExternalSources`, writes a run-local
`external_sources.wsources`, and runs Wwise external-source conversion into a
fresh directory below `converted`. It checks every expected WEM before
publishing the complete set to `projects/shared/ghostline-runtime/source/archive/mod/gq000/localization/en-us/vo`
with rollback on replacement failure, without deleting the source WAVs.

```powershell
.\tools\convert_wavs_to_wem.ps1 -NoCopy
```

Inspect and compare those outputs before running the command without `-NoCopy`
to intentionally replace the 13 active WEMs. `-SourceDir`, `-DestinationDir`,
and the mandatory nonempty `-Manifest` support an alternate dialogue set. Do
not convert audition candidates or a general build-output directory.

Useful docs:

- `modding_docs/for-mod-creators-theory/files-and-what-they-do/audio-files.md`
- `modding_docs/modding-guides/sound`
