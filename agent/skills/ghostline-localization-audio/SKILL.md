---
name: ghostline-localization-audio
description: Use for Ghostline subtitle and voiceover map alignment, voice design or cloning, WAV/WEM handling, localization JSON resources, and gq000_01 dialogue localization maintenance.
---

# Ghostline Localization And Audio Workflow

## Alignment Rules

- Read `docs/quest-scene-flow.md` for the three distinct journal/UI, spoken
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

## Legacy Generator Status

`create_files.py` and `template.scene.json` are legacy generation references.
Do not use them to regenerate the current `gq000_patch_meet.scene` graph,
dialogue sections, choice nodes, or scene timing. The established scene path is
`tools/generate_scene.py` plus
`tools/gq000_patch_meet.scene-spec.json`, checked by its validator and
`tests/test_generate_scene.py`.

The legacy generator previously wrote:

- subtitles
- VO map data
- `source/raw/gq000_01_manifest.json`

It also wrote scene dialogue/options and section/choice node IDs, but that
output is not safe for current scene work.

The legacy generator expects WAV files in
`source/archive/mod/gq000/localization/en-us/vo`. If a WAV named after a line
key exists, it renames it to the hashed actor filename.

`create_files.py` uses random dialogue gaps when building section timing, so
reruns can change generated scene timing even with the same dialogue. Treat
that as another reason not to use it for the active scene graph.

For spoken dialogue text or audio changes, keep subtitle entries, VO map
entries, `source/raw/gq000_01_manifest.json`, and spoken scene-line
`locstringIds` aligned, regenerate the scene through the current spec, then
convert changed raw CR2W-JSON with the WolvenKit workflow in
`agent/skills/ghostline-wolvenkit-cr2w/SKILL.md`.

## Voice Generation And WEM Conversion

- `voice_generate.py` is a hard-coded experimental candidate generator, not a
  build step. It emits three semantic-key WAV candidates per line in the
  working directory; audition, select, and rename one to the manifest-derived
  actor/hash basename manually.
- For the Player Character, V, use voice clone only.
- For custom characters, design a voice first, then clone it for repeated use.
- Cyberpunk stores voiceovers as Wwise `.wem` resources in archives.
- Voiceover `.json` resources map subtitle String IDs to voice files.
- Ghostline's legacy generator starts from WAV inputs, then prepares CR2W-JSON
  localization resources that must be converted before use.

Use `tools/convert_wavs_to_wem.ps1` to convert quest WAV voiceover files into
Wwise `.wem` files. The current authored WAV bank is temporarily tracked under
`generated` as 13 current/legacy duplicate pairs. By default the script reads
`source/raw/gq000_01_manifest.json`, selects only its 13 referenced basenames,
normalizes them into `wwise_conversion\ExternalSources`, writes
`external_sources.wsources`, runs Wwise external-source conversion, and copies
the results to `source/archive/mod/gq000/localization/en-us/vo` without deleting
the source WAVs.

```powershell
.\tools\convert_wavs_to_wem.ps1 -NoCopy
```

Inspect and compare those outputs before running the command without `-NoCopy`
to intentionally replace the 13 active WEMs. `-SourceDir`, `-DestinationDir`,
and the mandatory nonempty `-Manifest` support an alternate dialogue set. Do
not convert every WAV in `generated`: the 13 legacy hash-name files are
byte-identical source duplicates, and their WEM counterparts are currently
retained only for archive-baseline parity.

Useful docs:

- `modding_docs/for-mod-creators-theory/files-and-what-they-do/audio-files.md`
- `modding_docs/modding-guides/sound`
