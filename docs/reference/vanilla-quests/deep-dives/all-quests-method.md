# All quest types: scope, evidence and reproduction

This pass covers **all 416 quest entries in the saved local journal export**:
92 MainQuest, 90 StreetStory, 83 MinorQuest, 48 Contract, 47 SideQuest,
36 VehicleQuest, 17 CyberPsycho, two CourierSideQuest and one CourierQuest.
There are 361 paths outside `ep1/` and 55 inside it. Namespace is not expansion
ownership. These are journal identities, not a verified count of distinct
playable experiences: internal, duplicate-looking, umbrella and historical
entries remain visible. Unjournaled implementations receive a separate
[resource-family inventory](implementation-families/README.md).

Start with the [416-entry catalogue](all-quests/README.md),
[manual synthesis](all-quest-synthesis.md),
[connected paths and per-quest findings](all-quest-findings.md) and
[candidate mechanism contracts](all-quest-blocks.md).
The earlier [130-entry snapshot](corpus-method.md) and two manual pilot studies
remain separate historical research artifacts.

## Evidence layers

1. **Journal intent:** the saved export supplies premise, objectives, stored
   type, exact path and hash. Objective order is not execution order.
2. **Stored flow:** every indexed node retains its raw JSON pointer, graph
   namespace and socket edges. Embedded graphs have explicit owning-node
   handoffs. Scene interfaces, choices, actors, fact uses and speech bindings
   remain queryable.
3. **Execution context:** actual phase/scene call nodes and community bindings
   expand the forward graph context. Scene-state inspections and other resource
   bindings remain dependencies; they do not import an unrelated graph as a
   called child. Parent calls and launch definitions are separate context.
   In shared masters, exact journal nodes and their immediate socket neighbors
   define the selected context; embedded graphs owned by those nodes are
   retained. Selecting a master's root graph does not import all its siblings.
   A resource coordinating multiple exported quests receives the same local
   treatment when its dedicated depot family belongs to another quest. This
   prevents a shared journal/setup reference from importing that other quest's
   entire implementation; single-owner off-directory matches remain intact.
4. **Bindings:** exact resource hashes are matched against archive indexes.
   All matching vanilla providers are retained, without inventing load order.
   A matching index entry establishes availability; only explicitly indexed
   resources have decoded content evidence in this pass.
5. **Reduction proposals:** repeated connected paths and mechanism contracts
   suggest Ghostline blocks. They are not implemented compiler features or
   runtime-proven templates.

The generated dossiers are structural deep dives, supplemented by manual
source review and synthesis. They do **not** claim hundreds of manually played
or narratively reviewed quests. The two original pilots retain their deeper
manual review status. No installed game test is performed by these tools.

## Resource selection

The snapshot includes **13,943 resources**: 3,837 questphases, 734 `.quest`
roots, 822 `.gamedef` launch definitions, 3,139 scenes and 5,411 communities.
It indexes 22,760 quest graphs, 449,719 quest nodes and 303,769 scene nodes:
**753,488 source node pointers** in total. Counts include shared, test,
repair, ambient and launch contexts, rather than only reachable quest flow.

All nonhistorical resources of those five types were extracted from base
gamedata and then ep1 gamedata. Ep1 wins duplicate depot paths in this explicit
research selection. Recursive exact-path closure adds five scenes from the
engine and world archives. The [source selection](../../../../reference/quests/deep-dives/all-quests/source-selection.json)
records binary/raw SHA-256, provider archive, serializer identity and frozen
diagnostic JSON headers. Archive entry size and SHA1 are independently checked
against every selected binary, alongside its SHA-256.

The supporting ownership pass indexes 18 vanilla archives, including English
text/voice providers, containing 504,395 archive entries. This is not a
simulation of hotfix/mod precedence. Archive-index SHA1 is stored metadata;
payload SHA-256 is separately computed. Numeric TweakDB names, engine defaults,
installed executable version and active launch selection are not guessed.

`.quest` roots can contain authoring launch scaffolding next to production
phase calls. When phase/scene journal anchors exist, root journal references
are retained as activation context instead of importing their sibling setup
graphs into the primary flow. A root-only match remains explicit source
evidence, not proof that the installed game selects that launch route.

## Attribution and gaps

The final catalogue contains **371 journal-linked entries, 17 POI-only
associations and 28 unresolved identities**. Eighteen unresolved identities are
stored as MainQuest entries under version-tracking or template namespaces.
Every VehicleQuest, CyberPsycho and courier entry has an exact journal link;
that link can be an inspection, repair or retirement operation and does not by
itself establish an active playable route.

An exact complete quest path or descendant match is `journal-linked`. A POI
association is labelled separately and does not establish quest activation.
POI folders can flatten the region folders present in the journal; the tool
uses explicit minor-activity/street-story path transforms and records actual
matched paths. Filename/family hints never substitute for a verified match.
The [coverage table and gap register](all-quest-gaps.md) retain every unresolved
identity and POI-only association by exact path and stored type.

Unresolved journal identities receive dossiers with their exported intent and
the missing attribution. Missing direct graph resources, historical version
references and test/debug targets remain distinct. The full closure search
found 62 current graph identities without matches in the inspected vanilla
indexes; that total includes ambient, demo and test context. It is not a count
of broken playable quests or evidence that those branches are active or cut.

World NodeRefs remain registered-path/alias bindings unless a streaming owner
is explicitly resolved. Archive ownership of an entity or workspot does not
prove its controller or animation behavior. The pass retains spoken-line
bindings, but does not claim complete subtitle/VO/lipsync timing validation.
Mesh/texture closure, device/engine/script fact producers, save migration,
branch reachability and installed behavior require their own evidence.

The separate performance index retains scene section events, raw event-handle
pointers, authored timing fields, screenplay lines and interruption definitions.
All event pointers are checked against raw source data. Section events from
different routes are not flattened into an invented global chronology. Full
animation, VO and lipsync payload validation remains a separate boundary.
It contains **318,424 event occurrences across 3,139 scenes and 41 event
types**, including dialogue, skeletal animation, socket signaling, look-at,
idle-animation, VFX, IK, audio and gameplay transitions.

## Connected-pattern extraction

The miner enumerates every directed three-distinct-node, two-edge path in the
indexed graph namespaces. A signature contains the exact node/operation types
and both input/output socket labels. Recurrent candidates must occur in at
least two resources and contain a mechanism-bearing type. Pure routing paths
are filtered. Full occurrences retain source pointers and **every edge crossing
the three-node boundary**, including cut connections. This is a local shape
match, not graph isomorphism of entire quests or behavioral equivalence.
The snapshot contains 57,776 recurrent signatures and 713,216 occurrences;
these are structural extraction seeds, rather than 57,776 proposed compiler
features. The mechanism catalogue contains 36 candidate contracts.

Per-quest candidate lists respect selected embedded scopes. Forward dependency
contexts can still be shared and are identified as such. Fact writer/reader
links are data dependencies, never invented execution edges. Fact pointers
belong to their nearest containing graph node, so embedded-child writes are
not duplicated onto an enclosing phase node. Source operation defaults remain
omitted. Concrete values and bindings stay available beside the candidates.
The global fact index distinguishes explicit `questSetVar_NodeType` writes,
known comparison reads and other fact-name bindings. Achievement progress,
photo-mode callbacks and braindance clue events are retained as other uses
unless additional evidence establishes their direction; a field named
`factName` is not automatically classified as a reader or writer.

Before promoting a candidate, expand its boundary to include setup, actor/world
readiness, alternate exits, cancellation and cleanup; parameterize bindings;
then test already-satisfied predicates, interruption/re-entry, parallel event
order, save/load, reward delivery and once-only outcome commitment in game.

## Reproduction and queries

Run from the repository root. The frozen collector checks identities and does
not require the external journal export:

```powershell
py -B tools/collect_sidequest_evidence.py --selection reference/quests/deep-dives/all-quests/source-selection.json --scratch .tmp/all-quest-replay
py -B tools/index_sidequest_corpus.py --raw-root .tmp/all-quest-replay/raw --binary-root .tmp/all-quest-replay/cr2w --cache .tmp/all-quest-replay/indexed --workers 4
py -B tools/build_sidequest_catalogue.py --cache .tmp/all-quest-replay/indexed --journal reference/quests/deep-dives/all-quests/journal-input.json --data-out reference/quests/deep-dives/all-quests --docs-out docs/reference/vanilla-quests/deep-dives/all-quests --method all-quests-method.md --contracts all-quest-blocks.md
py -B tools/index_quest_archive_owners.py --out .tmp/all-quest-replay/archive-indexes
py -B tools/analyze_quest_corpus.py --data reference/quests/deep-dives/all-quests --docs docs/reference/vanilla-quests/deep-dives/all-quests --archive-indexes .tmp/all-quest-replay/archive-indexes
py -B tools/index_quest_scene_performances.py --data reference/quests/deep-dives/all-quests --docs docs/reference/vanilla-quests/deep-dives/all-quests --raw-root .tmp/all-quest-replay/raw
py -B tools/verify_sidequest_catalogue.py --data reference/quests/deep-dives/all-quests --dossier-subdir all-quests --raw-root .tmp/all-quest-replay/raw --binary-root .tmp/all-quest-replay/cr2w
py -B tools/verify_quest_analysis.py --data reference/quests/deep-dives/all-quests
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest 'Somewhat Damaged' --resource q305_bunker_hunt_timing.questphase --graph h0 --node 74
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest 'Gig: Hippocratic Oath' --events --event-type PlaySkAnim
```

The filenames of earlier helpers retain `sidequest` for compatibility; the
all-quest input and output arguments control this expanded scope. Regenerating
the catalogue replaces generated dossiers; run the analysis step afterward
to restore their connected-pattern and dependency supplements. Provider-index
metadata includes source archive timestamps, so an archive update requires
new provenance rather than silently reusing the old snapshot.
