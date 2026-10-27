# Workspots: Discovery And Quest Reuse

A workspot is a behavior tree for an actor's animation performance, not a
single pose. The `.workspot` resource names animation sets and rigs, then
organizes idles, clips, pauses, reactions, entry/exit animations, transitions,
and item actions. The animation samples live in the referenced `.anims`
resources. A filename alone cannot establish what the complete performance
looks like or whether it fits a new actor and location.

`tools/workspot_catalog.py` builds a local SQLite/FTS5 database, detailed JSON,
and a self-contained HTML browser from the actual extracted resources. It
searches animation names and reviewed descriptions as well as filenames.

The initial local inventory on 2026-10-26 contains **3,881 distinct depot
paths** (3,043 under `base`, 838 under `ep1`) and **11,053 distinct animation
names**, excluding the `<no_auto_transition>` control token. All extracted
resources decoded and indexed successfully. The selected project and vanilla
scene corpus supplies direct usage references for 194 workspots; it is not a
full world/scene scan. Five examples have structural descriptions; none of
these catalog reviews claims visual or runtime verification.

## Resource And Placement Boundaries

| Layer | Contribution | What still needs checking |
| --- | --- | --- |
| `.workspot` / `workWorkspotTree` | Entry hierarchy, animation names, rig/animset registrations, item policy, props, transitions | Actual motion, complete dependency availability, rig and body compatibility |
| `worldAISpotNode` | World position/orientation, spot resource, world NodeRef, AI spot flags | Navmesh approach, interaction alignment, actor ownership and lifetime |
| Community | Spawn/entry assignment, period and spot sequencing, persistent spot registration | Activation, spawn readiness, movement and cleanup |
| Scene external workspot data | Resource `dataId` and positioned `workspotInstanceId` | Correct instance binding, performer ownership, section/event timing and exits |
| Device/entity workspot component | Named resource binding for device-driven interactions | Component setup, interaction logic, prop equipment, player camera and cancellation |

Our existing `tools/generate_world.py` emits AI spots and community persistent
data. `tools/generate_scene.py` can emit `UseWorkspot` / `StopWorkspot` nodes;
its world-spot path uses `questUseWorkspotParamsV1.workspotNode`. A scene-local
instance uses a different binding (`scnUseSceneWorkspotParamsV1`), which should
be taken from a matching vanilla scene rather than substituted blindly.

For scene-local lookup, follow the workspot instance ID to the instance's
`dataId`, then to the matching external workspot resource registration.
For a world AI spot, follow `spot.resource`. An entity-driven interaction
can instead reference the resource through `workWorkspotResourceComponent`.
Do not apply the invisible-device scripting recipe to every native quest scene.

## Read The Tree, Not Just The Name

- `workSequence` / `workRandomList` contain children in `list`; their `idleAnim`
  matters even if there is no `workAnimClip` beneath them.
- `workAnimClip` names a clip. `workAnimClipWithItem` also carries item actions.
- `workEntryAnim`, `workExitAnim`, and `workTransitionAnim` carry different
  performance roles. Preserve offsets, flags, and synchronization settings.
- `workPauseClip` supplies timing rather than a new named animation.
- Entry `id.id` is the workspot entry ID. It is **not** the JSON `HandleId`,
  a scene instance ID, a scene data ID, or an animation index.
- Tree `loopInfinitely`, world `isWorkspotInfinite`, and quest use/stop
  settings are separate controls. A finite tree does not establish that a
  community actor will leave a spot.
- `finalAnimsets` records rig-specific animation registrations. Rig paths,
  visual tag restrictions, `globalProps`, `initialActions`, and item policy
  are useful reuse evidence. A registered rig is not a compatibility test.
- Missing authored fields in native JSON can represent engine defaults.
  The catalog preserves present settings and does not invent missing values.

The local patrol guide specifically requires disabling **Is Infinite** for
finite patrol spots. Its NPC path preview does not preview workspots/look-ats;
walking the preview path is not evidence that spot performance works in game.

## Build And Search

Run from the repository root. The configured game path comes from
`tools/toolchain.py` / `toolchain.local.json`; no game path is hard-coded in
the catalog. Extraction scans vanilla `archive/pc/content` and `archive/pc/ep1`,
excluding installed mod overrides. The extraction receipt records the command,
archive file identities and WolvenKit output. It does not claim to implement
the game's mod load order.

Extraction merges into its output tree. Use a fresh `--output` directory after
changing game versions or archive selections so removed resources cannot
survive from a previous extraction. Build reports extracted binaries missing
their decoded JSON as coverage failures.

```powershell
py -B tools/workspot_catalog.py extract
py -B tools/workspot_catalog.py serialize --workers 8
py -B tools/workspot_catalog.py build `
  --usage-root projects/ghostline/source/raw `
  --usage-root projects/shared/ghostline-runtime/source/raw `
  --usage-root projects/test-quests
py -B tools/workspot_catalog.py search "hands knees"
py -B tools/workspot_catalog.py search "tablet" --limit 20
py -B tools/workspot_catalog.py search "workExitAnim" --json
py -B tools/workspot_catalog.py review
```

Open `generated/workspots/review.html`. It works offline and includes search,
review-state filtering, animation lists, rigs, animation sets, entry/loop/exit
IDs, usage pointers, and expandable full structural evidence. It renders up
to 200 matching rows at once; refine the query to reach another subset.

Global `--output` precedes the subcommand. `build --raw-root` accepts another
**mirrored depot tree** of `.workspot.json` files; `--binary-root` supplies the
matching binaries for source hashes. Do not flatten by filename: two workspots
in different depot folders can have identical basenames.

Serialization uses the pinned native reader and a generated schema. Its
resume receipt binds the binary, writer, schema, and resulting JSON hashes.
Failures return a nonzero status and are recorded in `raw/serialization.json`;
opaque workspot tree data is rejected by the catalog rather than silently
indexed as an empty performance. Inspect failures before accepting coverage.

Usage scanning is opt-in because a full world corpus is large. Each reference
retains a source filename, source SHA-256, and exact JSON pointer. Add focused
serialized vanilla scene, entity, or world-sector roots with repeatable
`--usage-root`. These are direct resource references within the selected
corpus, not a complete dependency graph or proof that a scene actually plays
that workspot. Scene instance IDs and world placement are inspected at those
pointers in the source resources using the existing explorer tools.

## Data And Human Review

Generated files under `generated/workspots` are ignored and reproducible:

| File | Purpose |
| --- | --- |
| `binary/`, `raw/` | Extracted CR2W resources and mirrored decoded evidence |
| `extraction.json`, `raw/serialization.json` | Extraction scope, converter identity and failures |
| `catalog.json` | Full structural metadata, usage, merged annotations and failures |
| `summary.json` | Inventory counts, selected input coverage and failures |
| `workspots.sqlite3` | `workspots`, `search` (FTS5), and `metadata` tables |
| `review.html` | Portable read-only search/review report |

`reference/workspots/annotations.json` is the checked human-owned layer.
Rebuilding never rewrites it. Records are keyed by the full depot path:

```json
{
  "schema_version": 1,
  "workspots": {
    "base\\workspots\\example.workspot": {
      "label": "Short human-readable action",
      "description": "Describe what was observed, including variation and transitions.",
      "status": "unreviewed",
      "tags": ["seated", "tablet"],
      "notes": "Record required furniture, prop slots, actor and alignment constraints.",
      "evidence": []
    }
  }
}
```

Statuses are `unreviewed`, `structure_reviewed`, `visually_reviewed`,
`runtime_verified`, or `rejected`. Visual/runtime review requires nonempty
`evidence` and `source_sha256`. Use the catalog's binary SHA-256 when the
binary is available, otherwise its raw SHA-256. On mismatch the merged record
becomes `stale`; the original annotation is retained for re-review.
Evidence links are stored as text, not automatically fetched or executed.

The catalog deliberately does not generate confident pose descriptions from
names. `name_hints` are searchable tokens, not reviewed labels. A useful next
review pass should collect short videos covering entry, idle variations, and
natural/forced exits. Record actor body/rig, props, furniture height, facing,
root movement, clipping, and cancellation behavior with each capture. Offline
animation playback must resolve the rig-specific animation sets and execute
the relevant tree; previewing one clip cannot validate the whole workspot.

## Offline Clip Previews And Captioning

`tools/workspot_preview.py` now plans, prepares and renders source-motion
mannequin videos and timestamped contact sheets for supported base human rigs.
See [rendering and captioning](workspot-captioning.md) for the pilot commands,
resume behavior, renderer omissions and current Transformers model shortlist.
These are clip previews; complete workspot-tree playback and runtime validation
remain separate steps.

## Quest Acceptance

Before promoting a workspot into an advanced quest, inspect a vanilla usage
where possible, verify the intended entry ID, and test the target actor in the
actual placement. Check approach versus teleport, initial alignment, idle
variation, props/equipment, interruptions, natural and forced stop, movement
after release, and repeat activation. Player workspots also need camera/input
recovery checks. Keep scene/quest exits and cleanup under the owning quest's
lifecycle contract. Do not change current GQ000 handoffs based on catalog data.

Focused regression command:

```powershell
py -B -m unittest discover -s tests -p test_workspot_catalog.py -v
```

## Sources

- Local [animation/workspot scripting guide](../../modding_docs/modding-guides/animations/animations/abusing-workspots.md), also [upstream](https://github.com/CDPR-Modding-Documentation/Cyberpunk-Modding-Docs/blob/main/modding-guides/animations/animations/abusing-workspots.md).
- Local [patrol guide](../../modding_docs/modding-guides/quest/how-to-make-npcs-patrol.md).
- Local [community registration guide](../../modding_docs/modding-guides/quest/how-to-use-worldcommunityregistry-and-worldcompiledcommunity.md).
- Local [scene workspot lookup guide](../../modding_docs/modding-guides/quest/how-to-remove-an-animation-and-potentially-replace-it.md).
- Local [holocall scene example](../../modding_docs/modding-guides/quest/custom-video-holocalls.md) for world-spot entry binding, and [Johnny scene example](../../modding_docs/modding-guides/quest/johnny-glitching-and-talking-with-v.md) for a scene-local instance.
- Pinned `WolvenKit/WolvenKit.RED4/Types/Classes/work*.cs` class definitions,
  especially `workWorkspotTree`, `workWorkspotAnimsetEntry`, `workIContainerEntry`,
  `workSequence`, `workEntryAnim`, and `workAnimClipWithItem`.
