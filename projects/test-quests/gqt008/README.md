# GQT008 — interaction performance lab

An isolated native quest candidate in the floating Building UI layout at
`(140,100,700)`. Barry uses his vanilla character record and appearance with the
reviewed male_big seated performance presets. The story quests are unaffected.

## Build and package

Run from the repository root:

```powershell
py -B projects/test-quests/gqt008/implementation/build.py --deserialize
py -B -m unittest tests.test_interaction_lab -q
py -B tools/package_project.py --project gqt008 --profile gqt008
```

The build publishes editable raw resources and verified binaries into this
project. The packager produces one archive and registration containing the
quest, geometry, navigation, actor world, journal and greeting media. No separate
area package, GQT007 installation, runtime script or diagnostic CET helper is
required. The greeting's frozen donor inputs and hashes live in
`implementation/donors`; builds do not read the current GQT007 project.

The native build batches WolvenKit conversion and readback. Scenes, phases,
localization and the actor world use the shared typed comparison. Building
geometry uses the existing independent ghostline-red verifier for placement,
mesh references, original collision bytes and embedded navigation tile bytes;
the block additionally passes the typed comparison. Publication happens only
after every check succeeds.

This diagnostic uses `implementation/build.py` to compose its owned native
phases. `interaction.composition.json` supplies the journal/localization model;
it is not a generic stage-compiler quest manifest. The scene/world specs and
phase builder together define the runtime contract, covered by
`tests/test_interaction_lab.py`.

`implementation/world/interaction-lab.building.json` is a quest-owned copy of
the saved Building UI sky lab. It retains the floor, walls, desk, two chairs,
paperwork, mug and layer-241 navigation. Its workstation list is empty: this
quest's world spec owns Barry, the chair activity and triggers. The terminal
fixture is deliberately outside this performance test. The geometry exporter
rejects device/community NodeRefs before moving its resource paths into the
GQT008 namespace. The original saved area remains available in Building UI.

## Player walkthrough and choices

Load a test save after installing the candidate and restarting the game. A
convenient CET arrival command is:

```lua
Game.GetTeleportationFacility():Teleport(Game.GetPlayer(), Vector4.new(143,102,701,1), EulerAngles.new(0,0,0))
```

Keep a save from before this quest completes for repeat runs. Restarting the
game does not reset a completed quest or reactivate its terminated root.

1. The root waits until V is within the cleanup volume, activates Barry's
   community and waits for CharacterSpawned. Barry is friendly and invulnerable.
   The journal objective and marker activate; the first restoration scene waits
   for the chair activity's native **Work Started** acknowledgement.
2. Within 5 m of the chair, the owned attempt begins. It pauses the current
   activity with **IdleOnlyMode**, then waits for the 3.5 m inner trigger and
   non-combat state. The first entry plays Barry's vanilla “Who is it?” with
   its original lip animation; returning entries skip that greeting.
3. Choices are diagnostic labels, with these exact routes:

   | Choice | Result |
   | --- | --- |
   | Show a subdued reply. | MQ010 seated reply gestures, gaze and facial idle transitions; return to choices. |
   | Show an explanation. | MQ010 explanation gestures, gaze and facial idle transition; return to choices. |
   | Walk to the waiting mark, then return. | Stop the chair activity through exit 19; walk to the standing spot at `(145,104,700)` with teleport/instant disabled; wait for Work Started, hold 2.5 s, then restore the chair activity. Step outside the inner trigger to rearm. |
   | Go back to your activity. | End the attempt, restore activity, and rearm after V leaves the inner trigger. |
   | Finish the test. | End the attempt, restore activity, succeed the objective and quest, then retain Barry until V leaves the cleanup volume. |

The reaction previews are **silent**, with original donor timing retained.
They test performance layering; they are not new voiced dialogue. The greeting
is the only spoken line. There are no shards, messages, reward grants or story
side effects in this diagnostic quest.

## Ownership and return behavior

The root owns community activation, readiness, protection, activity restoration,
journal completion and departure cleanup. Each attempt child owns the scene and
an independent outside-5-m listener. **Complete**, **Deferred** and **Away** are
terminating outputs: the losing scene/listener branch retires with its child.
The parent waits two simulation ticks before issuing restoration commands.

Explicit deferral starts the outside-inner-trigger listener immediately,
alongside restoration; a native AND join waits for both. A quick step away and
return during restoration is therefore subscribed before that work completes.
The physical Away outcome already observed departure and goes directly to the
setup gate after restoration. It does not require another departure. Both
outcomes set `gqt008_deferred`; the next attempt uses the `resume` scene entry.

Restoration commands walk back to chair entry **2** and wait for **Work Started**,
then turn **IdleOnlyMode off** on the current activity and wait for Success.
The source-shaped IdleOnlyMode command has its native teleport flag, but targets
the current activity with a zero NodeRef; both actual navigation commands have
teleport and instant disabled. This mode command must not be presented as
navigation. Restoration and interrupt behavior remain engine test obligations.

The workspot database confirms the generic chair resource registers
`man_big.rig`, the male_big hands-on-lap animation set, entry-2
`sit_chair__2h_on_lap__01` sequence and exit-19 transition. That establishes a
structural binding, not visual alignment with the office chair. The source
workspot hashes and selected entries are recorded in `evidence/workspot.json`.

The root uses `gqt008_completed` to prevent a newly attached root from replaying
completed work. `gqt008_activity_restored` marks the completion route's native
acknowledgement; `gqt008_cleaned_up` follows community deactivation. These are
graph diagnostics, not claims that a visual result was observed.

## Playtest handoff

Record results against the package ID/hash in `generated/latest-package.json`
and identify the save, existing MQ010 state and installed mods. Do not install
the earlier `ghostline_interaction_lab` area package alongside this candidate:
its separate depot names place another room at the same coordinates. The
original navigation lab at `(100,100,700)` is spatially separate.

| Scenario | Required observation | Status |
| --- | --- | --- |
| First arrival / already inside after load | Solid visible floor; exactly one visible Barry; no speech before readiness/activity acknowledgement. | Pending |
| Idle → reply → explanation | Hands align with chair; gestures blend without full-body snapping; gaze reaches V; facial state changes are plausible. | Pending |
| Walking choice | Exit chair, walk continuously to the waiting mark, hold, walk back; no teleport, desk clipping or stuck workspot. | Pending |
| Leave before greeting | Attempt retires; activity restores; return reaches choices without repeating greeting. | Pending |
| Leave during greeting or either gesture | Old speech/animations stop; restoration completes; no delayed gesture revives after return. | Pending |
| Explicit defer, rapid leave/return | Listener catches departure during restoration; one resumed choice menu appears. | Pending |
| Leave during outward/return movement | Commands retire or are replaced deliberately; no duplicate actor or competing movement. | Pending |
| Finish while inside | Activity restores before journal completion; Barry remains until departure; cleanup fact follows deactivation. | Pending |
| Save/load before engagement, during preview, during restore, after completion | Correct owned branch resumes; no greeting replay after deferral, duplicate actor, duplicate completion or stuck listener. | Pending |

The first unverified boundary is installed game behavior. Native readback,
offline routes, graph checks and package hashes cannot establish these results.

## Verified candidate

Package **gqt008-847b1eb57c8d** contains 19 archive payloads and one ArchiveXL
registration. Archive listing, extraction, byte comparison and ZIP verification
passed. Only GQT008 is registered as an active quest; no numeric resource paths
remain unresolved in the package audit. This candidate is **not installed or
game-tested**.

All **1,091 Python tests** and repository Ruff checks pass. The durable receipt
is `evidence/verification.json`; native/build/package logs are under
`generated/verification-logs`.

ZIP: `generated/packages/gqt008-847b1eb57c8d/Ghostline_GQT008.zip`.

ZIP SHA-256: `a7b171d5b77e1a8492ead4fba4f854884a0760c9b388787858bf10c43b50f4a0`.

Archive SHA-256: `15025aa2ded3e03557d5bf99fe553a451df3429901f74044c7b2cb477c46cbc5`.
