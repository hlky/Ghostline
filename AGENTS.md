# Ghostline Agent Guide

Ghostline contains a quest-building system and separate Cyberpunk 2077 WolvenKit
mod projects. Keep this file as the
always-loaded routing layer; task-specific instructions live in repo-local
skill-style files under `agent/skills`.

## First Rules

- Work from the repository root unless a command says otherwise.
- Read `docs/reference/project-layout.md` for project ownership and build paths.
  `source`, `generated`, and `packed` are project-relative. There is no shared
  repository-root `source` tree. Use `tools/project_layout.py` to resolve projects
  and depot owners; never assume the repository root is a WolvenKit project.
- Read `projects/ghostline/quests/gq000/implementation/runtime-flow.md` before changing the current root/child phase
  handoff, meeting lifecycle, scene exits, triggers, or localization lookup
  paths.
- Treat `modding_docs` as a local reference submodule, not Ghostline-owned
  source, unless the task explicitly asks to edit those docs.
- Before guessing at Cyberpunk-specific behavior, search or read
  `modding_docs`.
- Do not edit `source/archive` resources as text. They are CR2W binaries,
  including resource paths ending in `.json`.
- Edit `source/raw` CR2W-JSON when changing packed resources. Plain quest,
  dialogue, voice-selection, character, and braindance authoring manifests live
  outside `source` and are not serialized directly back to CR2W.
- Treat `generated` as ignored, reproducible scratch output. Authored CR2W-JSON
  belongs under `source/raw`; reviewed source WAVs belong under the owning
  quest's `voice/source` directory.
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

- `projects/ghostline` owns the story `.cpmodproj`, story source trees,
  Iris/Cinder authoring, and story/development package profiles.
- `projects/test-quests/gqt###` are independent test WolvenKit projects,
  each owning its manifest, implementation, source trees, and package profile.
- `projects/shared/ghostline-runtime` owns Patch, shared runtime assets, and
  GQ000 baseline resources. Dependencies are explicit in each `project.json`.
- `projects/catalog.json` maps IDs and depot ownership. Game depot paths remain
  unchanged when workspace files move between owners.
- `quests/examples` and `quests/templates` belong to the building system.
  Templates have separate input source trees under `quests/templates/source`;
  neutral character catalogs/components/shells are in `quests/templates/characters`.

- `source/archive` contains packed/game-ready CR2W resources.
- `source/raw` contains editable CR2W-JSON for packed resources.
- `source/resources` contains WolvenKit loose resources, including ArchiveXL
  `.xl`, TweakXL YAML, REDscript, and engine config files. Project
  builds/staging copy them, but a manual scoped `pack source/archive` command
  does not.
- Project `characters` directories contain plain character manifests consumed
  by `tools/character_builder.py` and the local character UI.
  They are authoring inputs, not directly packed game resources.
- `braindance` contains reusable rig contracts, templates, and render presets.
  Quest-specific performance specs belong to the owning project. These are authoring inputs, not WolvenKit project source.
- `projects/ghostline/quests` contains the series bible and per-quest narrative,
  script, compiler-manifest, and implementation documentation.
- `projects/test-quests` also contains the test quest index, scenarios, and evidence.
- `projects/shared/ghostline-runtime/source/archive/base` may contain supporting base-game files. It currently
  contains base player-head mesh and morphtarget support resources. Treat them
  as unvalidated global overrides, not normal shipping content.
- `source/archive/mod` contains mod-owned packed resources.
- `projects/shared/ghostline-runtime/source/archive/mod/ghostline` contains generic Ghostline resources shared
  across the quest series, such as Patch's character resources.
- `projects/shared/ghostline-runtime/source/archive/mod/ghostline/characters/patch` contains Patch's custom NPC
  template set.
- `projects/shared/ghostline-runtime/source/archive/mod/gq000` contains the superseded prototype and reusable
  runtime baseline. `gq001` extends it and is the first canonical Ghostline
  story quest.
- `projects/shared/ghostline-runtime/source/archive/mod/gq000/phases` contains the main and stage questphase
  resources.
- `projects/shared/ghostline-runtime/source/archive/mod/gq000/scenes` contains scene resources for dialogue,
  interactions, animations, and related scene work.
- `projects/shared/ghostline-runtime/source/archive/mod/gq000/localization/en-us` contains quest subtitles,
  voiceover maps, and quest-specific onscreen localization.
- `reference/journal` contains serialized base-game `.journal` reference
  slices.
- `reference/world` contains reference `.streamingblock` and
  `.streamingsector` CR2W binaries plus their `.json` CR2W-JSON companions.
- `packed` is ignored generated install/ZIP staging. Rebuild it from
  `source/archive` and `source/resources`; do not treat it as source of truth.

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

Use the explorer tools documented in `docs/reference/tool-catalog.md` instead of dumping large
CR2W-JSON files into context:

- `tools/explore_questphase.py`
- `tools/explore_scene.py`
- `tools/explore_localization.py`
- `tools/explore_ent_app.py`
- `tools/explore_journal.py`
- `tools/explore_world.py`
