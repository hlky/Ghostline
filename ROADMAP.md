# Ghostline Roadmap

Last audited: 2026-04-28

This file records the current project state and the next work needed to turn `gq000` from a dialogue prototype into a playable quest slice. It is based on the files under `source`, the helper explorers in `tools`, and local references in `modding_docs`.

## Current Status

### Project registration

- `source/resources/Ghostline.archive.xl` exists and currently registers:
  - `mod\gq000\phases\gq000.questphase` as a root questphase under `base\quest\cyberpunk2077.quest`
  - `mod\ghostline\localization\en-us\onscreens\ghostline.json` for generic onscreen localization
  - `mod\gq000\journal\gq000.journal` for the first quest journal data
  - `mod\gq000\localization\en-us\onscreens\gq000.json` for quest-specific onscreen localization
- The ArchiveXL file does not yet register any `streaming: blocks:` resources.

### Patch character

- Patch has packed character resources under `source/archive/mod/ghostline/characters/patch`:
  - `patch.ent`
  - `patch.app`
  - body/head meshes, textures, and morphtargets
- `source/resources/r6/tweaks/ghostline/character_patch.yaml` defines `Character.GhostlinePatch` with:
  - `entityTemplatePath: mod\ghostline\characters\patch\patch.ent`
  - `displayName` and `fullDisplayName` set to `gq_npc_patch`
  - `affiliation: Factions.Ghostline`
  - `voiceTag: gq_patch`
- `source/resources/r6/tweaks/ghostline/faction_ghostline.yaml` defines `Factions.Ghostline`.
- `source/raw/mod/ghostline/localization/en-us/onscreens/ghostline.json.json` contains onscreen entries for `gq_npc_patch` and `mod_gq_faction_ghostline`.
- Raw CR2W-JSON source files now exist for Patch's root entity and appearance resource:
  - `source/raw/mod/ghostline/characters/patch/patch.ent.json`
  - `source/raw/mod/ghostline/characters/patch/patch.app.json`
- `py .\tools\explore_ent_app.py summary` reports:
  - `patch.ent`: 1 root appearance, 110 root components, 249 handles, 61 resolved dependencies
  - `patch.app`: 1 appearance definition named `default`, 47 appearance components, 103 handles
- `patch.ent` appearance `ghostline_patch_default` maps `appearanceName: default` to `mod\ghostline\characters\patch\patch.app`.

### Quest phases

- Packed questphase binaries exist:
  - `source/archive/mod/gq000/phases/gq000.questphase`
  - `source/archive/mod/gq000/phases/gq000_patch_meet.questphase`
- Editable raw JSON now exists for both current questphases:
  - `source/raw/mod/gq000/phases/gq000.questphase.json`
  - `source/raw/mod/gq000/phases/gq000_patch_meet.questphase.json`
- `gq000.questphase` has 7 graph nodes and 7 edges:
  - input
  - phase node id `2` containing setup/community/journal work
  - phase node id `3`, which loads `mod\gq000\phases\gq000_patch_meet.questphase`
  - logical hub node id `11` on the phase failure branch
  - facts DB manager node id `12` on the phase success branch
  - phase node id `13`
  - terminating output
- The root phase flow is `input -> phase id 2 -> gq000_patch_meet phase id 3 -> facts/logical branch -> phase id 13 -> output`.
- `gq000_patch_meet.questphase` currently has 7 graph nodes and 6 edges:
  - input
  - journal node for `points_of_interest/minor_quests/gq000_01_poi_patch_bridge`
  - trigger wait for `#gq000_01_tr_setup`
  - checkpoint `gq000_patch_meet`
  - trigger wait for `#gq000_01_tr_engage`
  - scene node for `mod\gq000\scenes\gq000_patch_meet.scene` at `#gq000_01_sm_patch_bridge`
  - terminating output
- The phase exits through the scene node socket `job_accept` into a terminating output. No post-accept gameplay phase/objective branch exists yet.

### Scene

- Packed and raw scene files exist:
  - `source/archive/mod/gq000/scenes/gq000_patch_meet.scene`
  - `source/raw/mod/gq000/scenes/gq000_patch_meet.scene.json`
- The scene has 18 graph nodes, 21 edges, 13 spoken lines, and 5 player choices.
- Actors:
  - Patch is spawned/despawned at `#gq000_01_sm_patch_bridge`
  - V is found in context via `Character.Player_Puppet_Base`
- The scene includes `performersDebugSymbols`, which is required for scenes built from scratch according to `modding_docs/modding-guides/quest/creating-custom-scenes.md`.
- The dialogue flow is currently:
  - Patch intro line
  - optional choices: `Ghostline?`, `Why me?`
  - required choice: `What's the job?`
  - optional choice: `Who's behind it?`
  - required accept choice: `I'm in.`

### Dialogue localization and VO

- `source/raw/mod/gq000/localization/en-us/subtitles/gq000_01.json.json` and `source/raw/mod/gq000/localization/en-us/vo/gq000_01.json.json` are aligned.
- `py .\tools\explore_localization.py check` reports no subtitle/VO coverage problems.
- `source/raw/gq000_01_manifest.json` records the generated line keys, string IDs, text, audio paths, and durations.
- The VO map points at `.wem` paths, and `source/archive/mod/gq000/localization/en-us/vo` now contains matching Wwise-generated `.wem` files alongside the authored `.wav` sources.
- `tools/convert_wavs_to_wem.ps1` normalizes WAVs into `wwise_conversion\ExternalSources`, writes `external_sources.wsources`, runs Wwise external source conversion for Windows with `Vorbis Quality High`, and copies WEMs back into the VO folder without deleting WAVs.
- Checked 2026-04-27: WolvenKit.CLI 8.17.4 exposes a `wwise` command, but its implementation only supports `.wem` to `.ogg` conversion when `--wem` is set and cannot convert the current `.wav` VO sources to `.wem`.

### Journal and quest UI

- Added journal explorer tooling:
  - `tools/explore_journal.py`
  - `py .\tools\explore_journal.py prefixes --with-types` summarizes one representative `.journal` file for each first-dot prefix in `journal_reference`.
- Explored representative journal reference prefixes:
  - `briefings`: briefing folders plus `gameJournalBriefing*` sections.
  - `codex`: codex categories/groups/entries/descriptions.
  - `contacts`: `gameJournalContact`.
  - `internet_sites`: internet site/page entries.
  - `onscreens`: onscreen groups and onscreen entries.
  - `points_of_interest`: `gameJournalPointOfInterestGroup` and `gameJournalPointOfInterestMappin`.
  - `quests`: `gameJournalQuest`, phase, objective, description, quest map pin, and codex link entries.
  - `tarots`: tarot group/card entries.
- Added packed and raw `gq000` journal resources:
  - `source/archive/mod/gq000/journal/gq000.journal`
  - `source/raw/mod/gq000/journal/gq000.journal.json`
- The `gq000` journal currently defines:
  - quest root `quests/minor_quest/gq000`
  - phase `quests/minor_quest/gq000/gq000_01`
  - objective `quests/minor_quest/gq000/gq000_01/gq000_01_obj_meet_patch`
  - description `quests/minor_quest/gq000/gq000_01/gq000_01_obj_meet_patch/gq000_01_desc_meet_patch`
  - quest map pin `quests/minor_quest/gq000/gq000_01/gq000_01_obj_meet_patch/gq000_01_qmp_patch_bridge`
  - point of interest `points_of_interest/minor_quests/gq000_01_poi_patch_bridge`
- Added packed and raw quest onscreen localization:
  - `source/archive/mod/gq000/localization/en-us/onscreens/gq000.json`
  - `source/raw/mod/gq000/localization/en-us/onscreens/gq000.json.json`
- Quest onscreen localization uses ArchiveXL-style `primaryKey: "0"` entries with unique `gl_` secondary keys, and the journal fields reference those secondary keys directly.
- Updated `gq000.questphase`, `gq000_patch_meet.questphase`, and `gq000_patch_meet.scene` raw and packed resources so journal references use full journal paths instead of bare leaf ids.

### Generated/editor support data

- `generated` contains older generated snapshots. Prefer `source/raw` when changing CR2W assets.
- `GraphEditorStates` contains WolvenKit editor layout state only. Do not treat it as packed game data.
- Helper tools exist for inspection:
  - `tools/explore_questphase.py`
  - `tools/explore_scene.py`
  - `tools/explore_localization.py`
  - `tools/explore_ent_app.py`
  - `tools/explore_journal.py`

## Missing Or Unresolved References

These are references found in current raw assets that do not have matching project-owned resources under `source`.

### World placement, trigger areas, and scene marker

Current references:

- `#gq000_01_sm_patch_bridge`
- `#gq000_01_tr_setup`
- `#gq000_01_tr_engage`
- `#gq000_01_tr_bridge_case_mood`
- `#gq000_01_tr_someone_coming`

Needed:

- Pick the final Patch meeting location and record the coordinates.
- Add a custom streaming sector containing the world nodes required by the quest:
  - a static marker for `#gq000_01_sm_patch_bridge`
  - trigger area nodes for the four `#gq000_01_tr_*` references
  - any supporting collision/visibility markers needed for the scene setup
- Add a streaming block that includes the sector.
- Register the block in `source/resources/Ghostline.archive.xl` using `streaming: blocks:`.
- Verify every NodeRef resolves in game before tuning quest graph timing.

Docs checked:

- `modding_docs/modding-guides/world-editing/README.md`
- `modding_docs/for-mod-creators-theory/files-and-what-they-do/file-formats/the-whole-world-.streamingsector/README.md`
- `modding_docs/for-mod-creators-theory/files-and-what-they-do/file-formats/the-whole-world-.streamingsector/noderefs.md`
- `modding_docs/for-mod-creators-theory/references-lists-and-overviews/reference-world-sectors/reference-.streamingsector-node-types.md`

### Patch community / AI spawn support

Current reference:

- `#gq000_01_com_patch_bridge`

Needed:

- Add the community/AI spot setup that backs Patch's scene AI manager reference.
- Do this through streaming-sector world nodes, not a standalone `.community` file. The local docs note that `.community` files are leftovers and that community registration happens in streaming sectors.
- Expected world-sector pieces:
  - `worldAiSpotNode` with a unique NodeRef
  - `worldCompiledCommunityAreaNode` or `_Streamable` as appropriate for the sector
  - `worldCommunityRegistryNode`
  - matching entry/phase/spot IDs so quest nodes can activate or deactivate Patch cleanly

Docs checked:

- `modding_docs/for-mod-creators-theory/files-and-what-they-do/file-formats/.community-files.md`
- `modding_docs/modding-guides/quest/how-to-use-worldcommunityregistry-and-worldcompiledcommunity.md`
- `modding_docs/modding-guides/world-editing/ai-and-npcs/creating-communities.md`

### Borrowed/base NodeRef

Current reference:

- `#mq003_pr_homeless` in `gq000_patch_meet.questphase` phase prefab data and root `gq000.questphase` phase prefab data
- `#mq003_pr_corpse` in root `gq000.questphase` phase prefab data

Needed:

- Confirm these are intentional base-game prefab references.
- If they are only placeholders, replace them with Ghostline-owned prefabs or remove them once the custom streaming-sector setup owns the required markers/triggers.

## Next Milestones

### 1. Make all current packed assets inspectable (complete 2026-04-28)

- Serialized `gq000.questphase` into `source/raw/mod/gq000/phases/gq000.questphase.json`.
- Serialized `patch.ent` and `patch.app` into `source/raw/mod/ghostline/characters/patch`.
- Added `tools/explore_ent_app.py` for `.ent` and `.app` inspection.
- Re-ran the questphase, scene, localization, and ent/app explorers and updated the current notes above.

### 2. Add journal and quest UI data

- Completed 2026-04-28.
- Created `gq000` journal and quest onscreen localization resources in raw and packed form.
- Registered both `journal:` and quest onscreens in `source/resources/Ghostline.archive.xl`.
- Updated scene and questphase journal paths to full journal hierarchy paths.
- Added `tools/explore_journal.py` and documented first-dot `.journal` reference prefixes in `AGENTS.md`.
- Docs checked:
  - `modding_docs/modding-guides/quest/how-to-add-new-text-messages-thread-to-cyberpunk-2077.md`
  - `modding_docs/modding-guides/quest/creating-custom-shards.md`
  - `modding_docs/for-mod-creators-theory/files-and-what-they-do/file-formats/translation-files-.json.md`

### 3. Add the meeting-location world data

- Decide the actual Patch bridge/meeting spot.
- Create a Ghostline-owned streaming sector and streaming block.
- Add the marker, triggers, and Patch community/AI nodes referenced by the current phase and scene.
- Register the streaming block in `Ghostline.archive.xl`.

### 4. Extend the quest beyond acceptance

- Add the next quest phase after `job_accept`.
- Define facts with `gq000_` prefixes for accepted job state, cache acquired, cache delivered, and quest completion.
- Add objective updates, mappin changes, and failure/completion branches.
- Replace placeholder/base references with Ghostline-owned resources where needed.

### 5. Validate audio packaging

- Wwise `.wem` files have been generated for the current WAV voice lines referenced by the VO map.
- Add lipsync resources if the chosen scene presentation requires them.
- Validate in game that subtitles, VO map, and audio assets remain aligned after any dialogue edits.

### 6. Pack and test in game

- Deserialize updated raw CR2W-JSON into `source/archive`.
- Confirm packed CR2W files start with `CR2W`.
- Pack the WolvenKit project.
- Check:
  - `Cyberpunk 2077\red4ext\plugins\ArchiveXL\ArchiveXL.log`
  - TweakXL load output
  - in-game Patch spawn
  - trigger progression
  - journal and mappin visibility
  - subtitles and voice playback

## Useful Commands

```powershell
py .\tools\explore_questphase.py summary
py .\tools\explore_questphase.py refs
py .\tools\explore_scene.py summary
py .\tools\explore_scene.py refs --kind NodeRef
py .\tools\explore_scene.py refs --kind journal_path
py .\tools\explore_localization.py check
py .\tools\explore_ent_app.py summary
py .\tools\explore_ent_app.py appearances
py .\tools\explore_ent_app.py components --resources-only
py .\tools\explore_ent_app.py refs --kind ResourcePath
py .\tools\explore_journal.py prefixes --with-types
py .\tools\explore_journal.py -f .\source\raw\mod\gq000\journal\gq000.journal.json summary
py .\tools\explore_journal.py -f .\source\raw\mod\gq000\journal\gq000.journal.json tree --max-depth 6
.\tools\convert_wavs_to_wem.ps1
```
