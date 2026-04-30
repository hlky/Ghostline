# Ghostline

Cyberpunk 2077 WolvenKit quest mod. The first playable slice is `gq000`,
centered on meeting Patch and accepting the first Ghostline job.

## Working Docs

- `ROADMAP.md` - current project state, blockers, and next milestones.
- `docs/scene-authoring-rules.md` - vanilla-first target rules for fresh scene
  creation tooling.
- `docs/crash-investigation.md` - extracted runtime findings from the
  2026-04-29/30 crash probe work.
- `docs/world-references.md` - quest prefab, NodeRef, marker, trigger, and
  community wiring notes.
- `docs/tooling.md` - helper tool command usage.
- `docs/packaging.md` - safe packaging, install layout, and runtime log checks.
- `agent/skills/*/SKILL.md` - task-specific agent notes for CR2W conversion,
  quest/scene/journal work, character tweaks, localization/audio, and
  ArchiveXL packaging.

## Repository Layout

- `source/raw` is the editable CR2W-JSON source for packed resources.
- `source/archive` is the packed/game-ready CR2W resource tree.
- `source/resources` contains loose ArchiveXL and TweakXL resources.
- `reference` contains serialized local reference assets used for comparison.
- `tools` contains small repo helpers for inspecting and generating resources.
- `generated` contains older generated snapshots. Prefer `source/raw` for
  current work.
- `GraphEditorStates` contains WolvenKit editor layout state only.
- `modding_docs` is a local reference submodule, not Ghostline-owned source.

## Source Rules

- Work from the repository root.
- Do not edit `source/archive` resources as text. They are CR2W binaries,
  including paths ending in `.json`.
- Edit `source/raw` CR2W-JSON when changing packed resources.
- `source/raw/gq000_01_manifest.json` is a plain generated manifest and is not
  serialized back to CR2W.
- Search `modding_docs` before guessing at Cyberpunk-specific behavior.
