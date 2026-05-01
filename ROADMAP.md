# Ghostline Roadmap

Last audited: 2026-05-01

This file tracks the current state and the next work needed to turn `gq000`
from a dialogue prototype into a playable quest slice. Detailed command usage,
runtime crash conclusions, world-reference notes, and packaging instructions now
live in focused docs:

- `docs/tooling.md`
- `docs/scene-authoring-rules.md`
- `docs/crash-investigation.md`
- `docs/world-references.md`
- `docs/packaging.md`

## Current Status

### Project Registration

`source/resources/Ghostline.archive.xl` currently registers:

- `mod\gq000\phases\gq000.questphase` as a root questphase under
  `base\quest\cyberpunk2077.quest`.
- `mod\gq000\journal\gq000.journal`.
- Generic onscreen localization at
  `mod\ghostline\localization\en-us\onscreens\ghostline.json`.
- Quest onscreen localization at
  `mod\gq000\localization\en-us\onscreens\gq000.json`.
- Subtitle map `mod\gq000\localization\en-us\subtitles\gq000_01_subtitles_map.json`.
- VO map `mod\gq000\localization\en-us\vo\gq000_01.json`.
- Streaming block `mod\gq000\world\gq000_patch_meet.streamingblock`.

### Patch Character

- Patch has packed resources under
  `source/archive/mod/ghostline/characters/patch`, including `patch.ent`,
  `patch.app`, body/head meshes, textures, and morphtargets.
- Editable raw files exist for the root entity and appearance:
  - `source/raw/mod/ghostline/characters/patch/patch.ent.json`
  - `source/raw/mod/ghostline/characters/patch/patch.app.json`
- `source/resources/r6/tweaks/ghostline/character_patch.yaml` defines
  `Character.GhostlinePatch` with `entityTemplatePath:
  mod\ghostline\characters\patch\patch.ent`, display names using
  `gq_npc_patch`, `Factions.Ghostline`, and `voiceTag: gq_patch`.
- `source/resources/r6/tweaks/ghostline/faction_ghostline.yaml` defines
  `Factions.Ghostline`.
- `patch.ent` appearance `ghostline_patch_default` maps `appearanceName:
  default` to `mod\ghostline\characters\patch\patch.app`.
- Patch's `.app` head/body mesh components now point at real
  `mod\ghostline\characters\patch\...` depot paths instead of unresolved
  numeric `ResourcePath` IDs. The optional `h0_cyberware_face` mesh is disabled
  because its numeric mesh ID did not resolve to any packed game or mod
  resource.
- Packaging still has a risk: `source/archive/base` contains copied
  `base\characters\head\player_base_heads\player_man_average\...` resources
  that should not ship as global base-path overrides unless validated.

### Quest Phases

- Packed and raw questphase resources exist for:
  - `mod\gq000\phases\gq000.questphase`
  - `mod\gq000\phases\gq000_patch_meet.questphase`
- `gq000.questphase` is the root flow:
  `input -> setup/community/journal phase -> gq000_patch_meet phase ->
  gq000_done fact -> output`.
- Current crash-surface reduction state: the old `gq000_patch_meet` failed
  output path through the logical hub and final fallback phase has been
  disconnected. Those nodes remain in the resource, but they are not on the
  active path.
- The root setup phase now activates/deactivates community entry `patch` with
  phase `default`, matching the generated community registry and streamable
  community area.
- `gq000_patch_meet.questphase` currently:
  - starts the POI journal entry,
  - waits for `#gq000_01_tr_setup`,
  - creates checkpoint `gq000_patch_meet`,
  - waits for `#gq000_01_tr_engage`,
  - waits for the Patch community at `#gq000_01_com_patch_bridge` to report
    `CharacterSpawned`,
  - starts `mod\gq000\scenes\gq000_patch_meet.scene` at
    `#gq000_01_sm_patch_bridge`,
  - exits through scene socket `end`.
- The scene node still has a `job_accept` socket, but the current reduced
  questphase test route does not use it.
- No post-accept gameplay phase/objective branch exists yet.

### Scene

- Packed and raw scene resources exist at
  `mod\gq000\scenes\gq000_patch_meet.scene`.
- The current scene is represented by
  `tools/gq000_patch_meet.scene-spec.json` and `tools/generate_scene.py`,
  including the reduced crash-surface routing.
- The current scene is a 17-node full meeting dialogue with 18 connected
  edges, 13 spoken lines, and 5 player choices.
- Normal-speed approach no longer crashes after adding a pre-scene
  `CharacterSpawned` gate for `#gq000_01_com_patch_bridge` in
  `gq000_patch_meet.questphase`.
- Patch is acquired from active community entry `patch` at
  `#gq000_01_com_patch_bridge` with the vanilla community actor pattern. V is
  found in context through `Character.Player_Puppet_Base`.
- The current scene flow is:
  `start -> puppet_ai / bridge_case_mood pause -> POI journal ->
  someone_coming pause -> Patch intro -> objective journal -> description
  journal -> intro choice hub`. The optional `Ghostline?` and
  `Why me?` branches loop back to the intro choice hub; the required
  `What's the job?` branch advances to the post-job choice hub. The optional
  `Who's behind it?` branch loops back to that second hub; the required
  `I'm in.` branch closes the scene through `end`.
- Scene mappin node `n17` for `gq000_01_qmp_patch_bridge` is still present, but
  is intentionally unconnected in the current crash-surface reduction build.
  The journal description node `n16` now routes directly to choice node `n8`.
- The intro choice probe currently sets `isSingleChoice: 0` on all three
  options, with `type.properties: 0` for the two optional/info branches and
  `type.properties: 1` for the main progression branch.
- Scene journal paths now follow the journal file-entry index rule: the POI path
  under `points_of_interest/minor_quests` uses `fileEntryIndex: 1`, while the
  objective, description, and quest map pin under `quests/minor_quest/gq000`
  use `fileEntryIndex: 2`.
- The later `Who's behind it?` and `I'm in.` choice group is restored in the
  generated scene.
- The fresh generated shape now uses root `version: 5`, `PLATFORM_PC`,
  `minorQuests`, vanilla spoken line IDs `1 + 256n`, choice option IDs
  `2 + 256n`, padded choice sockets, deterministic event IDs, and embedded
  vanilla-style `db_db`/`pl_pl`/`en_us` choice locStore coverage. Choice
  locstrings now get two `db_db` descriptors, a blank fallback and a source text
  payload, before the other locale blocks.
- The scene spec pins `Header.ExportedDateTime` so generator and WolvenKit
  deserialization output can be checked byte-for-byte across repeated runs.
- The previous 18-node generated dialogue scene crashed on approach. The
  10-node journal handoff probe was validated in game after fixing the quest
  mappin `fileEntryIndex`. The later normal-speed approach crash was fixed by
  adding the pre-scene `CharacterSpawned` gate in the questphase. The later
  `Ghostline?` `Db-db` display issue was fixed by switching choice locStores to
  the audited vanilla-style descriptor shape. The current reduced build removes
  scene-local mappin execution and `job_accept` questphase routing from the
  active path while crash isolation continues.

### Dialogue Localization And VO

- Subtitle and VO map raw resources for `gq000_01` are aligned by string ID.
- `source/raw/gq000_01_manifest.json` records generated line keys, string IDs,
  text, audio paths, and durations.
- The `gq000_01` dialogue locstring IDs were regenerated across the manifest,
  raw subtitles, raw VO map, and generated scene during the intro-choice
  semantics probe.
- The VO map points at `.wem` paths, and matching Wwise-generated `.wem` files
  exist alongside the authored `.wav` files.
- A subtitle map resource now registers the subtitle entries with ArchiveXL.
- The scene still uses a base generic facial lipsync animset as a placeholder;
  Ghostline-owned lipsync `.anims` files have not been integrated.

### Journal And Quest UI

- Packed and raw `gq000` journal resources exist at
  `mod\gq000\journal\gq000.journal`.
- The journal defines:
  - quest root `quests/minor_quest/gq000`
  - phase `quests/minor_quest/gq000/gq000_01`
  - objective `quests/minor_quest/gq000/gq000_01/gq000_01_obj_meet_patch`
  - description
    `quests/minor_quest/gq000/gq000_01/gq000_01_obj_meet_patch/gq000_01_desc_meet_patch`
  - quest map pin
    `quests/minor_quest/gq000/gq000_01/gq000_01_obj_meet_patch/gq000_01_qmp_patch_bridge`
  - point of interest
    `points_of_interest/minor_quests/gq000_01_poi_patch_bridge`
- Quest onscreen localization exists at
  `mod\gq000\localization\en-us\onscreens\gq000.json`.
- Journal references in the questphase and scene use full journal paths rather
  than bare leaf IDs.
- The quest map pin and POI mappin have been moved to dedicated always-loaded
  marker `#gq000_01_mp_patch_bridge`. Vanilla files confirm this must stay
  separate from scene marker `#gq000_01_sm_patch_bridge`; runtime validation is
  still pending.

### World Placement And Community

- Generated raw and packed world resources exist for:
  - `mod\gq000\world\gq000_patch_meet.streamingsector`
  - `mod\gq000\world\gq000_always_loaded.streamingsector`
  - `mod\gq000\world\gq000_patch_meet.streamingblock`
- The world spec uses captured origin `(-795.7447, 390.34177, 17.272781)`.
  Yaw remains provisional because the captured `ToVector4` did not include
  actor heading.
- The streaming block contains a Quest descriptor for the quest sector and an
  AlwaysLoaded descriptor for the always-loaded sector. The quest descriptor
  binds `questPrefabNodeRef: $/mod/gq000/#gq000_pr_patch_meet`.
- The quest sector contains four trigger areas, one AI spot, and one streamable
  community area.
- The always-loaded sector contains the community registry and concrete marker
  nodes needed for early NodeRef resolution.
- The community registry maps entry `patch/default` to source object id
  `7897875840529598144` and spot NodeRef
  `$/mod/gq000/#gq000_pr_patch_meet/#gq000_01_spot_patch_bridge`.
- Temporary runtime isolation state: the active world spec uses
  `Character.Judy` for the `patch/default` entry while scene crashes are being
  isolated. Revert it to `Character.GhostlinePatch` after the scene path is
  stable.
- See `docs/world-references.md` for the resolved prefab/NodeRef model and
  current world findings.

### Generated And Editor Support Data

- Prefer `source/raw` over `generated` when preparing CR2W assets for use.
- `generated` contains older generated snapshots.
- `GraphEditorStates` contains WolvenKit editor support data only. Do not
  treat it as packed asset source of truth.

## Open Blockers

- Validate the reduced crash-surface dialogue in game: scene `end` exit,
  bypassed scene-local mappin node, second choice hub, optional client branch
  loopback, and `I'm in.` close path.
- Validate the dedicated always-loaded map-pin marker
  `#gq000_01_mp_patch_bridge` in game.
- Rebuild the scene marker under a vanilla-style scene-prefab child path when
  fresh world/scene tooling replaces the current generated shape.
- Revert the temporary Judy community registry entry to `Character.GhostlinePatch`
  and re-test Patch spawn after the scene path is stable.
- Decide whether `source/archive/base` resources are still required. They
  should be excluded from normal install archives unless their impact is
  validated.
- Audit remaining `ep1\...` animation/effect dependencies in Patch's entity or
  explicitly require Phantom Liberty if Patch still crashes when streamed.

## Next Milestones

### 1. Validate Fresh Meeting Scene

- Use `tools/generate_scene.py` and
  `tools/gq000_patch_meet.scene-spec.json` as the source path for fresh scene
  resources.
- Validate the reduced full dialogue in game before restoring scene-local
  mappin execution or `job_accept` acceptance routing.
- If runtime issues remain, fix the generator/spec against vanilla reference
  shapes rather than patching the packed scene manually.
- Keep failed probe workarounds in `docs/crash-investigation.md` as historical
  context only.

### 2. Validate Meeting-Location World Data

- Confirm ArchiveXL loads `mod\gq000\world\gq000_patch_meet.streamingblock`.
- Confirm scene marker, setup trigger, engage trigger, case-mood trigger,
  someone-coming trigger, Patch community, and map-pin NodeRefs all resolve.
- Tune Patch yaw, workspot placement, and trigger radii against the real
  location geometry.

### 3. Restore Patch As The Community Character

- Switch the temporary `Character.Judy` registry record back to
  `Character.GhostlinePatch`.
- Test Patch spawn and approach after the scene startup path is stable.
- Continue custom-pathing or replacing Patch dependencies only if missing
  resource hashes change or Patch-specific crashes remain.

### 4. Extend The Quest Beyond Acceptance

- Add the next quest phase after `job_accept`.
- Define `gq000_` facts for accepted job state, cache acquired, cache
  delivered, and quest completion.
- Add objective updates, mappin changes, failure branches, and completion
  branches.
- Keep prefab NodeRef lifecycle aligned with the resolved model in
  `docs/world-references.md`.

### 5. Validate Audio Packaging

- Validate in game that subtitles, VO map, and `.wem` assets remain aligned
  after scene edits.
- Add Ghostline-owned lipsync resources if the final scene presentation needs
  them.

### 6. Pack And Test In Game

- Deserialize updated raw CR2W-JSON into `source/archive`.
- Verify packed CR2W resources.
- Build an install package from the scoped archive tree, not from the repo
  root.
- Check ArchiveXL, TweakXL, Patch spawn, trigger progression, journal/mappin
  visibility, subtitles, and voice playback.
