# Complete quest authoring migration

All ten active story and test quest manifests now use shared composition for
journal, localization, objectives, contacts, locations, and facts where those
declarations apply. Their build entry points collect quest phases and content
before publication. Quest-specific scene, world, device, and braindance logic
remains in the owning quest and participates in the same artifact transaction.

| Quest | Migration result | Collected resources |
| --- | --- | ---: |
| GQ001 | Shared composition and complete manifest build; existing GQ000 phase donors retained. | 8 |
| GQ002 | Shared composition, investigation/decision/debrief declarations, and complete build. | 15 |
| GQ003 | Shared composition and complete isolated prototype build; all 36 stages remain planned. | 39 |
| GQT001 | Shared phone/readable/objective declarations; owned laptop and device registry remain quest-specific. | 10 |
| GQT002 | Shared optional objectives and content; existing guard setup and parallel root preserved through the compiler root hook. | 13 |
| GQT003 | Existing composition/lifecycle pilot now uses the common build and conversion transaction. | 7 |
| GQT004 | Shared vehicle objectives/content; final cleanup template supplied in memory. | 10 |
| GQT005 | Shared review objective/counter/content and retained lifecycle; braindance resources and binary prerequisites use common publication. | 23 |
| GQT006 | Shared cyberpsycho journal, Regina messages, attachment, shard, and map variants; custom challenge/world behavior retained. | 12 |
| GQT007 | Shared journal/content and complete scene, subtitle, VO, lipsync, and world collection. | 12 |

GQ000 remains the superseded, preserved runtime baseline and reviewed donor for
the active quests. It is not an additional active quest awaiting this migration.
For GQ003, only its existing journal and localization are included in source
publication; prototype phases remain under an explicit isolated output root.
That makes the source publication set **112 resources** across all ten quests.

## Shared support

- `quest_authoring` resolves declarations without donor I/O when callers only
  need bindings. Localization keys and text resolve before collision checks.
- `quest_journal` owns journal construction and handle allocation across reviewed
  donors. It supports multiple objectives per phase, optional objectives,
  counters, preserved map-pin metadata, ordered phone entries, explicit legacy
  IDs, sender/delay/attachment fields, and readable file/onscreen entries.
- Explicit donor selections preserve existing metadata, including Regina's
  localized name. The small reviewed `regina_cyberpsycho` donor replaces loading
  the full reference contact tree in a quest-specific builder.
- `quest_build` provides complete builds, isolated output roots, staged native
  conversion with WolvenKit fallback, and combined raw/binary publication with
  rollback. Required binary assets are checked before conversion. Depot paths
  and publication destinations must stay within their intended directories,
  including when a directory is a symbolic link.
- Conversion requires independent WolvenKit read-back parity for requested
  typed values, embedded data, graph edges, and socket connection order and
  metadata. Native layout loss triggers a fresh WolvenKit write; unresolved
  differences stop publication. Known serializer representations are accepted
  only through bounded checks with local source evidence.
- The schema covers the new declarations. Catalog evidence includes selected
  donors and the shared source dependency chain.
- Unused partial publishers in GQT005–GQT007 were removed; scene inspection
  helpers return documents without writing source. GQT007 reads spoken text,
  line IDs, and audio paths from its dialogue manifest, and scene/voice-tag
  settings from its scene spec. All 47 resources from these three builders
  remain exactly equal before and after that cleanup.

The old manifest shorthand remains supported. Existing linear and parallel
flows keep their semantics; migration does not add failure/cancellation routes
or lifecycle side effects that a quest did not previously have.

## Preservation and intentional correction

Before editing, each migration captured the old normalized manifest, generated
journal/localization, and phase documents. Permanent regression tests compare
the resulting stage fields, typed entry data, phone order and timing, resource
paths, and localized text against those snapshots. World and scene-specific
tests cover the retained builders.

GQ003 had two entries at the same escort-gate journal path. The first pointed
to `#gq003_18_mp_escort_gate_01`; the later duplicate pointed to the corresponding
trigger. The migration keeps the marker-backed entry and removes the conflicting
duplicate. It preserves every unique journal path and the compiled stage graph.
This correction is explicitly covered in the migration regression.

Comparison with the reviewed raw resources also exposed older generator drift:

- GQ001, GQ002, GQT001, and GQT004 now declare their child prefab scopes
  explicitly, preserving the reviewed per-child context and the root defaults.
- GQ002 declares its reviewed combat threat function and zero duration. Other
  encounter defaults remain unchanged.
- GQT004's cleanup binds the actual player vehicle record. Live instantiated
  phases reject unresolved template tokens. The theft stage emits its declared
  completion fact, which the older raw resource omitted.
- Regenerated debug-step Boolean flags use `1`; integer step values are retained.

GQT005's scene rebuild differs from its prior raw file only in 16 near-zero
quaternion components, each at most `1.418e-23`; the same inputs through the
captured pre-migration generator produce the same candidate. Native verification
checks their reflected float32 representation.

## Verification

The published set contains 112 raw resources and 21 changed CR2W binaries.
Fifteen binaries were written with `ghostline-red` and six with WolvenKit; all
21 passed independent WolvenKit read-back comparison with zero semantic errors.
Publication verified candidate, manifest, serializer evidence, and original
source hashes first, retained backups, and then checked every published raw and
archive hash against the receipt.

The final shared CLI also built all seven GQT003 resources with `--deserialize`
into an isolated output tree. Real entity and world conversion probes exercised
the reflected-writer fallback and packed trigger geometry. Corruption tests
cover missing properties, changed graph wiring and socket order, lost embedded
files, unsupported shared handles, and stale serializer evidence.

The 30-block catalog has zero example or evidence errors, and the generated
authoring schema is current. The final project gate passed **680 Python tests,
Ruff, and 6 Rust tests** using:

```powershell
uv run --locked --extra dev python -B tools/check_project.py
```

The log is `generated/quest-migration/project-gate.log`. Published file hashes
were verified again after the gate.

Local verification records under `generated/quest-migration` include:

- `final-candidates.json`: the complete source publication inventory.
- `native/report.json`: tool and input hashes, selected writers, independent
  read-backs, accepted representations, and comparison results.
- `native/production-probes/report.json`: real entity and world conversion checks.
- `shared-native-smoke.log`: the complete GQT003 native build.
- `publication.json`: published hashes and the retained backup location.
- `project-gate.log`: the full Python, Ruff, and Rust gate.

No game installation or gameplay execution is part of this migration. Planned
quest content remains planned; serialization and compiler checks do not establish
in-game behavior.

See [quest composition](../authoring/quest-composition.md) and
[block catalog and scenarios](../authoring/quest-blocks.md) for authoring and build
commands.
