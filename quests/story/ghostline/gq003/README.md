# Black Lantern (`gq003`)

## Status And Scope

This is the narrative and implementation authoring package for the first
90-120 minute Ghostline quest. The canonical 36-stage compiler manifest,
objective copy, persistent state, phone threads, readable documents, two Iris
scenes, choice consequences, item/reward records, and provisional Mara
character manifest are authored and validated.

No final world origins are selected yet. The manifest therefore keeps all 36
stages `planned` and uses clearly named placeholder NodeRefs, communities,
prefabs, devices, triggers, routes, and vehicle records. Its complete graph
compiles for inspection, including the freight-yard parallel monitor,
stage-scoped prefab bindings, retry-blocking Mara defense, outcome-dependent
core/delivery, and multi-contact debrief topology.

The generated journal contains 28 objective phases, 23 quest mappins, ten phone
conversations, and five readable/computer entries. Both Iris scenes have scene
specs, CR2W-JSON, subtitles, subtitle maps, and VO maps. They deliberately have
no WEM audio yet. The poster reference is
`images/gq003-black-lantern-poster.png`.

## Narrative Contract

Iris has finished reconstructing the Quiet Spine cache recovered through
`gq001`. Its payload proves that Quiet Spine moves each identity in
two human couriers:

- the mnemonic subject carries memory fragments disguised as lived experience;
- the cipher courier carries the encrypted instructions needed to identify and
  reconstruct those fragments;
- neither courier can expose the route alone;
- the Kabuki tenant classifier disabled in `gq002` selected candidates whose
  disappearance would create little corporate or legal noise.

The relay shutdown forces Pair 07 into an expedited handoff. V can save Mara
Venn, the mnemonic subject, but the recovered cipher can still reconstruct the
identities of every person processed through Black Lantern. Morrow wants the
index left intact long enough to trace K. Morita. Iris wants the index erased.
Patch knew that Quiet Spine used people and concealed it from V, although he
claims he did not know that the implanted noise contained recoverable lives.

The final choice is not whether Mara lives. V saves Mara on the critical path.
The choice is whether saving the route's former and future subjects requires
destroying the best lead to its operator.

**Journal title:** Black Lantern

**Journal description:** Quiet Spine moved stolen identities through paired
human couriers. Rescue Mara Venn, recover her reconstruction cipher, and decide
whether the route is evidence worth preserving or a weapon that must be
destroyed.

## Pacing Budget

The 36 typed stages only reach the 90-120 minute target if the locations carry
real traversal and encounter space. Target the following first-play budget:

| Sequence | Target minutes |
| --- | ---: |
| Iris offer, report, and first scene | 10-14 |
| Freight-yard infiltration and investigation | 15-20 |
| Clinic assault, rescue, escort, and defense | 22-28 |
| Safe-site scene and Patch confrontation | 9-12 |
| Vehicle theft and two drives | 12-16 |
| Relay combat, investigation, and choice | 18-24 |
| Delivery and debrief | 5-7 |
| **Total** | **91-121** |

Do not pad the target with long passive waits. The transfer-window gate should
advance game time or allow the player to skip it, and each drive should carry
new dialogue or visual information.

## Documents

- [Canonical runtime flow](flow.md)
- [Act summaries](acts/)
- [Dialogue and text](script/)
- [Persistent state](implementation/state.md)
- [Assets](implementation/assets.md)
- [World selection](implementation/world.md)
- [Scene and tooling decisions](implementation/scenes.md)
- [Authoring plan](implementation/plan.md)
- [Continuity consequences](continuity.md)

## Build

Black Lantern is not shipping-buildable yet. Its complete planned graph and
location-independent content can be generated and validated, but world
selection, world/AI authoring, promoted CR2W binaries, ArchiveXL registration,
voice production, and in-game verification remain.

Validate the preproduction manifest with:

```powershell
py -B .\tools\quest_compiler.py validate `
  .\quests\story\ghostline\gq003\implementation\quest.json
```

Validation succeeds while every stage remains explicitly `planned`. Generate
the inspectable graph with:

```powershell
py -B .\tools\quest_compiler.py compile `
  .\quests\story\ghostline\gq003\implementation\quest.json `
  --out .\generated\gq003\gq003.questphase.json `
  --plan .\generated\gq003\gq003.plan.json `
  --allow-planned
```

Regenerate the journal and onscreen localization with:

```powershell
py -B .\quests\story\ghostline\gq003\implementation\build.py
```

Do not treat generated output as playable: placeholder world NodeRefs and
missing world/AI resources still prevent runtime integration. The Mara stage
emits no normal progression on failure and is preceded by a checkpoint with
`retryOnFailure`; automatic reload remains an explicit in-game validation item.
Do not register or pack the partial quest to silence warnings; the remaining
sequence is tracked in [the implementation plan](implementation/plan.md).
