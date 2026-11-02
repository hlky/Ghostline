# Race builder

`tools/race_builder.py` compiles a complete Game Scout race survey and explicit
driver/vehicle records into native world, scene, questphase, journal and
localization resources. The builder uses ArchiveXL registration and generates
no REDscript or CET runtime. Builds default to an isolated project preview;
they do not install anything into the game.

## Capture and configure

Use Game Scout's [race survey tools](../../tools/game_scout/README.md#race-surveys)
to mark the centreline, ordered checkpoints, grid spots, player start, staging,
activation workspot and finish. Use the owning project's registered depot prefix.
The activation mark is the **player workspot root transform** on clear ground,
not a flying-camera position. Place it beside the grid with space to approach.

Export `race-plan.json`, then write a builder spec beside it:

```json
{
  "schema_version": 1,
  "id": "dock_race",
  "title": "Dock Sprint",
  "survey": "race-plan.json",
  "entrants": [
    {
      "id": "racer_one",
      "grid": 0,
      "vehicle": "Vehicle.v_standard2_archer_quartz",
      "driver": "Character.sq024_city_race_corpo_racer"
    }
  ],
  "countdown_seconds": 3,
  "timeout_seconds": 300,
  "winning_places": 1,
  "reward": {"item": "Items.money", "quantity": 1000},
  "off_course": {"action": "fail", "distance_m": 50, "grace_seconds": 2},
  "rubberband": {"min_distance": 20, "max_distance": 150, "stay_in_front": true}
}
```

`checkpoint_spacing_m` sets intermediate gate spacing by travelled route
length (25-1000 metres; default 40). It is independent of spline point density;
the finish remains a separate gate. GQT009 uses 125 metres, producing nine
intermediate checkpoints plus the finish on its 1.2 km route. `checkpoint_mode:
vanilla` references the shipped MQ056 checkpoint template and configures its
signs and trigger through sector instance data instead of generating custom
`.ent` files.

`grid` selects a surveyed `start_grid` order. Each of the 1–12 opponents needs
a distinct grid and ID, an explicit `Vehicle.` record and an explicit
`Character.` record. `vehicle_appearance` and `driver_appearance` are optional;
their default is `default`. Use the [vehicle database](vehicles.md) to select
records; the builder checks record syntax, not the installed TweakDB or whether
a selected record has a suitable AI-driving setup.

The namespace `id` owns private quest facts, scene resources and journal paths;
give each built race a unique ID. The survey owns its stable depot subtree and
world references. Ownership must resolve to the selected registered project.
The current builder supports one ordered course/lap and one attempt. It does
not silently turn looped spline geometry into a multi-lap race or reset a
completed/failed quest for replay.

## Build commands

Run from the repository root:

```powershell
.venv/Scripts/python.exe -B tools/race_builder.py validate --spec path/to/race.json
.venv/Scripts/python.exe -B tools/race_builder.py build --spec path/to/race.json
.venv/Scripts/python.exe -B tools/race_builder.py build --spec path/to/race.json --deserialize
```

A complete authoring fixture is available at
[`quests/examples/races/example.race.json`](../../quests/examples/races/example.race.json).
Its coordinates are illustrative; they are not a surveyed, drivable course.

Default output is `<project>/generated/races/<id>`. `--output-root` selects
another preview directory; previews cannot be inside any project's source.
`--publish` deliberately writes the owning project's source trees instead of a
preview. It cannot be combined with `--output-root`. `--project` can select an
owner explicitly but cannot override a conflicting depot owner.

`--deserialize` stages binary conversion and semantic readback using
`ghostline-red` before publishing. It takes the generated JSON and reflection
schema directly; it does not look for an existing binary or invoke WolvenKit.
A conversion or readback failure preserves the earlier complete output set.
`--red-cli` and `--schema` override the configured native tool and schema paths.
Runtime archive packing remains a separate project packaging step.

The race flow follows MQ056's owned-car gate, scene-driven announcer/countdown,
device-driven checkpoint counter, water/distance recovery, and first-place
result. The payout is the native 10,000 eddies; legacy `winning_places`, payout,
and off-course-failure settings are normalized to that native behavior. Standing
waiting is retained. Spectator communities and route crowd-null areas are
generated for the new course; its lifecycle releases those areas, combat-event
suppression, door/brake restrictions, racing/HUD state, and clock pause.
Preparation runs in a child phase with cancellation and police failure, without
a custom spawn timeout. The countdown has a separate request entry and an
inside-car fact gate. The lifecycle owns the native save lock, gameplay
restrictions and mortality source; cleanup releases them before the persistent
availability phase waits three game days and the content lock before replay.
Both V and Johnny result variants and Johnny's situational lines are generated
directly. Course-owned streaming variants control barriers, native GPS arrows
and the checkpoint groups.

`world_spec.water_areas` supplies physical, surveyed recovery trigger volumes.
Without water volumes, distance recovery remains active; the builder does not
invent water or fall envelopes beneath the course.

`world_spec.race_dressing` accepts `gps_path` and `barriers` arrays of explicit
`position` and `yaw` transforms. These placements are kept exactly. When dressing
is omitted, GPS arrows use the authored spline vertices and outgoing headings;
road barriers require authored transforms. There is no fixed-spacing fill or
assumed road-edge offset. GQT009 stores its guidance transforms in its survey.

The three health commentary conditions (90%, 60%, 40%) arm together and share
one commentary entry. Speed commentary arms after 30 seconds and uses the
native persistent heard fact and random repeat branch. Opponent-destruction
commentary checks health, distance below 50 metres, the native random branch,
and a shared first-result gate. Johnny's readiness line, camera gate, teleport
effect, passenger assignment, result lines and entry cleanup belong to the phase.
Result dialogue is V, then a one-second pause, then Johnny.
Johnny's departure then waits two seconds, plays the native effect, and waits
one second before deactivation; discount pickup does not hold that sequence open.

Restriction groups follow preparation, mounting and countdown separately. The
inside-car fact follows the mounted-car setup by two seconds; announcer playback
follows that fact by one second. Opponent mortality changes ten seconds after
go. Every crew has a driver and front passenger; the passenger receives the
native reaction preset and persistent combat threats, owned by the attempt.
Win counts select the native rubber-band profiles (150/200/300/1000 metres,
with forward offsets 0/20/50/80). Remote-control availability follows the native
win-count condition.

On a win, the two-second delay, 2.5-second winnings bar and timed 10,000-eddy
payment run alongside result dialogue. The native courier/bike records and
reward crate provide the separate discount pickup. The reward objective and
mappin remain active until the crate interaction. Player entry into the reward
area selects the native loot tables before interaction; no direct coupon-item
grant is added. The courier waits in the native workspot until pickup, then
waits two seconds, leaves the workspot and mounts the bike. The normal mount
and 100-metre instant-mount fallback join before the one-second departure delay.
The courier follows its own departure spline, joins traffic and despawns beyond
150 metres; cleanup waits for that departure. Police prevention uses a separate terminal
socket and does not play ordinary losing commentary.

Finished opponents park; unfinished opponents continue to the finish. Wrecked
crews instantly unmount the passenger before the native short delay and
reactivation in their `finish` community phase,
then vehicle readiness and five ticks precede the final door lock. Leaving the
finish area retires those commands and deactivates the community after half a
second, independently of reward collection, courier departure and result VO.
The courier waits five seconds after success and until the player is more than
eight metres from its static arrival marker before spawning. Its post-pickup
despawn remains 150 metres from the explicitly referenced local player.
Content-token
blocking, vehicle-forbidden areas, radio state and world variants are released
as part of cleanup. The journal becomes inactive before the replay cooldown.

Course authors can provide `world_spec.finish_spots` per entrant,
`finish_splines` per entrant, `end_area_ref`, `reward_drop`, `courier_start`,
`courier_spline`, `courier_bike_start` and `courier_trigger_ref`. Missing finish
roles generate distinct parking splines, a cleanup area, a reward pickup area,
a courier workspot and a departure spline in the captured finish frame. They
never alias the race spline or the finish-crossing trigger. Authored overrides
remain available for the course's physical layout. Community `additional_phases` and spot `phase` values keep
start and finish spawn sets separate.

The preview contains:

- `source/raw`: course and community sectors/block, a checkpoint device entity,
  the activation scene, root/attempt phases, journal and onscreen localization.
- `source/archive`: matching CR2W binaries when conversion was requested.
- `source/resources/<id>.archive.xl`: root quest, streaming, journal and
  localization registration. JSON syntax is used as valid YAML.
- `source/resources/r6/tweaks/<id>.yaml`: race map title/description records.
- `packaging/profiles.json`: the owning project's profiles with the generated
  TweakXL file included in every profile that ships the race. Existing entries
  are preserved and repeated builds do not add duplicate paths. Preview builds
  stage this file; `--publish` updates the owning project's profile in place.
- `race-build.json`: source hashes, resource/binding inventory, result facts,
  runtime dependencies and remaining playtest cases.
- `race.world.json`: the survey world spec plus generated entrant spots and
  checkpoint visual bindings.

The generated registration is standalone. When promoting a race into a package,
include its loose registration and generated resource subtree in the owning
project's package profile. Do not install a raw-only preview or assume the
project's existing registration file automatically contains the new race.

Game Scout's `build_race` tool writes the spec/survey snapshot and produces the
same raw preview directly from a library race ID and entrant records. Use the
CLI for binary conversion. Restart the Game Scout MCP server after changing
its Python tool surface; no CET reload is required for the builder.

## Activation and playable route

Activation follows the explicit interaction boundary in MQ056's waiting scene.
`tools/race_resources.py` constructs the activation scene, checkpoint device,
journal and localization directly. It reads no templates. The scene creates
its own player, choices, standing workspot, camera/gameplay restoration and
named exit. Its start/end registries are derived from the nodes it creates,
and the builder validates every declared boundary before writing resources.
Standing performance and camera cleanup require in-game verification.

1. The race POI and waiting objective mappin activate before the staging gate.
   Entering staging starts the standing interaction scene.
2. Wait has the native 2,000-eddy condition, payment icon and progress bar.
   The scene's nonterminating `fade_out` exit starts phase-owned preparation;
   the ready fact releases fade-in and the delayed instruction.
   Johnny's appearance starts from that fade-out handoff, not availability or
   staging, and his spot stays within the native four-metre readiness gate.
3. Preparation spawns and explicitly positions the active player car, prepares
   the opponents and spectators, applies native time/weather and vehicle policy,
   and signals readiness. Standing exit restores gameplay independently of the
   stop-workspot output. The terminating waiting exit starts the attempt.
   Preparation enables only the two front-seat door interactions.
4. Mounting the owned car establishes the inside-car gate. Native announcer and
   countdown entries join before countdown playback. The native go event releases
   brakes, racing/HUD state and course variants.
5. Checkpoint devices increment the stock HUD counter. The phase reveals each
   next visual and waits for the corresponding counter value. Variants own the
   checkpoint lifetime; no extra device-reset actions are inserted.
6. Finish compares the shared opponent-finish flag with zero. First place pays
   10,000 eddies. Wanted level three, unmount and explicit abort have cleanup
   routes. Off-course recovery uses a two-second grace, fade, relocation, repair
   and fade-in; returning within 40 metres and outside water cancels the grace.
7. Cleanup retires competing listeners and Johnny's pending setup, releases the
   save lock, restrictions, mortality, brakes, doors and remote-control policy,
   ends racing/audio/HUD and retires world variants through their native lifecycle.
   Native weather resets over 30 seconds and clock pause is released. Result
   dialogue finishes before Johnny and spectators are deactivated. Journal and
   result state resolve before the three-game-day replay/content-lock gate.

Standing waiting remains the performance exception. Course geometry, physical
hazards and dressing transforms belong to the surveyed course. Source authoring
does not establish in-game behavior without a later build and playthrough.

## Surveyed post-finish stopping area

The authored world input can provide `finish_vehicle_forbidden_area` with
`position` (`x`, `y`, `z`), `yaw` in degrees, `outline` and `inner_outline`
(each a `box` with positive `width`, `depth`, and `height`), and an optional
positive `speed_limit` (default `20.0`, in the engine notifier's units).
The boxes share a centre and yaw; the inner box must fit inside the outer box.
The outer box limits speed and the inner box uses the native zero-speed limit.

Choose this area by following the road beyond the corrected finish in Game
Scout. The builder checks that the entire outer box lies beyond the finish
trigger's far edge, measured along the finish marker's forward direction.
This geometric check cannot establish road accessibility: survey the full
footprint for buildings, junctions, obstacles, and sufficient stopping space.
Keep the finish marker yaw aligned with the direction of travel.

The builder does not infer a stopping location from the finish or cleanup
area. If this field is absent, no finish vehicle-forbidden area is generated.
When supplied, its variant becomes active after a normal race finish and is
disabled during cleanup. Author the finish exit and final cleanup areas to
include the chosen post-finish stopping area so cleanup does not retire it
before the player reaches it.

## Validation boundary

Targeted tests check schema errors, owner/path boundaries, named readiness,
ordered crossing gates, checkpoint fact isolation, workspot activation,
terminal cuts, reward-only-on-success and preservation after conversion failure.
Regression coverage also forbids template reads during resource generation and
checks the scene boundary registries and workspot parameter type.

No installed race is validated by generating JSON or compiling CR2W. Playtest
standing alignment and both explicit actions; driver records/appearances; native
AI registration and course following; checkpoint visuals/progress; close finish
ordering; player unmount during countdown; abort/timeout/off-course cleanup;
and save/load around workspot use, countdown, finish and reward. In particular,
verify that the original car's brakes release after an interrupted mount and
that the failed attempt leaves no active commands or HUD state.
