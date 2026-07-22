# Ghostline

Cyberpunk 2077 WolvenKit quest mod. The first playable slice is `gq000`: meet
Patch, accept Ghostline's first job, infiltrate a guarded relay, and breach its
datacache, deliver the package through a native drop point, and complete
Morrow's phone debrief.

The current worktree candidate retains the runtime-confirmed custom Patch,
crash-free shared-slot scene lifecycle, sorted choice locStore fix, guarded
native breach, readable archived-conversation shards, and explicit guard
hostility. It adds the accessible Kabuki delivery, yellow quest marker,
two-choice Morrow exchange, reward, and quest completion. The focused runtime
route is in `docs/testing.md`.

## Working Docs

- `ROADMAP.md` - current project state, blockers, and next milestones.
- `docs/quest-design.md` - recovered faction, character, story, shard, and
  completion-message writing for `gq000`.
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
- `docs/drop-points.md` - exhaustive native drop-point index, reviewed-candidate
  policy, and deterministic authoring-time selection commands.
- `docs/character-creation-pipeline.md` - audited Patch/NPV structure and the
  manifest, catalog, headless-head, live preview, asset-index, and validation
  workflow for reusable NPC creation.
- `docs/tooling.md` - helper tool command usage.
- `docs/packaging.md` - safe packaging, install layout, and runtime log checks.
- `tools/scene_spec.md` and `tools/world_spec.md` - generator input contracts.
- `agent/skills/*/SKILL.md` - task-specific agent notes for CR2W conversion,
  quest/scene/journal work, character tweaks, localization/audio, and
  ArchiveXL packaging.

## Character Creator

The manifest-driven male/female generator, validator, headless
WolvenKit/Blender head builder, archive-derived asset index, and local WebGL
creator are available now. The commands without `--manifest` select Patch's
male-average profile:

```powershell
py -B .\tools\character_builder.py validate
py -B .\tools\character_builder.py generate --out .\converted\characters\patch
py -B .\tools\character_builder.py compare --generated .\converted\characters\patch
py -B .\tools\character_builder.py `
  --manifest .\source\characters\female-example.character.json validate
py -B .\tools\character_builder.py `
  --manifest .\source\characters\female-example.character.json generate `
  --out .\converted\characters\female_example
py -B .\tools\character_asset_index.py
npm install --prefix .\tools\character_ui --ignore-scripts
py -B .\tools\character_ui.py --open
py -B .\tools\character_ui.py `
  --manifest .\source\characters\female-example.character.json --open
```

See `docs/character-creation-pipeline.md` for current capabilities and
`docs/tooling.md` for the head-build command. UI generation remains isolated
until reviewed, but the current reviewed manifest has been applied to Patch's
checked-in raw and packed appearance. The checked female example uses the
tutorial's dedicated `WomanAverage` root, PWA head resources, and curated casual
appearance; its generated output remains isolated and still needs in-game
validation. The UI previews the real frame-specific head morphs immediately,
uncooks selected installed-game meshes on demand, and can assign real mesh
appearances from indexed PMA torso/legs/feet or PWA torso/legs primary meshes to
the generated outfit. Patch's current design manifest selects a
complete black-carbon dread-undercut bundle plus a grey high-collar shirt and
black computer cargos; `compare` now reports all four generated documents as
equivalent to their applied shipping sources.

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

- ArchiveXL is required for the root questphase, journal, localization,
  streaming registrations, and the custom relay's minimal `.devices` registry
  patch.
- TweakXL is required for the current `Character.GhostlinePatch` registry,
  Ghostline faction records, and the two readable Quiet Spine items defined in
  `source/resources/r6/tweaks/ghostline/gq000_shards.yaml`. The local test
  install uses TweakXL 1.11.3.
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
