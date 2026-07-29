# Runtime Testing And Evidence

The first dated section is the active next-test candidate. It explicitly says
when build/install evidence is still pending. Later sections preserve exact
historical baselines that isolated earlier failures.

Use a fresh save when validating questphase, scene, journal, or world-trigger
changes. Prefer a manual save made before any version of Ghostline was
installed or registered.

Avoid testing from autosaves or saves made after a failed probe. Quest facts,
journal visited state, active questphase nodes, checkpoints, and scene state can
persist in the save and leave `gq000` waiting in an old graph branch.

The project includes test-time autosave suppression resources:

- `source/resources/engine/config/base/user.ini`
- `source/resources/r6/scripts/Tduality/autosave_is_Not_included.reds`

These reduce accidental save contamination, but they do not clean an already
contaminated save. Keep a known-good pre-Ghostline manual save and return to it
for each start-flow validation pass.

## 2026-07-23 GQ002 Final-Polish Candidate

Installed archive SHA-256:
`E37C3498B0AF0EE01697C4542D579252DE844E4D529F6381EDAF0D0CFCA1BF94`.

All 165 automated tests pass. The archive contains 279 verified payloads and
the nine-file staged install and ZIP both match their sources. Build evidence
is retained at `H:\Ghostline-builds\gq002-final-polish-20260723`; the replaced
install is backed up at
`H:\Ghostline-backups\pre-gq002-final-polish-20260723`.

Retest from a clean pre-GQ002 save and verify:

1. All three relay guards stand on reachable walking surfaces; specifically,
   the melee guard is no longer embedded in the rear wall.
2. Complete the final relay breach once. Confirm only one native
   `EXTRACTED DATA` reward is shown and the phase does not retrigger the
   access-point device.
3. Leave the area. Confirm `Respond to Cinder` becomes the tracked objective
   instead of an empty quest header, and remains visible throughout the phone
   exchange.
4. Reply to Cinder and receive the final message. Confirm the response
   objective succeeds, XP and eddies are awarded, and `THE MACHINE STOPS`
   moves to Completed.

## 2026-07-23 GQ002 Return-To-Relay Candidate

Installed archive SHA-256:
`8F84793C62FF446B5A54E30429B03FD3C5E483AE0998D78372B596B407D1BF50`.

The verified build and ZIP are retained at
`H:\Ghostline-builds\gq002-return-relay-20260723`; the preceding nine-file
installation is backed up at
`H:\Ghostline-backups\pre-gq002-return-relay-20260723`.

Runtime confirmed the corrected security trigger and downstream quest flow.
This candidate fills the remaining silent transition with a dedicated
`Return to the target relay.` reach-area stage and yellow GPS-enabled pin.
Entering the ten-metre security trigger succeeds that objective, hides its
pin, and starts the existing combat phase.

Confirm from a clean/pre-GQ002 route:

1. The return objective and relay GPS pin appear after the shard stage.
2. The route terminates at the target relay rather than a remote device proxy.
3. Entering the trigger replaces the return task with
   `Neutralize the relay security.` and spawns the guards.
4. The already-confirmed decision, relay operation, exit, and debrief flow
   still completes.

## 2026-07-23 GQ002 Security-Trigger Candidate

Installed archive SHA-256:
`8FF1835A73F93B032FC4E1602FA1CC80234779706B085C385EBB7DFB91CE945B`.

The verified build and ZIP are retained at
`H:\Ghostline-builds\gq002-security-trigger-20260723`; the preceding nine-file
installation is backed up at
`H:\Ghostline-backups\pre-gq002-security-trigger-20260723`.

Runtime confirmed that the shard-acquisition fact advances the read objective.
The following security phase then appeared blank because its trigger was
centred four metres below the relay roof. This candidate centres the
ten-metre-tall combat trigger on the relay's `z=16.36` walking plane.

Resume from the clean-save route and confirm:

1. The archived-conversation objective clears after the final scan and
   presentation delay.
2. At the target relay, `Neutralize the relay security.` activates immediately.
3. All three Tyger Claws spawn on the visible rooftop plane and become hostile.
4. Defeating them advances to Cinder's relay-decision phone conversation.

## 2026-07-23 GQ002 Shard-Acquisition-Fact Candidate

Installed archive SHA-256:
`82C221619EBA15D39D5F82D53B9CCE86AEEB9107AEC15166718143043284B312`.

The verified build and ZIP are retained at
`H:\Ghostline-builds\gq002-shard-fact-20260723`; the preceding nine-file
installation is backed up at
`H:\Ghostline-backups\pre-gq002-shard-fact-20260723`.

Runtime proved that the readable Hostage Circuit shard is consumed into the
Journal and does not remain a dependable inventory stack. This candidate
therefore completes the read stage from the final scan's
`gq002_clue_invoice_scanned` acquisition fact, after a three-second
presentation delay. It does not wait on inventory ownership or the Journal
reader's visited flag.

From a clean pre-GQ002 save, complete the three scans and confirm the shard
notification is followed after roughly three seconds by the target-relay
security stage. Continue through the remaining quest to catch any downstream
regression.

## 2026-07-23 GQ002 Native-Scanner Candidate

Installed archive SHA-256:
`9291927EAF3059628AC57A97AB71C65D2424652258BEFD86B90025A546395DDC`.

The verified build and ZIP are retained at
`H:\Ghostline-builds\gq002-native-scanner-20260723`; the preceding nine-file
installation is backed up at
`H:\Ghostline-backups\pre-gq002-native-scanner-20260723`.

This candidate removes Ghostline's persistent yellow
`SetDefaultHighlightEvent` layer from all three relay clues. The antennas now
use their native blue device-scanner outline while `questScan Finished` remains
the progression condition. The shard stage advances from ownership of the real
readable item rather than a journal-visited event, because opening the pickup
notification overlay does not set the full Journal reader's visited flag.

Retest from a clean pre-GQ002 save:

1. Scan each relay and confirm only the native scanner outline appears; no
   yellow outline should remain after leaving scanner mode.
2. Confirm every completed scan clears its clue marker and activates the next
   clue in order.
3. Confirm the final scan awards the Hostage Circuit shard and the quest
   proceeds beyond `Read the archived conversation`.
4. Continue through the target-relay combat gate and confirm the remaining
   choice, relay-operation, leave-area, and debrief stages still complete.

## 2026-07-23 GQ002 Sequencing-Fix Candidate

Installed archive SHA-256:
`E5BAA7FE06E2BBD85A6D094C897F1BF847C4B3076B57C0A8CE8749138E5A4D77`.

The verified build is retained at
`H:\Ghostline-builds\gq002-sequencing-fix-20260723`; the preceding installed
files are backed up at
`H:\Ghostline-backups\pre-gq002-sequencing-fix-20260723`.

Use a clean pre-GQ002 save. This pass specifically verifies the corrected
generated-stage lifecycle:

1. Confirm Cinder stands visibly in the open rooftop space rather than
   intersecting the concrete column.
2. Accept Cinder's job and confirm only `Go to the Kabuki relay.` activates.
   Her relay-decision phone thread must not appear yet.
3. Enter the relay trigger and confirm the reach objective completes before
   `Inspect the relay network.` appears.
4. Confirm only the first clue marker is active. Scan its referenced antenna
   access point, then confirm its marker clears and the next clue activates.
   Repeat for all three clues.
5. Treat the antenna's native jack-in/minigame and reward as separate vanilla
   behavior during this investigation stage. The quest investigation advances
   from scanning the marked devices; the later `Jack in to the relay.`
   objective owns the required minigame completion.
6. Confirm the shard, security encounter, Cinder relay decision, relay
   interaction, leave-area objective, and debrief appear only in that order.

## 2026-07-23 GQ002 Runtime-Fixes Candidate

Installed archive SHA-256:
`F8738A94773AFFD415BEEA2C6A77CB21C22CF3B375ECAB88DC0E1C3CE2B98BC7`.

The verified build is retained at
`H:\Ghostline-builds\gq002-runtime-fixes-20260723`; the preceding install is
backed up at
`H:\Ghostline-backups\pre-gq002-runtime-fixes-20260723`.

Retest from a clean pre-GQ002 save:

1. Confirm Cinder stands on the rooftop and her dialogue begins only within
   the new three-metre engage volume.
2. Confirm each currently active investigation target receives the standard
   yellow quest outline and completes only after a finished scanner pass.
3. Confirm completing the final scan produces the archived-conversation
   notification; open and read it before security begins.
4. Confirm all three security actors stand on the walking surface around the
   relay, none intersects nearby geometry, and combat waits until the shard has
   actually been read.
5. Complete either phone branch and the remaining relay/leave stages. Confirm
   the final Cinder message is followed by a normal quest-complete notification
   and no active `The Machine Stops` objective remains.

## 2026-07-23 GQ002 Location/Combat-Fix Candidate

Installed archive SHA-256:
`34A7F1024B0BB5913F437CF63DEA9783E2636A064722D0E8A3416B0BEA20D0DF`.

The verified build is retained at
`H:\Ghostline-builds\gq002-location-combat-fix-20260723`; the preceding install
is backed up at
`H:\Ghostline-backups\pre-gq002-location-combat-fix-20260723`.

Retest from a clean pre-GQ002 save:

1. Confirm Cinder now appears on the separately proven contact pad used by the
   GQ001 Iris meeting rather than beside the Kabuki relay network.
2. Confirm the second clue has no offset quest pin and is instead clearly
   identified by its yellow quest outline.
3. Complete the final scan and confirm a readable
   `Archived conversation: Sato and Keene` shard is acquired with the normal
   inventory notification. The read objective should then wait for the entry
   to be opened.
4. Confirm security does not activate at the remote third clue. Return to
   within ten metres of the target relay and confirm the objective and combat
   begin there.
5. Confirm all three Tyger Claws are reachable on the visible rooftop walking
   plane and no actor is inside the structure.

## 2026-07-23 GQ002 Preview/Highlight-Delay Candidate

Build: `H:\Ghostline-builds\gq002-preview-highlight-delay-20260723`

Archive SHA-256:
`B2F418B7A80BA2950BC2A42C924A3D71061C45E0C55B2A0764935D835EC3C31D`

1. Confirm the second clue still has a world/map quest icon, but does not draw
   the incorrect GPS route to the native device's remote gameplay proxy.
2. Confirm each yellow device outline clears about one second after its scan
   completes.
3. Confirm reading the shard from the pickup-notification overlay is accepted:
   the read objective should complete after the three-second presentation
   window and progression should wait at the target-relay combat trigger.

## 2026-07-23 GQ002 Journal/Highlight-Fix Candidate

Build: `H:\Ghostline-builds\gq002-journal-highlight-fix-20260723`

Archive SHA-256:
`50134BD2F8BD116BA133F4AD456DD877562CDBCE97C290D600FB615710535328`

1. Confirm the second investigation clue has a quest pin anchored to the
   native access point rather than the former offset static marker.
2. After each completed scan, confirm that clue's yellow quest outline clears
   before the next clue becomes active.
3. Confirm opening the awarded Hostage Circuit shard completes `Read the
   archived conversation` and advances to the return-to-relay combat gate.

## 2026-07-23 GQ002 “The Machine Stops” Candidate

Installed archive SHA-256:
`783A11CF8FF248FEDFC3CC190BDE357B9D4309B2DEBE0D13A95BC5E0D15251EA`.

The verified build, extracted archive, staged package, and ZIP are retained at
`H:\Ghostline-builds\gq002-machine-stops-20260723`. The preceding nine
installed files are backed up at
`H:\Ghostline-backups\pre-gq002-machine-stops-20260723`.

Use a fresh or pre-GQ002 save and validate both outcome routes, reloading the
same clean baseline before the second route:

1. Confirm Patch’s `The Machine Stops` phone offer appears and selecting
   `On my way.` activates `Meet Cinder.` under the correctly named quest.
2. Confirm Cinder appears at the Kabuki meeting point, her opening line does
   not trigger before the six-unit approach boundary, and all five dialogue
   choices display correctly.
3. Exercise the two optional branches, then accept. Confirm all eleven spoken
   lines use the selected VO, show matching subtitles, and remain synchronized.
4. Confirm `Go to the Kabuki relay.` activates and routes to the native antenna
   access point around `(-1111.060, 1456.400, 16.360)`.
5. Scan each of the three clue markers. Confirm every clue completes once,
   remains complete, and the investigation advances only after all three.
6. Open and read `Archived conversation: Sato and Keene`; confirm its content
   describes the tenant classifier, clinic telemetry hostage circuit, and
   Tyger Claw security.
7. Confirm all three security actors spawn near the relay, patrol, become
   hostile to V, and the objective advances only after all are defeated.
8. In Cinder’s phone choice, select `Destroy the relay.` for the first run and
   `Spoof the shutdown.` for the second. Confirm the appropriate immediate
   response appears and V is instructed to jack in.
9. Complete the native access-point interaction/minigame. Confirm the selected
   outcome fact advances the same interaction stage without stalling.
10. Leave the marked area. Confirm remaining encounter actors clean up and
    Cinder’s debrief begins.
11. Confirm the debrief’s opening message is outcome-specific, both final V
    response choices work, and the quest reaches completion with no lingering
    objective, marker, actor, or interaction.
12. After each run, inspect ArchiveXL, TweakXL, REDscript, CET, and crash logs
    for new GQ002 errors or missing resource registrations.

## 2026-07-23 Six-Metre Contact Awareness Candidate

Installed archive SHA-256:
`AA0686E4604F94E4BBA79295041A9643C2D87891581D66CE1D89C743CA96D1E4`.

Patch and Iris now both start their opening lines at six metres. Their setup,
mood, and final interaction triggers are otherwise unchanged. All 116 tests
pass, all 226 extracted archive payloads match `source/archive`, and all eight
installed files match their verified sources.

Build evidence is retained at
`H:\Ghostline-builds\contact-trigger-6m-20260723-145709`; the preceding install
is backed up at
`H:\Ghostline-backups\pre-contact-trigger-6m-20260723-145805`.

## 2026-07-23 Iris Awareness And Drop-Point Nav Endpoint Candidate

Installed archive SHA-256:
`B2917118EF08A865A6A5F2547BF5869514B84F7175ADAD7732F2AF02E7DE368E`.

Build and extraction evidence is retained at
`H:\Ghostline-builds\iris-gps-nav-20260723-143811`; the replaced eight-file
installation is backed up at
`H:\Ghostline-backups\pre-iris-gps-nav-20260723-143913`. All 116 automated
tests pass, the candidate contains 226 entries, every extracted payload matches
`source/archive`, and all eight installed files match their verified sources.

The Iris opening line now waits for the 12-unit awareness trigger instead of
the earlier 20-unit circle; its four-unit vertical band is unchanged. The
drop-point journal marker now resolves at the native template's transformed
`main_slot/navQuery` approach point rather than inside the kiosk body. Its
journal Z offset is reduced from two units to one because the navigation slot
itself is already one unit above the device root.

For the next fresh-save pass:

1. Approach Iris up the stairs and confirm her opening line starts only near
   the upper landing.
2. Advance to delivery and confirm the yellow GPS route ends directly in front
   of `drop_point_009`, without the rectangular detour around the kiosk.
3. Confirm the yellow icon still appears at console height and depositing the
   datacache completes the objective normally.

## 2026-07-23 Delivery GPS And Marker-Height Candidate

Installed archive SHA-256:
`7C3BB9844EE0DD8BC65C1883D61AD0307E89593DFBFC69A8EFF2B7C504D93590`.

Verified seven-file ZIP SHA-256:
`92B71E698F9C4BE9EAF58597463B3A9BC931A84540EF2EE18C411F10CA95771C`.

Build and extraction evidence is retained at
`H:\Ghostline-builds\gps-marker-fix-20260723-002208`; byte-identical CR2W
round trips for both changed resources are retained at
`H:\Ghostline-audits\gps-marker-fix-roundtrip-20260723-002032`. The replaced
seven-file installation is backed up at
`H:\Ghostline-backups\pre-gps-marker-fix-20260723-002543`.

All 103 automated tests pass. The candidate archive contains the same 175
depot paths as the preceding installed build, every extracted payload matches
`source/archive`, all seven ZIP and installed files match `packed`, and exactly
two archive payloads changed:

- `mod\gq000\journal\gq000.journal`;
- `mod\gq000\phases\gq000_delivery.questphase`.

The preceding runtime pass confirmed the complete quest: native deposit,
package removal, delivery progression, both Morrow response routes, reward,
and quest success all worked. It exposed two presentation defects. The yellow
pin rendered close to the kiosk's floor-level entity root, and the map retained
a second dotted GPS leg toward the old bridge even though the short solid route
already ended at the correct drop point.

This candidate raises the journal pin by two units, matching the native drop
point template's `UI_Interaction` slot, and sets
`disablePreviousMappins: 1` only on delivery-pin activation. For the next
fresh-save pass:

1. Complete the quest through `Leave the relay area.` and let delivery start.
2. Open the map and confirm the route has no dotted continuation back toward
   the bridge.
3. At `drop_point_009`, confirm the yellow quest icon is at the kiosk console
   height rather than beside its base.
4. Deposit the datacache and confirm the already-proven Morrow/completion flow
   still finishes normally.

## 2026-07-22 Accessible Drop-Point 009 Candidate (Historical)

Installed archive SHA-256:
`1C669335E83C93F714455D24743C7F03E34F2FA381A60ABB9E8F35A85375EDCC`.

Verified seven-file ZIP SHA-256:
`D3F32A60C789030FB47BA9C3C06C9E48DBB7097F2F786EB858EF8551D3764275`.

Build evidence and the extracted/round-trip verification trees are retained at
`H:\Ghostline-builds\drop-point-009-yellow-20260722-234109` and
`H:\Ghostline-audits\drop-point-009-roundtrip-20260722-233650`. The replaced
seven-file installation is backed up at
`H:\Ghostline-backups\pre-drop-point-009-20260722-234356`. All 175 archive
entries match `source/archive`, all seven ZIP and installed payloads match the
staged tree, and all 103 automated tests pass. The six regenerated CR2W files
round-trip to byte-identical binaries. Relative to the preceding
delivery/debrief candidate, exactly three archive payloads changed:

- `mod\gq000\journal\gq000.journal`;
- `mod\gq000\phases\gq000_delivery.questphase`;
- `mod\gq000\world\gq000_always_loaded.streamingsector`.

World Inspector confirms the replacement target is the publicly accessible,
map-labelled Kabuki `drop_point_009`:

- NodeRef:
  `$/03_night_city/c_watson/kabuki/kabuki_drop_points_prefabAR4NTYY/drop_point_009_prefabBIYNP3Y`
- position: `(-1168.66333, 1309.51709, 19.9768238)`
- orientation: `(0, 0, 0.999, 0.044)`, approximately `175` degrees
- sector: `exterior_-19_20_0_0.streamingsector`

The quest reserves `Items.gq000_datacache` to that native device with the
vanilla `ReserveItemToThisDropPoint` fan-out confirmed against
`sts_wat_kab_05`. The journal UI instead targets Ghostline's always-loaded
`#gq000_03_mp_drop_point` at the same coordinates. This split is intentional:
ArchiveXL logged that it could not resolve the previous direct cooked mappin,
and the previous physical target was occluded. The replacement journal entry
uses `DefaultQuestVariant`, so the quest marker should be yellow rather than
fixer-green.

Use a save from before the Ghostline phone flow and validate the whole route.
In particular, do not continue a save that already entered the previous
delivery phase: its fire-and-forget reservation node may already be complete,
and installing a rebuilt questphase does not rewind saved graph state.

1. Complete the bridge meeting, relay encounter, breach, and leave-area beat.
   Confirm the breach grants `Datacache` in addition to both readable shards.
2. Confirm the tracker changes to `Deliver the datacache to the drop point.`
   and shows a yellow marker at the accessible `drop_point_009` kiosk.
3. Interact with the machine. Confirm it offers the quest deposit, removes the
   datacache package, and closes the delivery objective.
4. Confirm Morrow's `Quiet Spine` thread sends both opening messages and offers
   both V replies.
5. Select either reply. Confirm only its matching Morrow response appears,
   followed by `Keep this number...`.
6. Read the final message. Confirm the standard eddies/XP completion reward is
   granted and `GHOSTLINE` moves to Completed.

If step 2 does not start, check that `Datacache` was granted and that the
leave-area objective completed. If step 3 does not advance, inspect whether
the package remains in inventory and whether fact `gq000_datacache` was
incremented. Progression waits on that native deposit fact, not on the reserve
event output.

## 2026-07-22 Delivery + Morrow Debrief Candidate (Historical)

Installed archive SHA-256:
`0F971F97877421C181C5D4B114F5090D015DEE97B3FE7FFCF9091F57FD476158`.

Verified seven-file ZIP SHA-256:
`03BF484092377E5B022B9BE4867B1383544B46B24BA4769291904EC93395FBBB`.

Build evidence, exact CR2W round trips, archive extraction, and ZIP
verification are retained at
`H:\Ghostline-builds\delivery-morrow-20260722-224211`. The replaced seven-file
install is backed up at
`H:\Ghostline-backups\pre-delivery-morrow-20260722-224211`. All 175 archive
entries match the packable `source/archive` payloads byte-for-byte, all seven
ZIP and installed payloads match `packed`, and all 98 automated tests pass.
Relative to the runtime-confirmed explicit-player hostility build, four
payloads changed and one was added:

- changed `mod\gq000\phases\gq000.questphase`;
- changed `mod\gq000\phases\gq000_post_accept.questphase`;
- changed `mod\gq000\journal\gq000.journal`;
- changed `mod\gq000\localization\en-us\onscreens\gq000.json`;
- added `mod\gq000\phases\gq000_delivery.questphase`.

The cache breach grants a separate `Items.gq000_datacache` package along with
the two readable Quiet Spine shards. Its intended native deposit increments
the package `friendlyName` fact `gq000_datacache`, which advances the delivery
phase into Morrow's authored `Quiet Spine` phone thread. Both player replies
converge on the same final message, but only the matching branch response
should appear.

Runtime testing superseded this package before the deposit could be validated:
the selected kiosk was occluded by inaccessible geometry, its tracker led into
the building, and ArchiveXL logged that it could not resolve the direct cooked
mappin position. The active candidate above keeps the same delivery/debrief
graph while replacing both the native target and the journal-marker strategy.

Use a save from before the Ghostline phone flow and validate the whole route:

1. Complete the bridge meeting, relay encounter, breach, and leave-area beat.
   Confirm the breach grants `Datacache` in addition to both readable shards.
2. After leaving the relay area, confirm the tracker changes to `Deliver the
   datacache to the drop point.` and its marker resolves to the Kabuki machine.
3. Interact with that machine. Confirm it offers the quest deposit, removes the
   datacache package, and closes the delivery objective.
4. Confirm Morrow's `Quiet Spine` thread sends `Cache authenticated. Clean
   extraction.` followed by the courier-route message and then offers both V
   replies.
5. Select either reply. Confirm only its matching Morrow response appears,
   followed by `Keep this number...`.
6. Read the final message. Confirm the standard eddies/XP completion reward is
   granted and `GHOSTLINE` moves to Completed.

If step 2 does not start, check that `Datacache` was granted and that the
leave-area objective completed. If step 3 does not advance, inspect whether
the package remains in inventory and whether fact `gq000_datacache` was
incremented. The reserve event is deliberately fire-and-forget; progression
waits on the native drop-point fact rather than the event output.

## 2026-07-22 Explicit-Player Guard Hostility Candidate

Installed archive SHA-256:
`18D56C1F20C3600AFBA385BE4F6678D58825D0E29E5A350C72FA48FF4227B3E2`.

Verified seven-file ZIP SHA-256:
`D5FAC9FE9CE7DA060CDA3CA79114552D89D9D6BF7C2ED7699D999DBD65645674`.

Build evidence, an exact questphase CR2W round trip, archive extraction, and
ZIP verification are retained at
`H:\Ghostline-builds\guard-hostility-mq022-20260722-214120`. The replaced
seven-file install is backed up at
`H:\Ghostline-backups\pre-guard-hostility-mq022-20260722-214120`. All 174
archive entries match `source/archive` byte-for-byte, all seven ZIP and
installed payloads match `packed`, and all 88 automated tests pass. Comparison
against the preceding runtime-tested archive reports exactly one changed
payload: `mod\gq000\phases\gq000_post_accept.questphase`.

The preceding pass confirmed every other encounter change: all guards spawn
beside the relay, the short patrol works, the terminal is flat and correctly
marked, breach and shard delivery work, both conversations are readable, and
the leave-area cleanup completes. The guards remained passive even after the
objective changed to extraction. That proves the 25-unit trigger and graph
branch executed; the failed border-patrol command simply had no explicit
threat target.

This focused candidate replaces that one whole-community pulse with the
stronger vanilla `mq022_combat.questphase` pattern. For each named guard it:

- transitions the guard through `neutral` and `hostile` attitude groups;
- assigns V as the immediate combat target;
- injects an explicit `#player` combat threat with forced hostile attitude.

The hostility sequence is a side branch. It cannot block the reach-to-extract
objective transition if a guard has already died or cannot resolve.

Use a save from before the Ghostline phone flow. The focused retest is:

1. Complete the bridge conversation and approach the relay.
2. At about 25 units, verify all three yellow/neutral guard indicators turn
   hostile and the patrol/sentry AI is interrupted to attack V.
3. Confirm the objective still changes to `Extract the datacache.` and that
   evasion or breaching under pressure remains possible; kills are not an
   objective.

Everything after aggression is regression coverage only, since it already
passed: terminal pin, breach, two shard notifications/Journal entries,
`Leave the relay area.`, and cleanup outside 75 units.

## 2026-07-22 Hostile Guard + Patrol Candidate (Historical)

Archive SHA-256:
`DE2A28EF7F7D8D20B4FADF3B97BD0B96BB420FED8456AC0D57E9987B00ACFB2A`.
ZIP SHA-256:
`BCB1BDDE74877FF798EA9BDAABC550CA88A5DC8018CECB486E785152F34E5830`.
Evidence is retained at
`H:\Ghostline-builds\cache-encounter-hostile-patrol-20260722-205717`.

This build established the final relay transform, patrol, terminal mappin,
breach, shard, and cleanup baseline. Its one failure was guard aggression: it
copied a Badlands border-patrol threat pulse with null target references, which
does not create a target for otherwise passive community puppets.

The current delivery target, vanilla Kabuki `drop_point_009`, is documented in
`docs/authoring/world-resources.md` but was intentionally dormant in this historical
focused build.

## 2026-07-22 Cache Runtime-Fix + Patch Visibility Candidate (Historical)

Installed archive SHA-256:
`2C5179349DBD1AFF5A5A01123F83FF1DC76D8D91E45FE946CEA4DCAF0166BF80`.

Verified seven-file ZIP SHA-256:
`73B3C28C525DF298878FA011D5B8D9E79AF03C4FB35CAC740E8064A96CBDAB7C`.

Final build, Patch `.app` round-trip, and extraction evidence is retained at
`H:\Ghostline-builds\patch-genital-visibility-20260722-202817`; the underlying
cache-phase round trips remain at
`H:\Ghostline-builds\cache-runtime-fix-20260722-201715`. The immediately
preceding seven-file cache candidate is backed up at
`H:\Ghostline-backups\pre-patch-genital-visibility-20260722-202817`. All 174
archive entries match `source/archive` byte-for-byte after extraction, all
seven ZIP payloads match the staged tree, and all seven installed payloads
match that same tree.
Relative to the failed first-cache archive, this adds only
`mod\gq000\world\gq000_custom_devices.devices` and changes the journal,
quest onscreen localization, post-accept phase, always-loaded sector, and quest
sector; no archive payload was removed.

This candidate responds to the first cache runtime pass:

- the access point remains at `(-1000.02, 1497.2208, 8.3)` but now uses yaw
  `-91.4`, facing the personal-link workspot away from the cabinet;
- the streamable guard community is anchored at the cache and uses three
  verified Japantown Tyger Claw records, with whole-community activation and a
  whole-community spawn-readiness gate;
- the relay has a minimal Ghostline `.devices` registry patched into the
  global Night City device registry;
- successful breach immediately sets `gq000_cache_acquired`, then grants two
  readable Quiet Spine items with pickup notifications and Journal entries;
- `Leave the relay area.` becomes visible after extraction, and the surviving
  community cleans up only after V crosses the 75-unit boundary;
- Patch's fixed clothed appearance disables the inherited `t0_peen` and
  `t0_pubic_hair` meshes in both appearance copies. This is the only archive
  payload change from the otherwise identical cache runtime-fix build.

Runtime result: Patch was clothed; all three Tyger Claws spawned; breach,
automatic shard grants, both Journal entries, and the leave-area objective all
worked. The guards were 7–14 units away and remained passive, the `-91.4`
terminal was still perpendicular to the cabinet, and the extract stage had no
yellow quest pin because the reach-stage pin was disabled before extraction.
The historical hostile-guard/patrol candidate above replaced this build, and
the active explicit-player hostility candidate now supersedes that package.

Use a save from before the Ghostline phone flow. Then run this concise route:

1. Check ArchiveXL and TweakXL logs for the `.devices` patch and both
   `Items.GhostlineQuietSpine*` records without errors.
2. At the bridge, confirm Patch's trousers fully cover his lower body with no
   genital or pubic-hair mesh clipping, then accept the job.
3. Approach the relay; confirm all three Tyger Claws spawn at plausible
   navmesh positions and that combat is not required.
4. Confirm the socket faces outward, the 25-unit arrival gate changes the
   tracker to `Extract the datacache.`, and the native breach opens normally.
5. If practical, fail or cancel once and verify no progression; then succeed.
6. After success, confirm extraction closes, two automatic item pickup
   notifications appear, and both archived conversations are readable under
   Journal -> Shards. No separate world pickup is expected.
7. Confirm `Leave the relay area.` is tracked, then cross the 75-unit cleanup
   boundary and verify the objective succeeds and surviving guards deactivate.

If a debug console is available, also confirm `gq000_cache_acquired == 1`
immediately after successful breach rather than waiting for the hacking UI or
leave-area transition.

## 2026-07-22 First Cache Encounter Candidate (Historical)

Installed archive SHA-256:
`888E678162D6086124E1CC8AE3CDB39D58697129289A24C5E9DC15B53EEF2D05`.

Repo `Ghostline.zip` SHA-256:
`D4628E6652567DFE46CF9E1D707D002F5B436515F7C4ACE8D544AA3900CF8A69`.

Build and round-trip evidence is retained at
`H:\Ghostline-builds\cache-encounter-candidate-20260722`. The previous
installed six-file candidate and ZIP are backed up at
`H:\Ghostline-backups\pre-cache-encounter-20260722-191442`.

This candidate adds the first complete cache encounter after Patch's meeting:

- the mappin now targets the selected Watson/Kabuki recycling-station cabinet;
- a native physical access point starts disabled on the cabinet face;
- three inactive Tyger Claw entries activate when the cache phase begins;
- entering the 25-unit site radius changes the tracker to `Extract the
  datacache.` and enables the relay;
- native breach success completes the objective and unlocks both Quiet Spine
  archived conversations;
- surviving guards deactivate only after V leaves the 75-unit cleanup radius.

Runtime result: the socket rendered and launched the native minigame, but the
guard community did not spawn, the socket faced into the cabinet, and a
successful breach produced neither visible continuation nor shard pickup
notifications. The runtime-fix candidate above replaces this build for the
next test; the checklist below is retained as its original validation plan.

Use a save from before the Ghostline phone flow. Saves that already ran the old
terminating `gq000_post_accept` skeleton can retain stale phase/fact state.

1. Complete the phone and Patch bridge flow, choose `I'm in.`, and confirm the
   cache marker points to the cabinet site.
2. Approach the site and confirm all three Tyger Claws appear at plausible,
   navmesh-safe positions without a streaming crash.
3. Confirm stealth remains possible and killing every guard is not required.
4. At roughly 25 units, confirm `Go to the cache coordinates.` succeeds and
   `Extract the datacache.` becomes tracked.
5. Check that the mounted socket is visible, correctly aligned, and offers the
   native personal-link/breach interaction.
6. Fail or cancel one breach attempt if practical; confirm the objective does
   not complete, then retry and succeed.
7. Confirm notifications wait until the hacking UI closes, the extraction
   objective succeeds, and both Quiet Spine archived conversations become
   available/readable.
8. Leave the wider site radius and confirm any surviving spawned guards clean
   up without visibly popping while V is still at the relay.

For this historical build, the mount offset, guard transforms,
whole-community lifecycle, direct onscreen shard activation, and native
breach-success event were the runtime-unknown surfaces. Delivery and Morrow's
follow-up were intentionally dormant.

## 2026-07-22 Patch Root-Appearance Fix

Installed archive SHA-256:
`40148CE9F102C5CF77BEA31C1D9043FB20F53B8937873235BDBE3D1A82EF6786`.

Repo `Ghostline.zip` SHA-256:
`890166AA958650A537BCCA32B9B91214E139C3C4FBDF51AC431EF965668D7162`.

The first custom Patch run reached dialogue, displayed Patch's localized name,
and showed all three repaired first-menu labels, but the character was
invisible. TweakXL imported both Ghostline records without errors. The world
requested `default`, which is the internal definition inside `patch.app`, while
the root entity exposes `ghostline_patch_default` to spawners. Patch's root
`defaultAppearance` also used the internal name.

This build changes exactly two archive payloads relative to that run:

- `patch.ent` now defaults to `ghostline_patch_default`;
- the always-loaded community phase now requests
  `ghostline_patch_default`.

Runtime retest confirmed that Patch is visible before dialogue, the reviewed
hair/clothing render, and the first choice group displays all three labels.
The remaining focused checks are the second choice group and completion of the
accept-to-cache handoff on this exact custom-character build.

Build evidence is retained at
`H:\Ghostline-builds\patch-appearance-name-fix-20260722-130000`. The exact
invisible-actor install is backed up at
`H:\Ghostline-backups\pre-patch-appearance-name-fix-20260722-130000`.

## 2026-07-22 Custom Patch Shipping Build

Installed archive SHA-256:
`6B9456AE74DF057869A61E79B965EE8D98EACCE1369CD9C9BA469F2C8875B566`.

Repo `Ghostline.zip` SHA-256:
`1361CC10E31A620F77674C3BA74CA9643D4A64FF522584231FEC3719FBA1089D`.

This candidate adds the custom character to the preceding sorted-locStore
build. Exactly two archive payloads changed:

- `mod\ghostline\characters\patch\patch.app` applies the reviewed `hh_146`
  dread-undercut, grey high-collar shirt, black computer cargos, black/red
  boots, and existing face details;
- `mod\gq000\world\gq000_always_loaded.streamingsector` restores the
  `patch/default` community entry to `Character.GhostlinePatch`.

The quest phases, scene, triggers, localization, VO, and audio remain
byte-identical to the preceding candidate. TweakXL 1.11.3 is installed under
`red4ext\plugins\TweakXL`; because the game has not been launched since that
install, its runtime registration still needs confirmation.

Use a fresh pre-Ghostline save and run the complete route:

1. Confirm TweakXL loads and the Ghostline TweakDB records report no error.
2. Accept `On my way`, fast travel nearby, and approach normally.
3. Confirm Patch spawns instead of Judy and inspect hair, clothing, clipping,
   animation, LOD changes, and stream-out/in behavior.
4. Confirm the first choice group shows `Ghostline?`, `Why me?`, and
   `What's the job?`.
5. Confirm the second group shows `Who's behind it?` and `I'm in.`.
6. Confirm subtitles and VO remain aligned, then select `I'm in.` and verify
   the cache objective and marker activate.

Build and extraction evidence is retained at
`H:\Ghostline-builds\patch-ship-20260722-122203`. The previous six installed
Ghostline files are backed up with game-relative paths at
`H:\Ghostline-backups\pre-patch-ship-20260722-123307`.

## 2026-07-22 Sorted Choice-LocStore Build

Installed archive SHA-256:
`FEAEC7D66E6C3E492ACE2454A0E32FFB7E1DCBA6B8C08B7E44A427745BF21CAC`.

The successful but label-broken slot-0 build is backed up at
`H:\Ghostline-backups\pre-choice-locstore-sort-20260722-002552`.

The preceding run confirmed that scene startup, all dialogue subtitles/VO,
acceptance, and the cache objective work. This build changes only the meeting
scene's embedded localization ordering: `db_db`, `pl_pl`, and `en_us`
descriptor blocks are now sorted numerically by `locstringId`, matching every
audited vanilla scene.

Use a fresh pre-Ghostline save and repeat the meeting route. The focused checks
are:

1. Confirm the normal approach still reaches dialogue without a crash.
2. Confirm the first choice group shows all three labels: `Ghostline?`,
   `Why me?`, and `What's the job?`.
3. Exercise both optional responses and confirm each returns with the correct
   remaining labels.
4. Confirm the second group shows `Who's behind it?` and `I'm in.`. In the
   previous build the first of these incorrectly displayed `Why me?`.
5. Select `I'm in.` and confirm the cache objective still activates.

Build and round-trip evidence is retained at
`H:\Ghostline-builds\choice-locstore-sort-20260722-002552`.

## 2026-07-22 Lipsync Slot-0 Isolation Build

Installed archive SHA-256:
`87956AFFE3C7CD66E16AD8531D0784689B01A24DCA629FAF41C2291C6E70E40D`.

The previous mq003-sequenced build is backed up at
`H:\Ghostline-backups\pre-lipsync-slot0-20260722-000338`.

This build changes only the meeting scene relative to the previous installed
archive. The Patch-role actor (Judy at runtime) and V both use lipsync resource
ID `0`, and the scene contains one generic lipsync resource row. Use the same
route that reproduced the setup-boundary crash:

1. Load the known-good pre-Ghostline manual save.
2. Confirm the Patch phone message appears, select `On my way` to accept the
   meeting, and confirm the bridge objective/tracker appears.
3. Fast travel to the same nearby point and let world loading finish.
4. Approach the bridge at normal speed. Record whether crossing the 90-unit
   scene setup boundary—roughly 80-90 metres on the tracker—still crashes.
5. If it survives, continue through the 60-unit case-mood, 20-unit
   someone-coming, and 10-unit engage boundaries without pausing.
6. Confirm the opening line and first choice appear, then exercise all five
   choices and record labels, subtitles, VO, and return paths.
7. Select `I'm in.` and confirm the meet objective succeeds, its mappin clears,
   and the cache objective/mappin becomes active.

Do not use facial animation quality to judge this build: sharing the generic
slot is a crash-isolation probe rather than the intended final lipsync setup.

## 2026-07-21 MQ003-Sequenced Approach Build

Installed archive SHA-256:
`177500B67B2A6B975A597DF5D582797F006643BA6BC975E1D9CFBC66BC498BFD`.

The prior installed build is backed up at
`H:\Ghostline-backups\pre-mq003-sequence-20260721-233546`.

Repeat the route that crashed the synchronized current-raw build:

1. Load the known-good pre-Ghostline manual save.
2. Confirm the Patch phone message appears.
3. Select `On my way` to accept the meeting and confirm the bridge
   objective/tracker appears.
4. Fast travel to the same nearby point used in the crash report.
5. Confirm the game finishes world loading without a crash.
6. Approach the bridge at normal speed. Confirm Judy is already spawned before
   entering the 90-unit setup area and that crossing setup does not crash.
7. Continue without pausing. Around the 20-unit someone-coming boundary,
   confirm Patch's opening line plays; around the 10-unit engage boundary,
   confirm the first choice group appears instead of the previous crash.
8. Exercise all five dialogue choices and record their labels, subtitles, VO,
   and return paths.
9. Select `I'm in.` and confirm the meet objective succeeds, its mappin clears,
   and the cache objective/mappin becomes active.

This build changes only the meeting phase and scene relative to the previous
installed archive. Trigger geometry, world resources, and WEM files are
byte-identical, so any change at the 10-unit boundary isolates lifecycle
sequencing.

This build intentionally continues using `Character.Judy` for community
isolation. Patch cannot be validated until TweakXL is installed or that
dependency is removed.
