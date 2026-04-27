# Ghostline Roadmap

Last audited: 2026-04-27

This file records the current project state and the next work needed to turn `gq000` from a dialogue prototype into a playable quest slice. It is based on the files under `source`, the helper explorers in `tools`, and local references in `modding_docs`.

## Current Status

### Project registration

- `source/resources/Ghostline.archive.xl` exists and currently registers:
  - `mod\gq000\phases\gq000.questphase` as a root questphase under `base\quest\cyberpunk2077.quest`
  - `mod\ghostline\localization\en-us\onscreens\ghostline.json` for generic onscreen localization
- The ArchiveXL file does not yet register any `journal:` resources.
- The ArchiveXL file does not yet register any `streaming: blocks:` resources.
- The ArchiveXL file does not yet register quest-specific onscreen localization under `mod\gq000`.

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
- There are no raw CR2W-JSON source files for `patch.ent` or `patch.app`; if either is edited in WolvenKit, serialize them into `source/raw` before making further scripted changes.

### Quest phases

- Packed questphase binaries exist:
  - `source/archive/mod/gq000/phases/gq000.questphase`
  - `source/archive/mod/gq000/phases/gq000_patch_meet.questphase`
- The editable raw JSON exists only for `gq000_patch_meet.questphase`:
  - `source/raw/mod/gq000/phases/gq000_patch_meet.questphase.json`
- `gq000_patch_meet.questphase` currently has 7 graph nodes and 6 edges:
  - input
  - journal node for `gq000_01_poi_patch_bridge`
  - trigger wait for `#gq000_01_tr_setup`
  - checkpoint `gq000_patch_meet`
  - trigger wait for `#gq000_01_tr_engage`
  - scene node for `mod\gq000\scenes\gq000_patch_meet.scene` at `#gq000_01_sm_patch_bridge`
  - terminating output
- The phase exits through the scene node socket `job_accept` into a terminating output. No post-accept gameplay phase/objective branch exists yet.
- The raw source for root `gq000.questphase` is missing. This blocks reliable scripted review of how the registered root phase starts and hands off to `gq000_patch_meet`.

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
- The VO map points at `.wem` paths, but `source/archive/mod/gq000/localization/en-us/vo` currently contains `.wav` files and no `.wem` files. The final audio pipeline still needs Wwise/WEM conversion or a verified WolvenKit packing path.

### Generated/editor support data

- `generated` contains older generated snapshots. Prefer `source/raw` when changing CR2W assets.
- `GraphEditorStates` contains WolvenKit editor layout state only. Do not treat it as packed game data.
- Helper tools exist for inspection:
  - `tools/explore_questphase.py`
  - `tools/explore_scene.py`
  - `tools/explore_localization.py`

## Missing Or Unresolved References

These are references found in current raw assets that do not have matching project-owned resources under `source`.

### Journal and quest mappin data

Current references:

- `gq000_01_poi_patch_bridge`
- `gq000_01_obj_meet_patch`
- `gq000_01_desc_meet_patch`
- `gq000_01_qmp_patch_bridge`

Needed:

- Add a quest journal resource, for example `source/archive/mod/gq000/journal/gq000.journal`, with raw source under `source/raw/mod/gq000/journal`.
- Register it in `source/resources/Ghostline.archive.xl` using `journal:`.
- Add quest-specific onscreen localization for journal title/objective/description text, likely under `source/archive/mod/gq000/localization/en-us/onscreens/gq000.json`, and register it under `localization: onscreens: en-us:`.
- Keep journal paths aligned with the existing questphase and scene journal nodes.

Docs checked:

- `modding_docs/modding-guides/quest/how-to-add-new-text-messages-thread-to-cyberpunk-2077.md`
- `modding_docs/modding-guides/quest/creating-custom-shards.md`
- `modding_docs/for-mod-creators-theory/files-and-what-they-do/file-formats/translation-files-.json.md`

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

- `#mq003_pr_homeless` in `gq000_patch_meet.questphase` phase prefab data

Needed:

- Confirm this is an intentional base-game prefab reference.
- If it is only a placeholder, replace it with a Ghostline-owned prefab or remove it once the custom streaming-sector setup owns the required markers/triggers.

### Root questphase raw source

Current gap:

- `source/archive/mod/gq000/phases/gq000.questphase` exists and is registered, but `source/raw/mod/gq000/phases/gq000.questphase.json` does not exist.

Needed:

- Serialize the binary with WolvenKit CLI:

```powershell
$wk = 'H:\WolvenKit.Console-8.17.4\WolvenKit.CLI.exe'
& $wk convert serialize .\source\archive\mod\gq000\phases\gq000.questphase -o .\source\raw\mod\gq000\phases -v Minimal
```

- Use `tools/explore_questphase.py --file .\source\raw\mod\gq000\phases\gq000.questphase.json summary` to document the root graph.
- Confirm how the root phase activates `gq000_patch_meet`.

## Next Milestones

### 1. Make all current packed assets inspectable

- Serialize `gq000.questphase` into `source/raw`.
- If Patch character assets need more changes, serialize `patch.ent` and `patch.app` into `source/raw`.
- Re-run the three explorer tools and update this roadmap if the raw graphs differ from the current notes.

### 2. Add journal and quest UI data

- Create the `gq000` `.journal` resource.
- Add entries for the quest root, objective, description, point of interest, and quest mappin paths currently referenced by scene/quest nodes.
- Add quest-specific onscreen localization for those journal entries.
- Register both `journal:` and quest onscreens in `Ghostline.archive.xl`.

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

### 5. Finish audio packaging

- Convert or pack WAV voice lines into the `.wem` resources referenced by the VO map.
- Add lipsync resources if the chosen scene presentation requires them.
- Validate that subtitles, VO map, and audio assets remain aligned after any dialogue edits.

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
```

