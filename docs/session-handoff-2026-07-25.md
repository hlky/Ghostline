# Ghostline session handoff — 2026-07-25

## Immediate status

The active task is runtime validation of the third building-block harness:
`gqt003_extract_and_hold`.

The first GQT003 candidate crashed while loading a save. A WolvenKit-rebuilt
crash-fix candidate is now packed and installed, but the user has not tested
this replacement yet.

```text
Build:
H:\Ghostline-builds\gqt003-crashfix-20260725-153319\archive.archive

Installed:
H:\Cyberpunk 2077\archive\pc\mod\Ghostline.archive
H:\Cyberpunk 2077\archive\pc\mod\Ghostline.archive.xl

Archive SHA-256:
1B0E429FC00B228EA5A7ED5819CD89802992DD661D144D3C476A5EAAB655C00E

ArchiveXL SHA-256:
DD39DAD12CB4B5FC2EA41AC0B5C94AA20027F93D4DFDB84D029EFB30F24D7A6C

Previous-install backup:
H:\Ghostline-backups\pre-gqt003-crashfix-20260725-153430
```

The next action is to receive the user's save-load result. If the save loads,
continue runtime testing from the first objective. If it still crashes, inspect
the fresh crash report and current ArchiveXL/TweakXL/REDscript logs before
changing resources.

A fully native candidate made with the fixed `ghostline-red` is prepared but
deliberately not installed:

```text
Build:
H:\Ghostline-builds\gqt003-native-fixed-20260725-161339\archive.archive

Archive SHA-256:
6AD5FE4F27103C4571B7F2CBD2ECE4749B520966537F33E43F696CC621F14BA7

ArchiveXL SHA-256:
DD39DAD12CB4B5FC2EA41AC0B5C94AA20027F93D4DFDB84D029EFB30F24D7A6C
```

Its staging tree contains 331 files. Archive extraction returns all 328
packable payloads byte-identically, with no extras or differences. The three
expected omissions are Patch's `.tmp` file and the two `00_readme.txt` files.
Do not install this candidate until the current WolvenKit build receives its
first save-load result; this preserves a clean runtime comparison.

Expected flow:

```text
reach extraction relay
-> hack the access point to release Patch
-> escort Patch through three ordered gates
-> defend Patch for 20 seconds
-> quest succeeds
```

The first world placement and all lifecycle behavior are provisional.

## The load crash

The crashing report is:

```text
C:\Users\user\AppData\Local\REDEngine\ReportQueue\Cyberpunk2077-20260725-151831-28504-15292
```

It reports:

```text
EXCEPTION_ACCESS_VIOLATION
read address 0xFFFFFFFFFFFFFFFF
```

This is the same broad signature as the earlier malformed GQT004 load crash.
ArchiveXL completed the GQT003 journal, root-phase, localization, device, and
streaming-block merges before the crash. TweakXL imported successfully and
REDscript compilation completed successfully. The evidence therefore points
to a structurally unsafe packed CR2W resource rather than `.xl`, YAML, or
REDscript syntax.

The failing native-written GQT003 resources and the crash report text are
preserved at:

```text
H:\Ghostline-audits\gqt003-crash-20260725-153000
```

Do not overwrite or remove this directory; it is the regression fixture for
the now-fixed `ghostline-red` export/import compaction and schema-property
bugs.

## ghostline-red topology fix status

The export-pruning and missing-property parts of this defect were fixed and
pushed after this handoff was first written:

```text
2b2e1d7 (main, origin/main) Compact unused CR2W imports
02f35fe (main, origin/main) Write missing schema-backed CR2W properties
9b23d90 (main, origin/main) Prune unreachable CR2W exports
```

`ghostline-red cr2w-deserialize` had retained stale, unreferenced exports from
the binary template when authored JSON replaced a large template graph with a
smaller graph.

The authored JSON and a subsequent semantic serialization can look correct,
but the binary export/import tables still contain unused template topology.
The game appears to traverse or validate some of that retained topology during
save load and crashes.

Comparison against WolvenKit-built controls:

| Resource | Native exports | WolvenKit exports | Native imports | WolvenKit imports |
|---|---:|---:|---:|---:|
| `gqt003_extract_and_hold.questphase` | 86 | 53 | 11 | 4 |
| `gqt003_escort_patch.questphase` | 1,949 | 85 | 3 | 0 |
| `gqt003_defend_patch.questphase` | 1,970 | 106 | 3 | 0 |
| `gqt003_timed_defend.questphase` | 1,970 | 106 | 3 | 0 |
| `gqt003_always_loaded.streamingsector` | 21 | 7 | 0 | 0 |
| `gqt003_extract_and_hold.streamingsector` | 41 | 19 | 5 | 2 |
| `gqt003_extract_and_hold.streamingblock` | 1 | 1 | 4 | 2 |
| `gqt003.journal` | 47 | 30 | 1 | 1 |

The two simple phases provide useful controls:

| Resource | Native exports | WolvenKit exports |
|---|---:|---:|
| `gqt003_reach_extraction_relay.questphase` | 57 | 57 |
| `gqt003_release_patch.questphase` | 57 | 57 |

The device registry and onscreen localization were already identical in size
and topology between the native and WolvenKit builds.

Commit `9b23d90` now performs the required export reachability/pruning pass:

1. Begin at the final authored root chunk and every legitimate root-owned
   buffer/appendix.
2. Follow all authored handle, shared-handle, array, and nested object
   references.
3. Retain only exports reachable from that final graph.
4. Rebuild export/chunk indices and every handle reference after pruning.
5. Rebuild export indices used by embedded files and export parents.
6. Preserve unknown template data only when it remains reachable from the
   authored root. “Preserve untouched chunks” must not mean preserving
   disconnected template graph nodes.
7. Fail loudly if an emitted export cannot be proven reachable.

The implementation is verified against the preserved root, escort, and quest
sector fixtures. It emits the WolvenKit export counts and WolvenKit
independently serializes the resulting graphs with matching semantic explorer
views. After all three writer fixes, the full Rust suite reports 64 passed and
26 ignored; formatting, strict Clippy, and the release build pass.

Commit `2b2e1d7` completes the top-level container cleanup. It removes unused
CR2W imports and remaps retained resource-reference and embedded-file import
indices. The rebuilt root now has WolvenKit's 4 imports instead of the
template's 11; the streaming block and quest sector likewise match at 2
imports each.

Commit `02f35fe` resolved the separate template-scalar defect. It uses the
generated schema's RED type and ordinal metadata to insert non-default
fixed-size properties absent from the binary template, while leaving
zero/false/null defaults implicit. Rebuilding the known-bad always-loaded
sector now restores `entryActiveOnStart = 1`, `alwaysSpawned = true_`, and
`ghostline_patch_default`.

The complete native rebuild is retained at:

```text
H:\Ghostline-audits\gqt003-native-complete-all-20260725
H:\Ghostline-audits\gqt003-native-complete-roundtrip-20260725
```

WolvenKit independently serialized all eleven generic GQT003 outputs. All six
questphase explorer views and the journal views match, and every world
resource's semantic `Data` is equal to the WolvenKit control. The full Rust
suite reports 64 passed and 26 ignored; strict Clippy, formatting, and release
build pass.

The completed implementation covers both:

- shrinking/replacing a large `RedPackage` quest graph with a smaller one; and
- shrinking world/journal topology whose template contains more node/chunk
  definitions than the authored document.

The implementation is in:

```text
tools/ghostline-red/src/writer.rs
```

Use the preserved native files above as failing fixtures and the WolvenKit
controls below as the structural oracle:

```text
H:\Ghostline-audits\gqt003-wkit-all-20260725
H:\Ghostline-audits\gqt003-wkit-roundtrip-20260725
```

Acceptance status:

1. Native output has the same reachable graph topology and class population
   as the WolvenKit control.
2. The root has 10 graph nodes, 9 edges, 4 phase nodes, and 1 phase prefab.
3. The escort phase has 13 graph nodes, 12 edges, 85 exports, no phase
   prefabs, three trigger gates, follower-role assign/clear, and map-pin
   activate/deactivate.
4. The defend phase has 14 graph nodes, 14 edges, 106 exports, a 20-second
   delay, success and failure paths, and no phase prefabs.
5. The always-loaded sector has 7 exports; the quest sector has 19.
6. No disconnected template phase nodes, journal entries, world nodes, or
   unused imports survive the write.
7. WolvenKit and `ghostline-red` can both serialize the output without error.
8. The full Rust suite, `cargo clippy -- -D warnings`, release build, and all
   Ghostline Python tests pass.
9. A packed native candidate loads a save in game. This is the only remaining
   acceptance item and must wait until the installed WolvenKit control has
   received its first runtime result.

Useful Rust verification commands:

```powershell
Set-Location 'H:\projects\Ghostline'
cargo test --manifest-path .\tools\ghostline-red\Cargo.toml
cargo clippy --manifest-path .\tools\ghostline-red\Cargo.toml --all-targets -- -D warnings
cargo build --release --manifest-path .\tools\ghostline-red\Cargo.toml
```

The native fixes are structurally and semantically verified, but the installed
candidate intentionally remains the WolvenKit build until its first runtime
load test. Avoid rewriting the production binaries mid-test with:

```powershell
py -B tools/generate_gqt003_content.py --deserialize
```

Generation without `--deserialize` only refreshes authored raw JSON. A future
native runtime candidate may use `--deserialize` after preserving the current
WolvenKit binaries and performing the same round-trip audit.

## ghostline-red work already fixed and pushed

The submodule is clean at:

```text
2b2e1d7 (main, origin/main) Compact unused CR2W imports
```

Recent pushed commits:

```text
2b2e1d7 Compact unused CR2W imports
02f35fe Write missing schema-backed CR2W properties
9b23d90 Prune unreachable CR2W exports
e6b213d Write authored area shape outlines
8c089fe Write WolvenKit device registry appendices
a34201f Normalize WolvenKit boolean enum names
```

The first two were found while generating GQT003:

- `8c089fe` supports WolvenKit handle definitions that omit redundant
  `HandleId` fields and writes device-registry appendices.
- `e6b213d` writes the authored `AreaShapeOutline` base64 buffer rather than
  retaining the template outline.

The parent repository correctly shows `tools/ghostline-red` modified because
its gitlink has advanced from the parent commit. Do not reset it.

The user explicitly authorized fixing bugs in the submodule and pushing those
fixes to the submodule repository.

## Corrected GQT003 resource audit

All twelve GQT003 resources were rebuilt from the checked-in authored raw JSON
with WolvenKit:

```text
gqt003_extract_and_hold.questphase
gqt003_reach_extraction_relay.questphase
gqt003_release_patch.questphase
gqt003_escort_patch.questphase
gqt003_defend_patch.questphase
gqt003_timed_defend.questphase
gqt003.journal
gqt003.json
gqt003_always_loaded.streamingsector
gqt003_custom_devices.devices
gqt003_extract_and_hold.streamingblock
gqt003_extract_and_hold.streamingsector
```

WolvenKit control binaries:

```text
H:\Ghostline-audits\gqt003-wkit-all-20260725
```

WolvenKit round-trip JSON:

```text
H:\Ghostline-audits\gqt003-wkit-roundtrip-20260725
```

The corrected round trips verify:

- root: 10 nodes, 9 edges, 4 phase nodes, 1 prefab;
- escort: 13 nodes, 12 edges, follower role, three gates, final-hold pin;
- defend: 14 nodes, 14 edges, 20-second success/failure race;
- always-loaded sector: 3 nodes and persistent Patch community;
- quest sector: 7 nodes, including 4 trigger areas and the access point;
- journal: 27 entries, including all four objective phases and both map pins.

No unresolved template tokens were found in the production GQT003 phase,
world, or journal binaries.

The complete Python suite passes:

```text
Ran 190 tests
OK
```

The packed archive contains 328 packable payloads. All 328 extract
byte-identically against `source/archive`. The three deliberately unpacked
files are:

```text
mod\ghostline\characters\patch\body_28de7877-4cd1-48cc-9f9a-a3fdd074cc67.tmp
mod\ghostline\characters\patch\head\00_readme.txt
mod\ghostline\characters\patch\head\morphtargets\00_readme.txt
```

## GQT003 authored inputs

Primary inputs:

```text
source/quests/tests/gqt003_extract_and_hold.quest.json
tools/gqt003_extract_and_hold.world.json
tools/generate_gqt003_content.py
```

Generated raw resources:

```text
source/raw/mod/gqt003/
source/raw/mod/gqt003_extract_and_hold/
```

Packed resources:

```text
source/archive/mod/gqt003/
source/archive/mod/gqt003_extract_and_hold/
```

Registrations:

```text
source/resources/Ghostline.archive.xl
```

World placement:

```text
start:
ToVector4{ x = -1078.2563, y = 1313.9362, z = 5.174843, w = 1 }
yaw = -3.628360655

final hold:
ToVector4{ x = -1115.9425, y = 1431.5853, z = 5.433075, w = 1 }
yaw = 23.894821357
```

The root alone owns:

```text
#gqt003_pr_extract_and_hold
```

Every child sets:

```text
inherit_phase_prefabs: false
```

Patch uses:

```text
Character.GhostlinePatch
always_spawned: true_
is_workspot_infinite: 1
```

## Git state

Parent repository:

```text
branch: main
HEAD: a24c341 Add runtime-proven Vehicle Lab harness
origin/main: a24c341
```

That commit was pushed before GQT003 work began.

GQT003 is intentionally uncommitted pending runtime validation. The worktree
is dirty and must not be reset, discarded, or blindly restaged:

```text
 M ROADMAP.md
 M source/archive/mod/ghostline/quest_blocks/templates/escort_npc.questphase
 M source/quests/examples/template_building_blocks.quest.json
 M source/raw/mod/ghostline/quest_blocks/templates/escort_npc.questphase.json
 M source/resources/Ghostline.archive.xl
 M tests/fixtures/quest_blocks/ai_vehicle.quest.json
 M tests/test_advanced_quest_block_templates.py
 M tests/test_quest_building_blocks.py
 M tools/generate_advanced_quest_block_templates.py
 M tools/ghostline-red
 M tools/quest-schema-v1.json
 M tools/quest_compiler.py
 M tools/quest_spec.md
?? docs/session-handoff-2026-07-25.md
?? source/archive/mod/gqt003/
?? source/archive/mod/gqt003_extract_and_hold/
?? source/quests/tests/gqt003_extract_and_hold.quest.json
?? source/raw/mod/gqt003/
?? source/raw/mod/gqt003_extract_and_hold/
?? tests/test_gqt003_content.py
?? tools/generate_gqt003_content.py
?? tools/gqt003_extract_and_hold.world.json
```

The repo-local `ROADMAP.md` has already been updated with the crash, topology
evidence, audits, installed WolvenKit crash-fix, and verified but uninstalled
native candidate.

## Next-session first response

If the user reports that the WolvenKit crash-fix loads:

1. address the runtime GQT003 result directly;
2. record exact quest, access-point, Patch, marker, escort, or defend issues;
3. change only the relevant authored manifest/spec/generator;
4. use the fixed native writer for affected CR2W, serialize every result back,
   and compare it with the authored semantics; retain WolvenKit as the
   independent control while the native writer awaits its first runtime proof;
5. serialize every packed output back and compare semantics;
6. run all tests, pack, extract-verify, back up, and install;
7. update `ROADMAP.md`;
8. commit and push GQT003 only after the harness is runtime-proven.

If the save still crashes:

1. inspect the new crash report and current logs;
2. confirm the installed hashes match the candidate above;
3. compare the new report timing/signature with the preserved first crash;
4. temporarily narrow ArchiveXL registrations to isolate root versus world
   loading if necessary;
5. serialize resources from the installed archive, not merely
   `source/archive`;
6. retain each reduced crash/no-crash archive as a bisect fixture.
