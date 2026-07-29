---
name: ghostline-localization-audio
description: Use for Ghostline subtitle and voiceover map alignment, voice design or cloning, WAV/WEM handling, localization JSON resources, and gq000_01 dialogue localization maintenance.
---

# Ghostline Localization And Audio Workflow

## Alignment Rules

- Read `quests/story/ghostline/gq000/implementation/runtime-flow.md` for the three distinct journal/UI, spoken
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
  `source/raw/mod/gq000/localization/en-us/subtitles/gq000_01.json.json`
- subtitles packed:
  `source/archive/mod/gq000/localization/en-us/subtitles/gq000_01.json`
- ArchiveXL subtitle map raw:
  `source/raw/mod/gq000/localization/en-us/subtitles/gq000_01_subtitles_map.json.json`
- ArchiveXL subtitle map packed:
  `source/archive/mod/gq000/localization/en-us/subtitles/gq000_01_subtitles_map.json`
- VO raw:
  `source/raw/mod/gq000/localization/en-us/vo/gq000_01.json.json`
- VO packed:
  `source/archive/mod/gq000/localization/en-us/vo/gq000_01.json`

Quest-specific onscreens should live under
`source/archive/mod/gq000/localization/en-us/onscreens` and be registered in
`source/resources/Ghostline.archive.xl`.

## Scene And Localization Generation

The removed root-level scene/localization generator and scene template are not
part of the current workflow. Regenerate `gq000_patch_meet.scene` through
`tools/generate_scene.py` and
`quests/story/ghostline/gq000/implementation/scenes/patch-meet.scene-spec.json`, checked by its validator and
`tests/test_generate_scene.py`.

For spoken dialogue text or audio changes, keep subtitle entries, VO map
entries, `quests/story/ghostline/gq000/script/gq000_01_manifest.json`, and spoken scene-line
`locstringIds` aligned, regenerate the scene through the current spec, then
convert changed raw CR2W-JSON with the WolvenKit workflow in
`agent/skills/ghostline-wolvenkit-cr2w/SKILL.md`.

## Voice Generation And WEM Conversion

- Shared Patch and V speaker embeddings live under
  `quests/story/ghostline/shared/voice/embeddings`. SafeTensors files are
  canonical; do not reintroduce pickle-backed PyTorch copies.
- Voice audition generation is an explicit external authoring step, not a
  repository build command. Audition candidates and record the selected file
  in the quest-owned voice-selection manifest.
- For the Player Character, V, use voice clone only.
- For custom characters, design a voice first, then clone it for repeated use.
- Cyberpunk stores voiceovers as Wwise `.wem` resources in archives.
- Voiceover `.json` resources map subtitle String IDs to voice files.
- Generate localization CR2W-JSON from the quest-owned dialogue manifest, then
  convert and validate it before use.

Use `tools/convert_wavs_to_wem.ps1` to convert quest WAV voiceover files into
Wwise `.wem` files. Authored selections live in each quest's `voice/source`
directory; audition candidates and other generated outputs do not belong
there. By default the script reads
`quests/story/ghostline/gq000/voice/source` and
`quests/story/ghostline/gq000/script/gq000_01_manifest.json`, selects only its
13 referenced basenames, normalizes them into
`wwise_conversion\ExternalSources`, writes
`external_sources.wsources`, runs Wwise external-source conversion, and copies
the results to `source/archive/mod/gq000/localization/en-us/vo` without deleting
the source WAVs.

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
