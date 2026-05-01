# Packaging And Install Notes

This document keeps packaging command usage and install layout details out of
`README.md` and `ROADMAP.md`.

## Safe Pack Scope

Do not pack from the repo root. `WolvenKit.CLI build .` succeeds, but it has
previously packed support paths such as `reference`, `source/raw`, `generated`,
`GraphEditorStates`, `tools`, and `modding_docs` into the archive.

Pack from `source/archive` so the archive namespace only contains intended
depot paths:

```powershell
WolvenKit.CLI pack .\source\archive -o <out>
```

Expected depot roots in a scoped archive are:

- `mod\gq000\...`
- `mod\ghostline\...`
- `base\...` only if a specific test or validated dependency requires it.

## Base-Path Override Risk

`source/archive/base` currently contains copied
`base\characters\head\player_base_heads\player_man_average\...` resources.
Those are global base-path overrides and should not ship in the normal install
archive unless their impact on player/base NPC resources has been validated.

The no-base runtime probe still crashed, so these overrides are not the sole
cause of the current crash. They remain a packaging risk.

## Minimal Install Layout

Install the scoped archive as:

```text
Cyberpunk 2077\archive\pc\mod\Ghostline.archive
```

Install ArchiveXL registration beside it:

```text
Cyberpunk 2077\archive\pc\mod\Ghostline.archive.xl
```

Install TweakXL records under:

```text
Cyberpunk 2077\r6\tweaks\Ghostline
```

The TweakXL source tree is:

```text
source\resources\r6\tweaks\ghostline
```

## Runtime Checks

Check these after each install:

- `Cyberpunk 2077\red4ext\plugins\ArchiveXL\ArchiveXL.log`
- TweakXL load output
- ArchiveXL streaming block registration
- subtitle and VO map merge lines
- Patch or Judy community spawn, depending on the current isolation setup
- trigger progression
- journal and mappin visibility
- subtitles and voice playback

## CR2W Verification

After writing raw CR2W-JSON back into `source/archive` as CR2W resources,
verify packed resources start with the `CR2W` magic before packaging. The
current generated world resources were verified this way with WolvenKit.CLI
8.17.4.
