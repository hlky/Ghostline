# Cinematic source case studies

These six manually inspected section studies complement the generated
[416-entry index](README.md). Each locator names an exact resource, local
section and event handle. Full selected-section payloads and adjacent graph
edges are preserved in
[case-evidence.json.gz](../../../../../reference/quests/deep-dives/cinematic-scenes/case-evidence.json.gz).
[Raw verification and RID resolutions](../../../../../reference/quests/deep-dives/cinematic-scenes/raw-case-verification.json)
check all 412 events in the six sections against hash-matched raw sources.
They do not validate animation payloads or installed playback.

## Happy Together: a conversation exit coordinates camera and workspot

Resource: `base\quest\minor_quests\mq010\scenes\mq010_02_barry_talk.scene`.
The whole resource contains 254 events. Barry is actor 0 and Player actor 1;
entries include `Start 0` and `knock_on_door_in`. Named exits include
`barry_tier`, `door_locked_out` and `knock_on_door_out` alongside `End 0`.
These separate interactions already rule out a single linear transcript.

In section **265**, event handle **485** is a player-camera parameter event:
stored start 692, duration 1,000, `resetFov: true`, `resetDof: true`,
`overrideFov: false`, `overrideDof: false`. It should not be described as an
unconditional new FOV/DOF override just because other numeric fields exist.

The same section emits stamp `2:0` at stored time 1,333, and stamps `3:0`
and `4:0` at 3,132. At 3,132, handle **491** also requests an `IdleStand`
gameplay transition for performer 257. Graph edges route `2:0` to AND node
822, `3:0` to hub 824, and `4:0` to workspot node 266. Source pointer for
the camera event: `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/4`.

The owning `mq010_02_barry_talk.questphase`, graph h0 node **9**, launches
`Start 0` and overrides the interruption scenario, including explicit
`talkOnReturn: false`. Node **22** separately launches `knock_on_door_in`;
its `knock_on_door_out` signal deactivates a target at node 25. Scene defaults
alone therefore do not describe the actual caller's interruption policy.
These caller nodes and their edges are preserved in
[caller-evidence.json](../../../../../reference/quests/deep-dives/cinematic-scenes/caller-evidence.json).

**Reusable lesson:** retain multiple timed handoffs and camera restoration
inside a conversational beat. A generic end-of-dialogue callback would erase
the coordination. This section does not by itself establish the entire
approach/leave lifecycle; inspect the owning graph and caller before reuse.

## The Heist: recorded animation is embedded in a larger staged scene

Resource: `base\quest\main_quests\prologue\q005\scenes\q005_07_vip_apartment.scene`.
Its 592 events include 148 dialogue, 120 skeletal-animation, 101 look-at,
76 socket, 68 idle-change and four RID actor events. The source mixes
performance mechanisms rather than selecting one animation system per scene.

In section **2000**, handle **641** starts at stored time 176,567 for duration
30,000. It targets performer 769's `head`, uses RID animation table index
42, and places against `#q005_07_sm_vip_apartment`. That table index resolves
through resource ID to serial **17** in:

`base\animations\quest\main_quests\prologue\q005\q005_08_saburo\q005_08_saburo__saburo_dies__part7.scenerid`.

Pointer: `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/133`.
Handle 643 uses a different table index and serial in the same resource;
another selected event resolves into part8. The `.scenerid` path alone is
therefore insufficient to identify the performance channel.

**Reusable lesson:** a RID beat needs the scene's reference table, resource
handler, animation serial, performer component and origin marker together.
Copying a file path or an integer index is not a portable binding. Event
duration does not establish the complete scene duration or payload validity.

## I Fought the Law: playback, camera and clue windows share one section

Resource: `base\quest\side_quests\sq012\scenes\sq012_02a_braindance.scene`.
The whole resource has 165 events and ten actor definitions, including the
recorded participants, Johnny, a replacer and Player. Entry names include
`sq012_braindance_DEBUG_in` and `bd_only_prev`; a debug-looking name is not
evidence of which entry the installed quest selects.

Section **20** contains several actor RID events of stored duration 33,333.
Handle **6** targets performer 257's `head`, uses animation table index 3,
and resolves to serial **47** in
`base\animations\quest\side_quests\sq012\sq012_braindance\rid\sq012_braindance__part_a.scenerid`.
Its origin is `#sq012_02a_sm_braindance`.

Camera event **51** uses camera table index 0, resolving to serial **15**
in the same RID resource, and addresses `#sq012_bd_camera` for stored duration
33,333. Actor and camera reference tables are separate even when the resolved
resource matches. Pointer:
`/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/17`.

Clue event **59** defines `holt`, start 10,880 and duration 3,482, against the
`holt` entry of `#sq012_com_braindance`; `overrideFact` is explicitly false.
Its pointer ends in `/graph/2/Data/events/24`. These are stored local windows,
not observations of what happens after seeking or rewinding.

**Reusable lesson:** the portable unit is playback plus analysis behavior.
Actor movement alone omits camera, clue entity bindings and temporal windows.
Validate rewind, seeking, layers and cleanup separately from ordinary linear
playback. GQT005 already exposes this same production boundary.

## Pyramid Song: a single scene contains conventional and recorded beats

Resource: `base\quest\side_quests\sq030\scenes\sq030_09_pier.scene`.
Its 606 events include 137 dialogue, 122 skeletal-animation, nine RID actor
and eight RID camera events. The filename does not describe every contained
beat: section **2680** binds against `#sq030_10_sm_sex`.

Actor event **2211** targets performer 1's `head`, starts at explicit zero,
lasts 16,433, and uses RID actor index 63. That resolves to serial **93** in
`base\animations\quest\side_quests\sq030\sq030_10_sex\sex_judy_layout.scenerid`.
Camera event **2227**, at 16,433 for duration 6,533, uses camera index 10,
resolves to serial **12** in the same RID, addresses `#sq030_10_camera`,
and explicitly sets `activateAsGameCamera: 1`.

Their pointers are `/Data/RootChunk/sceneGraph/Data/graph/296/Data/events/2`
and `/Data/RootChunk/sceneGraph/Data/graph/296/Data/events/10`. The section
also has multiple timed socket outputs. Stamp `2:1` fans into world-data,
condition and item-manager operations; `2:0` has a separate world-data target.
Treating an ordinal as decoration would collapse distinct source behavior.

**Reusable lesson:** recorded takes and their world-state handoffs belong
inside a larger encounter lifecycle. Preserve origin, camera activation,
serials and socket ordinals; do not infer which world operation is cleanup
from the event type alone. Payload decoding and rig/placement review remain
separate requirements.

## Q305 brain-hack resource: rich staging without RID playback

Resource: `ep1\quest\main_quests\q305\scenes\q305_07_brain_hack.scene`.
The resource contains 1,199 events: 262 skeletal animation, 230 ordinary
look-at, 46 advanced look-at, 143 audio, 123 dialogue, 109 idle changes,
95 VFX and 17 camera-parameter events, among other types. There are no
`scnPlayRidAnimEvent` occurrences in this resource. Its fourteen actor
definitions include several separately named past/present Songbird roles.

In section **3453**, handle **2191** contains player-camera reset settings
and performer target 1 / slot `Head`. Handle **2192** is a camera placement
event at `/Data/RootChunk/sceneGraph/Data/graph/149/Data/events/1`; its other
fields are omitted. The graph routes the section into AND node 3455, with
hub 4933 supplying its input. The missing placement fields cannot be turned
into an invented camera move.

**Reusable lesson:** camera, audio, gaze, VFX and conventional performance
can supply a complex cinematic resource without RID actor events. Maintain
explicit role identity when several versions of a character coexist.

**Attribution caveat:** the frozen catalogue includes this resource in the
selected context of *Four Score and Seven*. This study reports that inherited
context, but does not claim the brain-hack sequence plays during that journal
entry. A resource-context association is broader than verified branch/entry
reachability. This is a Q305 implementation-family case, not a narrative
description of that epilogue.

## The Killing Moon: outcome ports and a camera-selection trap

Resource: `ep1\quest\main_quests\q306\scenes\q306_10_finale.scene`.
The 807-event resource exposes entries such as `standoff_start`, `deal`,
`countdown` and several preview-named routes. Exits include
`Reed_Takes_SB_Out`, `Reed_Dead_Out`, `failstate_kill`, `retreated_end`,
`v_shot_dead` and `draw_weapon`. These are distinct interface ports, not one
generic completion result; the phase's handlers determine persistent outcomes.

Section **5550** contains one RID camera event, handle **2607**, at explicit
zero for duration 6,633, with `activateAsGameCamera: 1`. It binds camera
`#q306_10_shot_0335` against `#q306_10_sm_finale`. Camera table index 0
resolves to serial **1** in:

`ep1\animations\quest\main_quests\q306\q306_10_finale\rid\q306_10_finale__cam_official_trailer__sh0335.scenerid`.

Pointer: `/Data/RootChunk/sceneGraph/Data/graph/385/Data/events/0`.
The incoming edge comes from condition node **5551**, which explicitly tests
`ep1_official_trailer > 0`. Its True route reaches camera section 5550 and
another target, 5850. This is concrete evidence of a trailer-specific gate;
the existence of the event does not establish a normal playable finale shot.
The gate is preserved in the [caller evidence](../../../../../reference/quests/deep-dives/cinematic-scenes/caller-evidence.json).

The owning `q306_05_launchpad.questphase`, graph h0 node **10**, starts this
scene through `Start 2`. Its `draw_weapon` output launches another call to the
same resource at node **41**, through `standoff_start`, while also signaling
nodes 49 and 53. Node 41 then routes `Reed_Dead_Out` to node 58. This is an
explicit example of a phase using multiple entries/calls into one scene;
flattening the resource into a single linear film would lose that contract.

The stored default interruption scenario explicitly uses distance >6 for
interrupt and <5 for return, with `talkOnReturn: 1`. This demonstrates separate
interrupt/return thresholds; it does not establish that every route uses them.

**Reusable lesson:** preserve outcome ports, caller overrides and conditional camera branches.
Inventory presence and a game-camera flag do not establish installed
reachability. A scene can carry preview/presentation scaffolding alongside
playable outcome logic.

## Inspect a case without dumping the whole resource

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource mq010_02_barry_talk.scene --graph scene --node 265
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource mq010_02_barry_talk.scene --events --node 265
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest 'I Fought the Law' --events --event-type PlayRid
```

Queries retain section boundaries. Stored timing values here remain in source
scene units; this report does not convert them into measured elapsed seconds.
