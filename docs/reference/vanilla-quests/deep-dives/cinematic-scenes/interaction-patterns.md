# From vanilla interactions to performance blocks

This pass follows the earlier [performance guide](interaction-performance.md)
into executable authoring blocks. It manually traces selected combinations in
*Happy Together* and *Space Oddity*, using the fully decoded audited scene
exports. *Machine Gun* supplies an additional equipment-action comparison.
It does not label hundreds of event inventories as manually reviewed scenes.

The [implementation guide](../../../../authoring/scene-performance-blocks.md)
describes the available blocks, content bindings and lifecycle boundaries.
Frozen source-derived event slices live in
[`quests/templates/performances`](../../../../../quests/templates/performances).
Each snapshot records its source SHA-256 and exact event pointers, together
with the required animation resources, actor grants and port declarations.

## Happy Together: reaction is a layered performance

Resource: `mq010_02_barry_talk.scene`, section **68**, duration **18,039**.
Barry's first body gesture, handle **221**, begins at **444** for **3,600**:
`sit_chair__2h_on_lap__01__what__sad__01`. A head gesture, handle **224**,
starts at **617** for **2,567**. Gaze changes at **795**. Expression/idle
transitions occur at **2,862**, **4,840**, **7,717** and **13,163**. The second
body gesture, handle **230**, starts at **7,388** for **9,367**:
`sit_chair__2h_on_lap__01__no__sad__02`.

The interaction therefore combines a maintained seated posture, expressive
body movement, face/gaze changes and speech. Adding just one arbitrary gesture
per subtitle would lose that relationship. Conversely, the head and body
tracks are independent: one should not replace the entire actor animation
whenever only expression or attention changes.

Implemented reduction: **`seated_sad_reply`** retains the two body gestures,
gaze and four baked facial idle transitions. Source dialogue and standalone
head-gesture clips are excluded. The latter need additional facial-resource
closure before becoming portable. Timing is retained within the beat and can
be offset to a new dialogue anchor; the author must still review its meaning.

## Happy Together: explanation changes emphasis within one pose

Section **72**, duration **29,031**, starts with gaze. Body clip **252** starts
at **5,149** for **5,000**, using
`sit_chair__2h_on_lap__01__talk__neutral__03`. A facial idle transition occurs
at **17,322**, followed by body clip **261** at **22,675** for **4,567**:
`sit_chair__2h_on_lap__01__this_or_that__neutral__01`.

The same hands-on-lap posture supports several kinds of emphasis. This suggests
a library organized by posture and intention, with compatible variants, rather
than a flat animation list. Implemented reduction: **`seated_explanation`**
preserves those two body gestures, gaze and the facial idle transition. It
does not copy the donor's head clips, dialogue or branching quest effects.

These first seated blocks retain male_big resources. They are not certified
for Iris, Cinder, Patch or arbitrary male/female bodies. Matching animation
names alone cannot establish skeleton, body-shape or furniture compatibility.

## Happy Together: arrival into a chair includes corrective motion

Section **484**, duration **4,300**, contains:

| Stored time | Mechanism | Role |
| ---: | --- | --- |
| 0 | Body clip 580, duration 4,300 | Walking-to-chair transition with root motion |
| 233 | Facial idle transition | Expression during arrival |
| 882 | Pose correction | Authored arm/spine adjustment |
| 1,700 | Look-at | Attention to the player |
| 2,087 | Pose correction | Further arm adjustment |
| 2,748 | Empty pose-correction group event | Preserved source correction state change |
| 4,299 | Socket signal 591 | Named interaction handoff |

The source body clip is
`walk_0__to__sit_chair__2h_on_lap__01__turn180l__01`. Its root-motion offset
contains Barry-apartment coordinates. Copying that event into another location
without replacing placement would transplant those coordinates too.

Implemented reduction: **`arrive_and_sit`** preserves all seven events,
including the corrective data, but requires a new origin and complete offset.
Its `settled` port corresponds to the source `2:0` signal. Original section
end and `settled` connect to different quest-wrapper nodes (58 and 485);
they are not interchangeable by assumption. New consumers are explicit.

Navigation to a spot and a local recorded/root-motion transition have different
jobs. **`workspot_move`** uses the existing native UseWorkspot builder to walk
a community actor into a world activity. It disables teleport and instant
placement and keeps the native `Work Started` and `Success` outputs separate.
It supplies no guessed timer for arrival. Source setup, navmesh and workspot
entry/exit semantics still need review for the intended location.

## Happy Together: standing releases an activity at a distinct moment

Section **768**, duration **5,067**, contains a standing body transition,
a socket event at time **0**, a facial idle change at **824**, gaze at
**1,102**, and another socket at **5,066**. Source outputs `3:0` and `2:0`
connect to quest-wrapper nodes 1012 and 1011 respectively. Node 1012 explicitly
uses `IdleOnlyMode` with `enableIdleMode: 1` and a zero workspot reference;
node 1011 uses a scene-local workspot binding. The immediate
signal and final-standing signal are separate from normal section completion.

Implemented reduction: **`stand_from_chair`** exposes `idle_only` and
`standing` while preserving body/expression/gaze timing. The semantic port
names describe the new library contract; the underlying source socket stamps
and their targets remain recorded evidence. **`workspot_idle`** reproduces
the idle-only command on the actor's current activity. This is distinct from
the **`workspot_exit`** adapter for stopping an owned activity with an explicit
exit entry and acknowledgement. A consumer must choose the correct entry/action for its
own workspot rather than assume Barry's phase bindings transfer directly.

The source's apartment transform is replaced explicitly. Its movement remains
a specific stand-from-chair clip; it is not a generic walk-away behavior.
Resume locomotion or a new activity through a separate owned handoff.

## Space Oddity: bystanders continue to perform

Resource: `mq003_01_homeless.scene`, section **6**, duration **9,818**.
Source actor IDs are 0, 1, 2 and Player 3. Performer **257** is therefore
Homeless_Fat, not V; performer **513** is Homeless_Suitcase.

At time **0**, Homeless_Fat shrugs in a wall-lean/cigarette posture. At **806**,
the table-leaning NPC looks toward him, then gestures at **2,353**. The smoker
has another talk gesture at **5,443**. Attention and body movement are spread
across participants rather than assigned only to whichever subtitle is active.

Implemented reduction: **`group_side_exchange`** retains those three body clips
and the performer-targeted gaze. It excludes a later static/world-space gaze
event that contains donor-specific coordinates. The two NPC roles are rebound
explicitly; no actor is inferred from a conventional numeric ID. Wall/table
placement, the cigarette and starting poses remain required content setup.

This pattern is useful for a witness, companion or second contact who should
respond during another person's exchange. It is not unrestricted background
gesturing: it is a specific compatible posture combination with known timing.

## Machine Gun: an action clip is only part of prop interaction

Resource: `mq007_01_gun_found.scene`. Section **161** contains a **2,600**
equip clip, section **162** a **2,000** weapon idle, and section **164** a
**400** unequip clip with a socket signal. The named clips are specifically
`stand__equip__skippy__01`, `stand__idle__skippy__01` and
`stand__unequip_skippy__01`.

This is a useful action/hold/exit pattern, but the weapon, player equipment
state and first-person ownership are part of the contract. This pass does
**not** promote it into a generic tablet/drink/handover block. Doing so would
claim portability the source does not establish. A future prop block needs
equipment/attachment setup, contact timing, role/rig compatibility, interruption
before and after commit, and restoration. The existing timed-port support is
the seam for those actions once that closure is reviewed.

## Caller behavior completes the interaction

The earlier [Barry caller study](case-studies.md) records a phase override of
`talkOnReturn: false` and separate main/knock scene calls. The source scene's
default interruption array is not the complete interaction policy. Likewise,
all transplanted performance blocks require community readiness, an entry
posture and an explicit exit/restoration owner.

The implementation compiles into the existing scene spec and can be wrapped
by the existing phase-level owned lifecycle blocks. It does not silently add
community activation, pose setup, navmesh, dialogue progress, reward facts or
a universal interruption state machine. Normal versus interrupted completion
and once-only gameplay commitment remain separate ports/contracts.

## Evidence and promotion boundary

The executable library uses five frozen presets from two manually reviewed
quest scenes, plus three native workspot adapters. The broader all-quest census
remains discovery context, not a claim that every candidate is portable.
The tests compare every selected event against its exact raw pointer and
source hash. The isolated preview checks compiled roles, handles, animation
tables, placement, timing and ports, followed by typed CR2W round-trip
verification. No story source resource is regenerated or installed.

Before promoting a particular content binding, inspect its actual motion and
run approach, obstruction, premature leave, return, normal completion,
interrupted completion and save/load scenarios. Check feet, chair contact,
hands/props, head direction, expression, camera/control ownership and cleanup
as visible behavior. Structural checks and the retained donor timing do not
establish that a new interaction looks natural in game.
