# Character Creation Pipeline

This document defines the target workflow for building Ghostline NPCs from a
small character specification. Patch is the first migration target. The goal
is to make normal character creation a select-and-build operation, with no
interactive Blender work required for an ordinary player-derived head.

The schema-v1 generator, curated Patch catalog, headless head build, live WebGL
head preview, installed-game asset index, and local web UI now exist. Patch's
reviewed design manifest has been applied to the shipping raw/packed appearance
and installed for focused runtime validation. The immutable original template
and original catalog selections remain available as a semantic regression
baseline. The temporary
shape-22 head smoke test proved the toolchain but was later shown to be a
geometry no-op rather than Patch's intended face.

## Current Reference Set

The design is based on:

- the current local Redmodding NPV guides in `modding_docs`;
- the character-creator and head cheat sheets in `modding_docs`;
- the downloaded NPV WolvenKit template at
  `H:\projects\tutorial_npv_wolvenkit_2_3-8328-4-0-9-1778610090`;
- Patch's packed and raw entity/appearance resources; and
- the installed game files under `H:\Cyberpunk 2077`.

The download directory labels the template as `4.0.9`, but the template files
do not contain an embedded version marker. Treat the directory name as
provenance, not as a machine-verifiable resource version.

Local tool versions checked on 2026-07-22:

- WolvenKit CLI: `H:\WolvenKit.Console-8.17.4\WolvenKit.CLI.exe`;
- Blender 5.1 with Cyberpunk IO Suite 1.8.0;
- Blender 4.4 without the Cyberpunk IO Suite.

Pin the selected Blender executable and add-on version in generated build
metadata. Do not silently fall back to another installed Blender version.

## What The Audit Established

### Root entity

Patch's `patch.ent` and the template's male `_your_male_character.ent` both
have 110 root components. After ignoring the appearance list, export timestamp,
and intended `defaultAppearance` change (`random` to `default`), their
serialized data is identical.

This makes the root entity a versioned template, not character-authored data.
The generator should clone a vetted male or female root, replace its appearance
entries and paths, and leave the engine-facing component graph intact.

Patch exposes one root appearance:

```text
ghostline_patch_default
  appearanceName: default
  resource: mod\ghostline\characters\patch\patch.app
```

These names serve different layers. Spawners, community phases, AMM lists, and
the root entity's `defaultAppearance` use the exposed root mapping name
`ghostline_patch_default`. Only `entTemplateAppearance.appearanceName` uses the
internal `.app` definition name `default`. Requesting the internal name from a
community creates a logical puppet that scenes can acquire, but leaves it with
no renderable appearance.

The downloaded male template exposes `casual` and `business` from the root and
contains `naked`, `casual`, and `business` definitions in its `.app`. The
generator must make the root list, `.app` names, TweakDB record, and requested
world appearance agree.

### Appearance

Patch's `default` appearance has 47 components. It includes:

- the male facial rig and facial animation setup;
- custom-path head, eyes, teeth, eyebrows, beard, makeup, scar/tattoo and
  personal-link meshes;
- male player body, arm, nail and genital meshes;
- hairstyle, dangle graph and shadow mesh;
- inner-torso, leg, shoe and face-accessory clothing components; and
- visual-controller, shadow, external and garment-support components.

The visible choices are data in the `.app`: mesh depot path, mesh appearance,
chunk mask, bind name, component type, and supporting components. They do not
need Blender. Clothing selection belongs in the same model as face overlays and
hair rather than in a separate handwritten editing workflow.

Patch still contains a disabled `h0_cyberware_face` component whose numeric
resource did not resolve. Numeric-only resource IDs are not acceptable output
from the future generator unless the validator can resolve them against the
game or staged mod assets.

### Head geometry

The template's `head_import.blend` contains three scripts:

1. `00_import_files.py` imports every adjacent `.morphtarget.glb`;
2. `01_apply_shapekeys.py` maps character-creator choices for eyes, nose,
   mouth, jaw, and ears to shape keys and applies them; and
3. `02_export_files.py` uses the Cyberpunk IO Suite to write import-ready
   `.glb` files.

This work can run in background Blender. Blender is still a geometry build
dependency, but it does not need to be a manual authoring step. A wrapper can
inject the five shape choices, execute the embedded operations in order, and
fail on missing morph targets, missing add-on modules, or absent output files.

The guide warns that a few creator indices are offset by one from their shape
key indices. Those exceptions must live in a versioned mapping table. The UI
must not hide an unverified guess behind a successful build result.

The exported male GLBs make one specific mismatch measurable. They contain
Basis plus 20 named variants per region, `h01` through `h20`. The embedded NPV
script subtracts one from the requested creator value, so values 2 through 21
select those targets and value 1 leaves Basis. Documented value 22 requests
missing `h21` and therefore also leaves Basis. Ghostline blocks 22 and derives
the browser's available target map from each GLB's `extras.targetNames`; it must
not infer success from Blender's process exit code.

## Source Of Truth: Character Manifest

Each character should have one reviewed JSON manifest. It describes intent;
generated CR2W-JSON and binaries remain build products until the migration is
proven. An abridged representative shape is:

```json
{
  "schema_version": 1,
  "id": "patch",
  "namespace": "mod\\ghostline\\characters\\patch",
  "frame": "male_average",
  "catalog": "source/characters/catalog.json",
  "entity": {
    "root_appearance": "ghostline_patch_default",
    "appearance_name": "default",
    "appearance_file": "patch.app"
  },
  "appearance": {
    "template_name": "default",
    "name": "default",
    "selections": {
      "hair": "patch_dread_undercut",
      "inner_torso": "patch_longsleeve",
      "legs": "patch_scavenger_pants",
      "feet": "patch_military_boots",
      "face_accessory": "patch_braindance_specs"
    },
    "indexed_overrides": {
      "inner_torso": {
        "depot_path": "base\\characters\\garment\\player_equipment\\torso\\t1_087_shirt__high_collar\\t1_087_pma_shirt__high_collar.mesh",
        "mesh_appearance": "quest005_grey"
      },
      "legs": {
        "depot_path": "base\\characters\\garment\\player_equipment\\legs\\l1_021_pants__cargo_computer\\l1_021_pma_pants__cargo_computer.mesh",
        "mesh_appearance": "camo_black"
      }
    }
  },
  "head": {
    "shapes": {
      "eyes": null,
      "nose": null,
      "mouth": null,
      "jaw": null,
      "ears": null
    }
  },
  "tweak": {
    "record": "Character.GhostlinePatch",
    "display_name": "gq_npc_patch",
    "voice_tag": "gq_patch",
    "affiliation": "Factions.Ghostline"
  },
  "requirements": {
    "phantom_liberty": true
  }
}
```

`null` head-shape values are intentional in this example: Patch's current
geometry does not record the original character-creator preset. The migration
must recover or deliberately choose those values before regenerating his head.

Catalog entries should contain the verbose CR2W details so manifests can stay
small. A clothing selection should resolve to a complete component bundle,
including shadows, cuffs, feet state, garment components and chunk masks where
required, rather than only a `.mesh` path. `indexed_overrides` is the current
provisional bridge: it replaces the primary mesh and real mesh-appearance name
inside a reviewed catalog bundle while retaining that bundle's companion
components.

## Current Patch Design

Patch's quest role is a low-profile signal broker: controlled, technically
equipped, and careful not to read as a gang or consumer brand. The reviewed
2026-07-22 creator pass therefore uses a dark practical silhouette with the
distinctive face details carrying most of the color:

- black-carbon `hh_146` asymmetrical dread undercut, including its vanilla
  animation graph, dangle rig, bindings, and NPC shadow;
- muted `quest005_grey` high-collar fitted shirt;
- `camo_black` computer cargo trousers;
- the existing black/red military boots and red/black braindance specs; and
- the existing spiral eyes, magenta brows, rose beard, gold earring, black/gold
  nails, and other authored face details.

The hair option is a complete reviewed catalog bundle. Its primary component
changes class, its skinning target changes, and two parent bindings are created
with deterministic unused CR2W handle IDs in both appearance copies. The two
indexed garments remain provisional primary-mesh substitutions: the old shirt
cuff and trouser shadow companions remain until rich bundle resolution can
replace them. This reviewed design is now the installed test candidate. Keep
future generated variants isolated until the hair animation, garment fit,
scene participation, LODs, and stream-out/in behavior pass in-game tests.

## Build Stages

The command-line build engine comes before the UI. Both must invoke the same
deterministic stages:

1. Validate the manifest and resolve every selected catalog entry.
2. Clone the pinned root `.ent` template and create its appearance mappings.
3. Create `.app` appearances from reusable component bundles.
4. Copy or extract required head/body resources into the character's unique
   `mod\...` namespace and rewrite all internal references.
5. Export selected head morphtargets to GLB with WolvenKit.
6. Run the pinned Blender executable in background mode to apply the selected
   shape keys and export mesh GLBs.
7. Import the GLBs back into the character's staged CR2W meshes with WolvenKit.
8. Generate the TweakXL character record and requested localization entries.
9. Run static validation, CR2W round trips, and an isolated archive build.
10. Emit a build report containing inputs, tool versions, generated files,
    dependencies, warnings, and hashes.

The generator must stage into a temporary/output tree first. It should update
`source/raw`, `source/archive`, and loose resources only through an explicit
apply step so a failed build cannot leave half a character in the project.

Current implementation:

- `tools/character_builder.py` validates manifests, generates isolated source
  files, compares Patch with its handwritten baseline, and runs the complete
  WolvenKit -> Blender -> WolvenKit head build;
- `tools/character_head_blender.py` executes the template's embedded scripts in
  background Blender and injects manifest shape values without editing the
  `.blend` file;
- `source/characters/patch.character.json` is Patch's schema-v1 manifest;
- `source/characters/catalog.json` is the first curated bundle catalog; and
- `tools/character_asset_index.py` derives searchable installed-game assets,
  real mesh appearances, and isolated mesh previews; and
- `tools/character_ui.py` serves the local UI from `tools/character_ui`, wires
  indexed PMA clothing selection into the same generator, and keeps generated
  files under ignored `converted/characters` output.

## Catalogs

The old NPV part picker is useful as a UI reference, but not as current source
data. The Redmodding cheat sheets state that it does not cover the newer 2.2+
appearances. Ghostline should build and own versioned machine-readable catalogs
from current inputs.

### Head and body catalog

Seed this catalog from the current cheat sheets and NPV template. Store:

- creator option number and game version;
- male/female frame compatibility;
- mesh and morphtarget depot paths;
- mesh appearance names;
- component/bind names and chunk masks;
- paired resources such as beard shadow, hair shadow, dangle graph, rig, and
  facial setup; and
- known creator-to-shape-key index corrections.

### Clothing catalog

Generate candidates from player-equipment and compatible NPC garment paths in
the game archive. For each selectable item, inspect the CR2W resource rather
than inferring behavior from its filename. Store:

- slot and body-frame compatibility;
- mesh path and all appearances;
- component type and bind name;
- chunk masks, garment-support needs and dependent pieces;
- expected body/feet state and shadow meshes; and
- expansion requirement.

The reviewed bundle catalog does not need committed thumbnails; the UI creates
isolated previews on demand. It still needs correct paths and complete bundles.

Do not commit copied vanilla binaries merely to populate a catalog. Paths and
derived compatibility metadata are sufficient; extraction happens locally
during a build.

The first generated path index now queries the current base appearance and EP1
gamedata archives. On the 2026-07-22 install it records 4,965 assets: 1,329
player-equipment records, 1,528 hair records, 1,772 head records, 144 body
records, and 192 player-item appearance resources. Of those, 3,560 are meshes
that can be previewed. The JSON lives under ignored
`converted/character-index`; it is derived machine state, not reviewed catalog
source.

PMA primary clothing meshes in the indexed `torso`, `legs`, and `feet` slots
are now directly selectable. Preview preparation serializes the exact cooked
`.mesh` to ignored CR2W-JSON metadata, reads its real
`meshMeshAppearance.name` values, and lets the user assign one of those values
to the outfit. Generation updates the slot's primary component in both the
normal and `compiledData` appearance copies. It deliberately keeps the curated
slot's cuff/shadow companion, so each new combination still needs in-game fit
validation.

This path layer is intentionally not the final bundle catalog. The next
enrichment pass must follow item/TweakDB records through root entity appearance
mappings, `.app` definitions, component/control entities, mesh appearances,
chunk masks, visual tags, parts overrides, animation/physics dependencies, and
the material graph. Archive provider and effective load-order winner must be
retained because current game archives contain changed duplicate paths and a
small number of unresolved numeric-only hashes.

The 2026-07-22 in-process audit bounds that richer pass. The effective player
wardrobe has 158 item-controller `.app` files containing 5,031 appearance
definitions and 12,850 components; those definitions reference 739 unique
meshes. Parsing those meshes exposes 13,839 mesh-appearance entries and 17,628
material entries. All resources parsed successfully in roughly 30 seconds after
WolvenKit service initialization, so full metadata indexing is practical
without bulk uncooking.

Use a small long-lived C# helper against the installed WolvenKit assemblies for
that stage. Initialize `HashService`, `ArchiveManager`, and `Red4ParserService`
once; extract selected `FileEntry` values to memory; retain path hash, nullable
resolved path, every provider archive, and the effective load-order winner. CET's
`tweakdbstr.kark` can initialize `TweakDBIDPool` before reading
`tweakdb_ep1.bin`, making the current 40,482 `Items.*` records resolvable.
Clothing records then supply equipment area, tags, entity name, and appearance
stem, while the exact component-to-mesh link still comes from the `.app` rather
than a filename guess.

Fingerprint the rich cache with archive size/mtime/index identity, TweakDB and
string-table identity, WolvenKit version, and catalog schema version. Preview
cache keys should include effective mesh SHA-1, mesh appearance, and exporter
settings.

## UI Boundary

The target UI is a thin front end over the manifest and generator. It should
provide:

- character identity, body frame and skin controls;
- face shape selectors with current option ranges;
- hair, beard, makeup, cyberware, scar, tattoo and piercing selectors;
- clothing slots with appearance variants and compatibility filtering;
- multiple named outfits backed by one character `.app`;
- dependency and conflict warnings before build;
- a manifest diff before applying generated files; and
- build, validate and package actions with readable error output.

A local web UI is the current frontend. It calls the same Python library/CLI as
the command line and contains no CR2W mutation logic. A pinned local Three.js
runtime loads WolvenKit's standard glTF output, gives orbit/zoom controls, and
applies the same named facial targets client-side as the final Blender script.
Changing a head value is therefore immediate; Blender is needed only to bake
the reviewed face into import-ready game meshes.

The UI also searches the generated installed-game index and can uncook a
selected `.mesh` into an isolated GLB preview cache. For supported PMA torso,
legs, and feet primary meshes it presents the appearances read from that exact
resource and provides `Use in outfit`; the selected override appears in the
outfit summary and is consumed by both validation and generation. Those item
previews use a neutral material today, and changing the selected mesh
appearance does not yet recolor the isolated GLB. Exact skin, hair, and
multilayer garment presentation requires RED material extraction/conversion or
baking. Preview fit also does not establish NPC runtime fit: player garment
support is driven by the equipped item system and is not automatically applied
to NPC appearance components.

The HTTP boundary is local-only and server-owned. It rejects non-loopback bind
addresses, ignores client attempts to replace template/source/tool paths,
serializes mutation jobs, serves generated files only from a character-specific
allowlisted root, and writes reports atomically. Preview cache fingerprints
include source/provider, tool, game, and exporter identities so upgrades cannot
silently retain stale geometry. Indexed assignments are re-resolved against the
server-owned installed-game index; category, PMA frame, primary-mesh role,
depot path, and appearance membership are checked again before the manifest is
accepted. PMA compatibility is taken from the final mesh filename rather than
parent-directory tokens, and failed cache refreshes cannot promote old geometry
or appearance metadata under a new fingerprint.

In-engine validation remains mandatory for clipping, garment behavior, facial
animation, materials, LODs, and streaming.

## Validation Contract

A generated character is not ready because WolvenKit produced CR2W files. At a
minimum, validation must prove:

- all depot paths are explicit and resolve to a staged mod or installed game
  resource;
- all authored resources are under the character's unique `mod\...` namespace;
- no generated file creates a `base\...` global override;
- root appearance names, `.app` appearance names, world selections and the
  TweakDB entity path agree; world/default selections must use the exposed root
  mapping name, not the internal `.app` definition name;
- component names are unique where the engine requires them;
- required companion pieces exist for hair and clothing bundles;
- every expansion path agrees with the manifest's declared requirements;
- the selected Blender add-on imports and exports all requested head meshes;
- WolvenKit re-import and serialize/deserialize round trips succeed; and
- the packed archive contains the expected payload and no temporary files.

Runtime validation remains mandatory for spawn, approach, facial animation,
scene participation, clothing deformation, LOD changes and streaming out/in.

## Patch Migration Plan

Patch should prove the pipeline without changing the stable quest lifecycle:

1. Install TweakXL and test the applied Patch entity/appearance independently
   of further character-generator changes. TweakXL 1.11.3 and the first
   shipping candidate are installed; runtime validation is pending.
2. Record or choose Patch's five head-shape values.
3. Encode the current 47-component `default` appearance as catalog selections
   plus explicit escape-hatch components where catalog support is incomplete.
4. Generate Patch into an isolated output tree and compare it with the current
   raw and packed resources.
5. Remove the unresolved cyberware component and eliminate global `base\...`
   overrides by custom-pathing all required head support resources.
6. Decide whether to remove the inherited Phantom Liberty references from the
   root template or declare the dependency. The current male template and
   Patch entity contain the same 17 `ep1\...` string occurrences; this is a
   template issue, not Patch-authored appearance data.
7. Spawn and stream the applied Patch through the current isolated-delta gq000
   world test.
8. Run the complete phone-to-cache regression with
   `Character.GhostlinePatch`; the registry is restored in the installed
   candidate.

## First Implementation Slice

The first slice is complete:

1. Schema version 1 supports a male-average character with one appearance.
2. The curated catalog contains Patch's current hair, inner torso, legs, feet,
   and face-accessory bundles plus safe disable choices. It also contains the
   reviewed `hh_146` dread-undercut bundle with its complete binding topology.
3. The CLI generates `.ent`, `.app`, TweakXL and localization into an isolated
   output directory.
4. The original Patch selections remain semantically equivalent to all four
   original baselines. The reviewed design manifest is now applied to the
   shipping `.app`; its entity, localization, and TweakXL outputs remain
   equivalent to their shipping sources, and `compare` checks those applied
   outputs.
5. A full smoke test selected Patch's 13 morphtargets, requested temporary
   shape value `22`, exported 13 GLBs, rebuilt 13 meshes with WolvenKit,
   verified every `CR2W` header, and recorded SHA-256 hashes. The later GLB
   audit established that 22 applies no named target, so this proves the build
   mechanics only. WolvenKit's garment-support warnings still need runtime
   interpretation.
6. The local web UI uses the same manifest, catalog, validator, generator, and
   head builder as the CLI. It renders the real 100-target core head, updates
   verified values 1 through 21 live, and passed browser QA on the actual GLB.
7. The installed-game index currently exposes 4,965 searchable character asset
   records. An indexed Patch military boot was successfully uncooked on demand,
   served through the allowlisted preview route, loaded by the same viewer, set
   to its real `black_red` appearance, assigned to the feet slot, and accepted
   by full manifest validation. Indexed PMA torso, legs, and feet primary
   components are covered in both appearance copies by regression tests.
8. A complete creator pass selected Patch's black-carbon `hh_146` dread
   undercut, `quest005_grey` high-collar shirt, `camo_black` computer cargos,
   existing military boots, and existing braindance specs. Browser and CLI
   generation produced the same `.app` SHA-256 and the 105 generated handles
   are unique (`0` through `104`). WolvenKit deserialized that isolated JSON to
   a 14,178-byte CR2W and serialized it back with all 105 handles unique and the
   hair component class, resources, appearance, and bindings preserved. The
   six `CruidDict` values are regenerated by WolvenKit on each `.app`
   deserialize/serialize pass, so validate this resource structurally rather
   than requiring byte-identical `.app` round trips.

The next slice is typed catalog enrichment and whole-character composition:
replace the provisional primary-mesh-plus-curated-companion model with full
clothing/control-entity bundles, carry material and visibility metadata,
assemble compatible head/body/clothing layers in one preview scene, and add a
fresh-character command that derives all output paths and record names from a
new identity. Indexed hair, head, arms, and player-item appearance resources
remain discovery/preview-only; reviewed hair options can already be added as
complete curated bundles. Patch's actual five shape values and the documented
option-22 mismatch must be resolved before replacing his current head meshes.

## References

- `modding_docs/modding-guides/npcs/npv-v-as-custom-npc`
- `modding_docs/for-mod-creators-theory/references-lists-and-overviews/cheat-sheet-character-creator.md`
- `modding_docs/for-mod-creators-theory/references-lists-and-overviews/cheat-sheet-head`
- `agent/skills/ghostline-character-tweaks/SKILL.md`
- `docs/packaging.md`
