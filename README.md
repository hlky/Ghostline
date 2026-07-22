# Ghostline

Cyberpunk 2077 WolvenKit quest mod. The first playable slice is `gq000`,
centered on meeting Patch and accepting the first Ghostline job.

The current installed candidate uses Judy for community/scene isolation. The
preceding shared-slot build completed the phone-to-cache-objective handoff; the
latest scene-only change sorts choice locStore descriptors and still needs the
focused label/no-regression pass in `docs/testing.md`. Patch's custom entity
remains a separate TweakXL-dependent validation step.

## Working Docs

- `ROADMAP.md` - current project state, blockers, and next milestones.
- `docs/quest-scene-flow.md` - the concrete root phase, meeting phase, scene,
  post-accept, trigger, and localization lookup flow.
- `docs/scene-authoring-rules.md` - vanilla-first target rules for fresh scene
  creation tooling.
- `docs/testing.md` - installed baselines, clean-save test routes, and focused
  runtime checks.
- `docs/crash-investigation.md` - historical runtime failures and the evidence
  behind the stable lifecycle.
- `docs/world-references.md` - quest prefab, NodeRef, marker, trigger, and
  community wiring notes.
- `docs/tooling.md` - helper tool command usage.
- `docs/packaging.md` - safe packaging, install layout, and runtime log checks.
- `tools/scene_spec.md` and `tools/world_spec.md` - generator input contracts.
- `agent/skills/*/SKILL.md` - task-specific agent notes for CR2W conversion,
  quest/scene/journal work, character tweaks, localization/audio, and
  ArchiveXL packaging.

## Repository Layout

- `source/raw` is the editable CR2W-JSON source for packed resources.
- `source/archive` is the packed/game-ready CR2W resource tree.
- `source/resources` contains loose ArchiveXL, TweakXL, REDscript, and config
  resources.
- `packed` is ignored generated install/ZIP staging, not authoring source.
- `reference` contains serialized local reference assets used for comparison.
- `tools` contains small repo helpers for inspecting and generating resources.
- `generated` contains older generated CR2W snapshots. The current authored
  WAV bank is a temporary exception; its manifest-filtered workflow is
  documented in `docs/tooling.md`.
- `GraphEditorStates` contains WolvenKit editor layout state only.
- `modding_docs` is a local reference submodule, not Ghostline-owned source.

## Runtime Dependencies

- ArchiveXL is required for the root questphase, journal, localization, and
  streaming registrations.
- TweakXL is required when the world registry is restored from the current
  Judy isolation record to `Character.GhostlinePatch`.
- Patch still references some `ep1\...` resources. Whether Phantom Liberty is
  a final hard dependency remains an open validation item in `ROADMAP.md`.

## Source Rules

- Work from the repository root.
- Do not edit `source/archive` resources as text. They are CR2W binaries,
  including paths ending in `.json`.
- Edit `source/raw` CR2W-JSON when changing packed resources.
- `source/raw/gq000_01_manifest.json` is a plain generated manifest and is not
  serialized back to CR2W.
- Search `modding_docs` before guessing at Cyberpunk-specific behavior.
