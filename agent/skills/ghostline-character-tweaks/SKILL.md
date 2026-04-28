---
name: ghostline-character-tweaks
description: Use for Ghostline character resources, Patch NPC work, entity and appearance files, TweakXL YAML records, custom factions, and keeping entity/template/localization references in sync.
---

# Ghostline Character And Tweak Workflow

## Character Resources

- `.ent` files are top-level entity containers.
- For NPCs, the root `.ent` is the game entry point and lists appearances that
  resolve into `.app` files.
- `.app` files hold appearance definitions and per-appearance components.
- Components on the root `.ent` are shared across appearances.
- Components in the `.app` are appearance-specific.
- For Patch, keep the root `.ent` and referenced `.app` appearance names in
  sync with the TweakDB `entityTemplatePath` and character record.

Patch resources:

- packed root entity: `source/archive/mod/ghostline/characters/patch/patch.ent`
- packed appearance: `source/archive/mod/ghostline/characters/patch/patch.app`
- raw root entity: `source/raw/mod/ghostline/characters/patch/patch.ent.json`
- raw appearance: `source/raw/mod/ghostline/characters/patch/patch.app.json`
- supporting body/head files live under
  `source/archive/mod/ghostline/characters/patch/body` and
  `source/archive/mod/ghostline/characters/patch/head`.

Generic Ghostline onscreen localization:

- packed: `source/archive/mod/ghostline/localization/en-us/onscreens/ghostline.json`
- raw: `source/raw/mod/ghostline/localization/en-us/onscreens/ghostline.json.json`
- includes Patch's display name and the Ghostline faction name.

Use `tools/explore_ent_app.py` from `README.md` to inspect entity and
appearance resources.

## TweakXL Resources

- `source/resources/r6/tweaks` is part of the mod.
- `source/resources/r6/tweaks/ghostline/character_patch.yaml` defines the
  custom NPC.
- `source/resources/r6/tweaks/ghostline/faction_ghostline.yaml` defines the
  custom Ghostline faction.
- TweakXL loads `.yaml` or `.tweak` files from Cyberpunk's `r6/tweaks`; in this
  WolvenKit project, author them under `source/resources/r6/tweaks`.
- Tweak YAML is indentation-sensitive. Use 2 spaces, not tabs.
- Tweak record names must be unique.
- Do not base Ghostline records on generated `inlineX` records, because those
  names can shift between game updates.
- When editing NPC tweak records, prefer copying structure from a working
  base-game example in WolvenKit's Tweak Browser.

Important NPC fields include:

- `entityTemplatePath`
- `displayName`
- `fullDisplayName`
- `voiceTag`
- `baseAttitudeGroup`
- `archetypeData`
- `affiliation`

Useful docs:

- `modding_docs/for-mod-creators-theory/files-and-what-they-do/file-formats/entity-.ent-files`
- `modding_docs/for-mod-creators-theory/files-and-what-they-do/file-formats/appearance-.app-files`
- `modding_docs/for-mod-creators-theory/core-mods-explained/tweakxl`
