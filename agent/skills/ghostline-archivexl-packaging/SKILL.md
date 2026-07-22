---
name: ghostline-archivexl-packaging
description: Use for Ghostline ArchiveXL registration, resource patching, localization/journal/streaming declarations, custom ArchiveXL tags, packaging, load order, and in-game registration troubleshooting.
---

# Ghostline ArchiveXL And Packaging Workflow

Read `docs/packaging.md` before building or installing an archive, and use
`agent/skills/ghostline-wolvenkit-cr2w/SKILL.md` to synchronize changed raw
CR2W assets first. This file records ArchiveXL ownership rules; the packaging
document owns the exact scoped build, extraction, payload-hash, and staging
procedure.

## ArchiveXL Resources

- `source/resources/Ghostline.archive.xl` is the ArchiveXL registration file.
- Keep `Ghostline.archive.xl` in `source/resources`. A full WolvenKit project
  build may stage it beside the archive, but the current manual scoped pack
  does not; copy it separately into the install/ZIP tree so ArchiveXL can
  process it.
- Use `quest: phases:` entries to attach Ghostline root questphases to the
  game, usually with `mod\gq000\phases\gq000.questphase` parented to
  `base\quest\cyberpunk2077.quest`.
- Add a Phantom Liberty standalone parent only when the quest is intended to
  initialize from PL standalone starts.
- Use `localization: onscreens:` entries to register custom onscreen
  translation JSON files.
- The current `localization: subtitles:` registration is
  `mod\gq000\localization\en-us\subtitles\gq000_01_subtitles_map.json`.
- The current `localization: vomaps:` registration is
  `mod\gq000\localization\en-us\vo\gq000_01.json`.
- Tweak fields like `displayName`, `fullDisplayName`, and faction
  `localizedName` should have matching globally unique `secondaryKey` entries,
  with `primaryKey` left as `0` for ArchiveXL-generated keys.
- Use `journal:` entries when adding custom journal resources.
- Use `streaming: blocks:` entries when adding world streaming blocks.
- Use `py .\tools\explore_world.py blocks` to inspect reference
  `.streamingblock` descriptors before shaping custom world registrations.
- Use `resource: patch:` for ArchiveXL resource patching instead of directly
  overwriting shared `.ent`, `.app`, or `.mesh` files when adding small changes
  to existing resources.
- Use `resource: link:` when multiple depot paths should resolve to the same
  resource, especially to avoid duplicate meshes for dynamic substitutions.
- Custom ArchiveXL tags live under `overrides: tags:` in `.xl` files, not in
  TweakXL YAML.
- ArchiveXL tags are case-sensitive, and component names should be unique.

Check `Cyberpunk 2077\red4ext\plugins\ArchiveXL\ArchiveXL.log` when `.xl`
registrations, localization, journals, streaming, or resource patches do not
appear in game.

Useful docs:

- `modding_docs/for-mod-creators-theory/core-mods-explained/archivexl`
- `modding_docs/for-mod-creators-theory/core-mods-explained/archivexl/archivexl-resource-patching`
- `modding_docs/for-mod-creators-theory/core-mods-explained/tweakxl`

## Packing And Load Order

- A manual `WolvenKit.CLI pack .\source\archive` build contains only archive
  payloads. It does not copy `source/resources/Ghostline.archive.xl`, TweakXL
  YAML, REDscript, or config files; stage those separately as documented in
  `docs/packaging.md`.
- A scoped pack from a directory named `archive` normally produces
  `archive.archive`. List and extract that file, compare extracted payload
  hashes with `source/archive`, and only then rename/stage it as
  `Ghostline.archive`.
- Do not pack from the repository root. That can sweep raw, reference,
  generated, tooling, and documentation paths into the archive.

- Cyberpunk loads legacy `.archive` mods from
  `Cyberpunk 2077/archive/pc/mod` in ASCII-alphabetical order by archive
  filename.
- REDmods under `Cyberpunk 2077/mods` load after legacy archive mods and also
  use ASCII ordering by mod folder unless REDmod load order is explicitly
  supplied.
- File conflicts are handled per resource path, and the first mod to change a
  file wins.
- Ghostline should avoid conflicts by using mod-owned paths unless
  intentionally overriding a base or dependency resource.
