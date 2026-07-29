# Black Lantern (`gq003`)

## Status And Scope

This is the narrative and implementation preproduction brief for the first
90-120 minute Ghostline quest. It defines the canonical 36-stage route,
objective copy, persistent state, text-only dialogue, readable documents,
ambient lines, choice consequences, and the remaining tooling decisions.

No locations, world origins, NodeRefs, communities, journal entries,
localization IDs, scene specs, quest manifest, or packed resources are selected
yet. The poster reference is `images/gq003-black-lantern-poster.png`.

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

Black Lantern is not buildable yet. It has no checked quest manifest, scene
specs, world origins, localization IDs, or CR2W resources.

The first build command becomes available after
`implementation/quest.json` is authored and every unresolved NodeRef or asset
is either selected or explicitly marked planned:

```powershell
py -B .\tools\quest_compiler.py validate `
  .\quests\story\ghostline\gq003\implementation\quest.json
```

Do not create placeholder packed resources merely to make this section
executable; the remaining authoring sequence is tracked in
[the implementation plan](implementation/plan.md).
