# Game Scout MCP

Independent Cyberpunk 2077 scouting tools for an MCP host. Own CET mod, Python
environment, transport, database, image store and routes. No imports from the
world-location capture package and no modification of FreeFly or the capture mod.
The installed FreeFly mod supplies flight and its existing scouting protections.

## Setup

From the repository root:

```powershell
.\tools\setup_game_scout.ps1 -GameRoot 'K:\Cyberpunk 2077' -RegisterCodex
```

The installer creates an isolated environment at `converted/game-scout/venv`,
installs `tools/game_scout/cet` into CET's `mods/game_scout`, and writes local
paths to `.local/game-scout.json`. An earlier Game Scout installation is backed
up outside CET's mods directory before replacement. It never reloads CET or
starts controlling the game. **Let any existing capture finish before reloading
CET mods.** Load a free-roam save, activate FreeFly and close the CET overlay.

```powershell
.\converted\game-scout\venv\Scripts\python.exe tools/game_scout_mcp.py doctor
```

`doctor` checks the Game Scout runtime heartbeat; it does not take control.
The MCP stdio launch command, usable from any working directory, is:

```powershell
H:\projects\Ghostline\converted\game-scout\venv\Scripts\python.exe H:\projects\Ghostline\tools\game_scout_mcp.py serve
```

Use `--config C:\absolute\path\game-scout.json` before `serve` to select a
different installation. `setup_game_scout.ps1 -RegisterCodex` registers the server
as `game_scout` using `codex mcp add`; it does not change other MCP entries.

## Interactive scouting

1. `observe` shows the current image and actual camera coordinates.
2. `begin_session` acquires control, snapshots camera limits/HUD state and hides
   supported HUD elements. FreeFly must already be active. Camera manipulation
   and saved captures also acquire a session when needed.
3. `move(forward=8, right=0, up=0)` moves along the camera's forward/right vectors,
   with world-vertical up. Motion is interpolated locally, then a fresh preview
   is returned. Regular moves are limited to 50 m and checked for collisions.
4. `look_at` aims at a world point or turns by relative yaw/pitch.
5. `inspect(u=0.5, v=0.5)` raycasts a point in the latest image. Coordinates are
   normalized left-to-right/top-to-bottom. The camera must still match that image.
   The nearest hit includes world coordinates and collision group; entity IDs,
   proxy IDs and templates are included when the installed inspection APIs resolve
   them. Sky/no-hit is reported explicitly; unavailable ray queries are errors.
6. `capture` saves a full-resolution PNG with a metadata sidecar; previews are
   JPEGs limited to 1280×720. `sweep` returns all requested heading previews;
   `orbit` captures around a target and reports collision-blocked segments.
7. `end_session` restores the scout-owned camera/HUD changes and releases control.

When HUD hiding is requested, supported HUD, subtitle and holocall settings are
snapshotted and restored when the session ends. The CET console command
`GetMod('game_scout').demoEnvironment()` sets the time to 12:00 and applies the
sunny weather override. A bindable CET hotkey, “Game Scout: clear weather and
midday”, invokes the same action. Time continues to advance; to remove the
weather override use `Game.GetWeatherSystem():ResetWeather(true)` in the console.

`go_to` accepts a saved viewpoint ID or `{x,y,z,yaw,pitch}`. All poses describe the
**active camera origin**, not the player's feet. Units are metres and degrees;
yaw 0 faces +Y, yaw 90 faces −X, positive pitch looks up. Pitch is limited to ±85°.
`allow_teleport=true` explicitly permits long travel and bypasses the motion-path
collision check. Ordinary movement stays collision checked unless the caller
explicitly sets `collision=false` for intentional FreeFly passage.

The camera uses native FPP pitch limits and body-yaw feedback. Screen rays are
calibrated with native `ProjectPoint`, without assuming a horizontal versus
vertical FOV convention. Camera origin, orientation, FOV, player position and
presentation timestamp accompany saved images. Loading controllers, player
attachment, fast-travel blackboards, pause state and fresh frame checks gate
captures. This does not guarantee every distant texture or object has streamed.

## Discoveries and connections

The library lives under `converted/game-scout/library`:

- `save_location`: name, description, tags and selected viewpoint IDs.
- `save_viewpoint`: camera pose, original image, notes and optional location link.
- `connect_locations`: observed passage/stairs/entrance links with directionality.
- `search_library`, `get_record`, `read_image`: retrieve records and show images.
- `coverage`: visited 8 m cells in XYZ, with 45° heading sectors.
- `export_library`: standalone JSON containing all records and coverage. Original
  image files remain in the library; the export contains their absolute paths.

SQLite commits each completed waypoint and saved record. Exports are independent
of the world-location database and can be consumed by a later importer. Locations
and viewpoints have their own IDs; image captions need not be paired.

## Race surveys

Race plans use their own library records (`kind="race"`), separate from camera
replay routes. They persist each mark in SQLite, including its role, order,
native heading, options, notes and capture provenance. No CET changes are
needed for these tools; restart the MCP server after updating its Python source
so the new tool definitions are available.

1. Call `create_race(name="Dock sprint", prefix="gqt009")`. Use the owning
   project's registered quest/depot prefix. Optional defaults are `looped=false`,
   `width_default=5` metres and `speed_mps=10` (36 km/h). Save the returned race ID.
2. Observe the road, then call `mark_race(race_id=..., role="spline_point",
   u=0.5, v=0.7)`. Surface marking raycasts the latest observed image and saves
   the hit coordinates, rather than the flying camera's origin. Aim at the
   intended road surface; an inspection can also hit a wall, roof or vehicle.
   A changed camera, missing hit, unready game or stop rejects the mark.
3. Add spline points in driving order, with more points around bends and grade
   changes. Add checkpoints in checkpoint order and mark the grid, player start,
   staging, activation workspot and finish. The default heading is the camera yaw; set `yaw` explicitly
   when looking down/sideways while marking the road. Native yaw is 0 toward +Y,
   90 toward -X, in degrees. This heading is retained in exported node rotations.
4. Add supporting marks and optional speed/width changes using the roles below.
5. Call `export_race(race_id=...)` to write `world.json` and `race-plan.json`
   beneath the library's `exports` folder. The response gives both absolute
   paths, missing requirements and warnings. `require_complete=false` allows
   an incomplete draft. Exporting does not take game control.

| Role | Export/use | Options |
| --- | --- | --- |
| `spline_point` | Ordered centreline points for a race spline | None |
| `checkpoint` | Marker and ordered checkpoint trigger binding | `width_m`, `depth_m`, `height_m` |
| `start_grid`, `player_start` | Spawn-point markers | None |
| `staging`, `finish` | Marker and trigger | `width_m`, `depth_m`, `height_m` |
| `activation` | Player standing-workspot root and interaction position on clear ground | None |
| `recovery` | Recovery spawn-point marker | None |
| `opponent_exit`, `reward`, `spectator`, `gps` | Named location markers for later quest/world bindings | None |
| `hazard`, `boundary` | Marker and trigger for later policy bindings | `width_m`, `depth_m`, `height_m` |
| `prop` | Location marker, plus an entity when an explicit depot template is supplied | `entity_template` |
| `speed_change` | Target speed at the nearest centreline station | Required `speed_mps` |
| `width_change` | Left/right widths from the nearest station until the next change/end | Required `left_m`, `right_m` |

Area dimensions default to 10 m across the road, 2 m along it and 4 m tall.
Options are passed as an object, for example
`options={"width_m":12,"depth_m":3,"height_m":4}`. A complete geometry survey
requires at least two spline points (three for a loop), a checkpoint, an opponent
grid mark, a staging mark, an activation workspot mark, exactly one player start and exactly one finish.
Recovery, run-off, reward, spectators and hazard plans remain author choices;
all captured marks appear in the handoff manifest.

For an explicitly known coordinate use `source="manual"`, `position={x,y,z}`
and `yaw`. `source="player"` takes the runtime's player position;
`source="camera"` is an explicit camera-origin mark and adds a ground-placement
warning on export. Manual marks and offline edits do not acquire game control.
`get_record` reads the full race; `search_library(kind="race")` finds plans, and
`export_library` includes them in its standalone bundle.

`edit_race_mark(race_id, mark_id, ...)` changes notes, name, options, position,
heading or per-role `order` without recapturing. Omitted fields are retained;
options replace that mark's option object. Use an unused order when reordering
(a temporary high order allows a swap). `mark_race(..., mark_id=...)` recaptures
an existing mark. `remove_race_mark` removes one mark; `configure_race` changes
description, loop mode or speed/width defaults without replacing any marks.

The export uses a unique subdirectory under `mod/<prefix>/races/<plan ID>` and
stable NodeRefs, so repeated exports keep identities and two plans do not collide.
Spline points are converted from captured world coordinates to local offsets
about the first point, with an identity spline rotation. Speed/width stationing
uses the piecewise-straight centreline (including loop closure) and warns about
tuning marks more than 5 m from it. Default generator handles produce straight
segments; **recompute station distances if you smooth the tangents later**.
Review projected stations at crossings and hairpins where the closest segment
may not be the intended one.

Feed the returned world spec to `tools/generate_world.py generate --spec <path>
--dry-run` from the repository root after resolving the owning project.
Unregistered prefixes require project/catalog ownership before production use.
The manifest contains mark-to-resource bindings and the remaining lifecycle
work: actors/vehicles/seats, countdown, ordered checkpoint activation and facts,
HUD/visuals, finish ordering, recovery, reward and cleanup. Checkpoint exports
are **quest trigger geometry**, not automatically active native checkpoint
devices or a playable race. The export does not install resources or modify
vanilla race facts. See the
[race construction study](../../docs/reference/vanilla-quests/deep-dives/races.md).

`build_race(race_id=..., entrants=[{"id":"racer_one","grid":0,
"vehicle":"Vehicle.v_standard2_archer_quartz",
"driver":"Character.sq024_city_race_corpo_racer"}])` builds the captured plan
into a native resource preview. The owning project comes from the survey's
registered depot prefix. Optional `settings` supplies countdown/timeout,
winning places, reward, rubber-banding and off-course policy. No game control,
REDscript or installation is involved. See the
[race builder](../../docs/authoring/races.md) for binary conversion and the
workspot-based activation contract.

## Routes and autonomous scouting

`record_route(name="Courtyard approach")` starts recording. Completed moves and
captures append camera waypoints; `record_route()` finishes. Route records survive
server restarts even if recording was interrupted. `replay_route(route_id=...)`
starts a background job and can recapture all waypoints at original resolution.
Each completed waypoint checkpoints job progress. After interruption, use its
`next_index` as `replay_route(start_index=...)` to resume the remaining waypoints.
`job_status` restores the latest persisted job after a server restart.
Replay does not append to a currently recorded route. Long travel still requires
explicit teleport permission. A route is limited to 500 waypoints.

`autonomous_scout(maximum_steps=20, radius_m=100, step_m=8,
maximum_seconds=600)` starts a bounded coverage job. It prefers less visited cells,
checks forward/sideways candidate segments for collision, and saves a route and
images. Defaults stay on the starting camera-height plane; upper/lower spaces can
be explored interactively or with separately recorded routes. It stops when the
step/time/radius budget is reached or no clear candidate remains. Time budgets
also bound pending movement/image waits. It is a geometric explorer; semantic
judgment about alleys, entrances and useful quest staging comes from the MCP
host reviewing images. The `explore_for_quests` prompt describes that workflow.

`job_status` reports progress, image IDs, route ID and stop/failure reason. Jobs
run in a worker thread so MCP remains responsive. Only one operation owns the
camera/capture backend at once. `observe` during a job returns live state and
progress; saved images can be read while a job continues.

## Stop and coexistence

`stop` writes an out-of-band interrupt and cancels Python image/job waits. The
game releases camera/HUD control on its next protocol poll (normally within
100 ms). The Python controller releases its OS locks after the runtime confirms
release. Bind **Game Scout: emergency stop** in CET for a game-side override.
If the MCP process dies, a five-second lease watchdog releases game-side control.
FreeFly remains in the player's chosen state; the scout does not disable it,
change weather/time, or teleport back on release.

Game Scout uses its own OS lock and, when configured, also respects the existing
capture controller's lock file. This lock path is the only coordination with
that system; there are no shared protocol commands, capture queues or database
writes. Reading the scout library never acquires game control. Concurrent MCP
processes cannot both own the camera. Command IDs, boot IDs, session IDs and
expiration times reject stale responses and commands after reconnect/reload.

HUD suppression covers bounded per-class controller
references; native game compatibility still needs an in-game smoke test. The
installer deliberately does not interrupt an active capture run to perform it.

## Verification and first native test

```powershell
.\converted\game-scout\venv\Scripts\python.exe -m unittest tests.test_game_scout -v
.\converted\game-scout\venv\Scripts\python.exe -m unittest tests.test_game_scout_races -v
```

The suite tests geometry, collisions/loading/cleanup through the Lua harness,
transport locking and stop release, independent image/location records, export,
route replay, exploration budgets, concurrent stop and a real stdio MCP client.

After loading the mod: observe → begin → move 5 m → inspect the image center →
look at the hit → sweep → save a viewpoint/location → record a short route →
replay it → stop → check ordinary camera/HUD control. Then try a small scout job
and interrupt it. Confirm native ray hits, FreeFly protections and HUD suppression
before leaving a long scouting job running. Mocked tests do not verify those
engine behaviors.
