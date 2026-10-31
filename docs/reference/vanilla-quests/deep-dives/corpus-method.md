# Full corpus: method, coverage and reproduction

This is the earlier **130-entry side/minor snapshot**. The current
[all-quest method](all-quests-method.md) supersedes its scope and reproduction
recipe. Shared helpers have since gained root/launch support, stricter call
and shared-graph scoping, and performance extraction. This snapshot's recorded
tool/document hashes describe its original inspection; they are not hashes of
the revised utilities. Its frozen resource and evidence identities remain
separate from the all-quest snapshot.

The [catalogue](catalogue/README.md) expands the two pilot studies to all
**130 `SideQuest`/`MinorQuest` journal entries** in the saved local export,
including Phantom Liberty. It deliberately includes untitled/internal and
ambiguous entries so omissions are visible. Gigs, NCPD activities and main jobs
are not added as independent dossiers unless the export classifies the entry
as a side/minor quest; their implementation resources can still be dependencies.

The journal paths divide into 114 outside `ep1/` and 16 under `ep1/`. This is a
journal namespace count, not an assertion about expansion ownership: follow-up
jobs and update content can use different depot and journal namespaces.

## What is complete, and what remains unproven

Every inventory entry has a dossier. The corpus build currently finds:

- **122 journal-linked entries:** exact `gameJournalPath.realPath` matches in
  decoded graph nodes, their connected sockets, relevant embedded graphs,
  forward phase/scene/community dependencies and resolved parent call sites.
- **One POI-linked entry:** Water Runs Dry has a corresponding POI in
  `ep1/quest/minor_quests/mq300/mq300.questphase`. Its quest-journal activation
  is not established by that link.
- **Seven unresolved entries:** the dossier retains journal objectives and
  any discovery hints but does not fabricate a phase/scene trace.

| Unresolved journal entry | Exact journal identity |
| --- | --- |
| NO_TITLE | `quests/side_quest/sq022_head_hunter` |
| Murk Man Returns Again Once More Forever | `quests/minor_quest/mq046_cave_vehicle` |
| Dressed to Kill | `quests/minor_quest/mq047_ad_vehicle` |
| One More Hour | `quests/minor_quest/mq402_stargazing` |
| Don't Sleep on the Subway | `quests/minor_quest/ue_metro_start` |
| Cyberpsychosis | `quests/side_quest/sq_cyberpsychos_regina` |
| Quartz "Bandit" | `quests/vehicle_metaquest/archer_bandit` |

“Unresolved” does not mean cut, inactive, impossible, or nonexistent. Journal
exports, world/entity scripts, compiled references and different game builds can
have different coverage. The source corpus and exact-path discovery probes are
recorded; these entries need an additional ownership/implementation investigation
before a behavioral block can be attributed to them.

The two pilot dossiers remain manually reviewed narrative/technical studies.
The expansion is **generated structural analysis**, with targeted source checks
and a [cross-quest synthesis](cross-quest-patterns.md). It does not claim the
same degree of manual branch-by-branch narrative review for every quest, and
none of the candidates gains runtime proof from this pass.

## Source snapshot

The checked [source selection](../../../../reference/quests/deep-dives/catalogue/source-selection.json)
lists **4,575 resources**, each with archive origin, binary SHA-256, serialized
JSON SHA-256 and serializer identity:

| Archive | Resources selected |
| --- | --- |
| `content/basegame_4_gamedata.archive` | 1,726 |
| `ep1/ep1_2_gamedata.archive` | 2,848 |
| `content/basegame_1_engine.archive` | 1 |

The base gamedata selection covers side/minor quest families and repair phases,
plus required shared main-quest/world resources. The expansion gamedata pass
includes supporting quest, world and community resources. Additional direct
graph references and global discovery/orchestration roots were extracted by
exact path. The engine archive supplies `vset_v.scene`.

For duplicate depot identities in the two gamedata archives, the expansion
archive was extracted after the base archive. This is an explicit research
selection, not a full simulation of installed hotfix/mod archive precedence.
Individual payload hashes identify the snapshot; archive-wide hashes were not
computed. Serializer `GameVersion` header values are not used to establish the
installed executable's version.

Native serialization produced 4,561 resources. Fourteen UTF-8 decoding
exceptions were recovered through WolvenKit. The selection records each
resource's actual serializer. The pilot evidence remains a separate snapshot;
it was not overwritten by the expansion.

Full provenance is in
[corpus provenance](../../../../reference/quests/deep-dives/catalogue/provenance.json).
The saved [journal input](../../../../reference/quests/deep-dives/catalogue/journal-input.json)
retains titles, paths, hashes and objective structure from the external export,
with its source hash. This makes catalogue generation independent of the
external export once the snapshot is saved.

## Tracing rules

1. Match complete journal roots and descendants, never a title alone. A POI
   match has its own weaker status and does not substitute for quest activation.
2. Locate matching nodes by resource, graph handle and graph-local ID. Preserve
   JSON pointers and socket edges; IDs repeat in different embedded graphs.
3. Include descendants of a journal-bearing embedded graph, even if the child
   has no journal nodes. Machine Gun's milestone graph is a concrete example of
   gameplay that an objective-only scan would miss.
   In a dedicated family file containing an anchor, retain sibling embedded
   graphs as shared context too: setup/progress can precede journal activation.
   Global shared masters stay scoped to matching embedded graphs and their
   descendants. The exact anchor list remains distinct from contextual graphs.
4. Follow phase/scene/community references forward. Follow actual phase/scene
   call sites backward for parent context; a scene-state condition referencing
   a resource is not classified as a call.
5. Keep shared masters and sibling quest families identifiable. A resource
   appearing in a dependency context is not exclusively owned by that quest.
6. Record the actual called entry, consumed output and nonterminating interface.
   Retain raw scene socket stamps and embedded quest-node input mappings.
7. Join screenplay option IDs to locstring IDs and embedded option labels.
   Report option-level conditions without claiming they are the entire
   eligibility rule; parent routes can add gates.
8. Pair fact writers and readers as **data dependencies**, not execution edges.
   Preserve explicit values/comparisons and leave omitted RED defaults omitted.
9. Identify repair and test/debug paths separately. Filename/directory role
   labels are evidence hints, not proof of runtime reachability. Historical
   version references remain listed but their graphs are not merged into
   current scenes.
10. Propose block contracts from actual stored types and locations. Their
    occurrence counts include dependency/repair context and are not counts of
    independent player experiences or isolated implementations.

The full corpus verified **411,198 source node pointers**: 238,715 quest nodes
in 9,782 root/embedded quest graphs and 172,483 scene nodes. All indexed graph
endpoints resolved; raw reference/fact pointers were checked too. These counts
include shared, test and repair resources and are not counts of reachable
side-quest gameplay nodes.

Remaining boundaries include transitive character/mesh/animation ownership,
world NodeRef definitions and streaming sectors, numeric TweakDB names,
full spoken subtitle/VO/lipsync joins, engine/save migration behavior and
runtime reachability. A direct graph resource missing from the selected
archives stays listed in the relevant dossier. Exact-path archive probes are
[recorded](../../../../reference/quests/deep-dives/catalogue/discovery-probes.json).

The dependency-closure search leaves nine direct graph identities unresolved:
six declared stunt scenes in the mq027 context, an `old` SSI-HQ scene in sq006,
the sq021 VR-game scene and the sq024 vehicle-hacking-manager phase. Their
references are retained in the dossiers. None was found by the recorded
exact-path probes of the selected non-language content/expansion archives;
that search result does not establish whether a branch is active or cut.

## Query checked evidence

Compressed shards keep the checked corpus manageable. They are JSON encoded
with deterministic gzip, grouped by depot family; gzip is storage only, not a
different data model. The
[manifest](../../../../reference/quests/deep-dives/catalogue/evidence-manifest.json)
records each shard hash. The query helper reads the checked shards directly:

```powershell
py -B tools/query_sidequest_evidence.py --quest 'Machine Gun'
py -B tools/query_sidequest_evidence.py --quest 'Machine Gun' `
  --resource 'mq007.questphase' --graph h606 --node 70
py -B tools/query_sidequest_evidence.py --quest 'The Hunt' `
  --resource 'sq021_randys_room.questphase' --graph h237 --node 191
py -B tools/query_sidequest_evidence.py --quest 'Shot by Both Sides' `
  --facts 'mq305_both_killed'
```

Use a full journal path for ambiguous `NO_TITLE` entries. `--node` requires a
graph namespace. The existing `explore_questphase.py` / `explore_scene.py`
helpers remain available against the reproduced raw scratch files.

## Reproduce extraction, indexing and dossiers

Run from the repository root with the configured local toolchain:

```powershell
# Replays only the checked explicit resource selection and verifies payloads.
py -B tools/collect_sidequest_evidence.py `
  --scratch .tmp/quest-deep-dives/replay

# Builds verified, resumable per-resource records.
py -B tools/index_sidequest_corpus.py `
  --raw-root .tmp/quest-deep-dives/replay/raw `
  --binary-root .tmp/quest-deep-dives/replay/cr2w `
  --cache .tmp/quest-deep-dives/replay/indexed --workers 4

# Regenerates the catalogue, compressed evidence and expanded contracts.
py -B tools/build_sidequest_catalogue.py `
  --cache .tmp/quest-deep-dives/replay/indexed

# Checks coverage, shard hashes, graph endpoints, exact raw pointers and links.
py -B tools/verify_sidequest_catalogue.py `
  --raw-root .tmp/quest-deep-dives/replay/raw `
  --binary-root .tmp/quest-deep-dives/replay/cr2w
```

The collector restores the recorded JSON header (diagnostic path/timestamp
metadata) after conversion, without altering `Data`, so another scratch path
can reproduce the frozen raw identity. It checks binary and raw JSON hashes
separately and stops if either differs. A mismatch requires toolchain/source
review and new provenance before publishing regenerated evidence.
Deterministic catalogue regeneration is tested against the same frozen raw
inputs; a fresh serializer/toolchain snapshot may require new provenance even
when game payloads are unchanged.

The collector requires the selected payload hashes to match and fails if an
archive update changed them. It does not install, pack, edit or overwrite game
assets. The corpus utilities and documentation are research artifacts; existing
Ghostline compiler/runtime behavior is unchanged.
