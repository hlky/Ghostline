# World Asset Discovery And Selection

Ghostline keeps reusable world locations in two generated indexes:

- `reference/world/world-sector-candidates.json` is the exhaustive,
  inexpensive binary-sector discovery result.
- `reference/world/world-assets.json` is the detailed placement catalog built
  from a deterministic sample of WolvenKit-serialized sectors.

The discovery index answers “which cooked sectors might contain this family?”
without serializing all Night City sectors. The placement catalog answers
“what concrete node, transform, resource, and NodeRef can a quest author
inspect or select?”

`reference/world/world-assets-curation.json` is the small human-owned review
layer. Generated catalogs must not be hand-edited.

## Safety model

Discovery does not prove that an object is reachable, enabled in the current
game state, compatible with a requested action, or safe to reuse outside its
vanilla quest.

Every detailed record therefore has:

- `categories`: structural families such as `terminal`, `access_point`,
  `antenna`, `door_lock`, `plant_target`, `drop_point`, `loot_anchor`, and
  `vehicle`;
- `tags`: narrower candidate uses;
- `review.accessibility`;
- `review.quest_safety`; and
- `selection_eligible`.

Default `list` and `choose` commands return only records whose accessibility
and quest safety are both `verified`. Pass `--include-unvetted` only for
development searches that will be reviewed in-game.

An asset can be physically accessible and still be rejected for quest use.
The Kabuki `sts_wat_kab_101` antenna access point is the first checked
example: it is reachable and hackable, but belongs to a vanilla activity.

Loot containers tagged `coordinate_anchor_only` are not invitations to mutate
the vanilla container. They are evidence of a walkable, authored location
near which a Ghostline NPC, trigger, or quest-owned device may be placed.

## Current generated coverage

The exhaustive pass scanned 23,691 extracted exterior sector binaries and
found 15,859 candidate sectors. Category matches are not mutually exclusive:

| Category | Candidate sectors |
| --- | ---: |
| Access point | 869 |
| Antenna/satellite | 3,130 |
| Door/lock/restraint | 8,758 |
| Drop point | 122 |
| Loot/staging anchor | 7,439 |
| Plant target | 9,064 |
| Terminal/computer | 1,591 |
| Vehicle/parking | 9,516 |

The detailed v1 catalog is a deterministic, bounded sample plus explicitly
requested known sectors: 760 serialized sectors and 10,055 normalized
placements. It contains 200 terminal candidates, 219 access points, 3,716
antenna visuals/devices, 2,271 doors or locks, 696 plant targets, 84 drop
points, 2,774 loot/staging anchors, and 491 vehicle candidates.

Only two records are default-selection eligible today:

- runtime-proven Kabuki `drop_point_009`; and
- the inspected Kabuki small weapon case as a coordinate-only walkable
  staging anchor.

The catalog intentionally exposes thousands of unvetted candidates for future
World Inspector review without silently treating them as safe.

## Commands

Discover candidate sectors from extracted cooked binaries:

```powershell
py -B .\tools\world_asset_catalog.py discover `
  --binaries H:\path\to\extracted\sectors
```

Serialize a deterministic bounded set. Repeat `--category` to select specific
families; omit it to sample every family:

```powershell
py -B .\tools\world_asset_catalog.py serialize `
  --binaries H:\path\to\extracted\sectors `
  --output H:\Ghostline-audits\world-assets\serialized `
  --limit-per-category 100 `
  --seed ghostline-world-v1
```

Build the normalized placement catalog:

```powershell
py -B .\tools\world_asset_catalog.py build `
  --sectors H:\Ghostline-audits\world-assets\serialized
```

Search unvetted computer candidates near a known point:

```powershell
py -B .\tools\world_asset_catalog.py list `
  --include-unvetted `
  --category terminal `
  --tag document_host_candidate `
  --region watson `
  --area kabuki `
  --near=-1082.949,1412.400,21.773 `
  --radius 500
```

Choose a reviewed anchor deterministically:

```powershell
py -B .\tools\world_asset_catalog.py choose `
  --category loot_anchor `
  --tag coordinate_anchor_only `
  --seed gqt003-extraction-site `
  --format placement
```

The same seed and filtered catalog produce the same record. `--format
placement` emits the fields normally needed by a world spec: origin, yaw,
native NodeRef, source sector, resource, tags, and asset ID.

## Reviewing a candidate

1. Use `list --include-unvetted` to choose a candidate.
2. Visit it in-game and inspect it with World Inspector.
3. Confirm the exact NodeRef, transform, resource, and expected interaction.
4. Check whether it belongs to a vanilla quest or changes with world state.
5. Add an annotation keyed by NodeRef (preferred) or catalog ID to
   `reference/world/world-assets-curation.json`.
6. Set accessibility and quest safety independently.
7. Add capability tags only when runtime evidence supports them.
8. Rebuild the generated catalog and test default selection.

The curation and catalog formats are specified by:

- `tools/world-asset-curation-schema-v1.json`
- `tools/world-asset-catalog-schema-v1.json`

## Test-quest routing

Recommended searches for the building-block test quests:

| Test need | Query |
| --- | --- |
| Terminal document | `terminal` + `document_host_candidate`; then verify the computer can host a quest-owned page/scene |
| Plant item | `plant_target` + `plant_target_candidate` |
| Release NPC | `door_lock` + `release_target_candidate` |
| Escort/defend staging | `loot_anchor` + `coordinate_anchor_only`, placing quest-owned actors nearby |
| Hack device | `access_point` + `hackable_candidate`, excluding vanilla-owned activity devices |
| Vehicle sequence | `vehicle` + `parking_anchor_candidate`; use the transform as a spawn/parking reference unless native reuse is explicitly verified |
| Delivery | `drop_point` + `native_interaction_reusable` |

For interactions, preserve the distinction between selecting a native device
and selecting coordinates on which to place a quest-owned clone. Most
unvetted terminals, doors, vehicles, and access points should initially be
treated as placement references, not directly modified world entities.
