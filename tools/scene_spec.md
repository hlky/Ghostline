# Ghostline Scene Spec

`tools/generate_scene.py` consumes a compact JSON spec and emits WolvenKit
CR2W-JSON for `.scene` resources. The checked-in production fixture is:

```powershell
py .\tools\generate_scene.py audit --spec .\projects\ghostline\quests\gq000\implementation\scenes\patch-meet.scene-spec.json
py .\tools\generate_scene.py generate --spec .\projects\ghostline\quests\gq000\implementation\scenes\patch-meet.scene-spec.json --dry-run
py .\tools\generate_scene.py generate --spec .\projects\ghostline\quests\gq000\implementation\scenes\patch-meet.scene-spec.json
py .\tools\generate_scene.py validate --file .\projects\shared\ghostline-runtime\source\raw\mod\gq000\scenes\gq000_patch_meet.scene.json --spec .\projects\ghostline\quests\gq000\implementation\scenes\patch-meet.scene-spec.json
py -B -m unittest discover -s tests -v
py .\tools\generate_scene.py generate --spec .\projects\ghostline\quests\gq000\implementation\scenes\patch-meet.scene-spec.json --deserialize
```

The generator uses vanilla scene shells from `reference/vanilla_extract_json`
and local WolvenKit source assumptions. It does not use the removed root-level
legacy scene template,
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
| `lipsync_animset` | No | Shared depot path used for emitted lipsync resource rows. The current generator cannot assign a different path per slot. |
| `actors` | Yes | Scene actors, currently `community` NPCs and `player` actors. |
| `spoken_line_order` | Yes | Manifest keys assigned screenplay IDs `1 + 256n`. |
| `choice_line_order` | Yes | Manifest keys assigned option IDs `2 + 256n`. |
| `choice_locales` | No | Locale descriptors to embed for every choice. Defaults to `db_db`, `pl_pl`, and `en_us`. |
| `entry_point` | Yes | Primary scene entry point name and node id. Every entry point must target a `scnStartNode`. |
| `entry_points` | No | Multiple named scene entries. Use with `start_nodes`; each entry must target its own start node. |
| `exit_points` | Yes | Scene exit point names and node ids. Include questphase sockets such as `job_accept`. |
| `start_node` | Yes | Primary start node id and outgoing destinations. Retained for backward compatibility when `start_nodes` is omitted. |
| `start_nodes` | No | Multiple start nodes for scenes with alternate questphase entry points. |
| `graph_order` | No | Explicit scene graph node order. If omitted, nodes are ordered by connections from the primary start node and unvisited nodes are appended. |
| `sections` | Yes | Dialogue section nodes and their spoken line keys. |
| `choices` | No | Choice nodes and options. |
| `quest_nodes` | No | Scene-local quest wrapper nodes for journal, mappin, trigger, AI setup, player item unequip, status effects, or gameplay/cinematic tier changes. |
| `props` | No | Scene props acquired with `findInNode`; generic RID camera entities should be declared here so the scene owns their lifecycle. |
| `xor_nodes` | No | Xor nodes for vanilla-compatible branch joins. |
| `rid_resources` | No | RID resource IDs and depot paths. Generated as synchronous `Default` references, matching the engine field and vanilla scenes. |
| `rid_animations` | No | RID resource/serial pairs exposed to body and head animation events. |
| `rid_camera_animations` | No | RID resource/serial pairs exposed to RID camera events. |
| `end_node` | Conditional | Terminal `scnEndNode` id. Required when `end_nodes` is omitted. |
| `end_nodes` | Conditional | Multiple terminal `scnEndNode` ids for distinct exits. Required when `end_node` is omitted. |

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

Scene-local quest wrapper nodes map input ordinal `0` to `CutDestination` and
ordinary executable flow to `In` at ordinal `1`. Every regular destination to
one of those nodes must therefore set `"input_ordinal": 1`; only an actual
`scnCutControlNode` may route to `CutDestination`. Validation rejects regular
flow that targets the cut-control socket.

`graph_order` is optional and should normally be omitted. Use it when the
runtime/editor shape intentionally keeps an unreachable graph node in a
specific position, such as the current fallback end node `18`, which has no
incoming scene-graph edge. When present, it must list every generated graph
node exactly once, and validation checks that raw scenes keep that order.

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
  "lipsync": 0
}
```

Actor performer debug symbols are generated as `actorID * 256 + 1`.
Prop performer debug symbols are generated as `propID * 256 + 2`.

`lipsync` is an index into `resouresReferences.lipsyncAnimSets`, not an actor
ID. Every referenced index must remain addressable after CR2W cooking. The
current production fixture deliberately gives the Patch-role actor and V slot
`0` and emits one generic row: an earlier two-slot fixture repeated the same
depot path, cooked to one runtime import, and crashed when V requested slot
`1`. Do not use
multiple indexes until the generator supports distinct valid per-slot resource
paths and the packed table has been verified.

RID player events can set `fpp: true` and provide `fpp_gender_params` with
gender masks plus trajectory-space blend and end-input Euler angles. Preserve
the exact values from the vanilla RID use site: generic sex cameras are
head-local FPP cameras, and vanilla wraps their playback in a
`scene_tier` quest node using `Tier4_FPPCinematic` and `force_empty_hands`,
then restores `Tier1_FullGameplay`. Use `unequip_player` with
`unequip_types: AllWeapons` when the weapon must remain holstered during the
preceding or following dialogue. `unequip_actor` targets a named community
entry and can use an exact `item_id` plus `slot_id`; this is appropriate for a
known NPC weapon that must be absent before a performance. Set `instant: true`
for a hard post-combat handoff, while keeping the underlying state-machine
bypass disabled. `realtime_delay` emits a vanilla-shaped real-time pause and
can give equipment/appearance changes a short settle boundary.
`player_status_effect` accepts a TweakDB record such as
`BaseStatusEffect.Knockdown`; status duration and recovery are owned by that
record.

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
      "node_id": 19
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
      "icon_tags": [
        "ChoiceCaptionParts.BraindanceIcon"
      ],
      "target_node_id": 7
    }
  ]
}
```

Every choice option gets embedded locStore descriptors for all configured
locales. The default order is vanilla-style `db_db`, `pl_pl`, then `en_us`;
`db_db` emits two descriptors per choice, a blank fallback payload followed by
the source text payload. Within every locale block, descriptors are sorted by
the unsigned numeric value of `locstringId`, not by manifest order or decimal
string order. Duplicate `db_db` descriptors stay adjacent.

The option `caption` is an authoring/debug label. Player-visible text resolves
from `screenplayStore.options[].locstringId` through the embedded `locStore`.
See `projects/ghostline/quests/gq000/implementation/runtime-flow.md` for the complete lookup chain and the separate
scene ID domains.

`single_choice` is written directly to `isSingleChoice`; do not use it to infer
whether an option is optional or progression-critical. Use `choice_type` for the
raw `gameinteractionsChoiceTypeWrapper.properties` value copied from the chosen
vanilla pattern. Optional `icon_tags` are emitted as string-backed TweakDBIDs;
copy their exact case-sensitive values from a validated vanilla interaction.

## Supported Quest Nodes

V1 supports the scene-local quest node shapes needed by `gq000_patch_meet`:

- `puppet_ai`: cinematic AI tier setup for a community actor.
- `pause_condition`: player trigger checks, optionally requiring player not in combat.
- `scene_tier`: player gameplay/cinematic tier and empty-hands state.
- `unequip_player`: unequip a player item category, optionally instantly.
- `unequip_actor`: unequip an item/category from a named community actor.
- `realtime_delay`: real-time delay in hours, minutes, seconds, and milliseconds.
- `player_status_effect`: add or remove a player status effect.
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
- RID resources must use synchronous `Default` references;
- spoken and choice screenplay IDs must follow vanilla item ID patterns;
- choice sockets must include the six dummy sockets;
- choice locStore entries must form the configured contiguous locale blocks;
- every locale block must be sorted by unsigned numeric `locstringId`;
- each `db_db` choice must have at least two payloads and put a blank payload
  first;
- graph destinations must point at existing nodes;
- ordinary graph flow into a scene-local quest node must target its executable
  `In` socket, never `CutDestination`;
- journal path `fileEntryIndex` values must match known journal namespaces;
- scene event IDs must be unique and cannot be the max-int placeholder.
