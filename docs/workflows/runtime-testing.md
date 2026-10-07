# Runtime Testing And Evidence

The latest recorded installation follows. Earlier candidates and failures are
kept in the linked evidence archive. Installation evidence does not imply that
later working-tree changes have been tested in game.

Use a fresh save when validating questphase, scene, journal, or world-trigger
changes. Prefer a manual save made before any version of Ghostline was
installed or registered.

## GQ001/GQ002 Lipsync Install (2026-08-27)

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
