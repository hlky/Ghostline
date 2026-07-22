# Ghostline Testing

The first dated section is the current installed candidate and required next
test. Later sections preserve the exact historical baselines that isolated the
scene-lifecycle and lipsync failures.

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
