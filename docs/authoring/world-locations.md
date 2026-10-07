# In-Game World Location Database

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
CET resolves the final ground height at runtime from the median of five nearby
downward collision probes, starts the player 0.3 m above that result, and lets
normal physics settle onto the surface; it does not search laterally. Starting
above the surface avoids the persistent camera blur triggered when an
inconsistent collision probe places the player slightly below the true standing
height.

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
- applies invulnerability plus available no-combat, no-movement, no-phone,
  no-scanning, and no-weapon-wheel restrictions;
- hides the currently drawn weapon entity and blocks combat-driven drawing;
- snapshots and suppresses prevention-system heat/escalation;
- applies time and weather without writing live camera zoom or FOV state;
- stages above the immutable world-derived pose, resolves the local ground
  surface, and teleports to that effective height.

For every destination, `ready` requires all of the following in the same game
update:

- the downward destination ground probe forms the streaming fence;
- there is no loading screen, menu, pause, or CET overlay;
- the player and first-person camera are attached in the destination world;
- actual position meets the configured tolerance; heading drift is recorded as
  capture metadata but does not block the frame;
- player position remains within the configured stability tolerance for the
  configured duration;
- a downward static-or-terrain ground probe succeeds at the destination;
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
checks UI/weapon suppression, display dimensions, finite pose values, and the
actual distance from the effective destination. Heading and FOV differences
remain recorded diagnostics and do not reject a frame.

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
