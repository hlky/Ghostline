# Ghostline Roadmap

Last audited: 2026-04-30

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
  facts/logical branch -> final phase -> output`.
- The root setup phase now activates/deactivates community entry `patch` with
  phase `default`, matching the generated community registry and streamable
  community area.
- `gq000_patch_meet.questphase` currently:
  - starts the POI journal entry,
  - waits for `#gq000_01_tr_setup`,
  - creates checkpoint `gq000_patch_meet`,
  - waits for `#gq000_01_tr_engage`,
  - starts `mod\gq000\scenes\gq000_patch_meet.scene` at
    `#gq000_01_sm_patch_bridge`,
  - exits through scene socket `job_accept`.
- No post-accept gameplay phase/objective branch exists yet.

### Scene

- Packed and raw scene resources exist at
  `mod\gq000\scenes\gq000_patch_meet.scene`.
- The current scene has 18 graph nodes, 21 edges, 13 spoken lines, and 5
  player choices.
- Patch is acquired from active community entry `patch` at
  `#gq000_01_com_patch_bridge` with the vanilla community actor pattern. V is
  found in context through `Character.Player_Puppet_Base`.
- The current dialogue flow is Patch's intro line, optional `Ghostline?` and
  `Why me?` choices, required `What's the job?`, optional `Who's behind it?`,
  and required accept choice `I'm in.`.
- Runtime crash isolation shows the world, community, trigger, scene startup,
  actor acquisition, journal objective, mappin, and stable intro-choice setup
  can work. The active crash surface is in generated scene section/choice
  structure. Fresh scene tooling should follow `docs/scene-authoring-rules.md`;
  probe workarounds in `docs/crash-investigation.md` are not target rules.

### Dialogue Localization And VO

- Subtitle and VO map raw resources for `gq000_01` are aligned by string ID.
- `source/raw/gq000_01_manifest.json` records generated line keys, string IDs,
  text, audio paths, and durations.
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

- Stabilize the non-intro scene response sections. Current evidence points at
  section node state, completion/output handling, or hidden section/event
  metadata rather than world streaming, actor lookup, VO/subtitle assets, or
  player line payloads.
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

### 1. Restart Meeting Scene Creation From Vanilla Rules

- Treat `docs/scene-authoring-rules.md` as the target structure for fresh scene
  tooling.
- Generate editable scene CR2W-JSON under `source/raw`, then use WolvenKit to
  produce packed `source/archive` resources.
- Use vanilla scene root metadata, actor acquisition, screenplay item IDs,
  section shapes, choice sockets, locStore coverage, and marker hierarchy.
- Treat failed probes of vanilla patterns as bad Ghostline implementation
  attempts, not as rules to preserve.
- Leave the unstable generated response sections behind when fresh tooling is
  ready.

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
