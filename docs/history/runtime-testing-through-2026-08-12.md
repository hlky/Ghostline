# Runtime Evidence Archive Through 2026-08-12

Historical build/install records follow. Their file counts and hashes describe
those candidates only; they are not current release assertions.

## GQT006 Retargeted 20-Second Doggy Candidate (2026-08-12)

Installed on 2026-08-12; in-game evidence is pending. The verified package is
`H:\projects\Ghostline\.tmp\package\gqt006-retargeted-doggy-20260812-213700`.
The preceding 17-file installation is backed up at
`H:\Ghostline-backups\pre-gqt006-retargeted-doggy-20260812-213900`.

The loss intimacy route now uses the custom
`mod\gqt006\animations\gqt006_goth_doggy_20s.scenerid`. It retargets the
vanilla `sex_09_2s_m` top motion onto Goth Baddie's 71-joint average rig and
the lower motion onto the 152-joint Player rig, supplies separate male/female
Player tracks, repeats the motion for 20 seconds with a six-frame seam blend,
and embeds the three-quarter side camera. The scene uses the RID camera rather
than the persistent static camera event, so section completion should release
the cinematic camera when node 61 restores `Tier1_FullGameplay`.

WolvenKit built and round-tripped both the RID and scene. The scene references
the custom RID synchronously (`Default`) and binds body serials 2/4/6 and
camera serial 8. The focused generator/content suite passes 52 tests. The
packed archive contains 493 payloads; all extracted payloads match
`source/archive`, including the custom RID, scene, and all four current Goth
Baddie face meshes. The archive SHA-256 is
`5C433A90352A0AC2550AEE0F9340FF8D995D8A6E33EFC263AD4F6CCF389BD050`;
the ZIP SHA-256 is
`5F89883E0F17AB6448165337DB8972B65728C5B1DEC202574F49DB222A8DFEC3`.

Review on a clean pre-GQT006 save:

1. Lose to Goth Baddie and continue through the loss dialogue.
2. Confirm the weapon is hidden before intimacy.
3. Confirm Goth is behind/on top, V is lower, hands are not deformed, and both
   actors sit on the same ground plane.
4. Confirm the side camera holds for the complete 20-second section and then
   returns to gameplay for the aftermath dialogue.
5. Confirm Goth Baddie's updated face is present.

Avoid testing from autosaves or saves made after a failed probe. Quest facts,
journal visited state, active questphase nodes, checkpoints, and scene state can
persist in the save and leave `gq000` waiting in an old graph branch.

The project includes test-time autosave suppression resources:

- `projects/ghostline/source/resources/engine/config/base/user.ini`
- `projects/ghostline/source/resources/r6/scripts/Tduality/autosave_is_Not_included.reds`

These reduce accidental save contamination, but they do not clean an already
contaminated save. Keep a known-good pre-Ghostline manual save and return to it
for each start-flow validation pass.

## 2026-08-12 GQT006 TPP Spawn Contract Crash Fix

Installed on 2026-08-12; in-game evidence is pending. The verified package is
retained at
`H:\projects\Ghostline\.tmp\package\gqt006-spawn-contract-isolated-20260812-205707`.

Archive SHA-256:
`768415C7E376875615F640C389DD8BF6446D7CEF6FF45760FCB4BC1F66B20784`.

This is an isolated one-payload update over the preceding RID anim-set/TPP
candidate: only `mod\gqt006\scenes\gqt006_goth_baddie.scene` changed. The
archive contains 492 extracted payloads, all byte-identical to the isolated
pack input; the scene and GQT006 focused suites pass 52 tests.

The failed candidate configured normal `Character.TPP_Player_Cutscene_*`
replicas with the deferred `No_Impostor` lifecycle (`spawnOnStart=0`,
`alwaysSpawned=1`) and accidentally retained the template actor's unrelated
MQ003 community reference. That left an unresolved scene-owned spawn during
the fight exit and produced an access violation through a null object. Both
replicas now use the vanilla normal-TPP contract (`spawnOnStart=1`,
`alwaysSpawned=0`, no forced visibility, empty community acquisition data).
The redundant first-use Activate and CharacterSpawned wait nodes were removed;
the selected replica is still deactivated after the intimacy shot.

Retest from a clean pre-GQT006 save:

1. Confirm V's intro line plays before the options.
2. Choose both fight-starting options in separate reloads and confirm the game
   enters combat without crashing.
3. Complete the loss route once and then resume the preceding intimacy checks.

## 2026-08-12 GQT006 RID Anim-Set And TPP Proxy Probe

Installed on 2026-08-12; in-game evidence is pending. The verified package is
retained at
`H:\projects\Ghostline\.tmp\package\gqt006-animsets-tpp-20260812-202847`.
The preceding 17-file installation is backed up at
`H:\Ghostline-backups\pre-gqt006-animsets-tpp-20260812-203134`.

Archive SHA-256:
`7CE86EDF401ACEF8A51DE12B61CA651E31453B87CE1E80CA40D38B9EF5E01E30`.

ZIP SHA-256:
`5262E39D3F7EAA95A294D971E32878A8C7CEF7EF3790200C673617BEBAB075C1`.

Relative to the preceding Doggy Third-Person Camera probe, exactly one archive
payload changed: `mod\gqt006\scenes\gqt006_goth_baddie.scene`. The archive
contains 492 extracted payloads, all byte-identical to the isolated pack input;
all 17 ZIP and installed files are byte-identical to staging. The scene,
world, and GQT006 focused suites pass 69 tests.

This fixes the omitted RID ownership data that prevented the actor animation
tracks from resolving. Goth now owns the `sex_09` top-role RID anim set; a
Player-gender condition activates a matching
`Character.TPP_Player_Cutscene_Male` or
`Character.TPP_Player_Cutscene_Female` replica with its own body and facial RID
sets for the lower role. The real Player is hidden during the shot, then shown
again while the selected replica is deactivated. This supplies V's complete
customized third-person body and head instead of exposing the headless FPP
Player puppet.

Both post-fight entries now put V in a persistent empty-hands tier and issue an
instant `AllWeapons` unequip. Goth receives an instant exact katana unequip,
with a 100 ms equipment settle boundary. Empty hands remain forced through the
aftermath and are released only immediately before the scene exit.

The two-second side-camera section now ends in a 0.25-second fade to black.
The real/proxy Player swap and Tier 1 restoration happen while black, followed
by a 0.25-second fade from black before the `You always celebrate like that?`
aftermath dialogue. This prevents the prior visible standing/interpenetrating
swap in the live side shot.

Test from a clean pre-GQT006 save:

1. Lose normally and confirm V's weapon disappears before the post-fight
   dialogue; Goth's katana should also be gone.
2. Continue to the intimacy choice and confirm the side camera shows Goth in
   the behind/top role and the gender-matched V replica on hands and knees for
   the complete `sex_09_2s_m` clip.
3. Confirm V has a complete head and current character customization in the
   third-person shot.
4. Confirm the shot fades to black at two seconds and returns to the real V in
   Tier 1 before the aftermath dialogue, with no visible actor swap or overlap.
5. Confirm weapons remain suppressed through the aftermath, then normal draw
   controls return after the scene exits.
6. Reload and test the V-wins branch once to confirm its unchanged
   `sex_06_5s_m` route still works.

This remains a targeted compatibility probe: `sex_09` serial 5 was authored
for the 152-joint Player rig, while Goth's NPV currently uses the 71-joint
female-average rig. The prior run did not test that compatibility because its
performer anim sets were entirely absent. If the V proxy animates but Goth
still does not, that result isolates the remaining work to retargeting only the
top-role track; actor placement and the vanilla RID itself need not otherwise
be redesigned.

## 2026-08-12 GQT006 Doggy Third-Person Camera Probe

Installed on 2026-08-12; in-game evidence is pending. The verified package is
retained at
`H:\projects\Ghostline\.tmp\package\gqt006-doggy-tpp-20260812-185729`.
The preceding 17-file installation is backed up at
`H:\Ghostline-backups\pre-gqt006-doggy-tpp-20260812-185947`.

Archive SHA-256:
`9A477F2B0EE89384395D40082924427E2012E43667AA5115B101B3A6674158B8`.

ZIP SHA-256:
`E0DC4DA9A9543B0E508AB4DDD945D06BE41A337C9E0D942CF9BF1F3337798118`.

Relative to the preceding Sex Handoff And Role Polish candidate, exactly two
archive payloads changed: `gqt006_goth_baddie.scene` and
`gqt006_goth_baddie_cyberpsycho.streamingsector`. The archive contains 492
extracted payloads, all byte-identical to the isolated archive input; all 17
ZIP and installed files are byte-identical to staging. The scene generator,
world generator, and GQT006 content suites pass 67 tests.

The Goth-wins intimacy route now uses
`base\animations\quest\lore\generic_sex\intercourse\sex_09_2s_m.scenerid`.
Goth is rebound to Player serial 5 for the behind/top role. A vanilla-shaped
Player-gender condition selects male-average body/head serials 3/9 or
female-average body/head serials 1/8 for V in the lower role. The resource is a
synchronous `Default` reference with vanilla Meredith's resource id
`123427870`; its close first-person camera serial 7 is not referenced.

The loss route enters `Tier5_Cinematic` and activates a separate stock
`engine\scenesystem\camera.ent` through a regular `scneventsCameraEvent`. The
camera is approximately 2.7 metres from the animation, 1.3 metres above the
scene origin, and has a full pitched three-quarter-side orientation rather
than a yaw-only transform. It uses the stock 60-degree FOV and cuts in at the
start of the two-second animation. The V-wins `sex_06_5s_m` route remains
unchanged on its original FPP RID camera.

This is intentionally a runtime probe. The generic skeletons share the core
human rig and Goth is a player-family NPV, but extracted vanilla third-person
scenes normally use spawned TPP V proxies rather than binding average-body RID
tracks directly to the real Player actor. If V is absent, headless, or badly
deformed, the next implementation step is a gender-selected
`Character.TPP_Player_Cutscene_Male/Female` proxy, not another camera offset.

Test from a clean pre-GQT006 save:

1. Lose normally, continue through the post-fight dialogue, and choose either
   Continue or Challenge.
2. Confirm the shot cuts to a wide three-quarter side view with the ground and
   both complete actors visible; it must not use the old low/upward FPP pan.
3. Confirm Goth is behind/top and V is on hands and knees for the full
   `sex_09_2s_m` clip.
4. Confirm V's body and head animate correctly for the current V gender. Note
   any missing head, hidden body, rig distortion, or clothing/weapon residue.
5. Confirm Tier 1 gameplay returns before the aftermath dialogue and the scene
   exits normally.
6. Reload and test the V-wins branch once to confirm its unchanged
   `sex_06_5s_m` route still works.

## 2026-08-12 GQT006 Sex Handoff And Role Polish

Installed on 2026-08-12; in-game evidence is pending. The verified package is
retained at
`H:\projects\Ghostline\.tmp\package\gqt006-sex-handoff-polish-20260812-174229`.
The preceding 17-file installation is backed up at
`H:\Ghostline-backups\pre-gqt006-sex-handoff-polish-20260812-174900`.

Archive SHA-256:
`AFDE7B12520CABB71058122B4D04E7901165F19747296115CB909D4D83192ED7`.

ZIP SHA-256:
`997F41B75A27957DFD96E5D5C04FD7832A891E1E5FCBD463B9761E76558C6A53`.

This candidate changes exactly six archive payloads relative to the preceding
RID hard-reference candidate: the GQT006 scene, its neutralize phase, and Goth
Baddie's four generated head meshes (`h0`, `he`, `heb`, and `ht`). The archive
contains 492 extracted payloads, all byte-identical to the scoped input; all 17
ZIP and installed files are byte-identical to staging. The focused scene and
GQT006 content suites pass 43 tests.

The loss route now uses vanilla Meredith's `sex_05_5s_f` binding: Goth uses
partner body/head serials 9/11, V uses FPP serial 5, and the camera uses serial
7. This puts V underneath while Goth takes the leading/top role. The win route
remains on `sex_06_5s_m`. Both RIDs are synchronous `Default` resources.

Both intimacy routes now match the generic vanilla sex-scene presentation:
the camera entity is acquired as a `findInNode` scene prop, V's exact RID FPP
gender-transition parameters are present, the scene enters
`Tier4_FPPCinematic` with `forceEmptyHands`, and it returns to
`Tier1_FullGameplay` before aftermath dialogue. No marker or camera height was
changed.

At the loss threshold, V is restored to 100 percent health before the scene
starts. The loss entry applies the self-expiring 2.5-second
`BaseStatusEffect.Knockdown`, waits through its recovery, explicitly unequips
all player weapons, and then starts dialogue. The win entry also unequips all
weapons before dialogue. The knockdown is the only runtime-probe item: its
TweakDB player behavior is appropriate, but no extracted vanilla quest was
found applying that status directly to V.

Test from a clean pre-GQT006 save:

1. Lose normally at the protected threshold. Confirm V's red low-health state
   clears, V is visibly knocked down/recovering for about 2.5 seconds, the
   weapon is gone, and the loss dialogue begins.
2. Choose Continue or Challenge. Confirm Goth is the top/leading actor and V
   is underneath in `sex_05_5s_f`.
3. Confirm the cinematic FPP view no longer renders V's gameplay arms, weapon,
   or body around the camera, and the aftermath returns to ordinary gameplay.
4. Reload the clean save and win nonlethally. Confirm the weapon is holstered,
   the existing `sex_06_5s_m` V-leading route still plays, and aftermath exits
   normally.
5. Confirm Goth Baddie's newer face (eyes 8, nose 2, mouth 6, jaw 3, ears 2) is
   visible in both her gameplay and postfight appearances.

## 2026-08-12 GQT006 RID Hard-Reference Fix

Installed on 2026-08-12; in-game evidence is pending. The verified package is
retained at
`H:\projects\Ghostline\.tmp\package\gqt006-rid-hardref-fix-20260812-165830`.
The preceding 17-file installation is backed up at
`H:\Ghostline-backups\pre-gqt006-rid-hardref-fix-20260812-170258`.

Archive SHA-256:
`B8935F2F99E2F2C3AA6BEB9A159A8258084E658AFC25FC37309BE729E72EBBC6`.

ZIP SHA-256:
`B2F3B1BD071011BA3D9BB7D57F84F4400B4A4A295B019E2740160B044E3B09B5`.

This candidate changes exactly one archive payload relative to the preceding
installed build: `mod\gqt006\scenes\gqt006_goth_baddie.scene`. Its
`scnRidResourceHandler.ridResource` now uses the synchronous `Default` import
required by the reflected `CResourceReference<scnRidResource>` field and used
by every inspected vanilla sex scene. The old `Soft` import allowed the world
camera entity to activate at its ground-level anchor before RID camera track 7
was available, producing the under-map view even though that track is authored
roughly 1.14--1.30 metres above the scene marker.

The camera event, camera/marker world transforms, dialogue sections, choices,
and quest flow are unchanged. WolvenKit was used to serialize the corrected
scene because the template-backed native writer preserves an existing import
flag when the depot path is unchanged. A WolvenKit binary-to-JSON round trip
confirms `Flags: Default` in the packed scene. The archive contains 492
extracted payloads, all byte-identical to the scoped input; all 17 ZIP and
installed files are byte-identical to staging. The focused character, quest,
scene, RID, and voice-selection suites pass 122 tests plus 28 subtests. The
repository-wide run exceeded its 120-second execution window without emitting
a failure result.

Test from a clean pre-GQT006 save:

1. Reach either post-fight choice normally; dialogue timing and option order
   should remain identical to the preceding runtime pass.
2. Choose an intimacy branch. Confirm the camera cuts immediately to the
   authored `sex_06_5s_m` view above ground and both actors animate for five
   seconds.
3. Confirm aftermath dialogue runs and the route exits normally.
4. If the camera still clips, retain this hard-reference fix and next isolate
   explicit camera-prop acquisition; do not compensate with an arbitrary
   camera or marker Z offset.

## 2026-08-12 GQT006 Scene-Socket And AI-Role Fix

Installed on 2026-08-12; in-game evidence is pending. The verified package is
retained at
`H:\projects\Ghostline\.tmp\package\gqt006-scene-socket-fix-20260812-160902`.
The preceding 17-file installation is backed up at
`H:\Ghostline-backups\pre-gqt006-scene-socket-fix-20260812-160902`.

Archive SHA-256:
`9ACEC354E9C5B7059F32640FBAE52B896BBE4E94CF858A78AC107D7CC878719C`.

ZIP SHA-256:
`2D015BBAB18FF301201EC022E08F30894AAC76B3F3CA26BA87D445347646E875`.

The archive contains 492 extracted payloads, all byte-identical to the scoped
archive input. The 17-file ZIP round-trip and installed tree are byte-identical
to staging. Relative to the preceding candidate, exactly two archive payloads
changed: `gqt006_neutralize_goth_baddie.questphase` and
`gqt006_goth_baddie.scene`. The unrelated dirty GQT005 braindance RID remains
pinned to the preceding candidate. The focused character, quest, scene, and
voice-selection suites pass 102 tests. The repository-wide run passes 441 of
444 tests and stops only on the same three pre-existing missing world-catalog
Python modules.

The previous runtime pass proved that the loss listener and combat release
reached the scene handoff, but the scene then dead-ended. All ten regular edges
into post-fight appearance quest nodes were targeting input ordinal `0`, which
maps to `CutDestination`; they now target executable `In` at ordinal `1`.
Validation rejects any future ordinary scene-flow edge into a quest node's
cut-control socket.

The loss route also now performs a vanilla-shaped living-boss handoff. Goth is
made friendly, her forced-alerted patrol role is cleared through
`AIClearRoleCommandParams.Success`, Cinematic AI takes over, and the phase
waits for both Goth and V to leave combat before starting the scene. No
explicit `boss_healthbar` HUD override is used: the friendly/cleared-role
lifecycle should dismiss it naturally and leaves a stale bar diagnostically
useful if the engine state is still wrong.

Test from a clean pre-GQT006 save:

1. Start the encounter normally and let Goth reduce V to the protected
   five-percent threshold without setting `gqt006_debug_goth_wins`.
2. Confirm Goth stops attacking, sheathes or otherwise relinquishes her combat
   role, the boss health bar disappears, and the `goth_wins_debug` dialogue
   begins automatically.
3. Choose Continue or Challenge. Confirm the intimacy appearance applies and
   the embedded camera takes over for the five-second `sex_06_5s_m` RID.
4. Confirm aftermath dialogue runs, Goth's default appearance is restored, V
   returns to full health and normal mortality, and the neutralize objective
   advances.
5. Reload the clean save, defeat Goth nonlethally, and confirm the `v_wins`
   post-fight dialogue also begins and reaches its Continue/Tease intimacy and
   Stop exit routes without stalling.

## 2026-08-12 GQT006 Scene-Handoff Fix

Installed on 2026-08-12; in-game evidence is pending. The verified package is
retained at
`H:\projects\Ghostline\.tmp\package\gqt006-scene-handoff-fix-20260812-152624`.
The preceding 17-file installation is backed up at
`H:\Ghostline-backups\pre-gqt006-scene-handoff-fix-20260812-152624`.

Archive SHA-256:
`C186E430FEC79AF963C5BCBDDF846C662B8FD694B86F0800950C268D49B0E60F`.

ZIP SHA-256:
`F9A8228C4A97595BB969B516E32C6CCDD8CC4652A824E4A65C3D2D955E02BCD3`.

The archive contains 492 extracted payloads, all byte-identical to the scoped
archive input. The 17-file ZIP round-trip and installed tree are byte-identical
to staging. Relative to the preceding candidate, exactly two archive payloads
changed: `gqt006_neutralize_goth_baddie.questphase` and
`gqt006_goth_baddie.scene`. The unrelated dirty GQT005 braindance RID was pinned
to the preceding candidate for this scoped runtime test. The focused character,
quest, scene, and voice-selection suites pass 109 tests.

The `v_wins` and `goth_wins_debug` scene entry points now target dedicated
`scnStartNode` nodes instead of entering directly through appearance nodes.
On V's loss route, Goth Baddie is made invulnerable, switched to Cinematic AI,
and moved to the neutral attitude group. After a 200 ms release delay, the
phase waits until V is no longer in combat before starting the post-fight
scene.

Test from a clean pre-GQT006 save:

1. Start the encounter normally, choose Accept or Threaten, and let Goth
   Baddie reduce V to the protected five-percent threshold without setting
   `gqt006_debug_goth_wins`.
2. Confirm Goth stops attacking, the red combat HUD clears, and the
   `goth_wins_debug` post-fight dialogue begins automatically. It must not
   remain indefinitely at the neutralized combat state.
3. Choose Continue or Challenge. Confirm the post-fight and intimacy
   appearances apply, then the scene cuts directly to the embedded camera for
   the five-second `sex_06_5s_m` RID. This candidate deliberately has no
   fade-to-black; the direct camera takeover is the expected result.
4. Confirm the aftermath dialogue runs, Goth's default appearance is restored,
   V is healed to full health, normal mortality returns, and the quest advances.
5. Reload the clean save, win nonlethally, and confirm the separate `v_wins`
   entry now starts its post-fight dialogue and reaches the same intimacy
   proof-of-concept.

## 2026-08-12 GQT006 Choice And Combat-Outcome Fix

Installed on 2026-08-12; in-game evidence is pending. The verified package is
retained at
`H:\projects\Ghostline\.tmp\package\gqt006-outcome-fix-20260812-1530`.
The preceding 17-file installation is backed up at
`H:\Ghostline-backups\pre-gqt006-outcome-fix-20260812-1540`.

Archive SHA-256:
`1AB8DFCE9BA5C0D6894951345F5C16045B2F4AF8E182A70B56550AEEFA312789`.

ZIP SHA-256:
`8DA7E1C7EB331906FA2D975C8C963FF3A02AE5067D20146F4F4262CCB46D58FC`.

The archive contains 492 extracted payloads, all byte-identical to
`source/archive`. The 17-file ZIP round-trip is byte-identical to the staged
install tree and all 17 installed files match it. The focused character,
quest, scene, and voice-selection suites pass 107 tests; the repository-wide
run passes 434 of 437 tests and stops only on three
pre-existing missing world-catalog Python modules.

This candidate retains the preceding pre-fight fix: the meeting
now waits on a dedicated five-metre dialogue trigger instead of the 25-metre
reveal trigger. Goth Baddie is neutral before combat, and scene start places
her AI in the Cinematic tier so hostility cannot pre-empt the dialogue-choice
node. The first runtime pass showed that choice type `1` renders yellow and is
promoted above type `0`; Accept/Threaten and both Continue branches now use
yellow type `1`, while Leave/Stop use cyan type `0`.

Accept and Threaten still hand off to the encounter's explicit target and
threat injection. Goth's lethal, defeated/unconscious, V-health, and debug
listeners are now armed directly from the player-protection node instead of
waiting on the threat command's unobserved `Success` output. V's loss threshold
is five percent, avoiding the one-percent floor plus health-regeneration race.
Relative to the preceding candidate, exactly two archive payloads changed:
the neutralize phase and scene.

Test from a clean pre-GQT006 save:

1. Do not set `gqt006_debug_start`. Travel to approximately
   `(-1026.87, 1279.59, 5.13)` from a clean pre-GQT006 save and confirm the
   pre-fight scene starts only within roughly five metres of Goth Baddie.
2. Confirm Goth Baddie remains neutral and does not attack during the scripted
   four-line introduction. After she finishes “...and you're mine,” confirm
   the three options appear in that order: yellow Accept, yellow Threaten, and
   cyan Leave. Also confirm all
   subtitles and VO play and that female and male V select the matching
   gendered WEMs.
3. Select Accept or Threaten. Confirm combat starts only after the selected V
   line and that Goth Baddie's reduced health and trimmed
   ability set produce a difficult but winnable fight.
4. Win nonlethally, continue the post-fight scene, and confirm her appearance
   changes from `postfight` to `intimacy`. Verify the five-second
   `sex_06_5s_m` RID, its embedded camera track, both actors, and the restored
   default appearance after the aftermath dialogue.
5. Repeat without setting `gqt006_debug_goth_wins` and let Goth Baddie reduce
   V to the protected five-percent health threshold. Confirm combat is
   intercepted without a death/reload screen, the `goth_wins_debug` scene
   entry starts, V is restored to full health before normal mortality returns,
   and the role-specific intimacy route exits cleanly. The debug fact remains
   available only as a manual fallback trigger.
6. Complete the evidence shard, leave-area, and Patch phone-report stages;
   confirm the Cyberpsycho journal entry and reward complete normally.

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
