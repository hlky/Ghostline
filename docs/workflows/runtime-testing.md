# Runtime Testing And Evidence

The latest recorded installation follows. Earlier candidates and failures are
kept in the linked evidence archive. Installation evidence does not imply that
later working-tree changes have been tested in game.

Use a fresh save when validating questphase, scene, journal, or world-trigger
changes. Prefer a manual save made before any version of Ghostline was
installed or registered.

## Isolated Story Project Install (2026-10-07)

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
