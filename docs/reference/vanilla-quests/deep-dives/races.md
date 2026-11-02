# Creating new vehicle races

Inspected 2026-10-31. The practical starting point is **MQ056's repeatable
race lifecycle, with a new owned course and entrant set**. SQ024 supplies the
underlying world and racing patterns. A questphase copy alone is insufficient:
MQ056 still uses SQ024 splines, finish triggers, world variants and shared HUD
facts. Neither family is an isolated drop-in template.

We have located the native course geometry, opponent commands, checkpoint fact
producer, HUD bridge, finish decision and recovery path. This establishes a
concrete construction plan. A newly authored race spline and complete custom
race have **not** been tested in game by this research.

## Sources and evidence

- [Focused evidence](../../../../reference/quests/races/evidence.json): 74
  selected quest/scene nodes and incident socket edges, three freshly decoded
  world sectors, checkpoint entity operations, source hashes and script anchors.
- [The Distance](all-quests/base-mq056_race_replay.md): broader MQ056 lifecycle,
  including repeatable entry, failure and reward context.
- [City Center](all-quests/base-sq024_city_race.md),
  [Santo Domingo](all-quests/base-sq024_santo_domingo_race.md),
  [Badlands](all-quests/base-sq024_badlands_race.md) and
  [the finale](all-quests/base-sq024_the_big_race.md): SQ024 comparison context.
- [Corpus method](all-quests-method.md): frozen graph provenance and coverage.
  The focused pack does not promote every dependency or old counter phase to
  an active gameplay path.

The world/entity payloads were read from
`K:/Cyberpunk 2077/archive/pc/content/basegame_3_nightcity.archive`.
Quest evidence comes from the checked all-quest corpus. Scripts were freshly
decompiled from `K:/Cyberpunk 2077/r6/cache/final.redscripts`, **not** the
`.modded` cache. The pack records the bundle and decompiler hashes; it does not
infer an executable game version from resource headers or timestamps.

The local modding wiki supplies general quest, vehicle and ArchiveXL guidance,
but the searched quest/file-format references contain no dedicated race
construction recipe. The detailed claims below come from decoded game data
and the local script bundle.

Locators use **resource basename / graph handle / node ID**. IDs repeat between
embedded graphs. Scene locators use the scene node ID. Consult the evidence's
full depot path and JSON pointer when adapting a node.

## How the system fits together

| Layer | Authored inputs | Responsibility |
| --- | --- | --- |
| World course | Race spline, speed spline, placement transforms, width sections, triggers, marker entities and variants | Defines the drivable course and physical interactions |
| Entrants | Community records, vehicles, driver/passenger assignments, start spots, per-vehicle commands and exit routes | Supplies opponents and their behavior |
| Quest lifecycle | Prefab activation, readiness, restrictions, native start/stop, checkpoint sequencing, finish tests, rewards and retirement | Coordinates one attempt |
| Vehicle UI | `VehicleRaceQuestEvent`, vehicle controller, HUD and shared facts | Displays countdown, time, progress and position |

There are two distinct starts: `questStartRace_NodeType` for native race state,
and the `VehicleRaceQuestEvent` mode `RaceStart` for the vehicle/HUD clock.
Likewise `questStopRace_NodeType`, `RaceEnd` and `Disable` serve different
parts of shutdown. Do not substitute one for the whole lifecycle.

The script-visible `RacingSystem` exposes `IsRaceInProgress()` and
`IsAIVehicleRegistered(vehicle)` in this bundle. It does not expose a convenient
script-visible `CreateRace(course, cars)` method. Use the native quest/command
precedent before inventing a scripting replacement. Internal registration,
position calculation and recovery implementation remain native engine behavior.

## Course resources and world ownership

The complete base world block contains 23,689 descriptors. Race sector filenames
are compiled hashes, so a filename search for `sq024` misses them. Resolve a
descriptor by its `questPrefabNodeRef` and variants, then follow `data.DepotPath`.

The City Center bindings are concrete:

| Compiled sector basename | Owning prefab alias | Contents inspected |
| --- | --- | --- |
| `quest_5aab979acf00452f.streamingsector` | `#sq024_pr_04_city_center_race` | 41 nodes: race/speed splines, eight quest triggers, marker entities and an AI spot |
| `quest_47de76de8df02b3e.streamingsector` | `#mq056_pr_citycenter_checkpoints` | 30 checkpoint marker entity nodes |
| `quest_0e2c89ba4e7e003c.streamingsector` | `#mq056_pr_01_citycentre` | Ten nodes including staging and checkpoint triggers |

These paths live under `base/worlds/03_night_city/_compiled/default/`.
Full prefab roots, block descriptors and registered NodeRefs are retained in the
focused evidence.

In the first sector, node index 3 is `worldRaceSplineNode`, debug name
`{sq024_spl_city_race_spline}`. It contains **116 `SplinePoint` elements** with
positions and two tangents per point. The node placement is approximately
`(-740.40271, -517.74036, 7.90620)`. Spline point coordinates belong to that
node's transform; do not substitute world positions into the local point array
without applying the transform.

`worldRaceSplineNode` inherits `worldSpeedSplineNode`, which inherits
`worldSplineNode`. The donor has a speed section with
`targetSpeed_M_P_S = 100` and `offsetDefault = 7`. Its width sections are:

| Stored `from` | Stored `to` | `left` | `right` |
| --- | --- | --- | --- |
| omitted | 3500 | 7 | 7 |
| 3500 | 4450 | 10 | 4.5 |
| 4450 | 4480 | 7 | 4 |
| 4480 | 5200 | 7 | 7 |
| 5200 | 5260 | 1.5 | 3 |
| 5260 | 5750 | about 3.4 | about 3.4 |

These are stored course parameters, not recommended tuning for a new route.
Confirm the engine's section-distance and offset behavior on a short custom
spline before scaling up. The separate node index 2, `#sq024_spl_city_race`, is
a `worldSpeedSplineNode`; it also has 116 points. Commands can carry both an
on-spline parameter block and a racing block. The selected command `type`
determines which block is relevant; merely finding both is not proof both run.

The course also owns water, finish, finish-spawn, backwards and sharp-turn
triggers. GPS guidance is a separate world variant: MQ056 setup toggles
`#loc_sq024_citycenter_racetrack_gameplay` / `gps_path`. A race spline alone
does not establish a working GPS presentation.

For a new course, create mod-owned streaming sectors/block, stable aliases and
matching node placement hashes. Follow the established
[world binding model](../../../authoring/world-resources.md): block descriptor,
sector `nodeRefs`, `nodeData.QuestPrefabRefHash`, phase prefab declarations and
inline phase activation must agree. A `debugName` does not register an alias.
Register the custom streaming block through ArchiveXL. Avoid replacing the
global Night City world block.

## Explicit player activation

MQ056's `mq056_01_city_race.scene` waiting branch begins at scene node 55.
The player selects the sit choice at 119, runs the FPP sit section at 121,
then enters the player workspot through 125. Its `Work Started` output enables
the get-up choice at 151. Section 154 restores the player/camera transition;
158 stops the workspot before the scene exits through 161. Walking into the
staging area is therefore not the player's acceptance of a race.

The builder constructs this explicit action sequence directly in
[`race_resources.py`](../../../../tools/race_resources.py), without templates.
Only its named `race_accepted` scene exit starts the generated attempt. The
attempt then prepares entrants and waits for the player vehicle before the
countdown and native race start. No additional REDscript admission helper is
generated. Graph boundary lists are derived from the created start/end nodes.

## Opponents and driving

MQ056's City Center community is
`base/quest/minor_quests/mq056/community/mq056_01_citycenter.community`.
It still references SQ024 start/end workspots. Its racing commands address
`#mq056_com_city_race` entries such as `team_1_v` through `team_5_v`.
Spawn vehicles and actors, assign seats, then verify readiness before release.
Assignment is not equivalent to a confirmed mount.

The active movement node is `questVehicleNodeCommandDefinition` with
`commandParams.type = Racing`. Its racing block supplies
`questvehicleRacingParams.splineRef = #sq024_spl_city_race_spline`.
City Center has several authored rubber-banding configurations:

| Graph / example node | `targetForwardOffset` | `minDistance` | `maxDistance` |
| --- | --- | --- | --- |
| h2917 / 3 | omitted | 20 | 150 |
| h3416 / 3 | 20 | 20 | 200 |
| h3915 / 3 | 50 | 20 | 300 |
| h4414 / 3 | 80 | 20 | 1000 |

All four examples target the main player and store `rubberBanding = true`,
`stayInFront = true`, and `pushOtherVehiclesAside = false`. These are distinct
graph configurations, not a demonstrated runtime difficulty order. Trace their
parent selection before assigning difficulty labels. Inactive on-spline blocks
also contain catch-up teleport settings; do not attribute those to the active
racing command without checking the selected block.

After an opponent reaches the finish trigger, a separate movement command
sends it toward an exit/end spline. For example h2917 node 19 references
`#sq024_spl_city_end_racer_000` in its on-spline block. A new route needs a safe
run-off/parking solution as well as the competitive spline.

## The complete checkpoint producer chain

The counter is **not just HUD telemetry or a quest trigger**. MQ056 uses
`base/quest/minor_quests/mq056/entities/mq056_checkpoint_marker.ent` with a
device operation container. WolvenKit serialization resolves its compiled
entity package at `/Data/RootChunk/compiledData/Data/Chunks`:

1. Chunk 6's persistent device state contains `TriggerVolumeOperationsTrigger`.
   Its `TriggerVolumeOperationTriggerData` selects component `trigger`, enables
   player activation and disables NPC activation.
2. The trigger executes operation `addFact` immediately.
3. `FactsDeviceOperation` adds **1** to
   `sq024_current_race_checkpoint_fact_add`.
4. After approximately **0.1 seconds**, `disableComponents` disables
   `ui_back`, `ui_front` and `trigger`, and requests device disable.
5. The quest observes the counter and shows the next world checkpoint marker.
   In `mq056_01_citycenter.questphase` h2428, node 4 shows
   `#mq056_city_checkpoint_001`; node 5 waits on the shared checkpoint fact;
   node 7 shows checkpoint 002 and node 8 observes value 1. Later nodes repeat
   this sequencing pattern.

The device operation stores `executeOnce = 0`. Its repeat prevention is the
authored disable behavior and lifecycle, rather than an execute-once flag.
Test duplicate crossings inside the disable delay, re-show/re-enable, rewind
through a marker and save/load. A successful one-pass crossing does not prove
the marker resets correctly for another attempt.

`RaceCheckpointSelector` records drive the front/back street-sign presentation.
The extracted entity uses `LCDScreens.RaceCheckpointForward`; world instances
also override selector records. Those records select the signs; the device
operation produces the checkpoint fact.

There are **30 marker nodes**, while the MQ056 scene's UI setup declares
`maxCheckpoints = 31`. Preserve the distinction between marker count, displayed
total and finish accounting. The focused sample does not prove the exact
off-by-one convention for an arbitrary custom course. Define and test that
contract explicitly rather than copying a total or silently changing it.

An auxiliary h2773 graph observes `mq056_checkpoint_fact_add` and writes the
shared counter. Its presence does not make it the only or primary producer;
the decoded marker entity establishes a direct producer outside quest graphs.

## Countdown and stock HUD integration

`mq056_01_city_race.scene` contains these event-manager quest nodes:

| Scene node | Event mode | Stored UI totals |
| --- | --- | --- |
| 38 | omitted; enum default is `PreRaceSetup = 0` | 6 positions, 31 checkpoints |
| 32 | `CountdownStart` | 6 positions, 31 checkpoints |
| 30 | `RaceStart` | 6 positions, 31 checkpoints |

All target `#mounted_vehicle`, manager `VehicleManager`, PS class
`VehicleComponentPS`, component `controller`. Match the whole routing contract,
including the mounted vehicle, instead of queuing only a UI event.

The decompiled vehicle/HUD chain explains why:

- The persistent controller forwards mode/totals to the UI and pushes
  `UIGameContext.VehicleRace` on `PreRaceSetup`; `Disable` pops that context.
- HUD setup needs a mounted vehicle. It captures the active vehicle blackboard
  and registers a fact callback on that vehicle.
- `CountdownStart` plays the stock countdown/position animations and shows
  the counters. `RaceStart` records simulation time and starts vehicle clock
  updates. This is simulation time, not a persistence-safe custom stopwatch.
- The HUD listens to **`sq024_current_race_checkpoint_fact_add`** by name.
- Position comes from `UI_ActiveVehicleData.PositionInRace`; on a position
  change, the HUD writes **`sq024_current_race_player_position`**.

Consequently, retain these fixed interface names when using the unmodified
stock HUD. Give private quest/result facts the new quest prefix. If custom
checkpoint entities write private progress, add a deliberate bridge to the
shared HUD fact, or deliberately adapt the HUD. Renaming every `sq024_` string
breaks this interface. Conversely, leaving every old SQ024/MQ056 fact untouched
risks changing vanilla progression.

`RacePlayerDistanceFromSpline` is another shared interface consumed by the
native-race quest patterns. Its producer is not established by the script
excerpts; verify it on the custom spline and retain the name unless deliberately
replacing that producer/consumer contract.

Treat shared native racing state and HUD facts as an exclusive resource. The
proposed custom lifecycle must refuse/defer while another race owns them,
claim ownership for one attempt, and release it after retirement. Do not clear
shared facts on generic quest startup or after another race takes ownership.
The HUD position fact is presentation-produced and only updates on changes;
do not use it as the sole authoritative finish signal.

## Finish ordering, recovery and cleanup

MQ056's City Center opponent graph h2917 node 8 waits for **that opponent's
vehicle** (`team_1_v`) in `#sq024_tr_city_race_finish`, with
`isPlayerActivator = false`. The graph includes a writer for
`mq056_city_race_enemy_finish` at node 13. Other entrant finish waits and
per-entrant finish facts exist beside it.

At the player's resolution, h5078 node 86 checks
`mq056_city_race_enemy_finish`, explicitly `Equal`, with the value omitted.
Its `True` socket succeeds the race objective at node 119 and calls win
commentary at 128; `False` fails it at 124 and calls lose commentary at 126.
The connected sockets establish those branches. Preserve the stored predicate
or inspect the default deliberately; do not reinterpret an omitted value as
`== 1`. A winning position display is not itself this result commit.

For a custom race, make ordered course completion a prerequisite to accepting
the player's finish. Give finish resolution a once-only commit, cancel losing
waits and bind reward delivery separately. A plain finish-area trigger is not
proof of checkpoint completion, a valid lap or first place.

Off-course handling has two thresholds, water handling and cancellation:

| Source | Violation-side stored value | Return-side predicate |
| --- | --- | --- |
| SQ024 Pacifica phase h901 / 28, 32 | `RacePlayerDistanceFromSpline`, 35; comparison omitted | distance < 34 |
| SQ024 Badlands phase h1070 / 28, 32 | water OR distance 50; comparison omitted | outside water AND distance < 40 |
| MQ056 City Center h1442 / 2, 4 | either water trigger OR distance 50; comparison omitted | outside both water triggers AND distance < 40 |

City Center warns `RETURN TO THE RACE`, starts a two-second wait, and has a
`CutSource` edge from node 8 to the pending timer node 7's `CutDestination` when
the return route fires. Recovery h1510 fades out, waits 100 ms, invokes
`questGoBackToRace_NodeType`, waits a second and repairs the mounted vehicle.
The native relocation algorithm is not exposed by the empty node payload.
Its dependence on a valid active race/spline must be tested on a new course.

Finish h1017 node 36 emits `RaceEnd`; node 41 holds `questStopRace_NodeType`.
Later h5078 node 58 emits `Disable`. The script's vehicle `CleanUpRace` also
cancels its clock tick and pops the race UI context on player unmount. These
are complementary retirement mechanisms, not proof that one event restores
all modified state. In the inspected script switch, `RaceEnd` stops the clock,
whereas `Disable` removes the HUD/context; retain both responsibilities.

A custom cleanup contract must retire opponent commands, pending timers and
finish listeners; hide/deactivate checkpoints/GPS and owned communities;
restore any brakes, door interactions, mortality, traffic/prevention rules,
remote-control permissions and gameplay restrictions it actually acquired;
disable the UI; stop native racing; and reset only owned attempt state.
SQ024/MQ056 source labels and world-event suppression are location-specific.
Do not transplant them as generic race requirements.

## A practical first custom race

Use an independent test project with a new ID/depot prefix resolved through
`tools/project_layout.py`. Do not attach the first experiment to the story
root or reuse global vanilla world overrides. The repository's general world
and quest tools are useful infrastructure. The world generator now accepts
[`race_splines` with speed and width sections](../../../authoring/world-resources.md#race-splines).
The [race builder](../../../authoring/races.md) generates a native preview from
Game Scout's survey export and explicit entrants, including the player workspot
activation gate. There is still no general compiler `race` stage or installed
custom-race proof.

1. **Prove one opponent on one new spline.** Choose an open road with a safe
   start/run-off. Author a short mod-owned `worldRaceSplineNode` using the
   inspected layout, local points/tangents, conservative speed/width sections,
   registered NodeRefs and valid placement/bounds. Spawn a driver/vehicle,
   wait for readiness, and run the native `Racing` command. Verify movement,
   native registration and shutdown in game.
2. **Prove an ordered short course.** Add three to five owned checkpoint
   entities, one active at a time, plus a separate finish. Adapt the inspected
   trigger/fact/disable operation package. Define the counter's initial value,
   accepted crossing sequence and whether the finish contributes to the total.
   Reject premature finish, skipped checkpoints and duplicate crossings.
3. **Connect staging and presentation.** Confirm player driver seat and all
   entrants; set up the vehicle UI, hold/release the start, run countdown,
   start native race state and the HUD clock at deliberate points. Confirm
   stock HUD progress/position on the custom course before adding more cars.
4. **Complete one route early.** Player finish versus opponent finish must
   produce exactly one result, then one reward and journal completion, followed
   by full retirement. Test lose/abort and then run the same race again.
5. **Add recovery and wider competition.** Test off-course distance reporting,
   water/blocked-route policy and native recovery on the custom spline. Then
   tune opponent count, rubber-banding, traffic suppression and optional combat.
6. **Add story/presentation after the route works.** Bespoke start/finish
   dialogue, spectators, GPS, VO and rewards can use the proven lifecycle.

Proposed authoring inputs should explicitly own `course`, `entrants`,
`checkpoints`, `staging`, `HUD`, `outcome`, `recovery` and `cleanup`. Store shared
HUD/native fact exceptions in that contract. Require the generator/audit to
report remaining vanilla NodeRefs, facts, source labels and journal paths,
with each reference either an intentional dependency or a failed retarget.
Use typed fields and reference resolution; avoid blind string replacement.

Follow [quest production](../../../workflows/quest-production.md) for the early
playable milestone and [build/package](../../../workflows/build-and-package.md)
for project-scoped packaging. Author CR2W-JSON under the owning `source/raw`;
use compatible binary templates or WolvenKit for new layouts. Keep loose
ArchiveXL/journal/localization registrations in `source/resources`. Pack with
WolvenKit and verify extracted installed payloads before handing off a test.

## Acceptance cases and remaining boundaries

| Area | Required cases |
| --- | --- |
| Entry | Start already inside staging; late mount; wrong seat; wrong/destroyed car; missing opponent; vanilla race already active |
| Course | Each checkpoint once; skip; wrong order; reverse crossing; duplicate within 100 ms; early finish; road blockage |
| Competition | Player first; opponent first; near-simultaneous finish; opponent destroyed/stuck; rubber-band behavior behind/alongside/in front |
| Recovery | Cross violation/return thresholds; return before timer; water; abort during fade; recovery to custom spline |
| Persistence | Load before start, during countdown, after checkpoint, near finish, after result before reward, and after retirement |
| Retirement | Unmount, death, abort, finish and replay; no stale UI/ticks, brakes, immortality, commands, markers or repeat rewards |

Confirmed statically: the source classes/bindings, checkpoint producer chain,
selected socket branches, course geometry/layout and fixed HUD facts.
Still requiring a named installed scenario: new-spline native registration and
position, actual checkpoint numbering/finish convention, native recovery,
save/load reconstruction, cross-mod compatibility, reward delivery and complete
repeatable cleanup. A serializer round trip cannot establish those behaviors.

## Reproduce the focused inspection

Run from the repository root. The graph-only pack can be rebuilt from checked
evidence without the game:

```powershell
py -B tools/build_race_research.py --scratch .tmp/race-research-empty --output .tmp/races-graphs.json
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest 'The Distance' --resource mq056_01_citycenter.questphase --graph h5078 --node 86
```

To reproduce the world/entity inspection, create `.tmp/race-research` and use
the pinned native CLI/schema. `extract --path` takes the exact depot path:

```powershell
$raceRed = '.\tools\ghostline-red\target\release\ghostline-red.exe'
$raceArchive = 'K:\Cyberpunk 2077\archive\pc\content\basegame_3_nightcity.archive'
$raceDepots = @(
  'base\worlds\03_night_city\_compiled\default\blocks\all.streamingblock',
  'base\worlds\03_night_city\_compiled\default\quest_5aab979acf00452f.streamingsector',
  'base\worlds\03_night_city\_compiled\default\quest_47de76de8df02b3e.streamingsector',
  'base\worlds\03_night_city\_compiled\default\quest_0e2c89ba4e7e003c.streamingsector',
  'base\quest\minor_quests\mq056\entities\mq056_checkpoint_marker.ent'
)
foreach ($raceDepot in $raceDepots) {
  & $raceRed extract $raceArchive --output .tmp/race-research/cr2w --path $raceDepot
}
```

Serialize the block/sectors to `.tmp/race-research/<basename>.json` with
`cr2w-serialize <binary> <json> --schema red-schema.json`. Use
`tools/explore_world.py -f <json> nodes --type Race` for a focused view.
The native entity export leaves its compiled buffer opaque in this inspection;
use WolvenKit to decode the checkpoint device operations:

```powershell
New-Item -ItemType Directory -Force .tmp/race-research/wkit | Out-Null
& 'H:\WolvenKit.Console-8.17.4\WolvenKit.CLI.exe' convert serialize .tmp/race-research/cr2w/base/quest/minor_quests/mq056/entities/mq056_checkpoint_marker.ent -o .tmp/race-research/wkit -v Minimal
.tmp/redscript/target/release/redscript-cli.exe decompile -b 'K:\Cyberpunk 2077\r6\cache\final.redscripts' -o .tmp/race-research/final.reds
py -B tools/build_race_research.py
```

The scratch decompiler is an existing local build, not a repository bootstrap
guarantee. The evidence pack records its hash and script anchors. Optional
`script-provenance.json` supplies bundle/tool identity; retain those identities
when updating the snapshot. World/entity sections are included only when their
scratch exports are present; graph-only output is deliberately incomplete.
