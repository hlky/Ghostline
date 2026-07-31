# In-Game World Location Database

The world-location pipeline turns the serialized Night City streaming sectors
into deterministic in-game capture destinations. It keeps the serialized
sectors read-only, processes one sector at a time, and stores searchable
features, planned poses, runtime evidence, captures, and failures in SQLite.

The capture path is deliberately event-driven. There is no fixed wait after a
teleport. CET emits `ready` from the first `onDraw` after every load, pose,
collision, velocity, camera, and suppression predicate passes. The Python
controller then calls `DwmFlush` to cross the next Windows composition boundary
and captures the exact game client rectangle.

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
places. Existing successful captures remain attached to an unchanged location
ID. Obsolete uncaptured places become `disabled` rather than being erased.

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
machines, loot containers, shops/storefronts, roads, fast-travel points, and
named-area shapes. Add new categories by adding another versioned rule; no
Python edit is required.

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

Object placement projects oriented instance bounds onto the configured local
forward axis. Degenerate sector bounds use the reviewed rule's
`front_extent_m`. Vending machines add 1 m clearance, loot containers add
0.5 m, and shops add 2 m. The heading remains the object's outward heading.
Candidates can define a category-specific 3D minimum separation; vending
machine poses currently use 3 m so adjacent machines do not produce redundant
captures while machines on different floors remain distinct.
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
observation is transiently absent, planning may reuse a previously observed
runtime area within 500 m; inferred labels never become new propagation seeds.

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
`onDraw` assigns `presented_frame` and atomically emits `event-ready.json`.
Python consumes it on the next 10 ms file-protocol poll, calls `DwmFlush`, and
captures. That poll interval is transport latency, not a minimum streaming
wait. A destination that becomes ready immediately is captured immediately.
`loading_timeout_seconds` only fails a destination that never becomes ready.

Commands, events, acknowledgements, and heartbeats carry schema, session, and
command IDs. A destination can emit `accepted`, `teleported`, `ready`,
`completed`, or `error`. Event types use separate atomic files, so a fast
transition cannot overwrite an earlier event required for auditing.

The database's `requested_*` columns remain the immutable planner output. The
sidecar separately records the runtime-resolved `effective_pose`, while capture
stores the observed player transform in `actual_*`; runtime evidence must never
feed back into the next requested pose.

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
black/loading-like, a configured HUD template matches, or the perceptual hash
duplicates an earlier capture. It retries immediately up to three total
attempts; there is no retry sleep.

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

## Resume, Retry, Status, and Export

An interrupted `in_progress` destination returns to `pending` on the next
session. CET independently restores normal play when the controller heartbeat
expires. Shutdown, Lua reload, an explicit controller restore, and the
emergency hotkey use the same restoration routine.

```powershell
py -B .\tools\world_location_capture.py status
py -B .\tools\world_location_capture.py retry
py -B .\tools\world_location_capture.py retry --failure-code streaming_timeout
py -B .\tools\world_location_capture.py retry --location-id place_0123456789abcdef
py -B .\tools\world_location_capture.py export
```

With no selector, `retry` requeues all failed places. Selectors can also filter
by category. `export` includes publishable places by default, verifies PNG,
sidecar, and thumbnail hashes, and writes both JSON and JSONL. Use
`--include-unpublishable` only for review exports.

## Verification

Run the focused suite:

```powershell
py -B -m unittest tests.test_world_location_capture -v
```

The tests cover transform/orientation decoding, stable extraction, object
offsets, R-tree and FTS indexing, metadata precedence, migrations, road
spacing, q000 border-scope classification, immediate and delayed readiness, the first-presented-frame contract,
malformed events, timeouts, stale heartbeats, interrupted queues, and exactly
three retries without a fixed delay.

Before a production run, execute an in-game smoke batch that includes every
anchor category, several districts, interiors, exteriors, and deliberately
unreachable points. Inspect restoration, images, sidecars, failure codes, and
latencies before expanding the queue.
