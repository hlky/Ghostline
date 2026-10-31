# Cinematic study: scope, method and reproduction

Inspected 2026-10-27. This pass extends the existing frozen
[all-quest corpus](../all-quests-method.md); it does not re-extract archives or
claim exhaustive manual viewing of all quests. The local modding documentation,
especially the scene-file and scene-node references, supplies orientation;
concrete claims come from the checked graph/performance evidence and six raw
section checks.

## Inputs and attribution

The input journal catalogue has 416 identities across all nine stored types.
The input performance index contains 3,139 `.scene` resources and 318,424
events across 41 types. The extractor's frozen archive selection and hashes
remain those of the all-quest corpus, including Phantom Liberty. There is no
new claim about installed archive precedence, active launch definitions or
which historical-looking journal entries remain playable.

The analyzer reads every performance shard, verifies its SHA-256 against the
performance manifest, and joins exact depots/raw/binary hashes to the existing
resource and graph index. It counts all stored section events, retaining
section boundaries, explicit timing-field presence, actor components, scaling
types and example event pointers. All 41 stored event types belong to at least
one declared capability family; families overlap, notably RID camera/camera.

It joins graph actors, acquisition plans, interfaces, node/edge counts, choice
counts, end-node types, embedded operation types and resource references. It
does not invent values for omitted source fields. `screenplay_lines` counts
stored screenplay records; event counts count occurrences, so the two need
not agree. Section co-occurrence means mechanisms occur somewhere in the same
section, not that their durations overlap.

Each journal dossier inherits the existing catalogue's `scope_resources`
selection. Parent-context scenes are listed separately and excluded from its
primary metrics. Whole-scene inventories still include alternate entries,
branches and possible preview scaffolding. No new reachability analysis or
scene-node pruning is performed. A resource listed for a quest is context
evidence, not proof that every event plays during that quest. The Q305
[case study](case-studies.md) gives a concrete attribution warning.

Unique global scene totals are deduplicated by depot. Per-quest and per-type
counts overlap and must not be summed into global totals. Unresolved and
POI-only journal identities stay labelled. No selected scene is an evidence
gap, not proof of a cinematic-free quest.

## Manual source review and raw verification

The six source cases cover ordinary conversation and workspot transitions,
mixed skeletal/RID staging, braindance playback/clues, recorded actor/camera
assembly, conventional animation/VFX staging and a branching finale with
preview-camera scaffolding. They are representative mechanism studies, not
statistically representative samples or narrative reviews of every quest.

The verifier checks the raw SHA-256 for all six scenes, their section pointers
and every event pointer/type/ID in those sections (412 events). It compares
presence and value of key timing, performer and RID reference fields. Actor
RID and camera RID indices are followed through their separate tables,
resource handlers and animation serials to exact depot paths. It does not
decode or validate the bound `.scenerid` payloads.

Five additional caller/gate node pointers are checked against hash-matched raw
resources: Barry's two phase calls, Q306's two launchpad calls, and its
`ep1_official_trailer` condition. Their stored data and incident edges are
retained in `caller-evidence.json`; this is source routing evidence rather
than installed branch execution.

Native serializer output can preserve animation-name structures as `$rawTail`.
This pass retains that boundary: it does not invent clip names from opaque
bytes or equate numeric table positions with human-readable animations.
Animation inventories, actual clip content, body/facial channel compatibility,
lipsync validity, VO/subtitle alignment, camera framing and collision need
their own evidence. Likewise, default interruption arrays are inventoried
without asserting that every route enables or handles them.

The separate Ghostline inventory uses `projects/catalog.json` and only each
registered project's own `source/raw` tree. Generated previews, template source
trees and vanilla reference files are excluded. It records scene hashes and
event types using `SceneExplorer`; it does not imply phase/workspot/script
presentation is absent when no scene section event exists.

## Outputs

| Artifact | Contents |
| --- | --- |
| [README](README.md) | Global capability/type coverage and all 416 journal identities |
| `quests/*.md` | Per-quest scene interfaces, actors, events, pointers and section capability combinations |
| [Scene index](scene-index.md) | All 3,139 resources, including resources outside journal contexts |
| [Synthesis](synthesis.md) | Cross-corpus interpretation and proposed authoring contracts |
| [Case studies](case-studies.md) | Six manually inspected local section mechanisms |
| [Ghostline comparison](ghostline-comparison.md) | Current project source inventory and production gaps |
| `analysis.json.gz` | Deterministic full metrics, joined scene metadata and quest attribution |
| `case-evidence.json.gz` | Full selected-section events, graph nodes and adjacent edges |
| `verification.json` | Analyzer input hashes, totals and output identities |
| `raw-case-verification.json` | Raw event checks and resolved RID reference chains |
| `caller-evidence.json` | Selected phase calls, overrides, gate and adjacent edges |
| `ghostline-scene-inventory.json` | Registered project raw paths, hashes and event counts |

Machine-readable outputs live in
[`reference/quests/deep-dives/cinematic-scenes`](../../../../../reference/quests/deep-dives/cinematic-scenes).
Compressed JSON uses a fixed gzip timestamp. Source-derived files and manually
written synthesis/case/method/comparison documents are separate: the analyzer
regenerates the index and quest dossiers without overwriting the manual prose.

## Reproduce and verify

Run from the repository root:

```powershell
py -B tools/analyze_cinematic_scenes.py
py -B tools/verify_cinematic_scenes.py
py -B -m unittest discover -s tests -p test_cinematic_scene_analysis.py -v
```

The analyzer needs checked compressed all-quest evidence and registered local
project raw sources. The raw verifier additionally needs the six matching
scene exports under `.tmp/quest-deep-dives/universal/raw`, or `--raw-root`
pointing to another identical extraction. Reconstruct that frozen input with
the all-quest method's collector if the cache is missing. A changed input hash
requires regenerating and reviewing the research, not silently treating it as
the old snapshot.

`--data`, `--out` and `--docs` on the analyzer allow isolated regeneration.
Use the corresponding `--data`/`--docs` on the verifier. Markdown links assume
the documented repository output layout. Deterministic regeneration is checked
by comparing the default and isolated analysis/case hashes and generated
Markdown bytes; the resulting receipt is retained in `regeneration-verification.json`.

Three focused regression tests cover separate section boundaries and omitted
timing, RID index/resource/serial separation, and escaped JSON pointer keys.
Corpus verification independently checks all input hashes, event totals,
unique journal identities, dossier presence and per-quest totals. These are
source-integrity and reporting checks. This pass does not run a build,
serialize resources, launch the game or establish installed behavior.
