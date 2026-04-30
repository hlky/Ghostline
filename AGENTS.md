# Ghostline Agent Guide

Ghostline is a Cyberpunk 2077 WolvenKit quest-mod repo. Keep this file as the
always-loaded routing layer; task-specific instructions live in repo-local
skill-style files under `agent/skills`.

## First Rules

- Work from the repository root unless a command says otherwise.
- Read `ROADMAP.md` before broad quest, world, journal, scene, or packaging
  work. Update it when work changes quest status, adds or removes resources,
  resolves a listed gap, or discovers a new blocker.
- Treat `modding_docs` as a local reference submodule, not Ghostline-owned
  source, unless the task explicitly asks to edit those docs.
- Before guessing at Cyberpunk-specific behavior, search or read
  `modding_docs`.
- Do not edit `source/archive` resources as text. They are CR2W binaries,
  including resource paths ending in `.json`.
- Edit `source/raw` CR2W-JSON when changing packed resources. The exception is
  `source/raw/gq000_01_manifest.json`, which is a plain generated manifest and
  is not serialized back to CR2W.
- Prefer `source/raw` over `generated` when preparing CR2W assets for use.
  `generated` contains older/generated snapshots.
- Treat `GraphEditorStates` as WolvenKit editor support data, not packed asset
  source of truth.

## Repo-Local Skill Files

Read only the relevant file(s) for the task:

- `agent/skills/ghostline-wolvenkit-cr2w/SKILL.md` - WolvenKit CLI,
  CR2W/raw conversion, and verification.
- `agent/skills/ghostline-quest-journal-scene/SKILL.md` - questphases,
  scenes, journal paths, and `gq000` quest UI resources.
- `agent/skills/ghostline-character-tweaks/SKILL.md` - Patch character
  resources, `.ent`/`.app` structure, and TweakXL records.
- `agent/skills/ghostline-localization-audio/SKILL.md` - subtitle/VO
  alignment, generator behavior, voice design, and WEM conversion.
- `agent/skills/ghostline-archivexl-packaging/SKILL.md` - ArchiveXL
  registration, resource patching, streaming blocks, and load order.

These are repo-local skill-style notes. They are not automatically installed
global Codex skills, so use the paths above as explicit references.

## Project Map

- `source/archive` contains packed/game-ready CR2W resources.
- `source/resources` contains WolvenKit loose resources, including ArchiveXL
  `.xl` files and TweakXL YAML files copied during packing.
- `source/archive/base` may contain supporting base-game files. It currently
  contains base player-head mesh and morphtarget support resources.
- `source/archive/mod` contains mod-owned packed resources.
- `source/archive/mod/ghostline` contains generic Ghostline resources shared
  across the quest series, such as characters.
- `source/archive/mod/ghostline/characters/patch` contains Patch's custom NPC
  template set.
- `source/archive/mod/gq000` contains the first Ghostline quest. `gq` means
  Ghostline quest, and `000` identifies the first quest.
- `source/archive/mod/gq000/phases` contains the main and stage questphase
  resources.
- `source/archive/mod/gq000/scenes` contains scene resources for dialogue,
  interactions, animations, and related scene work.
- `source/archive/mod/gq000/localization/en-us` contains quest subtitles,
  voiceover maps, and quest-specific onscreen localization.
- `reference/journal` contains serialized base-game `.journal` reference
  slices.
- `reference/world` contains reference `.streamingblock` and
  `.streamingsector` CR2W binaries plus their `.json` CR2W-JSON companions.

## Local Modding Docs

Useful starting points:

- `modding_docs/SUMMARY.md`
- `modding_docs/for-mod-creators-theory/modding-tools/wolvenkit.md`
- `modding_docs/for-mod-creators-theory/files-and-what-they-do/file-formats/quests-.scene-files`
- `modding_docs/modding-guides/quest`
- `modding_docs/for-mod-creators-theory/files-and-what-they-do/file-formats/entity-.ent-files`
- `modding_docs/for-mod-creators-theory/files-and-what-they-do/file-formats/appearance-.app-files`
- `modding_docs/for-mod-creators-theory/files-and-what-they-do/audio-files.md`
- `modding_docs/for-mod-creators-theory/core-mods-explained/archivexl`
- `modding_docs/for-mod-creators-theory/core-mods-explained/tweakxl`

## Helper Tools

Use the explorer tools documented in `docs/tooling.md` instead of dumping large
CR2W-JSON files into context:

- `tools/explore_questphase.py`
- `tools/explore_scene.py`
- `tools/explore_localization.py`
- `tools/explore_ent_app.py`
- `tools/explore_journal.py`
- `tools/explore_world.py`
