# SQ021 Computer And File-Read Flow

This document records the complete vanilla path from Randy's laptop world
placement to its Files UI and quest progression. It is the reference template
for Ghostline's `read_terminal_document` building block.

## Result

SQ021's Files content is authored in the laptop world node's instance
`RedPackage`. It is not injected by the quest, scene, global `.devices`
registry, `.psrep`, or the cooked inplace resource.

The decisive runtime dependency is the component CRUID mapping between that
instance package and `laptop_1.ent`. A laptop can render, animate, and expose
`Use` while still falling back to the entity template's empty computer
controller if these IDs do not match.

## Vanilla Resource Chain

```text
base\worlds\03_night_city\03_night_city.streamingworld
  -> base\worlds\03_night_city\_compiled\default\blocks\all.streamingblock
     descriptor 3566
  -> base\worlds\03_night_city\_compiled\default\
     exterior_19_-8_0_0.streamingsector
     nodeData 1232 -> node 1142
  -> base\gameplay\devices\masters\computers\laptop_1.ent
     plus node-local instanceData RedPackage
```

The laptop NodeRef is:

```text
$/03_night_city/se1/#loc_sq021_trailer_park/
loc_sq021_trailer_park_gameplay_prefabV4S2BNI/
#loc_sq021_trailer_park_devices/#sq021_randy_pc
```

Its NodeRef hash is `2807216846216680177`. The streaming-block variant range
is `var_real_pc_randy`; variant membership is represented by
`variantIndices`, despite the corresponding `variantNodes` arrays being
empty.

`nodeData[1232].CookedPrefabData` references
`4fd0915183681e53.streamingsector_inplace`, but that resource only carries
embedded entity templates. The computer's persistent controller data is
directly inside outer sector node 1142.

## Instance Package And Component Binding

The node-local package has three CRUID entries and three component chunks:

| Package index | CRUID | Chunk | Meaning |
| --- | ---: | --- | --- |
| 0 | `1108512084555509772` | `ComputerControllerPS` | World-authored raw/legacy fallback |
| 1 | `1131680419258347532` | `ComputerControllerPS` | Active controller matching `laptop_1.ent` |
| 2 | `1131680419258347552` | `gameScanningComponentPS` | Scanner matching `laptop_1.ent` |

The first ID is also used as a world-authored computer override identity on
unrelated vanilla computers; it is not unique to SQ021. The base entity
contains:

- `ComputerController` named `controller`, ID
  `1131680419258347532`; and
- `gameScanningComponent` named `scanning`, ID
  `1131680419258347552`.

Ghostline initially replaced the package CRUIDs with arbitrary IDs. The laptop
still appeared and was usable, but the runtime could not bind the authored
controller, so it used `laptop_1.ent`'s default empty `filesStructure` and hid
the Files tab. Preserving SQ021's exact CRUID dictionary made the custom file
appear in game.

Keep both controller chunks and the scanner chunk until a separate runtime
test proves the world-authored first controller can be removed.

## Files And Messages

The SQ021 controller has two content representations:

- controller 0 contains a raw video-backed file and nine inline emails; and
- controller 1 contains three journal-backed files and nine journal-backed
  emails.

The active journal file is:

```text
onscreens/emails/quests/side_quest/sq021_sick_dreams/
sq021_randy_files/01_cartoon
```

It is a `gameJournalFile`, is enabled, and carries:

```text
questInfo.factName = sq021_randy_pc_file_cartoon
```

Opening the file is what sets the fact. Neither the quest nor scene creates
the Files tab or inserts the file.

For a Files-only reusable computer:

- keep a non-empty `filesStructure` on both controller chunks;
- use an inline file with no journal path in controller 0 as a fallback;
- use the same file with a `gameJournalFile` path in controller 1;
- set `filesMenu = 1`;
- set `mailsMenu = 0` and `mailsStructure = []`;
- set `internetMenu = 0` and clear the inherited starting page;
- set `newsFeedMenu = 0` and `newsFeed = []`; and
- remove copied quest-specific scanner clues.

`filesMenu = 1` by itself is insufficient. The UI filters empty content
groups and omits the tab.

## Journal And Localization

SQ021's three files already exist in the base onscreen journal and therefore
resolve directly through `journalPath`. SQ021 does not activate those file
entries with quest journal nodes before use.

Ghostline-owned journal entries must be registered through ArchiveXL and
available before the laptop UI resolves them. The current GQT001 document is:

```text
onscreens/emails/quests/minor_quest/gqt001/files/diagnostic
```

Its `fileEntryIndex` is `5`, the zero-based path-component index of the
containing `files` entry. It is not a document-array index.

The entry title and body use Ghostline onscreen localization keys. The raw
inline controller retains literal title/body text as a fallback.

## Vanilla Quest And Scene Sequence

The relevant graph is nested inside:

```text
base\quest\side_quests\sq021\phases\sq021_randys_room.questphase
```

Path in the serialized resource:

```text
root node 17 -> phase node 5 -> phase node 2 -> 101-node phase graph
```

The normal file-click branch is:

```text
entry 97
  -> node 146 waits for sq021_randy_pc_file_cartoon > 0
  -> node 147 sends ToggleUIInteractivity(false)
  -> scene input 149: file_cartoon_in
  -> scene output: file_cartoon_out
  -> node 151 waits one real-time second
  -> node 140 clears sq021_randy_pc_file_cartoon to 0
  -> node 157 sends ToggleUIInteractivity(true)
```

The scene's `file_cartoon_in` branch reacts to the file, sets
`sq021_cartoon_seen`, and exits. It never creates computer content.

The `ToggleUIInteractivity` events use:

```text
managerName = ComputerManager
objectRef = #sq021_randy_pc
isUiEvent = 0
```

`ForceUIRefreshEvent` exists in SQ021 only for its dynamic web-page path. It
is not required for an ordinary file read.

## Global Device Resources

SQ021's NodeRef hash, node-data ID, and component CRUIDs are absent from:

- `03_night_city.devices`;
- `03_night_city_init.devices`; and
- direct values in `03_night_city.psrep`.

The sector has no `persistentNodes` entry for the laptop. Therefore
`.devices` and `.psrep` are not prerequisites for the Files UI.

A custom `.devices` entry may still be useful when a quest addresses a device
through device-manager operations. GQT001 currently completes through the
file's fact and does not target its laptop NodeRef from the quest graph, so its
registry entry is not part of the proven Files-tab requirement.

## Save Persistence

Device persistent state is save-backed. A save that streamed an earlier
Ghostline laptop package can retain copied SQ021 messages even after the
authored mail arrays are cleared.

Use a new NodeRef when materially changing a test device's controller state,
or test from a save that has never streamed that device. GQT001 uses the
revised identity:

```text
$/mod/gqt001/#gqt001_pr_signal_delay/#gqt001_terminal_laptop_r2
```

## Current Ghostline Implementation

Authoring and generated resources:

- `tools/generate_gqt001_content.py`
- `source/quests/tests/gqt001_signal_delay.quest.json`
- `source/quests/tests/gqt001_signal_delay.location.json`
- `source/raw/mod/gqt001/world/gqt001_laptop_instance.streamingsector.json`
- `source/raw/mod/gqt001/journal/gqt001.journal.json`
- `source/raw/mod/gqt001/localization/en-us/onscreens/gqt001.json.json`

The installed Files-only runtime candidate is retained at:

```text
H:\Ghostline-builds\gqt001-files-only-r2-20260724-201904
```

Archive SHA-256:

```text
791ED71FB1B443734153304DB609961D193BF7ECEE300CD09818BEEE10D5C166
```
