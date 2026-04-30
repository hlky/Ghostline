# Ghostline World Spec

`tools/generate_world.py` consumes a small JSON spec and emits CR2W-JSON for
Ghostline-owned `.streamingsector` and `.streamingblock` resources. The spec is
designed for a capture workflow: record coordinates in game, define local
offsets and trigger shapes in JSON, dry-run the output, then generate raw
resources and deserialize them with WolvenKit.

The checked-in example is `tools/gq000_world_spec.example.json`. It uses
reference coordinates and should be copied before producing real quest assets.

## Commands

```powershell
py .\tools\generate_world.py example
py .\tools\generate_world.py hash "$/mod/gq000/#gq000_pr_patch_meet/#gq000_01_spot_patch_bridge"
py .\tools\generate_world.py measure -- "origin=-287.155151,-1950.40015,8.960001" "target=-280.087708,-1943.4187,8.960001"
py .\tools\generate_world.py generate --spec .\tools\gq000_world_spec.example.json --dry-run
```

When the spec is ready for use:

```powershell
py .\tools\generate_world.py generate --spec .\path\to\gq000_patch_meet.world.json --register --deserialize
```

`--register` adds the generated block path to `source/resources/Ghostline.archive.xl`.
`--deserialize` converts generated raw CR2W-JSON to CR2W binaries under
`source/archive`.

## Coordinate Rules

Distances in the spec are world-coordinate units. Current reference-sector
evidence points to roughly `1` coordinate unit per in-game meter, but final
quest placement still needs an in-game check against HUD/objective distance
rounding.

Use XY distance for flat ground placement:

```text
sqrt((x2 - x1)^2 + (y2 - y1)^2)
```

Use XYZ distance when vertical separation matters:

```text
sqrt((x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2)
```

`WorldPosition` persistent data stores coordinates as `FixedPoint.Bits =
round(coordinate * 131072)`. The generator applies that conversion for
community workspot persistent data.

## Minimal Spec

```json
{
  "name": "gq000",
  "prefab_root": "$/mod/gq000/#gq000_pr_patch_meet",
  "origin": {
    "x": -287.155151,
    "y": -1950.40015,
    "z": 8.96000099,
    "yaw": -135
  },
  "markers": [
    {
      "ref": "#gq000_01_sm_patch_bridge",
      "position": {
        "from": "origin"
      }
    }
  ],
  "triggers": [
    {
      "ref": "#gq000_01_tr_engage",
      "outline": {
        "type": "rectangle",
        "width": 4,
        "depth": 4,
        "height": 2
      }
    }
  ]
}
```

## Top-Level Fields

| Field | Required | Default | Description |
| --- | --- | --- | --- |
| `_note` | No | Ignored | Free-form note field for humans. Unknown fields are ignored by the generator. |
| `name` | No | `ghostline` | Used only to build default output paths. |
| `prefab_root` | Yes | None | Root NodeRef for local refs. Local `#foo` refs become `<prefab_root>/#foo`. |
| `block_path` | No | `mod\{name}\world\all.streamingblock` | Depot path for the generated streaming block. |
| `quest_sector_path` | No | `mod\{name}\world\quest.streamingsector` | Depot path for the generated quest streaming sector. |
| `always_loaded_sector_path` | No | `mod\{name}\world\always_loaded.streamingsector` | Depot path for the always-loaded sector. Used when `community`, `always_loaded_node_refs`, or an always-loaded marker is present. |
| `origin` | Yes | None | Base coordinate and optional yaw. See position formats below. |
| `yaw` | No | `0` | Origin yaw fallback if `origin` is an array or omits `yaw`. |
| `streaming_box` | No | `world` | Quest descriptor bounds. See streaming box formats below. |
| `quest_sector_level` | No | `255` | `level` written into the generated quest `.streamingsector`. The block descriptor remains level `0`. |
| `always_loaded_level` | No | `1` | `level` written into the generated always-loaded `.streamingsector`. The block descriptor remains level `1`. |
| `markers` | No | `[]` | Static marker nodes to create. |
| `always_loaded_node_refs` | No | `[]` | Advanced: additional NodeRefs to register in the always-loaded sector without creating duplicate nodes. Prefer `markers[].sector = "always_loaded"` for journal/static mappin marker resolution. |
| `triggers` | No | `[]` | Trigger area nodes to create. |
| `community` | No | None | Optional Patch-style AI spot, streamable community area, and always-loaded registry. |

Depot paths may use `/` or `\`; the generator normalizes them to backslashes.

## Ref Rules

Any node `ref` can be local or absolute:

```json
"#gq000_01_tr_engage"
"gq000_01_tr_engage"
"$/mod/gq000/#gq000_pr_patch_meet/#gq000_01_tr_engage"
```

Refs beginning with `$/` are left unchanged. Other refs are made local by
adding `#` if needed, then appended to `prefab_root`.

Each generated node becomes an anchor after it is created. It can then be
referenced by later nodes using its original ref, full NodeRef, local name, or
`#local_name`. Order matters: markers are generated first, then triggers, then
community spot and area, then always-loaded registration-only refs.

## Position Formats

Absolute position as an object:

```json
{
  "x": -287.155151,
  "y": -1950.40015,
  "z": 8.96000099
}
```

Absolute position as an array:

```json
[-287.155151, -1950.40015, 8.96000099]
```

Relative position from an anchor:

```json
{
  "from": "#gq000_01_sm_patch_bridge",
  "forward": 8,
  "right": -2,
  "up": 0.25
}
```

Relative polar position:

```json
{
  "from": "origin",
  "distance": 12,
  "bearing": 90
}
```

| Field | Default | Description |
| --- | --- | --- |
| `from` | `origin` | Anchor to offset from. |
| `yaw` | Anchor yaw | Yaw used to interpret `forward`, `right`, and `bearing`. Can be a number, `origin`, `anchor`, or another anchor name. |
| `forward` | `0` | Local forward offset in world-coordinate units. |
| `right` | `0` | Local right offset in world-coordinate units. |
| `up` | `0` | Z offset. |
| `z_offset` | `0` | Alias for `up`; ignored if `up` is present. |
| `distance` | None | Adds a polar offset in local space. |
| `bearing` | `0` | Bearing in degrees relative to the resolved yaw. `0` is forward, `90` is right, `180` is back, `-90` is left. |

If `position` is omitted on a marker, trigger, community area, or spot, the node
is placed at `origin`.

## Yaw

Node `yaw` can be:

```json
-135
"origin"
"#gq000_01_sm_patch_bridge"
```

A numeric yaw is used directly. `origin` and `anchor` mean the yaw resolved by
the node's `position` anchor. Any other string is treated as an anchor name.

## Streaming Box

Use `"world"` while prototyping if you do not want tight descriptor bounds:

```json
"streaming_box": "world"
```

Use exact bounds when you know them:

```json
{
  "streaming_box": {
    "min": [-340, -2190, -145],
    "max": [-30, -1885, 160]
  }
}
```

Use automatic bounds with padding around every generated position:

```json
{
  "streaming_box": {
    "padding": 300
  }
}
```

`padding` defaults to `300` if a streaming-box object is provided without
`min` and `max`.

## Marker Spec

Markers create `worldStaticMarkerNode` entries.

```json
{
  "ref": "#gq000_01_sm_patch_bridge",
  "sector": "always_loaded",
  "position": {
    "from": "origin"
  },
  "yaw": "origin",
  "debug_name": "{gq000_01_sm_patch_bridge}",
  "tag": "None",
  "tag_ext": "None",
  "source_prefab_hash": "0",
  "node_data": {
    "max_streaming_distance": 120
  }
}
```

| Field | Required | Default | Description |
| --- | --- | --- | --- |
| `ref` | Yes | None | Marker NodeRef. |
| `sector` | No | `quest` | Use `always_loaded` to create the marker in the always-loaded sector instead of the quest sector. This is preferred for journal/static mappin marker refs that must resolve before the quest sector streams. |
| `position` | No | `origin` | Absolute or relative position. |
| `yaw` | No | Position anchor yaw | Node yaw. |
| `debug_name` | No | `{local_ref}` | `worldStaticMarkerNode.debugName`. |
| `tag` | No | `None` | Node tag. |
| `tag_ext` | No | `None` | Node `tagExt`. |
| `source_prefab_hash` | No | `0` | Node `sourcePrefabHash`. |
| `node_data` | No | Defaults | Advanced `worldCompiledNodeInstanceSetupInfo` overrides. |

## Trigger Spec

Triggers create `worldTriggerAreaNode` entries.

```json
{
  "ref": "#gq000_01_tr_engage",
  "position": {
    "from": "origin",
    "forward": 5
  },
  "yaw": "origin",
  "outline": {
    "type": "rectangle",
    "width": 4,
    "depth": 4,
    "height": 2
  },
  "notifiers": ["quest"]
}
```

| Field | Required | Default | Description |
| --- | --- | --- | --- |
| `ref` | Yes | None | Trigger NodeRef. |
| `position` | No | `origin` | Absolute or relative position. |
| `yaw` | No | Position anchor yaw | Node yaw. |
| `outline` | No | 2 x 2 rectangle, height 2 | Trigger area outline. |
| `notifiers` | No | `["quest"]` | Trigger notifier or list of notifiers. |
| `debug_name` | No | `{local_ref}` | `worldTriggerAreaNode.debugName`. |
| `tag` | No | `None` | Node tag. |
| `tag_ext` | No | `None` | Node `tagExt`. |
| `source_prefab_hash` | No | `0` | Node `sourcePrefabHash`. |
| `node_data` | No | Defaults | Advanced node-data overrides. |

### Trigger Outlines

Rectangle:

```json
{
  "type": "rectangle",
  "width": 8,
  "depth": 4,
  "height": 2
}
```

Aliases for `type`: `rectangle`, `box`, `square`.

| Field | Default | Description |
| --- | --- | --- |
| `width` | `size` or `2` | Local X size of the outline. |
| `depth` | `length`, `size`, or `width` | Local Y size of the outline. |
| `length` | None | Alias used as a fallback for `depth`. |
| `size` | `2` | Fallback square size. |
| `height` | `2` | Vertical trigger height. |

Circle or regular polygon:

```json
{
  "type": "circle",
  "radius": 5,
  "segments": 16,
  "height": 2
}
```

Aliases for `type`: `circle`, `disc`, `regular_polygon`.

| Field | Default | Description |
| --- | --- | --- |
| `radius` | `1` | Radius in world-coordinate units. |
| `segments` | `12` | Number of generated points. |
| `points_count` | `segments` or `12` | Alias with priority over `segments`. Must be at least `3`. |
| `height` | `2` | Vertical trigger height. |

Custom local points:

```json
{
  "points": [
    [-2, -2, 0],
    [3, -1, 0],
    [2, 3, 0],
    [-3, 1, 0]
  ],
  "height": 2
}
```

Custom points are local to the trigger node. The generator serializes them into
`AreaShapeOutline.buffer`, which is the source of truth for the outline.

### Trigger Notifiers

`notifiers` can be a single string, a single object, or a list.

```json
"notifiers": "quest"
```

```json
"notifiers": ["quest", "interior"]
```

Supported built-in notifier names:

| Name | Generated type | Notes |
| --- | --- | --- |
| `quest` | `questTriggerNotifier_Quest` | Default quest trigger notifier. |
| `interior` | `worldInteriorAreaNotifier` | Player-channel interior notifier. |
| `prevention` | `worldQuestPreventionNotifier` | Deescalation notifier. |
| `prevention_deescalation` | `worldQuestPreventionNotifier` | Same as `prevention`. |

Raw CR2W notifier data can be inserted for cases the generator does not know:

```json
{
  "raw": {
    "$type": "questTriggerNotifier_Quest",
    "excludeChannels": 0,
    "includeChannels": "TC_Default",
    "isEnabled": 1
  }
}
```

## Community Spec

The `community` block creates three pieces:

- `worldAISpotNode` in the quest sector
- `worldCompiledCommunityAreaNode_Streamable` in the quest sector
- `worldCommunityRegistryNode` in the always-loaded sector

```json
{
  "community": {
    "ref": "#gq000_01_com_patch_bridge",
    "entry": "patch",
    "phase": "default",
    "period": "Day",
    "character": "Character.GhostlinePatch",
    "appearance": "default",
    "source_object_id": "auto",
    "active_on_start": 1,
    "spot": {
      "ref": "#gq000_01_spot_patch_bridge",
      "position": {
        "from": "origin",
        "right": -1.5
      },
      "yaw": "origin",
      "workspot": "base\\workspots\\common\\wall\\generic__stand_wall_lean_back_cigarette__smoke__01.workspot"
    }
  }
}
```

| Field | Required | Default | Description |
| --- | --- | --- | --- |
| `ref` | Yes | None | Community area NodeRef. Also used to derive `source_object_id` when set to `auto`. |
| `position` | No | `origin` | Position for the streamable community area node. |
| `yaw` | No | Position anchor yaw | Community area node yaw. |
| `debug_name` | No | `{local_ref}` | Community area debug name. |
| `entry` | No | `patch` | Community entry name. |
| `phase` | No | `default` | Community phase name. |
| `period` | No | `Day` | Time period name. |
| `is_sequence` | No | `0` | Written to area and registry time-period data. |
| `source_object_id` | No | `auto` | Numeric entity hash. `auto` hashes the full community area NodeRef. |
| `source_prefab_hash` | No | `0` | Community area `sourcePrefabHash`. |
| `streaming_distance` | No | `0` | Community area `streamingDistance`. |
| `tag` | No | `None` | Community area tag. |
| `tag_ext` | No | `None` | Community area `tagExt`. |
| `node_data` | No | Defaults | Community area node-data overrides. |
| `community_area_type` | No | `Regular` | Registry item `communityAreaType`. |
| `active_on_start` | No | `1` | Initial state for the entry. |
| `character` | No | `Character.GhostlinePatch` | TweakDBID for the spawned character. |
| `appearance` | No | `default` | Single appearance fallback. |
| `appearances` | No | `[appearance]` | String or array of appearances. Overrides `appearance` when present. |
| `always_spawned` | No | `default__false_` | Registry spawn phase flag. |
| `prefetch_appearance` | No | `0` | Registry spawn phase flag. |
| `quantity` | No | `1` | Spawn quantity for the time period. |
| `spawn_in_view` | No | `default__true_` | Registry spawn entry flag. |
| `spawn_set_reference` | No | `None` | Registry spawn-set reference. |
| `registry_debug_name` | No | `registry` | Always-loaded registry node debug name. |
| `registry_source_prefab_hash` | No | `0` | Registry node `sourcePrefabHash`. |
| `spot` | No | Defaults | AI spot settings. Provide this explicitly for real specs. |

### Community Spot

The nested `community.spot` block controls the generated `worldAISpotNode`.

| Field | Required | Default | Description |
| --- | --- | --- | --- |
| `ref` | No | `#gq000_01_spot_patch_bridge` | AI spot NodeRef. |
| `position` | No | `origin` | Spot position. |
| `yaw` | No | Position anchor yaw | Spot yaw and persistent workspot yaw. |
| `global_node_id` | No | Hash of full spot NodeRef | Explicit `worldGlobalNodeID` override. |
| `workspot` | No | Wall-lean cigarette workspot | Workspot resource path. |
| `debug_name` | No | `{local_ref}` | AI spot debug name. |
| `source_prefab_hash` | No | `0` | AI spot `sourcePrefabHash`. |
| `tag` | No | `None` | AI spot tag. |
| `tag_ext` | No | `None` | AI spot `tagExt`. |
| `node_data` | No | Defaults | AI spot node-data overrides. |
| `is_workspot_infinite` | No | `1` | `worldAISpotNode.isWorkspotInfinite`. |
| `is_workspot_static` | No | `0` | `worldAISpotNode.isWorkspotStatic`. |
| `markings` | No | `[]` | CName markings on the AI spot. |
| `clipping_space_orientation` | No | `180` | `AIActionSpot.clippingSpaceOrientation`. |
| `clipping_space_range` | No | `120` | `AIActionSpot.clippingSpaceRange`. |
| `snap_to_ground` | No | `0` | `AIActionSpot.snapToGround`. |
| `use_clipping_space` | No | `0` | `AIActionSpot.useClippingSpace`. |

## Always-Loaded NodeRef Registrations

`always_loaded_node_refs` writes node-data entries and `nodeRefs` into the
always-loaded sector without adding duplicate concrete nodes. This remains
available for mirroring refs that already exist in another sector, but static
marker refs for journal mappins should usually be created directly in the
always-loaded sector with `markers[].sector = "always_loaded"`.

Preferred marker form:

```json
{
  "markers": [
    {
      "ref": "#gq000_01_sm_patch_bridge",
      "sector": "always_loaded",
      "position": {
        "from": "origin"
      }
    }
  ]
}
```

The short form reuses the position and yaw from an already generated anchor:

```json
{
  "always_loaded_node_refs": [
    "#gq000_01_sm_patch_bridge"
  ]
}
```

The object form allows an explicit position, yaw, and node-data overrides:

```json
{
  "always_loaded_node_refs": [
    {
      "ref": "#gq000_01_sm_patch_bridge",
      "position": {
        "from": "origin"
      },
      "node_data": {
        "max_streaming_distance": 9513.75586,
        "streaming_distance": 512,
        "uk10": 32
      }
    }
  ]
}
```

If `node_data` is omitted, these registrations use mq003-style mappin defaults:
`max_streaming_distance = 9513.75586`, `streaming_distance = 512`, and
`uk10 = 32`.

## Node Data Overrides

`node_data` can be used on markers, triggers, community areas, community spots,
and always-loaded NodeRef registrations. Leave this out unless a reference
sector shows you need to tune compiled node setup values.

```json
{
  "node_data": {
    "max_streaming_distance": 120,
    "streaming_distance": 100,
    "scale_x": 1,
    "scale_y": 1,
    "scale_z": 1,
    "uk10": 1024,
    "uk11": 512,
    "uk12": 0,
    "uk13": "0",
    "uk14": "0"
  }
}
```

| Field | Default | Description |
| --- | --- | --- |
| `scale_x` | `1` | Node setup scale X. |
| `scale_y` | `1` | Node setup scale Y. |
| `scale_z` | `1` | Node setup scale Z. |
| `max_streaming_distance` | `120` | Node setup `MaxStreamingDistance`. |
| `streaming_distance` | `100` | Node setup `UkFloat1`. |
| `uk10` | `1024` | Unknown node setup integer from references. |
| `uk11` | `512` | Unknown node setup integer from references. |
| `uk12` | `0` | Unknown node setup integer from references. |
| `uk13` | `"0"` | Unknown node setup NodeRef-like field from references. |
| `uk14` | `"0"` | Unknown node setup NodeRef-like field from references. |

The always-loaded community registry node uses a fixed internal node-data setup:
`max_streaming_distance = 17.320507`, `streaming_distance = 100000000`, and
`uk10 = 32`.

## Generated Outputs

Without `community`, the generator writes:

- quest sector JSON at `<raw-root>/<quest_sector_path>.json`
- streaming block JSON at `<raw-root>/<block_path>.json`

With `community`, `always_loaded_node_refs`, or an always-loaded marker, it also writes:

- always-loaded sector JSON at `<raw-root>/<always_loaded_sector_path>.json`

Archive targets mirror the depot paths under `source/archive`.

## Validation Workflow

1. Copy `tools/gq000_world_spec.example.json` to a quest-specific spec.
2. Replace `origin` with coordinates captured in game.
3. Use `measure` to compare captured points and planned offsets.
4. Run `generate --dry-run`.
5. Generate to a temporary raw/archive root if you want a clean deserialization test.
6. Run `generate --register --deserialize` only when ready to write project assets.
7. Inspect generated raw files with `tools/explore_world.py`.

Useful checks:

```powershell
py .\tools\explore_world.py --file .\source\raw\mod\gq000\world summary
py .\tools\explore_world.py --file .\source\raw\mod\gq000\world nodes --type TriggerArea --limit 0
py .\tools\explore_world.py --file .\source\raw\mod\gq000\world communities
```
