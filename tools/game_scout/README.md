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
