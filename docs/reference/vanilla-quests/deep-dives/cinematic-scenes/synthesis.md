# What the cinematic corpus teaches Ghostline

For the narrower animation/movement goal, start with
[making interactions feel physically believable](interaction-performance.md).

The strongest reusable unit is a **staged interaction with owned transitions**:
acquire actors, establish poses and attention, play a section, emit named
milestones, handle alternatives, and release control. A list of spoken lines
captures only part of that interaction. This is an interpretation of the
stored mechanisms below, not a claim to have watched every scene.

The [index](README.md) covers all 416 journal identities and inventories all
3,139 frozen scene resources. There are 318,424 section-event occurrences.
Only 320 journal identities have scenes in their selected forward context;
their union is 1,204 scene resources. The remaining resources remain searchable
in the [scene index](scene-index.md), including shared, ambient, test and
implementation contexts outside the journal selection. The 96 identities
without selected scenes are an attribution boundary, not 96 demonstrated
cinematic-free playable quests.

## Presentation is layered rather than a separate movie mode

| Stored mechanism | Event occurrences | Scenes containing it | What it supplies |
| --- | ---: | ---: | --- |
| Dialogue | 85,190 | 2,629 | Spoken-line scheduling and screenplay binding |
| Skeletal animation | 66,028 | 1,192 | Authored performance events on actor components |
| Gaze, including player look-at | 51,945 | 1,172 | Attention between performers and targets |
| Idle changes/additions | 18,167 | 899 | Baseline posture and pose continuity |
| IK | 6,794 | 660 | Additional contact/pose control |
| Camera events, parameters, placement and RID camera | 3,428 | 432 | Several distinct camera mechanisms |
| Prop attachment and equipment | 5,964 | 535 | Held/world objects and equipment changes |
| Audio events, excluding spoken dialogue | 6,322 | 502 | Additional sound scheduling |
| VFX, including braindance VFX | 8,436 | 528 | Effects tied to scene performance |
| Gameplay transition | 3,131 | 641 | Explicit transitions on performers |
| Timed socket signal | 51,856 | 1,145 | Section-to-graph synchronization |
| RID actor animation | 1,567 | 38 | Recorded performance references |
| RID camera animation | 693 | 44 | Recorded camera references; also counted in camera |

These are overlapping capability counts, not partitions or quality scores.
Speech and skeletal animation coexist in 1,051 scene resources and 13,639
event sections. Speech and gaze coexist in 1,027 resources and 12,398 sections.
This supports building coordinated speech/pose/attention sections. It does
not prove that any particular pair of events overlaps in time.

Recorded actor playback is a specialized part of the inventory: 38 scenes,
with actor and camera RID events coexisting in 32 scenes. Conventional
skeletal animation is much more widespread. A Ghostline cinematic roadmap
should therefore include reusable gestures, idles and gaze alongside RID
production. Absence of a RID event does not mean absence of a cinematic
performance; other event and workspot mechanisms remain available.

## A camera event does not necessarily take over the player's view

The camera inventory contains 2,482 parameter events in 407 scenes, 693 RID
camera events in 44 scenes, 244 camera events in 77 scenes, and nine placement
events in four scenes. The union is 432 scenes, not the sum of those columns.
Holocall cameras, player-camera parameters and recorded camera tracks must
remain distinct authoring choices.

Barry's section 265 explicitly requests player-camera FOV/DOF reset behavior.
SQ012 section 20 instead addresses `#sq012_bd_camera` and a RID camera serial.
SQ030 section 2680 explicitly includes `activateAsGameCamera: 1` on a recorded
camera event. These are different contracts. See the
[source cases](case-studies.md), which retain exact nodes and raw pointers.

The Q306 camera case also demonstrates a selection trap: its bound RID path
contains `cam_official_trailer`, and its incoming gate explicitly tests
`ep1_official_trailer > 0`. Its presence inside a production-family scene
does not establish that the normal playable finale selects it. A camera
catalogue needs caller/entry evidence before calling a track a playable shot.

## Section signals are part of the choreography

All 641 scenes containing gameplay-transition events also contain socket
events somewhere in the resource. Both mechanisms coexist in 2,635 sections.
This is structural co-occurrence, not proof of one universal ordering.

The Barry case shows a concrete connection: section 265 emits different socket
stamps into an AND node, a hub, and a workspot operation. Replacing that section
with a duration plus a single completion output would discard source behavior.
SQ030 similarly sends timed outputs into world-state and item-related nodes.

For tooling, represent a section as a local timeline with explicit graph ports.
Keep socket name **and ordinal**. Preserve animation scaling fields: 70,174
events explicitly carry `scnScalingData_KeepRelationWithOtherEvents` in this
snapshot. An event's stored start/duration alone may not describe its eventual
runtime schedule. Never concatenate all scene sections into one movie timeline:
choices, parallel routes, hubs, entries and interruptions determine execution.

## Actor acquisition and release belong in the scene contract

Across the indexed scene actor definitions, stored acquisition plans include
community (3,537), find-in-context (3,234), spawn-set (2,160), spawn/despawn
(1,179), spawner (285) and find-in-world (251). These are actor definitions
across resources, not unique people or independently spawned runtime entities.

The practical consequence is to parameterize acquisition and readiness rather
than assuming every performer is spawned by the scene. Community entry and
world marker bindings must travel with a portable performance. The owning
questphase still needs to establish readiness and determine eventual community
cleanup. The repository's [scene authoring rules](../../../../authoring/scenes.md)
already require this separation for Ghostline.

An interruption-scenario array is present in 3,096 scenes. Many inspected
records contain a default speaker-distance interrupt/return pair with omitted
parameters. Presence alone does not prove a tested distance, enabled state,
resume path or cleanup policy. Q306's stored default explicitly contains
distance >6 for interruption and <5 for return; those values belong to that
resource and are not universal engine defaults.

Caller overrides must be included in this review. Barry's owning phase node 9
explicitly overrides interruption behavior with `talkOnReturn: false`.
Inspecting only the scene-global default would miss that stored policy.

The end-node inventory contains 1,780 explicitly `NonTerminating` nodes, 60
explicitly `Terminating` nodes and 5,519 with omitted type fields. Do not convert
an omitted type into an explicit setting. Likewise, receiving a named output
does not establish that the entire scene and every competing listener have
retired. Quest outcomes and presentation cleanup require their own ownership.

## Quest types have different presentation footprints

MainQuest contexts contain 485 distinct scene resources, SideQuest 191,
MinorQuest 251 and StreetStory 329. These contexts overlap and may contain
whole resources with alternate routes. The numbers are useful for selecting
donors, not comparing cinematic quality or playable duration.

VehicleQuest is a useful counterexample: 27 of its 36 journal entries have a
scene in selected context, but their union is a single scene with zero section
events. That does not mean vehicle gameplay is absent; scene graph operations
and questphase/device behavior sit outside the section-event count. There are
251 zero-event scenes in the full inventory. Keep graph structure alongside
performance metrics.

The snapshot's largest event inventories include Q303's finale (4,121), Q304's
deal (3,983), Q303's nighthawks scene (3,022) and Q305's border crossing (2,775).
Large inventories include alternatives and scaffolding. They are navigation
priorities for further inspection, not rankings of screen time or importance.

## Candidate Ghostline authoring contracts

These are proposals grounded in recurring mechanisms, not implemented compiler
features or validated drop-in templates.

| Contract | Required content | Boundary that must remain explicit |
| --- | --- | --- |
| Staged conversation | Acquired actors, starting idle, gaze, gestures, dialogue bindings | Choice/re-entry policy, speaker readiness, release |
| Physical interaction | Pose/workspot, prop/equipment operation, IK, named contact/commit signal | Interruption before/after commit, prop ownership |
| Directed camera beat | Camera mode, origin, parameters/track, blend and restoration policy | Which camera is controlled and when it is released |
| Recorded performance | RID tables, resource handler, serial, performer component, origin marker | Payload compatibility, synchronized camera/audio, alternate routes |
| Braindance evidence beat | Recorded playback plus clue windows, layer behavior, sound/visibility | Seek/rewind, clue once-only effects, normal/interrupted exit, replay |
| Outcome-bearing encounter | Scene entry/outputs, phase handlers, transitions and cleanup | Nonterminating notifications versus committed outcomes |

The first extension worth pursuing is a small coordinated gesture/gaze/idle
contract with section ports. It addresses the gap between Ghostline's current
dialogue generator and the common vanilla scene shape. Camera beats and prop
interactions can then use the same lifecycle; RID-heavy work remains a more
specialized production pipeline. See the [current Ghostline comparison](ghostline-comparison.md).

Promotion requires a complete donor slice: entry and caller, required world
bindings, actor readiness, normal and alternate exits, cancellation, return,
camera/prop restoration and state commitment. Structural serialization and
hash verification should precede an installed test covering approach, departure,
re-entry, save/load and every retained outcome. No installed game test was
performed by this research pass.
