# Making interactions feel physically believable

The follow-up [interaction pattern study](interaction-patterns.md) now traces
concrete vanilla combinations into [reusable scene blocks](../../../../authoring/scene-performance-blocks.md).

The practical target is a character who is already doing something, notices
V, turns or moves naturally into the exchange, reacts while listening, and
returns to an activity afterward. This guide narrows the wider cinematic
study to animation, movement and physical interaction.

## The performance layers

| Layer | What the player sees | Relevant source mechanisms | Review concern |
| --- | --- | --- | --- |
| Background activity | Waiting nervously, working, smoking, checking a phone | Workspot idles, variations and item actions | Repetition, props and suitability for the character |
| Approach and positioning | Walking over, turning, settling at conversation distance | AI movement/splines, world markers and workspot entry | Navmesh, arrival condition, facing and personal space |
| Posture | Leaning, sitting, folded arms, shifting weight | Idle changes, workspot sequences and transitions | Compatible start/end poses and furniture alignment |
| Speech gestures | Shrugs, hand movements, head emphasis | Skeletal animation events and animation-set bindings | Meaningful timing, blending and avoiding a gesture on every line |
| Listening | Looking at the speaker, briefly glancing away, subtle reactions | Look-at, advanced look-at, animation and idle variation | Give the silent actor a performance too |
| Face and voice | Lip movement, expression and emotional response | Dialogue/lipsync bindings, facial animation resources | Mouth synchronization and expression are separate review needs |
| Physical actions | Taking a drink, using a tablet, touching a device | Workspots, prop attachment, equipment operations and IK | Hand contact, prop ownership and exact action milestones |
| Partner choreography | Exchanges requiring both bodies to agree | Synchronized workspot or recorded-performance bindings | Actor roles, alignment and interruption behavior |
| Departure | Turning away, standing up, resuming work or walking off | Workspot exit, gameplay transition and AI handoff | Avoid pose snapping, premature despawn and lingering control |

This is a proposed authoring breakdown. Each behavior needs a compatible
source performance and runtime review; the existence of a named clip is not
proof that it will fit an arbitrary actor or location.

## Workspots are a major existing source of ordinary human behavior

The repository's [workspot guide](../../../../authoring/workspots.md) records
3,881 distinct workspot paths and 11,053 distinct animation names in the initial
local inventory. A workspot can contain an entry, an idle, variations,
reactions, transitions, item actions and an exit. Reusing that coherent
behavior is often a better starting point than selecting an isolated pose.

The available local catalogue contains concrete name-based candidates:

- `stand_bar_lean180__rh_hold_drink__01__shrug__01` appears in the Q004 Judy
  bar-lean/whisky workspot. It is a candidate for a shrug while holding a drink;
  its character/prop/posture requirements must be reviewed before reuse.
- `stand__rh_on_chin__01__phone_check__nervous__01` and `...__02` occur in an
  EP1 standing nervous-wait workspot. These expose authored activity variations
  rather than just a static standing pose.
- `sit_chair_lean0__2h_elbow_on_knees__01` belongs to a nervous seated-wait
  family with look-around, look-left, phone-check and shuffle variations.
- Existing transition entries include standing-to-walking clips with different
  turn directions, and transitions between an arms-at-sides idle and a
  cigarette-holding idle. Entry and exit performances deserve their own
  selection rather than abrupt idle replacement.

These are structural/name findings, not new visual approvals. Broad catalogue
searches also match animation-set dependencies and can return irrelevant
results; inspect the tree's actual animation names and entry roles. For
example, a drink search can find an animal drinking clip. Search terms alone
do not identify suitable human interaction assets.

The existing [preview workflow](../../../../authoring/workspot-captioning.md)
can show decoded body motion and finger articulation on a source-skinned
mannequin. It does not reproduce engine IK, facial expression, furniture,
props, partner synchronization or workspot blending. Use previews to shortlist
motion, then validate the complete interaction in its intended setting.

## Movement should lead into performance

The local [patrol guide](../../../../../modding_docs/modding-guides/quest/how-to-make-npcs-patrol.md)
separates an NPC's preferred route from its workspot stops. The route does not
spawn an actor. Likewise, the repository separates AI spots, community ownership
and scene acquisition. A believable arrival needs both locomotion and a
transition into the selected performance; playing a walking clip does not by
itself establish navigation or arrival.

For each move, author its destination, facing, readiness/arrival condition,
pose entry and fallback if the player obstructs or leaves. For each furniture
interaction, review the chair/table height and orientation as part of the
performance. Foot sliding, hand misses and sudden rotation can undermine a
good clip.

## A concrete Ghostline meeting to aim for

This is an illustrative sequence, not an implemented or tested scene:

1. Iris is already occupied with a tablet, with occasional idle variation.
2. On V's approach, she acknowledges V with gaze before changing posture.
3. She finishes or suspends the activity, lowers/stows the prop using a
   compatible action, and turns or steps into a conversation position.
4. During dialogue, gestures mark selected changes in meaning. While V talks,
   Iris listens and reacts instead of remaining motionless.
5. A significant disclosure can change her posture or attention rather than
   simply triggering another arbitrary hand gesture.
6. If V leaves, the scene has an interruption state. On return, it resumes
   from an appropriate conversational/activity state.
7. At the end, Iris looks away, restores the tablet/activity or walks away
   through a coherent exit. Community cleanup happens under its own policy.

The realism comes from continuity and intention across these transitions.
Sparse, appropriate motion can communicate more than constant gesturing.

## What to prioritize in Ghostline

Start with **activity → acknowledgement → conversation → return to activity**.
That creates a small complete performance with actor readiness, gaze, posture,
one physical action, listening and exit behavior. The current story scene
inventory has dialogue events but no authored skeletal-animation events;
the [project comparison](ghostline-comparison.md) details that boundary.

Then develop reusable posture families—standing, leaning and seated—with
compatible entries/exits, a few gestures, listening reactions and prop rules.
Keep movement and animation milestones explicit so quest actions occur at the
intended physical moment. The [Barry case](case-studies.md) demonstrates timed
section signals into workspot/control logic, and the SQ012/SQ030 cases show
the richer recorded-performance boundary.

For each candidate, record the visible action, start/end posture, locomotion
or root displacement, performer roles, rig/animation sets, required furniture
or props, gesture/body scope, blending, interruptibility and visual/runtime
review status. A searchable catalogue organized by those properties would be
more useful for this goal than scene event counts alone.
