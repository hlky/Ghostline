# Runtime Testing And Evidence

The latest recorded installation follows. Earlier candidates and failures are
kept in the linked evidence archive. Installation evidence does not imply that
later working-tree changes have been tested in game.

Use a fresh save when validating questphase, scene, journal, or world-trigger
changes. Prefer a manual save made before any version of Ghostline was
installed or registered.

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
