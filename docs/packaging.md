# Packaging And Install Notes

This document defines the manual scoped build, verification, staging, and
install workflow. Current archive/ZIP hashes and retained build directories
belong in `ROADMAP.md` and `docs/testing.md`, not here.

## Sources Of Truth

- `source/raw` is the editable CR2W-JSON source.
- `source/archive` is the CR2W/depot tree passed to the archive packer.
- `source/resources` contains loose ArchiveXL, TweakXL, script, and config
  resources that must be staged separately from a manual archive pack.
- `packed` is ignored generated install/ZIP staging. Never edit it as source.

Do not pack from the repository root. `WolvenKit.CLI build .` previously swept
support paths such as `reference`, `source/raw`, `generated`,
`GraphEditorStates`, `tools`, and `modding_docs` into an archive.

## Pre-Pack Gate

Before packing a changed scene, phase, world resource, or localization map:

```powershell
py -B -m unittest discover -s tests -v
py -B .\tools\generate_scene.py audit --spec .\tools\gq000_patch_meet.scene-spec.json
py -B .\tools\generate_scene.py validate --file .\source\raw\mod\gq000\scenes\gq000_patch_meet.scene.json --spec .\tools\gq000_patch_meet.scene-spec.json
py -B .\tools\explore_localization.py check
```

For every changed CR2W-JSON resource, deserialize the intended raw file into
its matching `source/archive` directory and serialize that binary to an
isolated round-trip directory. Compare the round-tripped structure and, where
the resource is deterministic, its SHA-256. Follow
`agent/skills/ghostline-wolvenkit-cr2w/SKILL.md`.

A `CR2W` header proves only that a file is a CR2W container. It does not prove
that graph edges, handle references, resource indexes, locStore order, or
NodeRefs are valid.

## Scoped Archive Build

Use the known local CLI and pack only `source/archive`:

```powershell
$wk = 'H:\WolvenKit.Console-8.17.4\WolvenKit.CLI.exe'
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$buildDir = Join-Path 'H:\Ghostline-builds' "manual-$stamp"
New-Item -ItemType Directory -Path $buildDir | Out-Null
& $wk pack .\source\archive -o $buildDir
$candidate = Join-Path $buildDir 'archive.archive'
```

Because the input directory is named `archive`, the CLI output is normally
`$candidate`. Rename it to `Ghostline.archive` only after verification.

Expected depot roots are:

- `mod\gq000\...`
- `mod\ghostline\...`
- `base\...` only for a deliberate test or validated dependency.

WolvenKit does not pack arbitrary support files. The Patch `.tmp` file and two
head readmes currently remain in `source/archive` but are absent from the
archive payload; account for those known exclusions when comparing counts.

## Archive Verification

List the candidate and inspect the depot paths before installing it:

```powershell
& $wk archive $candidate --list
```

Reject a build containing repository/support roots such as `source\raw`,
`reference`, `generated`, `GraphEditorStates`, `tools`, or `modding_docs`.

Extract the candidate to a new verification directory:

```powershell
$verifyDir = Join-Path $buildDir 'extracted'
New-Item -ItemType Directory -Path $verifyDir | Out-Null
& $wk extract $candidate -o $verifyDir
```

Then verify:

- every listed depot path is intentional;
- every extracted payload matches the corresponding `source/archive` file by
  length and SHA-256;
- no expected depot path was added or removed relative to the intended
  baseline;
- the candidate archive SHA-256 is recorded in `ROADMAP.md` or
  `docs/testing.md`;
- the installed archive is byte-identical to the verified candidate.

For a scene-only candidate, explicitly prove that only the intended scene
payload changed from the last tested archive. Do not infer that from equal file
counts.

## Install Staging

The generated `packed` tree should mirror Cyberpunk's game directory:

```text
packed\
  archive\pc\mod\Ghostline.archive
  archive\pc\mod\Ghostline.archive.xl
  r6\tweaks\ghostline\character_patch.yaml
  r6\tweaks\ghostline\faction_ghostline.yaml
  engine\config\base\user.ini
  r6\scripts\Tduality\autosave_is_Not_included.reds
```

The `.archive` comes from the verified `archive.archive`. The remaining files
come from matching paths under `source/resources`.

The config and REDscript files suppress autosaves during repeatable quest
testing. They are development/test resources, not core Ghostline quest data;
make an explicit release decision before shipping them publicly.

Build a ZIP from the contents of `packed`, so `archive`, `r6`, and `engine` are
ZIP roots rather than nesting everything under a `packed` directory. Extract
the completed ZIP to a separate directory and compare every payload with its
staged source before distributing it.

## Runtime Dependencies

- ArchiveXL is required for questphase, journal, localization, and streaming
  registration.
- TweakXL is required for `Character.GhostlinePatch` and the Ghostline faction
  records. The current Patch shipping candidate exercises those records; the
  local test install has TweakXL 1.11.3, but its runtime log is pending the
  next game launch.
- Patch still has unvalidated `ep1\...` dependencies; Phantom Liberty may
  become a hard requirement if those are retained.

## Base-Path Override Risk

`source/archive/base` contains copied
`base\characters\head\player_base_heads\player_man_average\...` resources.
Those are global overrides rather than Ghostline-owned depot paths. The current
test archive retains them for baseline parity, but they should not ship in a
normal release unless their effect on V and base NPCs is explicitly validated.

The historical no-base probe still crashed, so the overrides were not the sole
cause of that old crash. The later scene-start failure was resolved separately
as a lipsync slot cardinality problem. Neither finding makes the base overrides
safe to ship.

## Runtime Checks

After installing the staged tree, verify:

- `red4ext\plugins\ArchiveXL\ArchiveXL.log` registers the root questphase,
  journal, onscreen localization, subtitle map, VO map, and streaming block;
- TweakXL load output is present before testing `Character.GhostlinePatch`;
- `r6\logs\redscript_rCURRENT.log` contains no new test-script errors;
- the community actor, trigger progression, journal/mappin state, subtitles,
  VO, scene exit, and next objective match the focused route in
  `docs/testing.md`.

Use a clean pre-Ghostline save for lifecycle tests. An archive/install hash
match cannot reset quest facts, journal visited state, checkpoints, or a scene
already persisted in the save.
