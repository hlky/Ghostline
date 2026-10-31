# Vanilla quest deep dives

The [cinematic scene study](cinematic-scenes/README.md) compares animation,
gaze, camera, prop, sound and scene-to-gameplay choreography across all 416
journal identities and 3,139 scene resources. It includes per-quest dossiers,
six manually inspected source cases and a comparison with Ghostline's current
scene authoring.

The research now includes the [all-quest catalogue](all-quests/README.md),
covering all 416 journal entries across every stored quest type, including
Phantom Liberty. Start with [scope and evidence](all-quests-method.md),
[manual synthesis](all-quest-synthesis.md), [connected patterns](all-quest-findings.md),
[mechanism contracts](all-quest-blocks.md) and the
[implementation-family inventory](implementation-families/README.md).
The [Ghostline reduction plan](ghostline-block-roadmap.md) maps the findings
to existing stage/lifecycle seams and concrete promotion criteria.

The earlier [side/minor quest catalogue](catalogue/README.md),
covering 130 base-game and Phantom Liberty journal entries. Start with its
[method and coverage](corpus-method.md), [expanded block contracts](expanded-blocks.md)
and [cross-quest compositions](cross-quest-patterns.md). Unresolved entries are
explicitly marked; generated structural dossiers and manually reviewed pilot
studies retain distinct proof/review status.

## Manually reviewed pilot

Inspected 2026-10-27. These dossiers reverse-engineer **Space Oddity (mq003)**
and **Happy Together (mq010)** into candidate Ghostline building blocks.
Both are player-facing side jobs, stored by RED as `MinorQuest` resources.

Start with:

- [Space Oddity](space-oddity.md): alternate access routes, scan investigation,
  device activation, staged vehicle arrivals, combat counting, loot and cleanup.
- [Happy Together](happy-together.md): staged meetings, delayed return,
  concurrent optional investigation, knowledge-gated choices and consequences.
- [Building-block catalogue](building-blocks.md): proposed contracts, existing
  Ghostline overlap, isolation boundaries and acceptance cases.

## Evidence and confidence

The source is the local installation's
`K:/Cyberpunk 2077/archive/pc/content/basegame_4_gamedata.archive`, extracted with
WolvenKit and serialized with the repository's native `ghostline-red` and RED
schema. This is an explicit base-game archive snapshot, **not a claim that
all installed mods, expansion overrides or save migrations were evaluated**.
See [provenance](../../../../reference/quests/deep-dives/provenance.json).

The two machine-readable indexes retain extracted-binary and raw-JSON hashes,
depot paths, exact JSON pointers, graph-local node IDs, handles, socket edges,
scene entry/exit names, actors, choice text, speech-event bindings, fact uses,
community entries and direct resource/NodeRef/journal/TweakDBID references:

- [mq003 evidence](../../../../reference/quests/deep-dives/mq003.evidence.json)
- [mq010 evidence](../../../../reference/quests/deep-dives/mq010.evidence.json)

The pilot extracted and serialized 52 resources. Of these, 21 historical scene
versions have identity records only; the other 31 are structurally indexed,
including two test scenes and five bugfix phases. There are 53 quest graphs
(embedded graphs included), 1,048 quest nodes and 924 scene nodes. Counts include
test and repair structures and are not counts of player-reachable gameplay.

Evidence locators in the dossiers use `file / graph hN / node ID` for phases
and `file / scene nID` for scenes. IDs repeat across embedded graphs. The
`pointer` beside each indexed node locates it in that resource's serialized
JSON. A graph handle is a serialization locator, not a stable engine identity.

Three labels apply throughout:

- **Observed:** stored node data and connected sockets in this snapshot.
- **Interpretation:** the player-facing meaning suggested by that structure.
- **Proposed:** a Ghostline reduction or API, not implemented by this research.

Omitted RED defaults remain omitted in the evidence. Do not read a missing
boolean, fact-write value, comparison or node mode as an explicitly authored
zero/false. Named `NonTerminating` outputs are especially important: they can
notify the parent without finishing their child phase.

The existing [journal references](../side-jobs.md) supply titles, premise and
objective labels. Their displayed objective order is journal hierarchy order,
not execution order. Their source export predates this extraction; current
graph edges and journal paths control the technical traces here.

## Coverage boundaries

The dossiers follow the selected roots through their directly referenced
phases, embedded graphs and production scenes. They also inspect the extracted
communities, alternate phase files and repair phases. They identify dependencies
on world prefabs, scene markers, workspots, splines, device persistent state,
TweakDB records and localization resources.

They do **not** claim a transitive asset closure. World NodeRef definitions and
their streaming-sector owners, full character/mesh/animation dependencies,
resolved numeric TweakDB record names, spoken subtitle/VO payload joins,
global quest-root eligibility and installed save behavior remain unresolved.
Scene line-to-locstring bindings are retained; that is not an audio-content audit.
The three production mq003 scenes and five production mq010 scenes are traced;
historical scenes and chicken-test scenes are not treated as active story flow.

No game assets, runtime generators, compiler behavior or installed package were
changed. These are static research candidates, not new runtime-proven templates.

## Reproduce

Run from the repository root. The output paths are ignored scratch trees; the
checked evidence and prose live outside project `source` trees.

```powershell
& 'H:/WolvenKit.Console-8.17.4/WolvenKit.CLI.exe' unbundle `
  'K:/Cyberpunk 2077/archive/pc/content/basegame_4_gamedata.archive' `
  -o '.tmp/quest-deep-dives/cr2w' `
  -r 'base\\quest\\(minor_quests|bugfixing\\minor_quests)\\(mq003|mq010)\\.*\.(questphase|scene|community)$'

# Ensure the schema matches the local toolchain first.
py -B -c "import sys; sys.path.insert(0, 'tools'); from ghostline_red import ensure_schema; ensure_schema()"

$diveBinaryRoot = (Resolve-Path '.tmp/quest-deep-dives/cr2w').Path
$diveRawRoot = Join-Path (Get-Location) '.tmp/quest-deep-dives/raw'
Get-ChildItem -LiteralPath $diveBinaryRoot -Recurse -File | ForEach-Object {
  $diveRelative = [IO.Path]::GetRelativePath($diveBinaryRoot, $_.FullName)
  $diveOutput = Join-Path $diveRawRoot ($diveRelative + '.json')
  New-Item -ItemType Directory -Force -Path (Split-Path $diveOutput) | Out-Null
  & './tools/ghostline-red/target/release/ghostline-red.exe' cr2w-serialize `
    $_.FullName $diveOutput --schema './red-schema.json'
  if ($LASTEXITCODE -ne 0) { throw "Serialization failed: $diveRelative" }
}

py -B tools/build_quest_deep_dive_evidence.py `
  --raw-root .tmp/quest-deep-dives/raw `
  --binary-root .tmp/quest-deep-dives/cr2w `
  --out reference/quests/deep-dives

# Focused source inspection:
py -B tools/explore_questphase.py `
  -f .tmp/quest-deep-dives/raw/base/quest/minor_quests/mq010/mq010.questphase.json edges
py -B tools/explore_scene.py `
  -f .tmp/quest-deep-dives/raw/base/quest/minor_quests/mq010/scenes/mq010_04_police_talk.scene.json choices
```

The exporter rejects unresolved graph endpoints. It preserves embedded graphs
separately and deliberately records historical versions by hash only. Re-running
it on the same serialized inputs should produce identical evidence files.
If the source archive/toolchain changes, refresh provenance and review the prose.

## Reference guidance used

- [Quest/scene workflow](../../../../agent/skills/ghostline-quest-journal-scene/SKILL.md)
- [CR2W workflow](../../../../agent/skills/ghostline-wolvenkit-cr2w/SKILL.md)
- [Scene lifecycle](../../../authoring/scenes.md)
- [Existing isolated block corpus](../../../../reference/vanilla_quest_blocks/README.md)
- [Local modding node reference](../../../../modding_docs/modding-guides/quest/scene-node-definitions.md)
- [Local socket reference](../../../../modding_docs/modding-guides/quest/name-and-ordinals-sockets-101.md)

Source sockets take precedence over generic diagrams when reconstructing an
individual scene-to-phase boundary.
