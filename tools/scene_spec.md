# Ghostline Scene Spec

`tools/generate_scene.py` consumes a compact JSON spec and emits WolvenKit
CR2W-JSON for `.scene` resources. The checked-in production fixture is:

```powershell
py .\tools\generate_scene.py audit --spec .\tools\gq000_patch_meet.scene-spec.json
py .\tools\generate_scene.py generate --spec .\tools\gq000_patch_meet.scene-spec.json --dry-run
py .\tools\generate_scene.py generate --spec .\tools\gq000_patch_meet.scene-spec.json --deserialize
py .\tools\generate_scene.py validate --file .\source\raw\mod\gq000\scenes\gq000_patch_meet.scene.json --spec .\tools\gq000_patch_meet.scene-spec.json
```

The generator uses vanilla scene shells from `reference/vanilla_extract_json`
and local WolvenKit source assumptions. It does not use `template.scene.json`,
`generated`, or `GraphEditorStates` as authoring inputs.

## Top-Level Fields

| Field | Required | Description |
| --- | --- | --- |
| `name` | Yes | Stable scene name used for deterministic event IDs and hashes. |
| `base_scene` | Yes | Vanilla CR2W-JSON scene used for root and choice node shells. |
| `choice_shell_node_id` | No | Specific vanilla choice node id to clone. If omitted, the first choice shell is used. |
| `manifest` | Yes | Dialogue manifest with `spoken_lines` and `choice_lines`. |
| `raw_path` | Yes | Generated raw CR2W-JSON destination under `source/raw`. |
| `archive_path` | Yes | Packed CR2W target path used in `Header.ArchiveFileName`. |
| `exported_datetime` | No | Stable `Header.ExportedDateTime`; defaults to `1970-01-01T00:00:00Z` for reproducible output. |
| `actors` | Yes | Scene actors, currently `community` NPCs and `player` actors. |
| `spoken_line_order` | Yes | Manifest keys assigned screenplay IDs `1 + 256n`. |
| `choice_line_order` | Yes | Manifest keys assigned option IDs `2 + 256n`. |
| `choice_locales` | No | Locale descriptors to embed for every choice. Defaults to `db_db`, `pl_pl`, and `en_us`. |
| `entry_point` | Yes | Scene entry point name and node id. |
| `exit_points` | Yes | Scene exit point names and node ids. Include questphase sockets such as `job_accept`. |
| `start_node` | Yes | Start node id and outgoing destinations. |
| `graph_order` | No | Explicit scene graph node order. If omitted, nodes are ordered by connections from `start_node` and unvisited nodes are appended. |
| `sections` | Yes | Dialogue section nodes and their spoken line keys. |
| `choices` | No | Choice nodes and options. |
| `quest_nodes` | No | Scene-local quest wrapper nodes for journal, mappin, trigger, or AI setup. |
| `xor_nodes` | No | Xor nodes for vanilla-compatible branch joins. |
| `end_node` | Yes | Terminal `scnEndNode` id. |

## Destinations

Destinations use scene socket coordinates:

```json
{
  "node_id": 8,
  "input_name": 0,
  "input_ordinal": 0
}
```

`input_name` and `input_ordinal` default to `0`, so regular section and choice
connections can be written as only `{"node_id": 8}`.

`graph_order` is optional and should normally be omitted. Use it when the
runtime/editor shape intentionally keeps an unconnected graph node in a specific
position, such as the reduced `gq000_patch_meet` scene keeping mappin node `n17`
present but disconnected. When present, it must list every generated graph node
exactly once, and validation checks that raw scenes keep that order.

## Actors

Community actors are acquired from an active streamable community area:

```json
{
  "key": "patch",
  "name": "patch",
  "kind": "community",
  "id": 0,
  "entry": "patch",
  "community_ref": "#gq000_01_com_patch_bridge",
  "appearance": "default",
  "lipsync": 0
}
```

Player actors use `findInContext`:

```json
{
  "key": "v",
  "name": "V",
  "kind": "player",
  "id": 1,
  "record": "Character.Player_Puppet_Base",
  "lipsync": 1
}
```

Actor performer debug symbols are generated as `actorID * 256 + 1`.

## Sections And Choices

Sections reference spoken manifest keys. Durations come from
`duration_ms`, with `line_gap_ms` and `section_tail_padding_ms` controlling
simple timing:

```json
{
  "key": "main_close_accept",
  "node_id": 7,
  "lines": [
    "gq000_01_v_choice_accept_line",
    "gq000_01_patch_rsp_accept_01"
  ],
  "on_end": [
    {
      "node_id": 18
    }
  ]
}
```

Choice nodes clone a vanilla choice shell and always emit one output socket per
option plus six dummy sockets named `1` through `6`:

```json
{
  "key": "choice_group_after_job",
  "node_id": 9,
  "actor_id": 0,
  "options": [
    {
      "choice_key": "gq000_01_v_choice_accept_short",
      "caption": "I'm in.",
      "single_choice": false,
      "choice_type": 1,
      "target_node_id": 7
    }
  ]
}
```

Every choice option gets embedded locStore descriptors for all configured
locales. The default order is vanilla-style `db_db`, `pl_pl`, then `en_us`;
`db_db` emits two descriptors per choice, a blank fallback payload followed by
the source text payload.

`single_choice` is written directly to `isSingleChoice`; do not use it to infer
whether an option is optional or progression-critical. Use `choice_type` for the
raw `gameinteractionsChoiceTypeWrapper.properties` value copied from the chosen
vanilla pattern.

## Supported Quest Nodes

V1 supports the scene-local quest node shapes needed by `gq000_patch_meet`:

- `puppet_ai`: cinematic AI tier setup for a community actor.
- `pause_condition`: player trigger checks, optionally requiring player not in combat.
- `journal`: POI, objective, and description journal activation.
- `mappin`: quest map pin activation.

These nodes are deliberately narrow. Add a new explicit builder when a future
scene needs another quest node type.

### Journal Path `file_entry_index`

`file_entry_index` is the zero-based path component index of the containing
`gameJournalFileEntry`, not the leaf entry index or CR2W handle index.

For `quests/minor_quest/gq000/gq000_01/gq000_01_obj_meet_patch`, component `2`
is `gq000`, a `gameJournalQuest` and therefore the containing
`gameJournalFileEntry`. The objective, its description, and its quest map pin
all use `file_entry_index: 2`.

For `points_of_interest/minor_quests/gq000_01_poi_patch_bridge`, component `1`
is `minor_quests`, a `gameJournalPointOfInterestGroup`, so the POI journal node
uses `file_entry_index: 1`.

The generator infers known namespace indexes when `file_entry_index` is omitted
and validation fails if a known path uses a mismatched index.

## Validation

`validate` fails if generated scenes drift from the current v1 contract:

- root metadata must be `version: 5`, `PLATFORM_PC`, `minorQuests`;
- entry and exit points must use vanilla-style arrays;
- actor debug symbols must match WolvenKit performer ID formulas;
- spoken and choice screenplay IDs must follow vanilla item ID patterns;
- choice sockets must include the six dummy sockets;
- choice locStore entries must cover the configured locales;
- graph destinations must point at existing nodes;
- journal path `fileEntryIndex` values must match known journal namespaces;
- scene event IDs must be unique and cannot be the max-int placeholder.
