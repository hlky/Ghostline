# Reusable scene performance blocks

These experimental blocks compile into native `.scene` data through
`tools/generate_scene.py`. They implement selected combinations of body
animation, gaze, expression changes, movement placement and timed action
signals from reviewed vanilla source. Their
[source study](../reference/vanilla-quests/deep-dives/cinematic-scenes/interaction-patterns.md)
explains what the source combines and which boundaries remain caller-owned.

The library is frozen under `quests/templates/performances`, with source paths,
SHA-256 hashes and JSON pointers. It does not depend on ignored corpus caches.
Existing specs without `performance_blocks` keep their prior scene output.
This does not change any story quest or install a package.
These are scene-level authoring blocks. Quest manifests continue to call the
generated scene through their existing stage/lifecycle interfaces.

## Available blocks

| Block/preset | Emits | Required setup |
| --- | --- | --- |
| `pose_beat / seated_sad_reply` | Two seated body gestures, gaze and four facial idle transitions | Compatible male_big-derived performance; hands-on-lap seated posture; listener |
| `pose_beat / seated_explanation` | Two explanatory gestures, gaze and a facial idle transition | Same seated posture and compatible body/facial graph |
| `pose_beat / group_side_exchange` | Shrug/talk for a wall-leaning smoker, table gesture and attention from a second NPC | Compatible rigs, cigarette, wall and table posture already established |
| `pose_beat / arrive_and_sit` | Walking-to-chair transition, expression, gaze and three pose corrections | Reviewed chair placement, full root-motion binding and compatible source pose/rig |
| `pose_beat / stand_from_chair` | Standing transition, expression, gaze and idle-only/standing milestones | Correct starting chair pose, full root placement and explicit milestone policy |
| `workspot_move` | Native UseWorkspot command with walking, teleport/instant disabled | Ready community actor, world AI spot/resource, reachable placement and chosen workspot entry |
| `workspot_idle` | Native IdleOnlyMode command on the actor's current activity | Current activity already owned; explicit acknowledgement route |
| `workspot_exit` | Native StopWorkspot command with explicit exit entry | Activity ownership, chosen exit entry/animation, acknowledgement route |

These are specific donor performances, not automatic retargeting. The seated
source uses male_big animation sets; the group source uses different body
types and posture families. Facial idle settings are preserved from the source.
Rig, body shape, facial graph, props and furniture still need review for a new
actor. A CName containing `male` or `female` is not proof of actual compatibility.

## Attach a performance to dialogue

Keep the existing dialogue section, screenplay and localization. Add:

```json
{
  "performance_blocks": [
    {
      "key": "contact_explains",
      "kind": "pose_beat",
      "preset": "seated_explanation",
      "section": "explanation",
      "actors": {"speaker": "contact", "listener": "v"},
      "anchor_line": "contact_explanation_01",
      "start_ms": 0
    }
  ]
}
```

`section` names an existing section key. `anchor_line` must appear exactly once
in that section and in `spoken_line_order`; otherwise it fails. `start_ms` is
a nonnegative offset from that line, or from section start when no anchor is
given. Donor internal timing is preserved and the section grows to fit the
whole beat. No automatic stretching, random gesture selection or trimming is
performed. Align the gesture to the meaning of the new speech during review;
an anchor alone does not make Barry's performance fit another character's line.

Each block has a unique `key`, which contributes to deterministic event IDs.
Every event and nested handle gets a fresh scene identity. Actor IDs and
performer IDs are remapped separately; performer 257 in Space Oddity belongs
to an NPC, while the generated scene reserves it for the real player. The
library preserves the donor role's NPC/player kind rather than blindly copying
numbers. Distinct roles must bind distinct actors.

The compiler imports the exact animation sets needed by the selected body
clips, their animation-name rows, and the actor's matching cinematic-set
grants. Identical resource registrations share one row with merged clip names.
Unrelated donor dialogue,
localization, quest facts, journal effects and world coordinates are excluded.
The first presets deliberately omit standalone head-gesture clips requiring
additional facial-resource investigation; baked facial idle transitions remain.

## Place movement explicitly

Sitting and standing presets require a binding for every role using root motion:

```json
{
  "root_motion": {
    "speaker": {
      "origin": "#my_quest_chair_origin",
      "offset": {
        "$type": "Transform",
        "position": {"$type": "Vector4", "X": 0, "Y": 0, "Z": 0, "W": 0},
        "orientation": {"$type": "Quaternion", "i": 0, "j": 0, "k": 0, "r": 1}
      }
    }
  }
}
```

The zero offset is illustrative, not validated chair placement. The compiler
replaces the source apartment offset; it never carries Barry's furniture
coordinates into another quest. Quaternion and numeric checks catch malformed
bindings, not incorrect physical alignment. The source arm/spine corrections
are retained for review; they are not automatically suitable for another body.

For navigation into an activity, use a separate `workspot_move`:

```json
{
  "key": "walk_to_counter",
  "kind": "workspot_move",
  "node_id": 50,
  "actor": "contact",
  "workspot_ref": "#my_quest_counter_spot",
  "entry_id": 4294967295,
  "is_workspot_infinite": true,
  "on_work_started": [{"node_id": 20}],
  "on_success": []
}
```

Use the scene's existing connection syntax to enter node 50 at executable
input ordinal 1. `Work Started` and `Success` stay distinct native outputs;
the adapter does not replace either with a guessed delay. Choose the source
entry deliberately; `4294967295` is the explicit native unspecified-entry
sentinel, not a discovered entry in every workspot. Infinite workspots need an
explicit retirement owner. This command does not activate the community or
prove pathfinding/arrival. `repeat_on_interrupt` defaults to false and may be
set explicitly for a deliberately repeating command.

## Keep timed milestones visible

`stand_from_chair` exposes `idle_only` at source time 0 and `standing`
at 5,066 within its 5,067-unit section. `arrive_and_sit` exposes `settled` at
4,299 within its 4,300-unit section. These remain section-local stored timing
values; installed scheduling still needs verification.

Every port must have destinations in `on`, or be deliberately named in
`ignore_ports`. Empty destination lists are rejected for named ports. Output
stamps are allocated per target section and retain their event/socket pairing.
For example:

```json
{
  "on": {
    "idle_only": [{"node_id": 80, "input_ordinal": 1}]
  },
  "ignore_ports": ["standing"]
}
```

Here node 80 can be a `workspot_idle` with the actor and an `on_success`
acknowledgement route. It emits source-derived `IdleOnlyMode` / `enableIdleMode`
settings, targeting the current activity through the source's zero workspot
reference. It does not stop the activity or initiate navigation. Native flags
are retained for this mode, including the source's teleport flag; it must not
be interpreted as a walking command. A later `workspot_exit` can stop an owned
world activity using an explicit `workspot_ref` and `exit_entry_id`. An exit can also name
`exit_animation`; the underlying UseWorkspot builder now preserves both exit
fields. Do not choose both the timed milestone and section end to dispatch
the same once-only quest effect without a separate guard.

## Lifecycle composition

The block owns its event data, animation bindings and declared ports. The
surrounding scene/phase owns acquisition, initial pose, navigation, community
readiness, interrupt policy, return entry, workspot release, camera restoration
and eventual cleanup. Keep normal and interrupted exits separate. Use the
existing [owned lifecycle composition](owned-lifecycle-blocks.md) around bound
work/restoration phases when exclusive outcomes and ordered cleanup are needed.

Review these boundaries for each content binding:

1. Community is active and every required actor is acquired before the first beat.
2. The chosen activity can be entered from the actor's actual pose/location.
3. Leaving before arrival or during speech retires the old movement/performance route.
4. Returning chooses a deliberate resume/activity state rather than replaying setup.
5. An action's persistent effect occurs at its intended milestone and only once.
6. Normal and interrupted paths restore activity/control before signalling completion.
7. The NPC leaves or resumes work visibly before departure-owned community cleanup.

The new adapters do not implement a universal interrupt/resume state machine.
That policy remains content-owned, as it does in the inspected vanilla callers.

## Build and verify

The [example spec](../../quests/examples/interaction-performance.scene-spec.json)
is a structural recipe catalogue with placeholder furniture, props and actor
bindings. Its sequential layout is not a proposed playable interaction.

```powershell
py -B tools/build_scene_performance_library.py
py -B tools/generate_scene.py generate --spec quests/examples/interaction-performance.scene-spec.json --dry-run
py -B tools/build_scene_performance_preview.py --deserialize
py -B -m unittest discover -s tests -p test_scene_performance.py -v
```

The example also includes an unconnected exit-adapter configuration as part of
its catalogue. It does not imply that stopping during a standing clip, or
changing directly from a chair into the smoker posture, is a valid production route.

The preview stays under `.tmp/scene-performance-preview`; it is not packed,
registered or installed. Conversion uses the existing typed WolvenKit readback
check. The report records event/resource counts and raw/binary hashes.

Tests check exact donor events against raw pointers/hashes, source identity,
role remapping, placement, milestone ports, timeline anchoring, fresh handles,
resource/name grants and rejection of overlapping full-body performances.
Independent scene validation detects lost resource grants, duplicate handles,
missing timed sockets and out-of-section events. Unsupported fields fail
rather than silently changing playback. These checks establish authoring and
serialization integrity; installed acceptance is still required.

Verification on 2026-10-27: the repository suite passed **1,086 tests**, including
14 performance-block checks. Ruff passed. The composed preview passed CR2W
conversion and typed WolvenKit readback; four existing production specs kept
identical output to the original generator. The library regenerated
byte-identically. Source, implementation and preview hashes are retained in
the [verification receipt](../../reference/quests/deep-dives/interaction-blocks/verification.json).
New actor/furniture bindings have no installed or visual acceptance yet.
