# In-Game World Location Database

## Camera survey v2 (2026-10-28)

`tools/world-location-capture-survey-v2.json` uses a separate `category-runs/survey-v2`
workspace. All eligible views are requeued, including previously captured centers.
Earlier category databases, image files and capture history are retained. Known
kill zones and rejected/uncalibrated placements remain excluded.

Context views have center and ±45° headings; targeted device/entrance detail
views stay single. Parking uses four headings at 90° intervals, 2 m above the
previous player position with camera pitch −20°. Every sidecar records the
actual active-camera orientation and origin as well as the player position.

FreeFly must be active. Loading UI lifecycle, player attachment and fast-travel
blackboard signals pause movement and capture, with a 30-second loading budget.
Frame checks add temporal settling and learned engine-labelled loading-screen
signatures; these do not prove that every distant object has finished streaming.
Pose settling and active visual retries retain their short 5-second limits.

Context obstruction checks use a small ray grid. Up to two lateral moves may
improve a blocked view, restricted to preapproved in-scope candidates. Otherwise
the best available view is kept with obstruction diagnostics. A shared geographic
route groups nearby stations across categories. Clear moves up to 20 m use gradual
FreeFly movement; larger or blocked moves use teleportation.

After reloading CET mods (or restarting the game), activate FreeFly and run:

```powershell
.\tools\run_world_location_survey_sample.ps1
```

This captures ten trial views: three landing angles, four raised parking headings,
and three vending-machine context angles. Inspect them before the full pass:

```powershell
.\tools\run_world_location_batch.ps1
```

The batch launcher now resumes the combined survey by default. `-Categories`
filters the shared route; `-Legacy` selects the earlier category workspaces.
`tools/prepare_world_location_survey.py` builds a new snapshot and refuses to
overwrite an existing survey database. The manifest under `survey-v2/reports`
records queue totals and preserved history. Runtime behavior still requires an
in-game trial; mocked camera and loading checks cannot establish native behavior.

The location-scouting caption proposal and original 32-image review are documented in
`docs/authoring/world-location-captioner.md`. The proposed machine-readable
contract is `tools/world-location-caption-v1.schema.json`; sample manifests,
contact sheets, review notes and a validated manual example are under
`converted/world-location-database/reports/captioner-review-20261027`. This is a
captioner design, not a completed bulk captioning run or capture-publication step.
Contract revision 0.2.0 captions each image independently for quest-location
selection: physical layout, scene features, connections, visual character,
structural lighting and concrete scene uses. Pair evaluation, HUD annotation and
generated verification checklists were removed; capture QA is a separate stage.

## Fast-Travel Category Pilot (2026-10-27)

`tools/world-location-capture-fast-travel-v1.json` owns the separate
`converted/world-location-database/category-runs/fast-travel-v1` workspace.
It reuses a read-only snapshot of the static world index, with no road captures,
places, attempts or sessions copied into its working history. Roads remain the
default preset; the shared launcher accepts `-Config` to select another workspace.

223 indexed anchors become 190 locations after 5 m anchor deduplication: 380
views total. The corrected `usable_side_pair` profile uses entity-local **+X**,
transformed by the placed entity rotation, at the entity's original height.
`arrival_area` is 1.5 m in front of the usable side and faces outward;
`terminal` is 5 m in front and faces back toward the installation.
The user confirmed in game that the inferred -X side was behind the terminal,
so the usable-side rule was reversed to +X. The interaction-workspot transform
alone did not establish the visible front. Previous +Y and -X captures remain
historical evidence, and all 380 views were requeued after the correction.
Pair IDs, reciprocal view IDs and native fast-travel
marker/record references remain in provenance. FreeFly preserves the planned pose.
The extracted entity references and correction audit are under
`converted/fast-travel-front-references` and the workspace report
`reports/fast-travel-usable-side-fix.json`. Corrected framing still needs visual
confirmation for the individual terminal/metro-gate appearances.

The initial pilot selected eight geographically spread locations (16 views).
The user subsequently requested the entire category: all 380 views are now
enabled, with `require_category_calibration=false` and explicit
`category_capture_approved=true`. This authorizes capture, not publication or a
claim that every camera angle has been reviewed. The original pilot IDs remain
in `workspace.pilot_anchor_ids`, and the sample launcher still selects those views.

With FreeFly active and the CET overlay closed, run:

```powershell
.\tools\run_world_location_fast_travel_sample.ps1
```

The selected views and initial database audit are in the workspace's
`reports/fast-travel-calibration-sample.json` and `reports/workspace-manifest.json`.
This preparation does not start capture or change the roads queue.

## Unattended Category Batch

`tools/run_world_location_batch.ps1` waits for the current controller's OS lock
to become available, then sequentially runs the roads, fast-travel, drop-point,
vending-machine, parking-area and road-barrier presets. `-Categories` selects a
subset in that order. Every runner still performs its own preflight and acquires its OS locks.
It resumes pending/interrupted locations; it does not recapture completed views
or automatically retry previously failed locations. A fatal runtime/game failure
stops the batch rather than launching another controller into the unhealthy game.

`tools/world-location-capture-drop-points-v1.json` owns the separate
`category-runs/drop-points-v1` workspace: 103 anchors and 206 views. Both views
use the anchor's original height and a 3 m outward offset. `drop_point` faces the
device, and `surroundings` faces outward. Existing calibrated extraction rules
provide placement; the full category is capture-approved at the user's request.
Native hazards and ordinary image/metadata review remain active.

With FreeFly active and the CET overlay closed:

```powershell
.\tools\run_world_location_batch.ps1
```

The vending-machine preset is `tools/world-location-capture-vending-machines-v1.json`
and its workspace is `category-runs/vending-machines-v1`. It selects 2,000 of
8,466 indexed machines after hazard filtering and 15 m minimum 3D viewpoint
spacing. If more candidates survive, a deterministic sample distributed across
Morton spatial order limits the queue to 2,000. Completed locations take priority
when replanning. Each location gets one **outward** view toward the street or
surrounding space, preserving the machine's serialized height. Placement uses
the existing 0.45 m family front extent plus 1 m clearance along the extracted
forward axis; it does not face back at the machine. Other categories and their
capture histories remain separate.

The next capture-approved category queues are separate workspaces with fresh
capture histories, using read-only snapshots of the drop-point world index:

- `parking-areas-v1` / `world-location-capture-parking-areas-v1.json`: 708 pending
  views at 354 parking stops after 50 m anchor spacing and hazard filtering.
  Opposite views share a viewpoint 4 m along the native parking marker's forward
  axis: one looks back at the parking context, the other toward the surroundings.
- `road-barriers-v1` / `world-location-capture-road-barriers-v1.json`: 222 pending
  views at 111 barrier installations after 10 m anchor spacing and filtering.
  Viewpoints are 8 m on either side, looking toward the barrier. The pairing
  avoids relying on an inferred usable-side sign.

Both queues have reciprocal location IDs and shared pair IDs. All pending pairs
are complete; excluded views remain disabled. Camera usefulness still needs
image review for each category. The archived database and existing captures are
unchanged. Resume vending and then capture the new queues with:

```powershell
.\tools\run_world_location_batch.ps1 -Categories vending_machine,parking_space,road_barrier
```

The batch also includes separate `fake-garage-doors-v1`, `intercoms-v1`,
`access-points-v1`, `terminals-v1`, and `fake-doors-v1` workspaces. Pending views
at preparation were 542, 326, 380, 876, and 15,070 respectively. Every pending
view has a reciprocal partner and a shared pair ID. Fake door families are
filtered by extraction rule, so the two workspaces do not overlap. Their outward
view is 1.5 m along the indexed normal; their building view is 15 m along it,
facing back, at the original door height with FreeFly. Exterior-side correctness
still requires per-model image review. The unscoped legacy planner retains both
door families together for compatibility.

Intercoms, access points and terminals use device/context pairs from nearby AI
workspot or parking references, rather than guessing the model front. References
must be 3–20 m away with at most 3 m vertical drop and a distance/height ratio of
at least three. Missing suitable references defer 24 intercom, 163 access-point
and 94 terminal anchors after deduplication; those reports are in each workspace's
`reports/site-survey-ground-gaps.json`. Reference positions do not prove line of
sight or absence of intervening walls. Camera usefulness needs image review.

The smaller new queues run before the large fake-door queue. Run all category
queues, including pending vending views, with `run_world_location_batch.ps1`
without `-Categories`. Completed captures are skipped. A running older batch
does not acquire categories added after it started; invoke the updated launcher
to include these additions. No existing or archived capture history was changed.

## Active Category Workspace (2026-10-27)

The default configuration is now `tools/world-location-capture-roads-v1.json`.
Its output is `converted/world-location-database/category-runs/roads-v1`.
Only the `road` category may be planned/captured in this workspace. The launcher
writes logs under that workspace's reports directory and accepts `-Category road`.

The previous `full-world` directory is the archive: 2,099 captures and the original
database remain at their existing paths. `ARCHIVED.json` records the database
hash/counts and points to the successor. CLI write operations reject archived
workspaces; status/export can still read them. The fresh database reused the
world index but contains no old captures, attempts, sessions, or place overrides.

The original 2,816 proxy-center road proposals remain disabled. Road geometry now
comes from native `worldBendedMeshNode` instances with `isBendedRoad=true`:
`deformationData[].W.xyz` supplies local centerline stations and `.Y.xyz` supplies
longitudinal directions. Apply instance scale, quaternion rotation, then position
to stations; directions receive scale/rotation only. The local `deformedBox`
validates stations, with 0.25 m tolerance; it never substitutes for the curve.
Positions interpolate adjacent baked stations by arc length. Headings interpolate
their native directions. Each segment stays independent, so shared template
meshes or nearby endpoints cannot create shortcuts through buildings. Metro/rail
templates, malformed frames and stations outside their local envelope are excluded.

The user confirmed the eight-view sample in game. The active workspace now enables
broader road coverage with 250 m minimum separation across native segments, using
3D distance and retaining opposing views together. Existing captured sample
positions take priority and retain their capture history. The deformation method
is approved; individual captures still require ordinary metadata/image review.
Other categories and the old proxy proposals remain disabled.

Run the expanded queue with FreeFly active and the CET overlay closed:

```powershell
.\tools\run_world_location_overnight.ps1 -Category road
```

`prepare-road-sample` can deliberately return to a small calibration queue. It
rebuilds this derived road geometry from read-only sectors
and enables four separated city-road positions, with opposing views at each.
In sample mode, only `workspace.calibration_capture_road_ids` enter that queue;
all eight views retain `needs_calibration` until reviewed in game. Replanning
retains the sample selection. The native source sector, node, mesh and stable pair
IDs accompany each view. Hazard exclusions remain in force.

Activate FreeFly, close the CET overlay, then run:

```powershell
.\tools\run_world_location_road_sample.ps1
```

The sample manifest is `reports/road-calibration-sample.json` in `roads-v1`.
`reports/road-deformation-build.json` records the decoded road count and rejected
instances. To rebuild the sample deliberately (reads the whole sector collection):

```powershell
.venv\Scripts\python.exe -B tools/world_location_capture.py prepare-road-sample
```

The world-location pipeline turns the serialized Night City streaming sectors
into deterministic in-game capture destinations. It keeps the serialized
sectors read-only, processes one sector at a time, and stores searchable
features, planned poses, runtime evidence, captures, and failures in SQLite.

CET emits `ready` from the first `onDraw` after every load, pose, collision,
velocity, camera, and suppression predicate passes. Python then uses Windows
Graphics Capture for the game window, rejects black/loading frames and applies
the configured `visual_settle_seconds` interval (currently 2 seconds) before
capturing the client rectangle. Readiness and visual settling are separate
checks; heading and FOV drift are recorded as diagnostics, not rejection gates.

## Files and Output

The implementation lives in:

- `tools/world_location_capture.py` — CLI entry point;
- `tools/world_locations/` — SQLite, extraction, planning, protocol, capture,
  validation, and export modules;
- `tools/world-location-capture-v1.json` — versioned rules and capture profile;
- `tools/world_location_capture_cet/` — reversible CET runtime;
- `tests/test_world_location_capture.py` — offline and protocol acceptance tests.

The configured output is:

```text
converted/world-location-database/full-world/
  locations.sqlite3
  capture-config.json
  runtime/
    cet-runtime.json
  captures/<named-area>/<location-id>/
    <capture-id>.png
    <capture-id>.json
    <capture-id>.webp
  reports/
  exports/
```

The installed CET mod uses its own `runtime` directory because CET sandboxes
file access to each mod. `runtime/cet-runtime.json` records that resolved path
for the Python controller; it does not copy or relocate capture images.

## Python Setup

Create or activate the Python environment used for Ghostline, then install the
streaming parser and image dependencies:

```powershell
py -m pip install -r .\tools\requirements-world-locations.txt
```

`ijson` is mandatory for large sectors. Without it, the indexer accepts only
small fixtures (up to 64 MiB) and fails before attempting to load a large file
into memory. Pillow supplies lossless PNG capture and lossless WebP thumbnails;
NumPy and OpenCV perform HUD-template validation.

## Index and Plan

Run both commands from the repository root:

```powershell
py -B .\tools\world_location_capture.py index
py -B .\tools\world_location_capture.py plan
py -B .\tools\world_location_capture.py status
```

`index` compares the relative path, byte length, modification time, and
extraction-rule version of every sector. Unchanged sectors are skipped. Each
changed sector is parsed independently and committed in one transaction. If a
changed sector is malformed, its old features are removed so stale coordinates
cannot remain searchable. `--content-hash` adds SHA-256 provenance at the cost
of a second I/O pass over changed files. `--limit` is for fixture/development
runs and disables stale-sector pruning.

`plan` rebuilds derived fast-travel, road, and area tables, then upserts stable
places. An unchanged pose keeps its queue state, failure details, runtime labels,
and capture evidence. Replanning is not a retry. A changed pose or resource
binding becomes pending and loses its current capture/publication status; old
captures and attempts remain available as history. Obsolete places become
`disabled`, including historical captured places, and cannot be retried.

Planning rejects nonfinite/negative distances and a zero road sampling interval
before changing derived tables or the queue. Invalid serialized coordinates fail
the sector explicitly instead of being silently converted to origin coordinates.

The versioned `scope_rules` in `tools/world-location-capture-v1.json` exclude
the region south of the Night City border wall. The boundary is derived from
vanilla `q000_nomad`: the border fence-gate point supplies the origin, the
illegal-crossing trigger supplies the wall tangent, and the checkpoint entrance
and `border_crossed` trigger identify the outside and inside respectively.
Planning retains all source features, records the rule and signed boundary
distance on every place, and marks excluded places `out_of_scope` and
`disabled`. They never enter the capture queue and cannot be requeued by
`retry`.

The SQLite database has R-tree indexes for features, roads, areas, and
fast-travel points, plus FTS5 indexes for feature and place names, categories,
resources, and tags.

## Classification and Calibration

Classification is controlled by `classification_rules` in
`tools/world-location-capture-v1.json`. Rules can match resource paths, node
types, debug names, component data, and tags. The checked rules cover vending
machines, non-body loot containers, shops/storefronts, roads, fast-travel
points, AI workspots, crowd parking spaces, drop points, computers/terminals,
physical and virtual access points, functional doors/gates, utility devices,
gameplay antennas, security devices, named-area shapes, vanilla occupancy, and
quest-ownership areas. Add new categories by adding another versioned rule; no
Python edit is required.

Use `resource_patterns` when a family must match its actual depot path rather
than arbitrary strings elsewhere in the serialized node. This prevents debug
names, prefab paths, or nested references from turning corpse containers into
shops or billboards into doors. `exclude_resource_patterns` applies the same
field-specific rule to exclusions. The older `patterns` and `exclude_patterns`
continue to search the complete serialized node text when that broad behavior
is intentional.

Each rule declares one or more `anchor_roles`, which are copied into feature
metadata and tags and included in new capture sidecars and exports:

- `capture_origin` identifies a calibrated coordinate eligible for planning;
- `semantic_evidence` describes nearby site utility without promising that the
  vanilla object can be reused;
- `spatial_metadata` and `route_evidence` enrich geographic queries;
- `ownership_risk` identifies vanilla quest, community, population, or
  security evidence that requires rejection or explicit runtime review.

The configured capture origins use category-specific 3D spacing followed by a
global 10 m physical-location spacing pass. Scope is evaluated before spacing,
so an excluded neighbor cannot suppress an eligible destination. Within the same
category priority, an unchanged captured representative wins over new nearby
candidates to preserve finished coverage. AI workspots and parking nodes are
more aggressively deduplicated because the serialized world contains tens of
thousands of workspots and both raw and compiled parking representations. When
different categories compete inside 10 m, the configured category priority
keeps the more quest-useful anchor while every source feature remains available
as nearby semantic evidence. Exact-coordinate views belonging to the winning
anchor remain together, so a road's `along` and `against` captures are retained
as two views of one physical location.

Workspot resource paths retain useful staging vocabulary such as chair, bar,
stairs, lean, stand, or synced interaction. They remain vanilla activity
evidence: do not reuse an existing workspot or community solely because its
coordinate was capturable. Drone and vehicle workspots are excluded from
ground-level capture planning.

Fast-travel points now provide sparse capture origins in addition to nearest
fast-travel metadata. Virtual access points, gameplay antennas, security
devices, vanilla occupancy, and quest areas remain semantic/risk features and
do not enter the capture queue.

Changing `extraction_rule_version` deliberately invalidates every sector's
classification cache. Stop any active capture session before running `index`
with a new rule version, then run `plan` and inspect the category counts before
starting another capture batch.

`feature_identity_version` separately controls the identity salt for extracted
features. It is pinned to `1.1.0` while the additive Fake Door classifiers refresh
the extraction cache (`1.2.0` for regular doors, `1.3.0` for fake garage doors,
and `1.4.0` for site surveys and the security-path correction).
This preserves existing feature/location IDs and
capture history. Deliberately change the identity version when old anchors must
be replaced; coordinate, rotation, source identity, and classification-rule ID
are already part of each feature's identity.

### Fake Door retrofit surveys

The `fake_door` family matches placed `worldEntityNode` instances of
`single_door_decorative.ent`, `double_door_decorative.ent`, and
`gate_decorative.ent` under `base/gameplay/devices/doors/final`. Native inspection
confirms that the gate template contains a `FakeDoor` with garage/shutter and
decorative gate appearances. Its separate `fake_garage_door_v1` classifier adds
`fake-garage-door` tags and `door_kind: garage_gate` planning provenance while
using the same pair IDs, offsets, and capture category. It excludes proxy meshes, functional doors,
and quest-specific resources merely named "fake door". Each entity produces:

- `outward`: 1.5 m along the door's transformed local +Y, facing outward;
- `building`: 15 m along that same axis, facing back toward the doorway.

Distances are configurable in `fake_door_rules`. Both views retain the source
door height for direct FreeFly placement. Local +Y is the
initial exterior-side convention; validate representative door appearances in
the smoke batch and use `orientation_corrections` for reversed families. Ground
readiness does not establish unobstructed façade visibility or retrofit suitability.

These surveys bypass ordinary category/global spacing and do not contribute to
sparse-road coverage, so neither their partner nor an existing ordinary capture
can suppress them. Geographic queue ordering uses the common doorway anchor.
The normal scope boundary still applies independently to each requested viewpoint.

The views have distinct `location_id` values and a shared stable
`capture_pair_id`. Planning provenance, captured JSON sidecars, and JSON/JSONL
exports retain the pair ID, `capture_view` (`outward` or `building`, named `view`
inside planning provenance), and reciprocal `paired_location_id`. Captioners
should group by non-null `capture_pair_id`, then select the latest current capture
for each of the two view labels. Retries keep
that identity; a failed partner remains an incomplete pair rather than being
silently substituted. Provenance also retains the door anchor, outward vector,
offset distance, source node/instance identity, and orientation-review requirement.

On an existing database, use `plan --category fake_door` after indexing to add or
refresh only this family using the existing geographic metadata tables. This
leaves every other category's queue and capture state unchanged, including legacy
captures with retired anchors. A full `plan` intentionally reconciles all families
and can disable historical locations that no longer match the current planner.

```powershell
.\.venv\Scripts\python.exe -B tools/world_location_capture.py plan --category fake_door
.\.venv\Scripts\python.exe -B tools/world_location_capture.py capture --category fake_door --limit 20
```

The 2026-10-27 queue addition indexed all 16,256 sectors without errors and found
7,633 decorative doors (5,434 single, 2,199 double). It planned 15,266 views:
15,112 pending and 154 outside scope. The snapshot audit verified all 1,603 prior
captures and the prior queue state were preserved. Total pending work became
27,973 places, plus one interrupted place recovered automatically on capture.
The audit and paired planning manifest are generated at
`converted/world-location-database/full-world/reports/fake-door-queue-audit.json`
and `fake-door-capture-pairs.jsonl` in the same directory. The manifest includes
both planned views and their queue/scope states, including incomplete eligible
pairs near the scope boundary. No in-game capture was started by this addition.

The subsequent fake garage/gate addition found 271 `gate_decorative.ent`
placements across 128 sectors and added 542 in-scope pending views. The combined
family now contains 7,904 pairs, with 15,654 queued views and 154 outside scope.
Total pending work is 28,515 places plus the interrupted place. Snapshot checks
verified the 1,603 existing captures, existing pair IDs, and previous queue states;
all unrelated location records remained unchanged. The pair manifest and audit
above were refreshed with these garage/gate pairs.

### Entrance, route, and installation surveys

`site_survey_rules` adds paired views for these categories:

| Category | Views | Initial placement |
|---|---|---|
| `intercom` | `entrance`, `approach` | 2 m and 12 m outward, facing the entrance |
| `elevator` | `entrance`, `lobby` | 3 m outward, opposing headings |
| `security_checkpoint` | `approach`, `reverse_approach` | Opposing sides, 6 m from the anchor |
| `road_barrier` | `approach`, `reverse_approach` | Opposing sides, 8 m from the anchor |
| `security_device` | `device_context`, `surroundings` | Opposing headings at a nearby ground reference |
| `antenna` | `installation`, `surroundings` | Opposing headings at a nearby ground reference |

Security indexing accepts the actual `gameplay/devices/security_systems/` path
as well as the older singular and alternate paths. Checkpoint gates and lockers
are classified separately before the broader security rule. Both classifications
retain `ownership_risk`; capturing a device does not establish that it can be
reused by a quest. Elevator doors, lift entities and floor terminals, intercoms,
and traffic road-blockade entities have dedicated classifiers. Existing physical
access-point antennas keep their source feature classification and original queue;
the antenna survey also selects those resources for the additional context pair.

Each family has a configurable 3D anchor-spacing pass, applied before producing
both views. It never drops one partner alone or competes with other categories.
Identical opposing ground viewpoints are deduplicated together. Captured survey
representatives have preference when planning the same family again.

Elevated installations use nearby calibrated workspots, parking, doors,
fast-travel points, terminals, or utility devices as candidate floor references.
The initial search is within 25 m horizontally and at most 30 m below the target.
References must be at least 4 m away and at least twice the vertical separation
away horizontally, avoiding a view directly underneath an overhead device.
The source reference and target positions are retained in provenance. These are
candidate floor heights; CET still resolves the actual local surface and gates
capture readiness. No line-of-sight or accessibility verification is implied.
Anchors without a suitable reference are omitted from the capture queue and
reported in `reports/site-survey-ground-gaps.json`.

```powershell
.\.venv\Scripts\python.exe -B tools/world_location_capture.py plan --category site_surveys
# Or update one survey family:
.\.venv\Scripts\python.exe -B tools/world_location_capture.py plan --category security_device
.\.venv\Scripts\python.exe -B tools/world_location_capture.py capture --category security_device --limit 20
```

The scoped planning commands leave earlier capture families unchanged. The
overnight launcher already captures these new pending locations without extra
arguments. All survey pairs use the same `capture_pair_id`, `capture_view`, and
`paired_location_id` sidecar/export fields as Fake Doors. Generated handoff
manifests are `reports/site-capture-pairs.jsonl` for the new site families and
`reports/capture-pairs.jsonl` for all paired families together. Their rows retain
queue and scope status so captioners can identify incomplete pairs.

The 2026-10-27 addition indexed 5,327 security devices and queued 7,846 new views:
432 intercom, 440 elevator, 14 checkpoint, 6,324 security-device, 230 road-barrier,
and 406 antenna views. Another 34 planned views were disabled by the scope
boundary. Ground-reference gaps excluded 560 security and 10 antenna anchors;
these remain in the index and the gap report for later review. The snapshot audit
at `reports/site-survey-queue-audit.json` verified all earlier location records
and captures remained unchanged. Total pending work became 36,361 locations plus
one interrupted location; the existing 1,603 captures were preserved. All 144
world-location tests passed. No in-game capture was started.

Capture eligibility is independent from extraction. Every matched feature is
kept, while a feature is queued only when both `capture_enabled` and
`calibrated` are true. A standard family rule establishes its normal forward
axis. Put reversed or nonstandard assets in `orientation_corrections`, for
example:

```json
{
  "id": "vending-family-reversed-v1",
  "resource_pattern": "base\\gameplay\\devices\\vending_machines\\special_family",
  "forward_axis": "-y",
  "yaw_correction_degrees": 0
}
```

Object placement uses the reviewed rule's `front_extent_m` along its configured
outward axis. Serialized `worldNodeData.Bounds` is streaming reference metadata,
not a proven local object box, so it does not determine camera offsets. Vending
machines add 1 m clearance, loot containers add
0.5 m, and shops add 2 m. The heading remains the object's outward heading.
Candidates can define a category-specific 3D minimum separation. Vending
machines use 10 m, while dense workspot, parking, shop, fast-travel, and road
families use larger category-specific spacing before the global 10 m pass.
CET captures the planned XYZ directly with FreeFly enabled. It does not ground
snap, stage above a surface, or require collision beneath the viewpoint. This
preserves elevated building-facing and other aerial views.

Road proxy nodes are grouped by their road-spline resource folder. That folder
is treated as an independent branch; discontinuities become explicit branch
records. The proxy centers form the initial centerline approximation. Capture
points are spaced by at least 250 m both along the branch and in straight-line
distance. Branches shorter than 250 m receive one midpoint with opposing views,
while longer branches retain a 50 m endpoint inset. Every accepted point
creates `along` and `against` poses.

Road points within 250 m of an object candidate retain that coverage. Away
from objects, points from all road branches are deduplicated globally to 500 m
3D spacing, reducing repetitive captures across parallel roads in sparse areas.

Named areas primarily come from the runtime district manager because the
serialized sectors do not contain usable Night City district polygons. CET
caches every valid area observation while a destination settles. If an
observation is transiently absent, planning may fill missing area fields from a
previous runtime observation within 500 m. It retains exact spatial fields and
marks inferred labels separately; they never become new propagation seeds.

Because proxy centers and asset axes are extracted evidence rather than manual
ground truth, calibrate representative assets and review road geometry during
the in-game smoke batch before treating a new family as publishable.

## Metadata Review

Field resolution follows this precedence:

1. runtime identifiers/localized names reported by CET;
2. spatial or localized data extracted from resources;
3. reviewed overrides in `metadata_overrides`.

The runtime reports the current district hierarchy and interior state when the
game API exposes them. The planner calculates the exact horizontal nearest
road-segment point and nearest fast-travel point. A marker or debug identifier
is retained as provenance even when it is not yet a reviewed display name.

A place stays in `needs_metadata` until fast-travel, street, and named-area
names are all present. It can be captured, but it cannot be published. Add a
reviewed field using an SQLite client against `metadata_overrides`; every row
requires the target type/ID, field name, JSON-encoded value, reviewer, review
time, and reason. Re-run `plan` after road, area, or fast-travel overrides.

Useful review queries:

```sql
SELECT location_id, category, nearest_fast_travel_name,
       nearest_street_name, named_area
FROM places
WHERE review_status <> 'resolved'
ORDER BY queue_order;

SELECT road_id, name, length_m
FROM roads
WHERE name IS NULL
ORDER BY road_id;
```

## CET Installation and Game Setup

The October 27 orientation audit is recorded in
`converted/capture-orientation-audit/orientation-audit.json`, with compact native
screen and binding transforms in `screen-transform-evidence.json`. Fast-travel
uses the in-game checked local +X face. Vending-machine controls and drop-point
UI placement support their existing local +Y offsets; vending views face outward.
Seven rare appearance-specific vending templates remain individually unverified.
Generic personal-link workspots are copied across unrelated devices and must not
be used alone to infer the usable face. Other device families retain category
calibration requirements; mixed screen and parent rotations need per-resource
review. Two-sided barriers and target-based ground-context views are less
sensitive to front-sign changes.

The controller watchdog keeps its same-session heartbeat cache between commands.
A newly received command gets one normal heartbeat lease for transient file-read
failures. Matching acknowledgements are processed before watchdog expiry; a real
expiry publishes a failed completion before discarding the command. Reload CET
after installing this runtime. Resume preserves completed captures and recovers
the interrupted destination automatically.

Capture, preflight, and visual-settle timeouts now default to five seconds per
attempt in every category preset. Restrictions cleared by a load are reapplied
at most once per second while retaining their original ownership snapshot.
Loading progress only blocks a frame when its controller root is visible;
uninitializing that controller clears the loading flag. Cleanup verifies removal
of capture-owned effects, rather than requiring unrelated pre-existing effects
to survive scripted transitions.

Area-entry/new-location banners, security-zone alerts, stealth-zone HUD, journal
quest updates and custom quest notifications also have explicit root-widget
suppression. Their queues and delivery remain active. Presentation callbacks and
capture draw callbacks re-hide the roots; references are capped at one per known
controller class and cleared on uninitialization. The CET heartbeat reports
`hud_suppression_revision: area-zone-quest-interactions-v2` and the retained HUD
slot count. Interaction widgets, dialogue choices, interaction tooltips and loot
prompts use the same capture-only root hiding on presentation and draw callbacks.
Their gameplay interaction data is not changed. Reload CET to activate an update.

Install Cyber Engine Tweaks for the current game version first. Then install
the checked runtime into that existing CET installation:

```powershell
py -B .\tools\world_location_capture.py install-cet `
  --game-root "D:\Games\Cyberpunk 2077"
```

The installer refuses to replace a locally modified CET runtime unless
`--force` is supplied. Start or reload CET after installation and bind
`World Location Capture: emergency restore` in CET's Bindings tab. CET does
not permit mods to assign a default hotkey.

HUD, subtitle, and holocall preferences use explicit path/name pairs from the
game's `r6/config/settings/options.json`. The runtime checks each variable with
`HasVar` before reading it and never enumerates a configuration group from a
configurable path. A missing variable therefore fails the destination without
invoking the engine's fatal invalid-group assertion.

Prepare the game as follows:

- load the dedicated free-roam capture save;
- use first person;
- activate the installed FreeFly mod before starting the batch and leave it active;
- use borderless-windowed mode with a 1920×1080 client area;
- close the CET overlay and disable Steam, Discord, driver, recording, or other
  overlays that could appear in the client rectangle;
- keep Cyberpunk 2077 as the foreground window.

The default capture profile is 10:00, clear weather, and 80-degree FOV. Use
separate dedicated saves for different quest states. The runtime never changes
quest facts.

## Capture State and Readiness

At the first destination, CET snapshots the settings and game states that it
changes. Capture mode remains active across the batch. It:

- disables all Boolean HUD and subtitle settings in their settings groups;
- clears onscreen/warning notification blackboards and hides observed phone,
  message, holocall, and generic-notification controllers;
- requires FreeFly to be active and verifies its invulnerability/AI invisibility;
- applies no-combat, no-movement, no-phone, no-scanning, and no-radial-menu restrictions;
- hides the currently drawn weapon entity and blocks combat-driven drawing;
- snapshots and suppresses prevention-system heat/escalation;
- applies time and weather without writing live camera zoom or FOV state;
- teleports directly to the immutable world-derived XYZ pose.

For every destination, `ready` requires all of the following in the same game
update:

- FreeFly is active, GodMode and AI invisibility are verified, V is out of combat, police
  prevention is disabled, and heat is zero;
- there is no loading screen, menu, pause, or CET overlay;
- the player and first-person camera are attached in the destination world;
- actual position meets the configured tolerance; heading drift is recorded as
  capture metadata but does not block the frame;
- player position remains within the configured stability tolerance for the
  configured duration;
- HUD, subtitle, notification, phone, weapon, and input restrictions are active;
- `GetDisplayResolution()` reports exactly 1920×1080.

When the predicates first become true, CET changes to `armed`. The next
`onDraw` rechecks the predicates, assigns `presented_frame`, and emits
`event-ready.json` with a matching session heartbeat.
Python consumes it on the next 10 ms file-protocol poll, then captures through
Windows Graphics Capture after the visual settling interval. The poll interval
is transport latency. `loading_timeout_seconds` bounds both runtime readiness
and the visual capture wait, including a window that never delivers a frame.
Capture requires at least two advancing WGC presentation timestamps. CET keeps
checking readiness while frames settle; an opened overlay, movement, loading
screen, or other lost predicate rejects the attempt. Python independently
checks protection/combat evidence, UI/weapon suppression, display dimensions, finite pose values, and the
actual distance from the effective destination. Heading and FOV differences
remain recorded diagnostics and do not reject a frame.

The readiness/visual timeout is 45 seconds. An incorrect or moving flight pose
has a separate 5-second timeout (`pose_timeout_seconds`). The stationary-pose
predicate is followed by the existing rendered-frame settling interval; it does
not claim that a floor collision proves streaming is complete. All three requested
coordinates are immutable and checked independently by Python.

Ordinary failed attempts retry while protected capture mode remains active.
Final cleanup attempts to return to the starting pose and restore capture-owned
HUD/settings/restrictions; incomplete final cleanup is a warning. FreeFly remains
active, and its GodMode/AI invisibility are never removed by the capture runtime.
Do not toggle FreeFly or move during a batch. The runtime checks flight on every
update and before the draw that authorizes an image.

Readiness includes `ui_details`; phone-container visibility is diagnostic only,
because visible containers need not contain any visible phone pixels. Native
Border Crossing and lethal-volume exclusions remain applied independently of
flight. `-LocationId <id>` selects a smoke test without changing the queue.

OS-owned exclusive locks protect both the runtime directory and queue database.
A second controller fails before deleting protocol files or recovering interrupted
rows; process termination releases locks automatically. Startup requires a fresh,
idle, restored CET heartbeat advertising protection contract version 1, so an old
loaded Lua runtime cannot consume the queue after files are updated.

API signatures were checked against the installed REDmod
`core/systems/godModeSystem.script` and `cyberpunk/player/player.script`.
Native damage, hostile NPC/camera detection, and shutdown restoration still need
a live smoke test after CET reload before the unattended run.

Commands, events, and acknowledgements carry schema, session, and command IDs.
Controller heartbeats identify the session; CET heartbeats identify the active
session and command. Mismatched session evidence is rejected. A destination can
emit `accepted`, `teleported`, `ready`,
`completed`, or `error`. Event types use separate atomic files, so a fast
transition cannot overwrite an earlier event required for auditing.
The controller heartbeat continues through image validation, file encoding,
storage, and acknowledgement so slow disk work cannot trigger restoration
halfway through a successful capture.

The database's `requested_*` columns remain the immutable planner output. The
sidecar separately records the runtime-resolved `effective_pose`, while capture
stores the observed player transform in `actual_*`; runtime evidence must never
feed back into the next requested pose.
Persisted observed pose, readiness, FOV, and runtime area use the latest verified
capture-time snapshot. The initial ready event remains available for auditing.

## Image Validation and Publication

Capture rejects globally blurred frames using Laplacian variance. A rejection
causes CET to restore capture mode completely before retrying the same location,
so persistent camera focus/blur state cannot leak into later captures.

Run the queue or a smoke subset:

```powershell
py -B .\tools\world_location_capture.py capture --game-profile capture-free-roam
py -B .\tools\world_location_capture.py capture --limit 20
```

The controller rejects the frame when the client or captured image is not
exactly 1920×1080, the CET evidence or pose is invalid, the image is
black/loading-like, a configured HUD template matches, or its exact RGB pixels
repeat a previously fingerprinted capture at another destination. New captures
store a `dhash64` perceptual fingerprint and a pixel SHA-256. Perceptual matches
alone do not discard similar but distinct views. Historical captures are not
silently rewritten to add fingerprints. The controller retries up to three
total attempts after CET confirms restoration; there is no retry sleep.

Configure crops of common visible HUD states under
`capture.validation.hud_templates` before publication. Each entry can contain
`name`, `path`, `threshold`, and an optional `[x, y, width, height]` `region`.
Without templates, valid captures are retained with `needs_ui_review` and are
not publishable. This makes the missing visual check explicit rather than
silently claiming that no HUD was visible.

The controller atomically writes the original PNG, JSON sidecar, and lossless
WebP thumbnail, then commits their paths and hashes in one database
transaction. It records `teleport_to_ready_ms`, `ready_to_capture_ms`, and total
latency. A place becomes publishable only after metadata is resolved, visual
validation is complete, the capture hashes are valid, and CET confirms that
normal play was restored at session end.

The ready event and actual pose are recorded before image validation, so a
rejected frame retains its destination evidence. Failed attempts record a
specific reason such as `blurred_frame`, `duplicate_frame`, `frame_timeout`, or
the CET runtime error code. Their `error_detail` contains structured validation
and runtime evidence. When a frame was available, a lossless WebP diagnostic
preview is retained under `captures/_rejected/<location_id>/<attempt_id>.webp`.
It uses the configured thumbnail width, capped at 960 pixels in either dimension.
The failure record identifies it as a preview, stores its hash and original
frame dimensions, and retains quality metrics from the full frame. Rejected
frames do not become capture rows or publishable images.

Publication checks the individual capture's files, hashes, sidecar identity,
current requested pose and anchor, visual validation, metadata, and verified
session restoration. A historical successful capture cannot make a pending,
disabled, out-of-scope, or changed destination publishable.

## Resume, Retry, Status, and Export

An interrupted `in_progress` destination returns to `pending` on the next
session. CET independently restores normal play when the controller heartbeat
expires, including the idle interval between destinations. A failed restoration
retains its snapshot for recovery and aborts retries; a negative acknowledgement
alone is not proof that normal play was restored. Shutdown, Lua reload, an explicit controller restore, and the
emergency hotkey use the same restoration routine.

```powershell
py -B .\tools\world_location_capture.py status
py -B .\tools\world_location_capture.py retry
py -B .\tools\world_location_capture.py retry --failure-code streaming_timeout
py -B .\tools\world_location_capture.py retry --location-id place_0123456789abcdef
py -B .\tools\world_location_capture.py export
```

With no selector, `retry` requeues eligible failed places. Selectors can also
filter by category. The compatibility `tools/reset_world_location_queue.py`
uses the same failed-only operation and refuses to change an active session's
queue. Interrupted work is recovered by the capture controller; disabled,
rejected, and out-of-scope places are not resurrected by retry/reset.
Use `retry --recapture --location-id <id>` to queue an explicitly selected
successful capture again. Existing captures and attempts remain in its history.
`capture --location-id <id>` and `capture --category <category>` restrict the
pending queue; repeat either selector to include several values.

`status`, `review`, and `export` open the existing database read-only. `export`
assesses each image independently against its own validation, sidecar, hashes,
and session restoration, plus the current location pose and metadata. It writes
JSON and JSONL together. Actual pose, FOV, and capture profile come from that
image's sidecar, even if a later attempt changed the location's observed pose.
Use `--include-unpublishable` for review exports: these retain publication
blockers and whether the image matches the current plan, but still reject broken
file integrity. Report outputs cannot replace the database or capture evidence.

## Visual Capture Review

Build a local HTML gallery and JSON snapshot without changing the queue:

```powershell
py -B .\tools\world_location_capture.py review --limit 0 `
  --output .\generated\world-capture-review\review.html
```

Open the HTML file in a browser. The gallery shows the latest capture for each
location and failed locations, including diagnostic previews when available.
Search by location, resource, street, or failure; filter by category, area,
image quality, and queue status. It renders 48 cards per page with lazy images,
full-size image and sidecar links, quality measurements, source evidence, and
publication blockers. Technical quality does not establish quest suitability.

The default report includes 300 locations; `--limit 0` includes all matches.
Repeat `--category` or `--location-id` to narrow the report before its limit is
applied. Add `--verify-files` to recalculate successful capture file hashes;
the faster default checks paths and sidecars and explicitly marks hashes as
unverified. Rejected previews remain diagnostic evidence.

Select **Retry** on useful locations with bad shots. The page produces explicit
PowerShell commands containing the database path and selected IDs. It does not
execute commands or approve images. After running the retry command, capture
those IDs to keep the new batch focused:

```powershell
py -B .\tools\world_location_capture.py retry --recapture `
  --location-id place_0123456789abcdef
py -B .\tools\world_location_capture.py capture `
  --location-id place_0123456789abcdef
```

Rebuild the report after captures or metadata changes; it is a static snapshot.

## Verification

### Overnight launch

Use the repository environment consistently; a system Python can import an
unrelated installed `tests` package or lack the Windows capture backend.

```powershell
.\.venv\Scripts\python.exe -B -m unittest discover -s tests -p 'test_world_location*.py' -q
.\.venv\Scripts\python.exe -B tools/world_location_capture.py preflight --game-root 'K:\Cyberpunk 2077'
```

`preflight` is read-only and returns exit code 1 for blockers. It checks imports,
SQLite integrity, free space, installed bridge/configuration (with `--game-root`),
the descriptor, a fresh idle CET heartbeat with capture mode inactive, and the
1920×1080 game client. It does not establish that the loaded save is suitable,
that every anchor is calibrated, or that a smoke batch has passed. Missing HUD
templates are a warning: captures remain subject to UI review before publication.
The disk check uses a 10 GiB startup floor, not a full-queue storage guarantee.

The 2026-10-26 review found that the game moved from `H:` to `K:` and its bridge
was disabled. The current bridge was installed at `K:\Cyberpunk 2077` and the
descriptor updated; the previous `init.lua.disabled` was preserved. Reload CET
mods or restart the game to load the installed bridge. Load the dedicated capture
save, close overlays, and bind the emergency restore hotkey before the smoke batch:

```powershell
.\.venv\Scripts\python.exe -B tools/world_location_capture.py capture --limit 20
.\.venv\Scripts\python.exe -B tools/world_location_capture.py review --limit 50 --verify-files
```

Inspect the new images and restoration, then launch later with:

```powershell
.\tools\run_world_location_overnight.ps1
# Optional bounded batch:
.\tools\run_world_location_overnight.ps1 -Limit 1000
```

The launcher requires passing preflight and writes a timestamped combined log
under the configured default `full-world/reports` directory. Run only one capture
controller at a time. Capture prevents automatic system/display sleep for its
duration, releases the request on exit, and returns a nonzero exit code when
final restoration is unverified. Keep the desktop unlocked and the game in the
foreground. Ctrl+C uses the controller's restoration path; force termination
relies on CET's heartbeat watchdog. Resume with the same launcher; an interrupted
destination is recovered automatically. Failed destinations remain failed until
explicitly retried, and successful captures are preserved.

At review time the queue contained 12,861 pending places, one interrupted place,
161 failures, and 1,603 captures. Existing PNGs averaged 2.63 MiB, suggesting
roughly 33 GiB for remaining originals, plus sidecars, thumbnails, rejected
previews, and database growth. Free space was about 355 GiB. These are observations,
not a completion-time or storage guarantee; the full queue may span several nights.

Run the focused suite:

```powershell
py -B -m unittest discover -s tests -p 'test_world_location*.py' -v
```

The tests cover transform/orientation decoding, stable extraction, object
offsets, R-tree and FTS indexing, metadata precedence, migrations, road
spacing, q000 border-scope classification, immediate and delayed readiness, the first-presented-frame contract,
malformed events, timeouts, stale heartbeats, interrupted queues, and exactly
three retries without a fixed delay. Regression suites also cover failed-frame
evidence, restoration barriers, unchanged and changed replans, nearest-neighbor
selection, per-capture publication, targeted retries, and read-only gallery
generation with protected output paths.

Before a production run, execute an in-game smoke batch that includes every
anchor category, several districts, interiors, exteriors, and deliberately
unreachable points. Inspect restoration, images, sidecars, failure codes, and
latencies before expanding the queue.
