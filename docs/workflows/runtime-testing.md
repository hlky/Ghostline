# Runtime Testing And Evidence

Recorded installations and scoped evidence follow. Installation evidence does
not imply that later working-tree changes have been tested in game.

Use a fresh save when validating questphase, scene, journal, or world-trigger
changes. Prefer a manual save made before any version of Ghostline was
installed or registered.

## Playtest handoff contract

For each candidate, name the package/profile and installed hash receipt,
the behavior changed, the suitable starting save, the exact action to test,
and the expected visible result. Explain restart requirements and persisted
state: an archive replacement cannot reset facts, visited journals, saved
controllers, or a scene already in progress. Use a pre-registration save for
new lifecycle proof; use an affected existing save deliberately for migration
or repair tests. Do not require a full replay when a focused save is sufficient.

Include applicable transition scenarios early:

| Scenario | Check |
| --- | --- |
| Fast travel inside setup | The already-inside player can start the conversation. |
| Defer, step away briefly, return | Choices or a return exchange reappear without repeating the full introduction. |
| Kill guards or approach quietly | Progression follows the intended combat/stealth policy. |
| Interrupt and retry the link | No false commit, stuck prompt, or duplicate reward. |
| Successful link and unplug | HUD completes once, without a late failure; next objective activates. |
| Leave while dialogue plays | The later departure gate accepts an already-outside player. |
| First remote line | Speaker readiness preserves its setup for the player's reply. |
| Read shards in sequence | Grants, read objectives, comments, and upload instructions match player knowledge. |
| Receive reward and finish | Inventory confirms delivery; journal completes independently of optional messages. |
| Finish beside the NPC | NPC remains until the intended departure cleanup. |

Record observed outcomes separately from authoring/readback and package tests.
For a regression, compare the previous working build and distinguish observed
facts from a proposed cause. Include presentation checks from the
[item guide](../authoring/items-and-equipment.md#quest-rewards-and-custom-quickhacks).

## GQ004 completed playthrough (2026-10-25)

The user confirmed the final `love-actually-736fbdd18ed4` package was all good
and reported a complete playthrough of about ten minutes including driving.
See its [playtest route](../../projects/ghostline/quests/gq004/implementation/PLAYTEST.md),
[installed hashes](../../projects/ghostline/quests/gq004/implementation/install-receipt.json),
and [retrospective](../../projects/ghostline/quests/gq004/RETROSPECTIVE.md).
That confirmation does not establish exhaustive save/load, both-V-voice, or
every stealth/combat scenario coverage. The optional link diagnostic loader and
update hook were subsequently disabled; the location chooser and logs remain.

## Isolated Story Project Install (2026-10-07)

### Delayed follow-up and restored local autosave settings

The GQ002 offer now follows `gq001_completed > 0` with a separate
`questGameTimeDelay_ConditionType` pause condition: zero days, 12 hours,
zero minutes, zero seconds. The timer starts after completion, and neither
the message nor its reply choices can activate while either gate is pending.
This follows the completion-then-game-time-delay pattern documented in
`modding_docs/modding-guides/quest/how-to-add-new-text-messages-thread-to-cyberpunk-2077.md`;
the vanilla `sq011_follow_up.questphase` also uses the same condition type.

Installed candidate: `projects/ghostline/generated/packages/story-8089469b907f`.
The archive SHA-256 is
`9baeb18c2629caa53070c8d96bf13d6bd32d60fb1e7088b2e35bd78912942cee`.
All 174 archive payloads and ZIP entries match their frozen inputs, and all
seven story install files match the verified candidate. The project gate
passes 753 Python tests, Ruff, and seven Rust voice-tool tests. Cooked typed
readback verifies the completion gate, timer values, and graph connections.

At the user's request, the local `engine/config/base/user.ini` setting
`AutoSaveEnabled = false` and
`r6/scripts/Tduality/autosave_is_Not_included.reds` were restored separately
from the story release profile. The latter suppresses vendor/ripperdoc
leave-scenario autosaves. Both installed files match their authored resources;
the earlier `.disabled-story-20261007-185644` backups remain preserved.
The story installer does not delete these separately installed settings.

The subsequent Iris screenshots show an intact head during speech, with a
reported faint mark near the forehead that appears/disappears as her head
turns. Cooked appearance readback preserves the authored skinning and parent
bindings. Every bone referenced by the head, facial-cyberware, and personal-link
meshes exists in Iris's facial rig. No detached binding or missing bone was
identified; the images cannot distinguish minor hair/cyberware surface clipping
from a rendering artifact. Iris's appearance remains unchanged.

The install receipt, previous-install backup, autosave restoration receipt,
Iris investigation, and conversion/test logs are under
`projects/ghostline/generated/runtime-followup-20261007`. Restart the game to
apply the package and autosave settings. Validate that GQ002's text arrives
only after GQ001 completes and another 12 game hours elapse. This timer has
not yet been observed in game; it cannot retract a previously delivered text.

### Playback repair after in-game feedback

The first isolated install sent both quest offers immediately. The supplied
in-game screenshots also showed Patch bowing his head with an offset cigarette
and Iris's head mesh stretching severely during her opening line.

The repair gates GQ002's initial phone message on `gq001_completed > 0`, before
any message or choice is activated. That fact is set by GQ001's final delivery
phase after the Morrow response and reward. Patch now uses
`generic__stand_ground__wait__01.workspot`, without a cigarette prop, and every
dialogue section has a look-at event targeting V's camera slot.

The previous lipsync duration repair stripped required constant skeletal
references. Successful import, clip-name matching, and duration matching did
not detect this defect. All 36 Patch/Iris/Cinder clips were rebuilt with a
complete neutral additive reference: 344 joints, 1,031 constant skeletal keys,
and two neutral translation keys carrying the WAV duration. Independent
WolvenKit readback confirms unchanged facial keys, durations within 50 ms, and
skeletal rest values within `6.1e-7` of the rig reference. Iris's player-head
rig and the female lipsync donor have identical bone and facial-track ordering.
The compiler now defaults to this complete neutral-reference policy, including
reconstructing channels lost by an earlier stripped import. The three editable
raw CR2W companions also pass WolvenKit import/readback verification.

The repaired package is
`projects/ghostline/generated/packages/story-66af954da806`, with 174 archive
payloads and seven install files. Archive and ZIP extraction match the frozen
inputs; all seven installed files match the verified candidate. The installed
archive SHA-256 is
`faa4bbf18bffee19f013bde0bcfa74722d60c2051621f618d36f9029bf3f50ba`.
Audit logs, per-clip evidence, the install receipt, and the previous installation
backup are under `projects/ghostline/generated/runtime-repair-20261007`.

The repaired project passes 751 Python tests, Ruff, and seven Rust voice-tool
tests. The GQ002 gate, Patch scene, and exact world-resource path replacement
pass cooked typed readback. The repaired package has **not yet been tested in
game**. Restart the game and use a pre-Ghostline save to verify that only the
GQ001 offer arrives initially, GQ002 unlocks after GQ001 completes, Patch faces
V naturally, and Iris/Cinder speak without mesh deformation. Offers already
delivered by the previous build persist in saved journal state.

### Original isolated install (superseded)

Generated the GQ001/GQ002 questphases, dialogue, localization and world assets,
converted all 36 reviewed WAVs to WEMs, and installed the `ghostline` project's
`story` profile with its declared shared runtime dependency. The package has
174 archive payloads and seven install files. Archive extraction and ZIP
extraction match the staged source by SHA-256; all installed files match the
verified candidate. Only GQ001 and GQ002 are registered as active quest roots.

The installed `Ghostline.archive` SHA-256 is
`dbb4a4d84d4887fc1bec5c64a2f2eca907bf49ebda804ce3a170dda7b2059602`.
The candidate and extraction evidence are in
`projects/ghostline/generated/packages/story-3148ef93931c`. The install receipt,
lipsync audit, conversion logs and previous installation backup are in
`projects/ghostline/generated/story-install`. Ten previous repo-owned test and
development loose files were verified against their source and preserved with
`.disabled-story-20261007-185644` suffixes.

GQ001 uses all 13 Patch and 12 Iris clips. Nine missing Patch clips were added;
both NPC and V voice tags now appear in each meeting's lipmap. Cooked scene
readback preserves the custom NPC voice tags and both voice variants select
explicit clip names. Iris and Cinder clips were reimported without inherited
donor skeleton animation, which had stretched short clips to the donor's
duration. WolvenKit exports confirm all 36 story clips have facial keys and
match their reviewed WAV durations within 50 ms.

The project gate passes 747 Python tests, Ruff, and seven Rust voice-tool tests.
These checks establish cooked asset and installation integrity. In-game
dialogue playback has not been tested; validate the story on a fresh save.

The native `ghostline-red` writer now synthesizes missing reflected nested
properties, preserving custom scene voice tags, and grows lipmap value arrays,
including voice tags, animset references and scene entries. Regression tests
cover populated and empty arrays, nested 64-bit tags, and unsupported growth.
Independent WolvenKit readback verifies the two story scenes, three lipmaps,
and an additional expanded lipmap against their authored values. Unsupported
empty handle arrays still require a compatible export template. Scene builds
retain semantic verification and WolvenKit fallback before publishing assets.

## Previous GQ001/GQ002 Lipsync Install (2026-08-27)

Packed and installed the current full `source/archive` tree with WolvenKit.
The verified candidate and extracted payload evidence are retained at
`H:\projects\Ghostline\.tmp\package\manual-20260827-073206`.

The archive contains 505 payloads. Every extracted file matches the
corresponding `source/archive` file by length and SHA-256. The installed
`H:\Cyberpunk 2077\archive\pc\mod\Ghostline.archive` is byte-identical to the
candidate; its SHA-256 is
`B5DA77A93B1DBBD367DE0C1D376FEF6FC36574A9CE255F61D4810AB6F289FD0F`.
The 17-file install includes the archive, `Ghostline.archive.xl`, all current
Ghostline TweakXL YAML files, and the existing test-time autosave suppression
resources.

The installed archive explicitly contains the gq001/gq002 meeting scenes,
lipmaps, and localized female-average lipsync animsets. The focused lipsync
suite passes 11 tests, both scene audits and validators pass, and both
subtitle/VO maps remain aligned. The previously enabled standalone
`Goth_Baddie` archive, ArchiveXL file, and three TweakXL files were preserved
with timestamped `.disabled-manual-20260827-073206` suffixes to prevent their
gqt006 resources from competing with the full Ghostline install.

## Earlier Evidence

The [dated runtime evidence archive](../history/runtime-testing-through-2026-08-12.md)
preserves prior candidates, hashes, failures and test outcomes. These historical
records do not establish runtime validation for later authoring changes.

## Current Authoring Verification

The September maintainability fixes are tracked in the
[review and completion record](../reviews/2026-09-05-maintainability-review.md).
Automated checks and archive extraction establish authoring/package integrity;
new in-game evidence must be recorded separately after a focused runtime test.


## Building Lab motel NPC traversal (2026-10-26)

The user observed a spawned NPC walk successfully after selecting **Teleport V
to start** again, then **Walk NPC to end**. The record entered earlier was
`Character.Judy`; the runtime report does not independently record actor identity.
The captured report confirms the ground workshop to upper workshop route:
native endpoint query passed, physical NPC movement passed, 24.05 m travelled
in 19.42 seconds, 185 position samples, and no detected teleport jumps.
This establishes one in-game upstairs traversal, not validation of every kit,
door state, reverse route, or shell retrofit.

Evidence and installed-file hashes are retained under
`projects/experiments/building-lab/generated/runtime-evidence/20261026-083809-motel-walk`.
The installed archive SHA-256 is
`3807ffd27d757565137bb9181c36eb429121d92881fb5052b993a911463ee341`,
from verified package `building-lab-test-2ea3cdfe3711`. A spawn-status-only Lua
update had been installed during the running session; whether it had been
reloaded before this observation is unknown. The recorded helper hash describes
the file on disk, not proof of which Lua revision was loaded. The earlier
"wait for NPC to assemble" label was static and did not establish spawn failure.
Repeating player staging preceded success, but the cause of that dependency
has not yet been isolated.


### Motel geometry corrections after screenshot review

The user supplied four screenshots showing an invisible shared-wall back in
service, flicker beside the upper stair landing, an open horizontal band between
storeys, and exposed stair undersides. The builder now adds the opposite
shared-wall facing, closes the storey slab band, clips rising guards below the
continuous upper guards, and constructs closed concrete stair/guard bodies with
thin floor caps. Generated box caps normalize the vanilla floor's 2.5 mm lip.
The browser preview renders structural bodies even with room ceilings hidden.

Package `building-lab-test-8bbb841a3710` passed native serialization/readback,
archive extraction and payload/ZIP hash verification. All 41 building tests
pass, including shared facing alignment, slab continuity, nonoverlapping guard
volumes, and stair body/cap continuity. The navigation sector is byte-identical
to the one used for the successful NPC walk. The candidate contains 241 mesh
placements and 173 collision boxes. The archive SHA-256 is
`9dbcf6d37aae5d49d86e7537df0e2985d095f039f665b08be5e273970f0eb2b7`.
All four installed files match the verified stage; installation occurred with
Cyberpunk closed. Receipt and previous-file backups:
`projects/experiments/building-lab/generated/runtime-installs/20261026-084546-geometry-fix`.
Screenshots, offline preview and correction evidence:
`projects/experiments/building-lab/generated/motel-geometry-fix/evidence`.
Restart/load the test save and revisit all four views, check door reveals, then
repeat both stair directions. These visual corrections still need in-game
verification; the earlier NPC walk proves only the previous installed geometry.


### Workshop/service query failure and remaining stair seams

The user reports other start/end pairs work, but Ground workshop to Ground
service returns no path. Captured report at 2026-10-26 08:58:28 UTC has both
endpoint statuses OK, NPC owner, and an empty path. The user separately confirms
V can open and cross the automatic door. This is not a successful NPC door test.
Vanilla navigation metadata from `navigation_-1_-1_0_3.streamingsector` confirms
the generated Door area 10, flags 3, bidirectionality 1, matching global-node
IDs and base worldOffMeshUserData shape; no proven metadata error was found.

The CET harness had refused to send any movement command after a failed direct
query. It now allows normal AI navigation commands when both endpoint samples
are valid, retains the failed query separately, and records door PS state and
component availability. A Lua callback regression exercises empty query results,
continuous observed arrival, separate pass flags, and rejection of missing
endpoints. This does not establish that an NPC can cross the door in game.

The two new stair screenshots show slab/guard face overlap at the shaft edge.
Floor and ceiling rectangles now terminate at the guards' exterior faces. This
removes positive-volume overlap instead of moving coincident faces slightly.
The same native navigation binary is retained. All 42 building tests pass,
including slab/guard overlap rejection; native readback and package verification
pass. Installed candidate: `building-lab-test-abffe0db6f1e`; archive SHA-256:
`e8f306bc2b3e4616ff639691d811097b6e2cb2232ff6f5301237808191ad72da`.
Game was closed for installation; all four installed files match the stage.
Receipt/backups: `projects/experiments/building-lab/generated/runtime-installs/20261026-091434-door-seam`.
Evidence, screenshots, failed report and callback regression:
`projects/experiments/building-lab/generated/door-seam-fix/evidence`.
Retest Ground workshop to Ground service with Teleport V to start, Bring NPC to
start, then Walk NPC to end. The command may now be attempted despite the direct
query failing. Recheck both pictured shaft seams. Door movement and seam changes
remain pending in-game verification.


### Door jump rejection and absolute NodeRef correction

The user saw Judy teleport into service after the diagnostic failed-query walk.
The report at 2026-10-26 09:21:33 UTC confirms `native_query_passed=false`,
`command_accepted=true`, `teleport_detected=true`, and
`npc_movement_passed=false`: a single sample jumped 7.572 m in 0.1083 s.
The helper issued an AIMoveToCommand with navigation enabled, not an explicit
teleport to the destination. The exact engine/actor fallback causing the jump
has not been isolated. Door diagnostics show both custom aliases resolved to
zero, so no device PS state was available through those references.

The local NodeRef documentation requires registering absolute `$/` paths before
using aliases. Building Lab incorrectly registered bare `#building_...` aliases.
Door and entrance references now use `$/03_night_city/#building_...` throughout
sector registration, placement hashes, device registry and navigation link IDs.
The complete-path gate is restored now that the diagnostic attempt has shown
an engine jump. Teleport failures have an explicit message, and departure is
sampled before SendCommand to catch even synchronous engine relocation.

All 44 building tests pass, including an executable Lua callback regression
covering failed-path refusal, ordinary observed motion and synchronous jump
rejection. Native serialization/readback, package extraction/hash verification
and unlocked/locked adapted-Detour controls pass. None proves the corrected
reference binding works in game. Installed candidate:
`building-lab-test-789960e9eda8`; archive SHA-256:
`07664d7524e2818e895b477e2ecea688066122ef80fac7d2f126c85c86ad283c`.
Receipt/backups: `projects/experiments/building-lab/generated/runtime-installs/20261026-092754-door-references`.
Failed runtime evidence: `projects/experiments/building-lab/generated/runtime-evidence/20261026-092231-door-teleport`.
New offline evidence: `projects/experiments/building-lab/generated/door-reference-fix/evidence`.
The game was closed for installation and all four files match the verified stage.
Restart and retry workshop/service. First require a complete native query, then
normal observed movement through the door; nonzero reference resolution alone
is not NPC traversal proof. New absolute-path IDs change the door identities,
so previous saved controller state does not establish this candidate's state.


### Door references resolve; path still absent; bounds-tree candidate

The next runtime report (2026-10-26 09:31:17 UTC) confirms both door references
now resolve to their expected full-path hashes. Both entities and their off-mesh
components exist; automatic door PS is powered, closed, unlocked, unsealed,
not disabled and not unpowered. Both endpoint samples are valid but the NPC-owned
direct query still returns an empty path. Absolute-reference correction therefore
fixed a real binding defect but did not establish the complete route.

Compared a vanilla Human tile containing a Door polygon against the generated
tile. Vanilla has a quantized BV tree (2N slots); the previous generator omitted
it because upstream Detour has a linear-search fallback. The game has not been
shown to use that fallback for off-mesh attachment. The new candidate generates
the bounds tree using VAND X/Z/Y axes, quantization 10, preorder subdivision,
negative subtree escape indices and final padding. This is a concrete format
alignment, not a proven explanation of the game failure.

All 45 building tests pass, including per-polygon BV coverage and escape-tree
traversal. Independent Detour controls allow the unlocked door and stairs and
reject the locked door with the new tree. All 15 room presets / 60 native
resources pass independent serialization/readback. The CET harness also records
an independent AI StartPathfinding/GetResult query, plus resolved connection IDs
and component bindings. The secondary API's live result remains untested.

Installed candidate `building-lab-test-0d5df1d91dcb`; archive SHA-256:
`554abc51bdb596218c782a488067e7596a004a278fc9ca5fab348d89a84f148c`.
Receipt/backups: `projects/experiments/building-lab/generated/runtime-installs/20261026-093913-door-bv`.
Failed report and new offline evidence:
`projects/experiments/building-lab/generated/door-bv-fix/evidence`.
All four installed files match the verified stage; game closed for installation.
Restart and query workshop/service, allowing three unpaused seconds for the
secondary query. Only attempt the walk if the direct native path passes.


## Rancho side-bay retrofit install (2026-10-26)

The user reports the motel route works after the BV-tree candidate. The retained
report contains a complete direct path through the door from Ground service to
main stairs top; it was captured while movement was pending, so it is not a
finalized sampled NPC movement pass. The secondary AI query reports failure
while the direct query succeeds; it remains diagnostic and does not override
the direct result or physical observation.

Installed `building-lab-test-d1eeb1688c60` from
`projects/experiments/building-lab/generated/rancho-retrofit/generated/packages-final`.
Archive SHA-256:
`751bea8f8c3592b69fd7ad31c8df51c8abdaa91b03b319701c8a6587d4744fd2`.
All four installed files match the verified stage. Game was closed. Previous
motel files and last report are backed up under
`projects/experiments/building-lab/generated/runtime-installs/20261026-101604-rancho`.
The installed ArchiveXL 1.27.0 satisfies the actor/instance deletion requirement.

The original front-bay candidate has a second low barrier in its approach.
The first active test instead uses side instance 3 of placement 530 in
`exterior_-11_-23_0_0`, and wall actor 118/shape 0 of placement 850 in
`exterior_-2_-3_0_3`. One blocking stand generator is also cleared: static
placement 427 and two-shape collision actor 48 of placement 1377 in
`exterior_-6_-12_0_1`. Full source SHA-256, placement/actor/instance counts,
resource identity, poses and collision bytes were verified against fresh reads
of the installed archive/pc set. The base-content-only collision sector has a
different placement count and index; the full installed set matches the
surveyed 872-placement version. No unrelated game files were replaced.

The build adds an 18 mÃ‚Â² lined room, a ceiling at 3.5 m below the retained roof,
a brick exterior doorway frame and automatic native door. Explicit door
endpoints put the owned tile's inside attachment first and connect the surveyed
street point. A short Regular/Floor off-mesh link joins the retained interior
layer 0 to the custom layer 200. Floor links now use Regular area 3; area 12
means Jump and was incorrectly used by the earlier generic entrance writer.
Both destination-surface selections are exercised by the offline controls.

47 building tests, native resource readback, package extraction/hash checks and
unlocked/locked Detour controls pass. The 0.3 m radius entrance corridor's
intersecting primitive boxes are exactly the selected wall and generator.
No live retrofit result is claimed. Evidence is under
`projects/experiments/building-lab/generated/rancho-retrofit/evidence`.

Playtest: load a city save, select Street approach -> Rancho interior, teleport
V to start and first walk through as V. Then bind/spawn an NPC, bring it to
start, query, and walk if the query passes; reverse afterwards. Watch doorway
alignment, floor/ceiling seams, neighbouring walls, occlusion, distance streaming
and save/load. Do not use a save inside the now-replaced floating motel lab.


### Rancho original-door revision â€” 2026-10-26 10:35 UTC

User screenshots show the side sliding leaf extending beyond the brick corner
and an offset frame; the original long-faÃ§ade white fake door remains. That
side proposal is superseded. The active layout restores its side wall and
generator and replaces the original static white leaf/casing with vanilla
`single_door_hinged.ent` / `doors_single_hinged_h`. This uses matching vanilla
meshes, aligns the casing to the surveyed original frame, and uses the stock
+90 degree inward swing. Selected old casing/door-bay collision is replaced by
generated jambs/header plus the native physical casing and leaf. A 2.5 m
collision lintel clears the measured 2.455 m top of the native leaf.

Candidate `building-lab-test-2a1e5f3733ea` passed 48 building tests, Ruff, JS syntax,
four-resource native readback, package extraction and payload/ZIP hash checks.
Eight offline Detour controls cover inbound/outbound, unlocked/locked and both
interior-layer selections; unlocked succeeds, locked fails as intended.
Evidence: `projects/experiments/building-lab/generated/rancho-original-door/evidence`.
Installed four hash-verified payloads with Cyberpunk closed; archive SHA-256
`9f74c47781b53f5767a4ac87f20259dcddba12c42f829ddd1b4fd44dadd381a8`.
Receipt and prior files:
`projects/experiments/building-lab/generated/runtime-installs/20261026-103519-rancho-original-door`.

Playtest the existing white door, using updated Street approach -> Rancho
interior. First V in/out and closed/open alignment, then NPC query and observed
walk in both directions. Visual fit, physical crossing, occlusion/streaming and
native NPC interaction are not yet verified in game for this revision.


### Rancho fake-leaf collision fix — 2026-10-26 10:43 UTC

User reports the native hinged door opens but V cannot walk through. A full
primitive-box sweep of the entrance identifies retained static fake-leaf
collision: placement 850, actor 123, shape 0 in
`exterior_-2_-3_0_3.streamingsector`. Local bounds are
X [-2.2541, -0.7530], Y [-3.1133, -3.0147], Z [0.0300, 2.4700],
covering the open entrance. The prior casing actor 17 and door-bay actor 124
selections did not include this independent fixed box. The layout now deletes
that precise actor/shape pair; no whole collision node is removed.

48 building tests, Ruff, four-resource native readback and verified package
extraction/hashes pass. Candidate `building-lab-test-b72cb3881408` installed
with the game closed; all four payloads rehashed. Archive SHA-256:
`b286bc975daf6178674462ac3bcbc58f4a13fbec069fc1f145ae10684ecab4e8`.
Evidence, pinned actor/shape records and screenshots:
`projects/experiments/building-lab/generated/rancho-door-collision/evidence`.
Backup/receipt: `projects/experiments/building-lab/generated/runtime-installs/20261026-104335-rancho-door-collision`.
Retest V crossing first, then NPC query and observed crossing both directions;
no successful runtime crossing is claimed for this revision.


### Rancho residential house — installed 2026-10-26 11:32 UTC

User authorized proceeding with the surveyed larger house. Authored layout:
`projects/experiments/building-lab/buildings/rancho-residential-house.building.json`.
First playable ground floor is 180 m², eight unfurnished rooms, seven hinged
doors, eight warm point lights. Original porch/steps, roof and balcony remain.
Upper-floor and rear exterior routes are outside this test.

Replaces sealed decorative door placement 212 in `exterior_0_-34_0_0` and
proxy placement 98 in `exterior_0_-17_0_1` (owner 15517176256055994014).
No static shell collision is deleted. Porch/steps are measured from vanilla
geometry; four nav triangles and a Floor link connect to the surveyed street.
Indexed feature screening found no gameplay feature in the estimated interior;
nearby ambient occupants remain. Door identity search found its decorative
entity/proxy pair rather than quest-owned door wiring.

A real overlap failure appeared during full room validation: vanilla terrain
under the house could win nearest-poly queries and bypass the front door.
The final candidate replaces only Human navigation placement 2 in
`navigation_0_-9_0_3` with a mod-owned copy of `navigation_0_-14_0.navmesh`.
All 25 buffers/topology/metadata are retained; only 43 fully enclosed terrain
polygons have flags disabled. Byte-diff guards prove all other bytes identical.
The full copied resource receives its own complete streaming bounds. Vehicle
navigation stays in the original sector. Installed archive-index inspection
found an expansion override; final sources were freshly extracted/serialized
from `ep1_1_nightcity.archive`, superseding the earlier base-content candidate.

51 building tests, Ruff, five-resource native readback, payload/ZIP extraction
hash checks, and 64 offline street/room route controls pass. Controls cover
every room in both directions, both tile load orders and locked/unlocked entry.
Candidate: `building-lab-test-a905553b5a96` under
`projects/experiments/building-lab/generated/residential-house/generated/packages-ep1`.
Archive SHA-256: `1353de660313224d7ac1064257dc12341edc6fd7bcff24e17797acf739ce19cc`.
Installed four rehashed payloads with Cyberpunk closed; prior retrofit/report
backed up under
`projects/experiments/building-lab/generated/runtime-installs/20261026-113218-residential-house`.
Evidence is `projects/experiments/building-lab/generated/residential-house/evidence`.

Handoff: relaunch, city save, Street approach to Entrance hall, Teleport V to
start. First test V up the steps, through the front door and all rooms. Then
query and observe an NPC walk to hall and each room, both directions. Prioritize
rear bedroom, utility and study. Check original navigation replacement in
ArchiveXL logs, proxies/occlusion, collision, light levels, door swings and
save/load/distance streaming. No live V or NPC pass is claimed for this build.


### Rancho house visual correction — installed 2026-10-26 12:01 UTC

User confirmed NPC walking works. Preserved runtime report independently records
Street approach → Bathroom: native query and observed traversal passed,
teleport_detected=false, 15.44 m in 14.12 seconds, observed 11:50:52 UTC.
Evidence and five supplied screenshots are under
`projects/experiments/building-lab/generated/residential-house/evidence/playtest-20261026`.
This confirms that recorded route on the preceding candidate, not every room
or the new revision's live behaviour.

Camera-dependent disappearance on approach and in rooms matches retained
vanilla occlusion. Decoded the instanced occluder appendix using WolvenKit's
one-byte count + 64-byte matrices format. Three complete groups belong only
to this house: placement 425 / three matrices in `exterior_0_-17_0_1`,
524 / two in `exterior_0_-5_0_3`, and 571 / three in `exterior_0_-9_0_2`.
Exact surveyed source hashes, expected node/instance counts and whole-group
acknowledgements guard their ArchiveXL removals. Neighbouring-house groups
remain unchanged. The installed ArchiveXL source handles these as dummy-node
replacements; individual occluder matrix deletion is unsupported. Audit:
`projects/experiments/building-lab/surveys/rancho-residential-house-occlusion.json`.

Shared door casings now sit at the wall volume centre; the house front door
has the matching surveyed 8.75 cm inward offset. The 26 cm deep native casing
spans both faces of the 17.5 cm wall. All seven house casings are covered by
geometry regression checks. Collision solids and door navigation endpoints
are preserved; both navigation resource binaries are byte-identical.

Candidate `building-lab-test-a3f424928a7f`:
`projects/experiments/building-lab/generated/residential-house-visual-fix/generated/packages`.
Archive SHA-256: `c7805a62c0dad7219f551d452d3bd48951187fe1a9f71a1ad3832793067871f7`.
53 building tests, Ruff, five native resource readbacks, package extraction/hash
checks and all 64 bidirectional/load-order/door-lock route controls passed.
Installed four rehashed payloads with Cyberpunk closed; previous payloads and
runtime report backed up under
`projects/experiments/building-lab/generated/runtime-installs/20261026-120133-house-visual-fix`.
Local Building Lab server restarted to load the corrected compiler.

Handoff: relaunch and load the city test save. Approach the front door from
outside, pause at the threshold, enter every room, and pan/turn at the supplied
problem angles. Check door-frame seams from both sides and door crossings.
Repeat one NPC route to check the shifted physical doors; do not infer the
visual result from offline controls. Save/load and distance streaming remain
live checks.


### Rancho house stairs, upper floor and windows — installed 2026-10-26 12:26 UTC

User confirmed the occlusion correction, then reported doorway join lines and
a low roof edge inside the rear bedroom. User requested stairs/upstairs rooms
and windows, and explicitly preferred correcting the room footprint over
hiding the intrusion with a lower ceiling.

Authored plan now has 12 rooms / 225 m²: 171 m² ground, 54 m² upper. Storey
rise is surveyed 4.0 m. Rear bedroom moved to X=6..9, Y=-12..-6; the measured
roof edge 125 reaches only X=3.978, so the 3.5 m ceiling remains. New 1.2 m
stairs rise 4 m over 6 m with 1.5 m landings. Side corridor is separate from
flight/guards. Exact rectangular slab subtraction handles a shaft inside a
3 m tile; continuous room containment and native route checks cover it.
Plain plaster door surrounds replace the stock doorway trim in this layout.

Ground Utility and Upstairs bedroom windows retain blocking glass/wall
collision. A mod-owned Rancho mesh clone uses a real glass material instead
of the vanilla fake-room parallax slot; no global material override. Original
geometry export compares exactly (501 vertices, 458 triangles), and native
readback preserves render-buffer bytes and material assignments. Source facade
render replacements are pinned to placement 399 instance 1 and placement 387
instances 6/7 in `exterior_0_-17_-1_1`; other instances stay. Precise survey:
`projects/experiments/building-lab/surveys/rancho-residential-house-upstairs.json`.

55 Building Lab tests, Ruff, six native resource readbacks and 112 offline
controls pass. Routes include street ↔ all rooms and foot/top stair points,
locked/unlocked front door and both tile load orders. Windows keep full
collision, so no nav aperture is cut there. WolvenKit packed and extracted the
archive; every archive/ZIP/install payload hash passed.

Candidate `building-lab-test-95a71d2619cb` under
`projects/experiments/building-lab/generated/residential-house-upstairs/generated/packages`.
Archive SHA-256: `af9e944f73ed4b88c93dd08cee139306fc07dcb5a0ff2b756ef434a44d6387cc`.
Four payloads installed with the game closed; prior package and runtime report:
`projects/experiments/building-lab/generated/runtime-installs/20261026-122603-house-upstairs`.
Local editor restarted. Current evidence contains two supplied screenshots,
window geometry export and full offline control results. Runtime behaviour
of this revision remains unverified.

Handoff: relaunch, city save, Street approach → Upstairs bedroom. Test as V
first, including rear bedroom roof clearance, join lines, two window views,
side corridor, stair headroom and landings. Then Bring NPC to start, query,
and observe the walk. Swap start/end and repeat downwards. Foot/top stair
points isolate the flight; Upstairs bathroom is also selectable. Inspect
physical movement rather than treating a successful query as traversal proof.

### Rancho house access revision — installed 2026-10-26 13:23 UTC

User's exterior survey revealed the garage, rear porch door and wraparound
balcony. Previous live feedback identified an awkward stair arrangement,
upstairs floor flicker, a support through the landing wall, and NPC steering
through the open front door leaf. The earlier NPC walk confirms basic movement
only; it is not a clean physical-clearance pass.

Current candidate `building-lab-test-d1bce9cb9d42` is under
`projects/experiments/building-lab/generated/residential-house-access/generated/packages`.
Four payloads installed and hash checked with the game closed. Previous files
and runtime report are backed up under
`projects/experiments/building-lab/generated/runtime-installs/20261026-132337-house-access`.
Archive SHA-256: `8348a6d7e800b2e3d50b1567c01c8aade29f6f225e603b6d8da67aa9c02a2fea`.

Plan: 14 rooms / 287 m², two storeys. Fixed-open garage workshop bay with
0.6 m physical step-up into the Living room; actual rear porch entrance and
vestibule; upstairs lounge and native balcony side door. Three exact clutter
placements/collision shapes cleared from the retained balcony. Stairs reverse
with matching risers, navigation, guards and foot/top probes. Exact native
roof support instance 414/1 and its collision are replaced by a shortened
piece ending before the lining. Wall caps/foundations and floor mesh lips
remove overlapping upper-floor faces. Open hinged leaf footprints reserve
0.3 m agent clearance on floors and garage landing.

58 tests, Ruff and six native resource readbacks pass. WolvenKit packed and
extracted the archive; ZIP/install hashes match. All 176 adapted-Detour controls
pass with both load orders, both directions and sealed-house negative controls.
The retained rear porch originally had an overlapping native polygon 0.17 m
too high; a 51-polygon flag-only mask resolves that snap while preserving all
25 native buffers. No new live pass is claimed.

Next: V through all three ground entrances, upstairs and full balcony, then
NPC Street approach ↔ Garage workshop / Rear vestibule / Upstairs lounge /
Balcony front. Observe front leaf avoidance and reverse the stairs route.
Inspect upstairs floor flicker, landing support, door casing alignment and
balcony floor/rail/clutter clearance. The barrel keepout is approximate.
Survey and ten screenshot hashes:
`projects/experiments/building-lab/surveys/rancho-residential-house-access.json`.

### Rancho floor-plan and garage revision — installed 2026-10-26 13:52 UTC

User reported a wrong garage aperture, implausible small-room arrangement,
rear entry facing an internal door and awkward stairs. The garage source
frame is scaled roughly 4.4 m wide; the previous 3 m infill was the error.
The new 4.3 m lining uses a scaled native automatic w300_h250 shutter device,
actual controller identity and matching dynamic frame/panel. Source frame 93,
panel 94 and their pinned collision are removed. Floor finish is raised above
retained terrain with real internal steps.

The ground plan now has open front living circulation, fewer partitions and
a rear entrance passage beside a compact return stair. Two 1.2 m flights rise
2 m each over 3 m runs, joined by a 1.2 m turn. Guard-specific slab subtraction
preserves physical floor at the top exit. Upstairs rooms respect roof wings;
bathroom access is from the upper bedroom. Native geometry and routes are
experimental until observed in game.

Candidate `building-lab-test-cfeba1bd6c30` under
`projects/experiments/building-lab/generated/residential-house-plan/generated/packages`.
Archive SHA-256 `2f6e26f740a6bd942c9332a3dda8d3c734182e60f555239eda9c45f57eebceae`.
Four payloads installed/hash checked with Cyberpunk closed; prior files and
runtime report backed up under
`projects/experiments/building-lab/generated/runtime-installs/20261026-135203-house-plan`.
60 tests, Ruff, JavaScript syntax, six native resource readbacks and 152 offline
controls pass. No live pass yet. Test V and NPC through garage/rear/front,
the return stair both ways and the balcony. Inspect the entire shutter opening,
threshold, step-up, turn/headroom and top landing rather than query success alone.

An old Building Lab server process initially reported a 6..15 m stair-run rule.
Restart fixed it; GET house and POST compile both HTTP 200 with the new 3 m
return flights and one navigation island. Editor refresh is required for new JS.


### Rancho corner stair / expanded garage (26 October, 14:58 UTC)

Current candidate: `building-lab-test-779affa2310c`, project
`projects/experiments/building-lab/generated/residential-house-corner-stair`.
Installation receipt:
`projects/experiments/building-lab/generated/runtime-installs/20261026-145855-house-corner-stair/installation.json`.
Four payloads installed and hash checked with the game closed. 61 tests, seven
native readbacks and 160 offline controls pass; live runtime remains unverified.
The internal garage door now enters the living extension through a side-wall
step-up; it no longer shares the stair foot. Test this new path and the straight
stair in both directions with V, then an NPC. Inspect shutter closing/opening,
window reveals, roof-height bulkheads and the two restored rear corner walls.
Reload the saved Rancho house in Building Lab to replace a stale local draft;
restart its Python server after compiler changes.
