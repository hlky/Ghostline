# Build, Package, And Install

Use `tools/package_project.py` for runtime packages. It is the single owner of
profile selection, WolvenKit packing, archive listing/extraction, payload hashes,
loose-resource staging and ZIP verification. Successful extraction establishes
package integrity; in-game behavior needs the focused runtime checks below.

Select a project with `--project ghostline` or `--project gqt###`. Every `source`
path below is relative to that project's directory. The repository root owns
the tools, not a combined source tree. See [project layout](../reference/project-layout.md).

## Sources And Pre-Pack Gate

Edit CR2W-JSON under `source/raw`, then convert and round-trip changed resources
into `source/archive` using the [CR2W workflow](../../agent/skills/ghostline-wolvenkit-cr2w/SKILL.md).
Plain manifests under `quests`, `characters` and `braindance` are authoring inputs.
ArchiveXL, TweakXL, REDscript and config inputs belong under `source/resources`.

```powershell
uv sync --locked --extra dev
uv run python -B tools/check_project.py
```

Run the owning quest/scene/world/localization validators for changed assets.
A `CR2W` header alone does not validate graph edges, handles, resource indexes,
locStore order or NodeRefs. The package command does not rebuild authored raw
files or silently convert working-tree binaries.

## Profiles

Each project owns `packaging/profiles.json`. The root file only routes legacy
profile names to those projects. These selections are available:

| Profile | Activation and contents |
| --- | --- |
| `story` | GQ001/GQ002 roots, GQ000 runtime support, Patch/Iris/Cinder and their dependencies; no test activation, base-character overrides or autosave suppression |
| `gqt001`–`gqt004` | One selected test quest and its explicit shared dependencies; GQT003 includes GQ000 runtime support |
| `gqt005` | Braindance test, required Patch resources and its test tweaks |
| `gqt006` | Standalone Goth Baddie encounter, including referenced custom animations; forbids tutorial dependencies |
| `gqt007` | Barry lipsync test and localized animset |
| `development` | Story-only active roots and shared support, base overrides and autosave suppression; excludes incomplete GQ003 preproduction assets/registration |

Selection starts at each character entity and follows named references from
packed CR2W string tables plus authored raw companions, including paths hidden
in embedded/hash-only binary representations. The registered lipmap must prove
any scene-local lipsync remapping. Missing owned references fail before packing.
Typed numeric resource paths resolve against the inventoried depot hashes.
When a selected character mesh has no parsed raw companion, the selector keeps
that character's entire owning bundle, including textures and morph resources;
this also applies to characters reached transitively. The report records each
fallback. Fine-grained character pruning requires decoding the embedded material
buffers first. The static audit reports unresolved hashes and external game
dependencies; dynamic runtime behavior still needs game validation.

Story/test profiles deduplicate byte-identical character meshes into deterministic
shared paths and generate `resource.link` aliases for every original path. This
requires ArchiveXL 1.14 or newer. `--keep-duplicate-meshes` produces a comparison
candidate with original paths and no deduplication aliases. Authored binary
resources remain unchanged. Tutorial support is included only through a named
dependency; base-character overrides remain outside normal releases.

## Build And Verify

```powershell
# Review selection without external tools or publication.
uv run python -B tools/package_project.py --project ghostline --plan

# Build, list, extract, hash-check and verify the ZIP.
uv run python -B tools/package_project.py --project ghostline

# Same gate for the standalone encounter.
uv run python -B projects/test-quests/gqt006/implementation/package_standalone.py
```

Paths resolve explicit CLI arguments, `GHOSTLINE_*` environment variables,
`toolchain.local.json`, then discovery. Copy `toolchain.example.json` to configure
your workstation. A supplied WolvenKit path is used for pack, list and extract.

Each run owns a unique `<project>/generated/packages/<profile>-<id>` directory containing
the frozen archive/loose inputs, `selection.json`, pack/list/extract logs,
verification extractions, final `install` tree, ZIP and `verification.json`.
The receipt records every selected/extracted hash and every install/ZIP hash.
An archive or ZIP mismatch fails the run before a verified result is returned.
Files in failed run directories are diagnostic candidates, not verified builds.

The packer compares the exact path set, not only the file count. Every extracted
payload must match its frozen input by length and SHA-256. ZIP entries and bytes
must then match the staged install tree. Shared alias files are checked against
the same source bytes used to establish deduplication.

Runtime archives use WolvenKit. The native packer's historical extraction
success did not establish game-startup compatibility; see
[native archive experiments](../history/native-archive-experiments.md).
Never pack the repository root or install an unverified scratch candidate.

## Install

Add `--install --game <game-root>` to an already reviewed profile build when
installation is intended. Installation rechecks staged hashes and rolls back
replaced files if publication fails. The standalone wrapper also accepts
`--disable-ghostline`; it requires `--install` and preserves uniquely named
backups of the combined archive, registration and tweaks.

Install/ZIP roots are `archive`, `r6`, and (development only) `engine`, without
an enclosing `packed` directory. `packed`, `generated`, and `.tmp` are ignored
outputs; none is the source of truth. Record focused in-game results in
[runtime testing](runtime-testing.md), and retain the corresponding verification
receipt so observations identify the exact candidate.

For local story testing, autosave suppression can remain installed separately
from the release profile: `projects/ghostline/source/resources/engine/config/base/user.ini`
sets `AutoSaveEnabled = false`, and
`projects/ghostline/source/resources/r6/scripts/Tduality/autosave_is_Not_included.reds`
suppresses the vendor/ripperdoc leave-scenario autosaves. The October 7 story
cleanup disabled these files; they were subsequently restored at the user's
request. Normal story installation replaces its declared files and does not
remove these local settings. Restart the game after changing them.

## Runtime Dependencies

- ArchiveXL is required for questphase, journal, localization, and streaming
  registration. It also patches
  `mod\gq000\world\gq000_custom_devices.devices` into Night City's global
  `03_night_city.devices` registry; the custom access point must not rely on
  sector placement alone for controller lookup. GQT001 no longer requires the
  experimental local ArchiveXL extension: its working computer is a complete
  Ghostline-owned sector instance with correctly bound component CRUIDs. The
  earlier extension investigation remains documented in
  `docs/authoring/archivexl-resource-patching.md`, but it is not a runtime
  dependency of the current test.
- TweakXL is required for `Character.GhostlinePatch`, the Ghostline faction,
  both readable Quiet Spine shard records, the separate datacache delivery
  package, and `QuestRewards.gq000_completion` in `gq000_shards.yaml`. The
  local test install uses TweakXL 1.11.3.
- Patch still has unvalidated `ep1\...` dependencies; Phantom Liberty may
  become a hard requirement if those are retained.

## Base-Path Override Risk

`projects/shared/ghostline-runtime/source/archive/base` contains copied
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
  journal, onscreen localization, subtitle map, VO map, streaming block, and
  custom `.devices` resource patch;
- TweakXL load output is present before testing `Character.GhostlinePatch`,
  either `Items.GhostlineQuietSpine*` record, `Items.gq000_datacache`, or the
  completion reward;
- `r6\logs\redscript_rCURRENT.log` contains no new test-script errors;
- the community actors, trigger progression, journal/mappin state, subtitles,
  VO, scene exit, cache breach, datacache deposit, Morrow thread, reward, and
  quest completion match the focused route in
  `docs/workflows/runtime-testing.md`.

Use a clean pre-Ghostline save for lifecycle tests. An archive/install hash
match cannot reset quest facts, journal visited state, checkpoints, or a scene
already persisted in the save.
