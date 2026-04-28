---
name: ghostline-localization-audio
description: Use for Ghostline dialogue generation, subtitle and voiceover map alignment, voice design or cloning, WAV/WEM handling, localization JSON resources, and gq000_01 conversation regeneration.
---

# Ghostline Localization And Audio Workflow

## Alignment Rules

- Scene `locstringIds`, subtitle entries, and voiceover map entries must stay
  aligned.
- The subtitle String ID is the stable link between on-screen dialogue text and
  the voiceover resource.
- Use `py .\tools\explore_localization.py check` to verify subtitle/VO map
  coverage before packaging dialogue changes.

Current `gq000_01` dialogue localization files:

- subtitles raw:
  `source/raw/mod/gq000/localization/en-us/subtitles/gq000_01.json.json`
- subtitles packed:
  `source/archive/mod/gq000/localization/en-us/subtitles/gq000_01.json`
- VO raw:
  `source/raw/mod/gq000/localization/en-us/vo/gq000_01.json.json`
- VO packed:
  `source/archive/mod/gq000/localization/en-us/vo/gq000_01.json`

Quest-specific onscreens should live under
`source/archive/mod/gq000/localization/en-us/onscreens` and be registered in
`source/resources/Ghostline.archive.xl`.

## Generator

Run this from the repo root to generate the `gq000_01` conversation resources
from `template.scene.json`:

```powershell
python .\create_files.py
```

The generator writes:

- subtitles
- VO map data
- scene dialogue/options
- section and choice node ids
- `source/raw/gq000_01_manifest.json`

The generator expects WAV files in
`source/archive/mod/gq000/localization/en-us/vo`. If a WAV named after a line
key exists, it renames it to the hashed actor filename.

`create_files.py` uses random dialogue gaps when building section timing, so
reruns can change generated scene timing even with the same dialogue.

The generator writes CR2W-JSON files, not game-ready CR2W binaries. Convert
them before use with the WolvenKit workflow in
`agent/skills/ghostline-wolvenkit-cr2w/SKILL.md`.

## Voice Generation And WEM Conversion

- `voice_generate.py` is the voice design and voice clone process.
- For the Player Character, V, use voice clone only.
- For custom characters, design a voice first, then clone it for repeated use.
- Cyberpunk stores voiceovers as Wwise `.wem` resources in archives.
- Voiceover `.json` resources map subtitle String IDs to voice files.
- Ghostline's generator starts from WAV inputs, then prepares CR2W-JSON
  resources that must be converted before use.

Use `tools/convert_wavs_to_wem.ps1` to convert quest WAV voiceover files into
Wwise `.wem` files. The script normalizes WAVs into
`wwise_conversion\ExternalSources`, writes `external_sources.wsources`, runs
Wwise external source conversion, and copies WEM files back into the VO folder
without deleting the source WAVs.

```powershell
.\tools\convert_wavs_to_wem.ps1
```

Useful docs:

- `modding_docs/for-mod-creators-theory/files-and-what-they-do/audio-files.md`
- `modding_docs/modding-guides/sound`
