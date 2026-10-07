# Braindance Authoring

This document owns the reusable Ghostline braindance authoring workflow.

Ghostline's braindance authoring source is a strict JSON performance spec.
`tools/braindance_scene.py` validates the spec and invokes Blender in background
mode to create an inspectable `.blend`, an animated GLB handoff, and a
deterministic metadata manifest. `tools/braindance_rid.py` consumes that
manifest and a vanilla template to build a real REDengine `.scenerid`.

The checked tooling fixture is:

`projects/test-quests/gqt005/braindance/gqt005_braindance_analysis.json`

Generated files default to `.tmp/braindance` and are not packed game resources.

## Commands

```powershell
py -B .\tools\braindance_scene.py validate `
  --spec .\projects\test-quests\gqt005\braindance\gqt005_braindance_analysis.json

py -B .\tools\braindance_scene.py plan `
  --spec .\projects\test-quests\gqt005\braindance\gqt005_braindance_analysis.json

py -B .\tools\braindance_scene.py build `
  --spec .\projects\test-quests\gqt005\braindance\gqt005_braindance_analysis.json

# After making intentional animation edits in the generated .blend:
py -B .\tools\braindance_scene.py bake `
  --spec .\projects\test-quests\gqt005\braindance\gqt005_braindance_analysis.json

# Rebuild gqt005, retarget a Kimodo SOMA BVH onto Patch, then rebake the
# existing scene handoff. The generated root trajectory is discarded so the
# authored ACTOR_patch path, cameras, clues, and entry point remain unchanged.
py -B .\tools\kimodo_braindance.py `
  --spec .\projects\test-quests\gqt005\braindance\gqt005_braindance_analysis.json `
  --bvh .\braindance\motions\kimodo\gqt005_patch_cautious_walk.bvh `
  --actor patch `
  --build-before `
  --bake-after

py -B .\tools\braindance_rid.py validate `
  .\projects\test-quests\gqt005\.tmp\braindance\gqt005\gqt005_braindance_analysis.handoff.json

py -B .\tools\braindance_rid.py compile `
  --handoff .\projects\test-quests\gqt005\.tmp\braindance\gqt005\gqt005_braindance_analysis.handoff.json `
  --template C:\path\to\sq012_braindance__part_a.scenerid `
  --actor-template Holt `
  --actor-template Holt `
  --output .\projects\test-quests\gqt005\.tmp\braindance\gqt005\gqt005_braindance_analysis.scenerid
```

The builder discovers Blender from `--blender`, `GHOSTLINE_BLENDER`, `PATH`,
the standard Blender Foundation installation directory, or Steam. Use
`--dry-run` to inspect the exact Blender command and normalized plan. Use
`--no-glb` when only the authoring `.blend` and handoff manifest are needed.

## Kimodo Motion Retargeting

`tools/kimodo_braindance.py` accepts the standard T-pose SOMA BVH exported by
NVIDIA Kimodo and retargets it onto one existing `man_base` performer. The
default destination is frames `0..149`, with smooth eight-frame entry and
15-frame exit blends into the scene's original procedural body animation.
The retarget maps the compatible torso, head, limb, eye, and finger joints;
SOMA end joints, its extra finger-tip joints, jaw, and BVH root are ignored.

This is intentionally a body-motion replacement rather than a scene-layout
replacement. The actor root animation from the checked performance spec still
owns world position and facing. That keeps a generated single-actor clip from
drifting away from braindance clue volumes or recorded-camera framing. Run with
`--dry-run` to inspect the exact Blender command. The adjacent generated
`.kimodo.json` records the mapping and discarded channels used for the bake.

## Generated Blender Contract

The generated scene contains:

- `BD_ORIGIN`: the relocatable coordinate origin;
- `ENVIRONMENT_REFERENCE`: non-shipping proxy geometry or imported GLTF;
- `ACTORS`: one `ACTOR_<id>` root per performer;
- `PROPS`: reserved for later attachment authoring;
- `CAMERAS`: the recorded-perspective camera;
- `CLUES`: visual, audio, or thermal clue markers.

Actor performer IDs follow the scene rule `actor_id * 256 + 1`. Actor roots,
the recording camera, clues, timeline markers, interpolation, frame range, and
custom Ghostline metadata are generated deterministically.

If an actor declares `asset.path`, the builder imports that `.glb` or `.gltf`
under its actor root. Without an asset it creates a colored humanoid proxy.
This makes the checked fixture buildable without proprietary game exports while
allowing a real Cyberpunk rig/mesh GLB to replace the proxy.

The checked full-body authoring contract is:

- `braindance/rigs/man_base.glb`, a clean rig-only GLB with no mesh or
  imported animation actions; and
- `braindance/rigs/man_base.skeleton.json`, the exact 71-joint RED
  skeleton order, parents, rest transforms, and trajectory-joint index.

Declare both the asset and skeleton contract on each rigged actor. The optional
`body_animation` block can generate a gait synchronized to the actor's authored
root motion:

```json
{
  "asset": {
    "path": "braindance/rigs/man_base.glb"
  },
  "rig": {
    "contract": "braindance/rigs/man_base.skeleton.json"
  },
  "body_animation": {
    "type": "walk_from_root_motion",
    "stride_length": 0.85,
    "leg_swing_degrees": 22.0,
    "knee_bend_degrees": 30.0,
    "arm_swing_degrees": 18.0,
    "phase_degrees": 0.0
  }
}
```

Blender can reorder `armature.data.bones` during GLB import. The bake therefore
resolves every pose bone by name and emits it at the index recorded by the
skeleton sidecar; Blender collection order is never treated as RED joint
order. Missing or duplicate names, a sidecar-order mismatch, or a contract-hash
mismatch fails validation.

An actor may also declare `facial` and `cyberware` RID channels. Each channel
accepts an optional channel-specific GLTF asset, an exact Blender armature
object name, and zero or more float-track bindings:

```json
{
  "facial": {
    "armature": "FaceRig",
    "tracks": [
      {
        "index": 17,
        "object": "FaceMesh",
        "data_path": "data.shape_keys.key_blocks[\"JawOpen\"].value"
      }
    ]
  },
  "cyberware": {
    "asset": {
      "path": "converted/actors/patch_cyberware.glb",
      "armature": "CyberwareRig"
    },
    "tracks": []
  }
}
```

Track indices are RED rig indices, not arbitrary labels. The bake resolves
each Blender data path to a number on every frame. Facial and cyberware
armatures are sampled independently from the body armature.

Actor transform keys animate the performer root relative to `BD_ORIGIN`.
When `body_animation` is present, the builder clears imported actions and
authors the requested body motion; otherwise animation already present in an
imported rig GLB is preserved. Custom control rigs, skeletal acting, and hand
contacts can be authored in the generated file. The `bake` command opens that
existing `.blend` without rebuilding it, evaluates every frame, and refreshes
the GLB and RID handoff. This is the path for intentional manual Blender edits.

For a rig-contract actor, the bake records all joints in the sidecar's exact
order. If an actor imports multiple armatures, set `asset.armature` to the
intended Blender object name. The selected RID template actor must have the
same bone count; the compiler fails closed on a mismatch. Proxy actors have no
armature, so they encode authored root motion on the template's trajectory
joint and may retain a compatible template full pose. That proxy fallback is
never used for a rig-contract actor.

Camera keys require a location and exactly one of:

- `rotation_degrees`; or
- `look_at`, which the builder converts to Blender's `-Z` camera direction.

Clue objects carry layer, fact, and active-frame custom properties. The handoff
manifest preserves the same fields for later `.scene` generation.

`rid_signature` is optional on actors and the recording camera. It defaults to
the actor `id` and `Camera`, respectively. Use it when the RID event signature
in the consuming `.scene` must differ from the authoring object name.

## RID Compiler

The existing CLI scripts remain the public entry points. Their implementation
is divided under `tools/braindance_support`: `rid_types` and `rid_codec` own
pure metadata/animation operations; `rid_compile` assembles authored samples;
`rid_validation` independently checks handoffs and compiled output; `rid_io`
owns WolvenKit conversion and binary verification. SIMD preview decoding stays
in its existing preview tool because it describes a different representation.

The compiler accepts either a binary `.scenerid` or WolvenKit's serialized
`.scenerid.json`. A suitable test template is the vanilla resource:

```text
base\animations\quest\side_quests\sq012\sq012_braindance\rid\
sq012_braindance__part_a.scenerid
```

The template supplies compatible RED layouts, handle shapes, actor bone/track
cardinality, camera record structure, and the full-pose fallback needed only
by a proxy actor. The named Holt actor slot is therefore a structural template,
not an animation source. For a rig-contract actor the compiler rebuilds the
complete body buffer from Blender samples and never merges or retains Holt's
pose channels or compressed pose bytes. The template itself is not copied into
Ghostline source control. Repeat `--actor-template` in handoff actor order to
select rig-compatible structural layouts by their vanilla RID signatures.
When omitted, the compiler uses the first animated actor slots.

The compiler:

- prunes unused template actors and cameras;
- assigns deterministic actor, body-animation, camera, and camera-animation
  tags and serial numbers;
- applies each actor's first authored transform relative to `BD_ORIGIN`;
- samples evaluated actor roots, pose bones, camera transforms, and focal
  length at the authored frame rate;
- samples separate facial and cyberware armatures plus declared Blender float
  properties at the same rate;
- encodes new RED compressed-animation buffers with normalized times, RED
  quaternion packing, per-joint TRS channels, and all seven camera tracks;
- emits `facialAnimations` and `cyberwareAnimations` as new compressed
  buffers when those channels are declared, validating their joint and track
  indices against the selected vanilla layout;
- moves actor trajectory samples into
  `animSplineCompressedMotionExtraction`, using RED's logical root joint `0`
  while retaining the rig's `trajectoryBoneIndex`, and writes matching scene
  root-motion and camera LOD samples;
- invokes the built WolvenKit CLI for CR2W serialization;
- checks CR2W magic, serial/handle uniqueness, counts, signatures, durations,
  key payload sizes, joint/track indices, and sampled curve checkpoints;
- serializes the generated binary back to JSON, repeats semantic validation,
  and requires every custom animation-buffer hash to remain identical.

Alongside the binary it writes:

- `<name>.scenerid.json`, the exact authored WolvenKit document;
- `<name>.rid-report.json`, including source hashes, encoded joints/channels,
  animation-buffer hashes, output hash, and both validation passes.

The checked `gqt005` build uses the full 71-joint contract for both Patch and
the guard. Each actor receives a newly encoded pose buffer and motion
extraction; their buffer hashes differ from Holt's structural template and
from each other. The RID report records the expected and authored pose-joint
counts with `template_pose_fallback_used: false` for both actors.

## Scene, Quest, And Depot Integration

Scene linkage stays in `tools/braindance_pipeline.py`. The support package keeps
clue construction and independent clue auditing together in `clues`, uses the
read-only `SceneGraphIndex` for graph queries, and audits actor/camera/lifecycle
contracts in `scene_audit`. `publication` owns CR2W conversion, depot staging,
and hash-bound runtime evidence. The validators inspect emitted structures;
they do not regenerate expected output with the production builder.

`tools/braindance_pipeline.py` links the compiled RID to an authored
rewindable scene template. It rebuilds all RID resource/reference tables,
binds body events by performer, binds facial and cyberware events by performer
and component, binds the RID camera, retimes playback, retargets scene-origin
markers, and fills clue layer/fact/time data from the handoff.

```powershell
py -B .\tools\braindance_pipeline.py link-scene `
  --scene-template C:\path\to\authored_bd.scene.json `
  --rid-json .\projects\test-quests\gqt005\.tmp\braindance\gqt005\gqt005_braindance_analysis.scenerid.json `
  --handoff .\projects\test-quests\gqt005\.tmp\braindance\gqt005\gqt005_braindance_analysis.handoff.json `
  --rid-depot-path mod\gqt005\braindance\gqt005_braindance_analysis.scenerid `
  --scene-origin '#gqt005_bd_origin' `
  --camera-ref '#gqt005_bd_camera' `
  --output .\projects\test-quests\gqt005\source\raw\mod\gqt005\scenes\gqt005_braindance_analysis.scene.json `
  --binary-output .\projects\test-quests\gqt005\source\archive\mod\gqt005\scenes\gqt005_braindance_analysis.scene
```

The template must already define its actors, camera prop, functional
`bdview`/`bdfog`/`bdsetup` props, rewindable section, both BD visibility
events, playback event slots, exit point, and interruption scenario.
The camera prop must resolve `--camera-ref` to a `worldEntityNode` backed by
`engine\scenesystem\camera.ent` (or another compatible camera entity) in a
registered streaming sector. The `.scenerid` remains a normal depot resource
referenced by the scene; it does not receive its own ArchiveXL registration.

The vanilla BD support props do not spawn at the scene origin. SQ012 and Q004
use a second always-loaded `worldStaticMarkerNode` with an empty
`scnSceneMarker` payload. GQT005 mirrors SQ012's local support-marker offset
`(-9.85009765625, -0.0001220703125, -0.40000152587890625)` and targets
`bdview`, `bdfog`, and `bdsetup` at `#gqt005_bdview_spawner`; clue entities and
actors remain relative to `#gqt005_bd_origin`. The origin itself is a populated
`scnSceneMarker`. Its animation-event entries are generated from the linked
scene's retained editor event IDs and that scene's own root-motion start/end
transforms, rather than copying donor actor coordinates. This pairing supplies
the vanilla view/fog/setup placement contract while keeping the authored scene
relocatable.

The linker fails if any handoff body/facial/cyberware/camera clip lacks a
matching playback event, if a playback event uses an unmapped performer, or if
required clue layers are absent.

The quest linker retargets the single scene node in a braindance questphase
template, including the real `scnWorldMarker.nodeRef` shape, and requires a
pause/cleanup gate:

```powershell
py -B .\tools\braindance_pipeline.py link-quest `
  --quest-template C:\path\to\authored_bd.questphase.json `
  --scene-depot-path mod\gqt005\scenes\gqt005_braindance_analysis.scene `
  --scene-origin '#gqt005_bd_origin' `
  --output .\projects\test-quests\gqt005\source\raw\mod\gqt005\phases\gqt005_review_braindance.questphase.json `
  --binary-output .\projects\test-quests\gqt005\source\archive\mod\gqt005\phases\gqt005_review_braindance.questphase
```

Both commands can invoke the pinned WolvenKit CLI directly. Production assets
can then be copied to validated depot paths with a hash manifest:

```powershell
py -B .\tools\braindance_pipeline.py package `
  --asset 'projects\test-quests\gqt005\.tmp\braindance\gqt005\gqt005_braindance_analysis.scenerid=mod\gqt005\braindance\gqt005_braindance_analysis.scenerid' `
  --asset 'projects\test-quests\gqt005\source\archive\mod\gqt005\scenes\gqt005_braindance_analysis.scene=mod\gqt005\scenes\gqt005_braindance_analysis.scene' `
  --asset 'projects\test-quests\gqt005\source\archive\mod\gqt005\phases\gqt005_review_braindance.questphase=mod\gqt005\phases\gqt005_review_braindance.questphase' `
  --depot-root .\projects\test-quests\gqt005\source\archive `
  --manifest .\projects\test-quests\gqt005\.tmp\braindance\gqt005\package.json
```

Only `mod\...` and deliberate `base\...` depot paths are accepted. Escapes,
duplicates, missing inputs, and copy hash mismatches fail closed.

For the checked test quest, `projects/test-quests/gqt005/implementation/build.py` performs the
complete promotion. It authors a lightweight Patch-only launcher with a
`Play braindance` choice using the vanilla
`ChoiceCaptionParts.BraindanceIcon`, a short actor-acquisition section, and
Patch/V performer symbols. The quest waits for the whole Patch community,
then starts the launcher immediately. The persistent actor-attached choice
owns interaction distance instead of depending on a separate world-trigger
gate. The launcher emits `play_braindance` into a separate three-node
rewindable scene with explicit Patch/guard/V performer symbols. The generator
links the authored RID and visual/audio/thermal clues, compiles the root and
child phases, creates journal/localization/world resources, serializes routine
template-backed resources with WolvenKit by default, and writes the package
manifest. The native writer remains an explicit differential-test option, and
its onscreen-localization path uses the typed codec so default
`primaryKey = 0` fields remain implicit.

## Runtime Evidence

Structural readiness is not labeled as an in-game pass. Runtime evidence is
bound to the exact packaged hashes and requires all eight cases: forward seek,
backward rewind, visual/audio/thermal layer switching, normal cleanup,
interrupted cleanup, and replay after cleanup.

```powershell
py -B .\tools\braindance_pipeline.py runtime-init `
  --name gqt005_braindance_analysis `
  --package-manifest .\projects\test-quests\gqt005\.tmp\braindance\gqt005\package.json `
  --output .\projects\test-quests\gqt005\.tmp\braindance\gqt005\runtime-evidence.json

py -B .\tools\braindance_pipeline.py runtime-record `
  --evidence .\projects\test-quests\gqt005\.tmp\braindance\gqt005\runtime-evidence.json `
  --case seek_forward --passed --notes 'Clean-save test at 8.0 seconds'

py -B .\tools\braindance_pipeline.py runtime-verify `
  --evidence .\projects\test-quests\gqt005\.tmp\braindance\gqt005\runtime-evidence.json `
  --depot-root .\projects\test-quests\gqt005\source\archive
```

`runtime-verify` fails until every case is recorded as passed and every
packaged file still matches the tested hash.

## Support Boundary

The working pipeline is now:

```text
performance JSON
  -> Blender scene
  -> evaluated per-frame actor/bone/camera samples
  -> newly encoded RED animation buffers
  -> .scenerid + JSON/report
```

The animation compiler covers body/root motion, indexed body/facial/cyberware
armature TRS, arbitrary facial float tracks, camera transform, focal length,
and all camera float tracks. No `.anims` transplant is required, and the
checked `man_base.glb` is an authoring rig rather than a donor animation clip.

The report records
`animation_source.mode: authored_blender_samples_encoded`,
`custom_skeletal_animation: true`, `custom_facial_animation`,
`custom_cyberware_animation`, and `custom_camera_buffer: true`.

Scene RID-table/event linkage, quest scene-node linkage, CR2W conversion,
production depot staging, and hash-bound runtime evidence are implemented.
Actual runtime cases remain unpassed until a person runs the generated
candidate in game and records each result; the tooling deliberately cannot
turn a structural audit into runtime evidence.
