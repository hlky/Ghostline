---
name: ghostline-character-tweaks
description: Use for Ghostline character resources, Patch NPC work, entity and appearance files, TweakXL YAML records, custom factions, and keeping entity/template/localization references in sync.
---

# Ghostline Character And Tweak Workflow

## Current Runtime State

The production world spec names logical community entry `patch/default` and
maps it to `Character.GhostlinePatch`. The preceding Judy route is the
crash-free scene/world baseline; the current installed candidate changes only
the Patch appearance and community character relative to that candidate, so
custom entity, appearance, TweakDB, faction, and dependency behavior remain
isolated runtime variables.

The local game install audited on 2026-07-22 has ArchiveXL and TweakXL 1.11.3.
The TweakXL plugin was installed immediately before the Patch candidate and has
not yet produced a launch-time log. Confirm it loads before interpreting a
missing or failed Patch spawn as a character-resource defect.

## Character Resources

Read `docs/character-creation-pipeline.md` before building or restructuring a
player-derived NPC. It records the audited NPV template relationship, proposed
character manifest/catalog boundary, headless Blender path, validation contract,
and Patch migration order.

- `.ent` files are top-level entity containers.
- For NPCs, the root `.ent` is the game entry point and lists appearances that
  resolve into `.app` files.
- `.app` files hold appearance definitions and per-appearance components.
- Components on the root `.ent` are shared across appearances.
- Components in the `.app` are appearance-specific.
- For Patch, keep the root `.ent` and referenced `.app` appearance names in
  sync with the TweakDB `entityTemplatePath` and character record.
- Keep the two appearance namespaces distinct: communities/spawners and
  `defaultAppearance` use the root mapping `name`
  (`ghostline_patch_default`), while `appearanceName` selects the internal
  `.app` definition (`default`). Using the internal name in the community can
  spawn a scene-acquirable but invisible puppet.

Patch resources:

- packed root entity: `source/archive/mod/ghostline/characters/patch/patch.ent`
- packed appearance: `source/archive/mod/ghostline/characters/patch/patch.app`
- raw root entity: `source/raw/mod/ghostline/characters/patch/patch.ent.json`
- raw appearance: `source/raw/mod/ghostline/characters/patch/patch.app.json`
- supporting body/head files live under
  `source/archive/mod/ghostline/characters/patch/body` and
  `source/archive/mod/ghostline/characters/patch/head`.
- Patch still references some `ep1\...` resources, so Phantom Liberty may be a
  runtime dependency unless those references are replaced. The downloaded male
  NPV template has the same 17 `ep1\...` string occurrences in its root entity,
  so address this in the reusable root template rather than Patch's appearance.
- `source/archive/base` contains copied player-head support resources. They are
  global overrides and remain a shipping risk; do not infer that they are safe
  merely because the Judy isolation route works.

Generic Ghostline onscreen localization:

- packed: `source/archive/mod/ghostline/localization/en-us/onscreens/ghostline.json`
- raw: `source/raw/mod/ghostline/localization/en-us/onscreens/ghostline.json.json`
- includes Patch's display name and the Ghostline faction name.

Use `tools/explore_ent_app.py` as documented in `docs/tooling.md` to inspect entity and
appearance resources.

Patch's root entity was compared with the downloaded NPV male template on
2026-07-22. Both contain 110 root components. After excluding appearance
mappings, export timestamp, and the intentional `defaultAppearance` value, the
serialized documents are identical. Clone a pinned and validated root template;
do not reconstruct that component graph per character.

The downloaded female NPV root is independently pinned at
`source/characters/templates/npv-female.ent.json`; its paired appearance is
`npv-female.app.json`. The female root has 116 components and the appearance
declares `WomanAverage`, so never derive a female character by relabeling the
male root. `tools/character_builder.py` owns the `male_average`/`female_average`
profiles that bind entity type, PMA/PWA filename token, preview source, and head
range. Manifests, template identities, catalogs, and indexed assignments must
all agree with that profile.

The local NPV `head_import.blend` embeds import, shape-key application, and
export scripts. Blender 5.1 has Cyberpunk IO Suite 1.8.0 installed, while the
local Blender 4.4 does not. `tools/character_builder.py head` now performs the
complete selected-morphtarget export, background Blender shape application,
GLB export, and WolvenKit CR2W rebuild. A 13-mesh Patch-subset smoke test passed
through the toolchain, but the later GLB audit proved that temporary shape value
22 selected no target: the male files contain Basis plus `h01` through `h20`,
not `h21`. The male profile permits the mechanically verified range 1 through
21. The female PWA core contains 21 named variants per region, including
`h21`, so the female profile permits 1 through 22. The smoke run also emitted
WolvenKit garment-support warnings; do not apply generated meshes to shipping
characters or treat the warning as resolved without runtime validation.

Character authoring inputs:

- `source/characters/patch.character.json`
- `source/characters/catalog.json`
- `source/characters/female-example.character.json`
- `source/characters/female-catalog.json`
- `source/characters/templates/npv-female.ent.json`
- `source/characters/templates/npv-female.app.json`
- `tools/character_builder.py`
- `tools/character_asset_index.py`
- `tools/character_ui.py` and `tools/character_ui/*`

The current generator produces `.ent`, `.app`, TweakXL, and localization in an
isolated output tree. Patch's immutable original appearance template lives at
`source/characters/templates/patch-original.app.json`. The reviewed design
manifest has been applied to the shipping raw/packed `.app`; `compare` now
checks generated output against the applied source paths and reports all four
documents equivalent. Keep new UI generation isolated under
`converted/characters` until it is explicitly reviewed and applied.

The female example additionally stages only tutorial meshes referenced by its
selected appearance. The template stores those paths as numeric ResourcePath
hashes, so the builder recognizes their lowercase FNV-1a values, rewrites them
to explicit character-owned paths before generation, and permits only the exact
mapped hashes after a WolvenKit round trip. The female full-body mesh embeds
texture paths under `tutorial\npv\your_female_character`; its four required
texture resources are staged at that original namespace until the internal mesh
references are patched. The female root also retains EP1 references, so the
checked example declares Phantom Liberty and is not yet shipping content.

The local UI uses a pinned Three.js runtime to render the real morph-target GLB
and applies creator values as browser morph influences. The
`character_builder.py preview` command prepares that GLB without Blender.
`character_asset_index.py` derives
searchable candidates from the current installed archives and can uncook a
selected mesh for a neutral-material preview. It also serializes the exact
cooked mesh to ignored CR2W-JSON so the UI can enumerate real
`meshMeshAppearance` names. PMA primary meshes in `torso`, `legs`, and `feet`
may be assigned for Patch; PWA primary meshes in `torso` and `legs` may be
assigned for the female example. The server re-resolves them against its
installed index and the generator replaces the primary component in both normal
and `compiledData` copies. The corresponding curated bundle's cuff/shadow
companion is retained provisionally. Female indexed feet remain preview-only
because the tutorial boot is not a validated garment anchor.

Curated hair options may describe binding topology as well as resource paths.
The `patch_dread_undercut` option changes the primary component class, rewires
skinning, adds parent transforms, and carries the matching animgraph, dangle
rig, and NPC shadow. The builder must apply those changes to both component
copies and allocate new CR2W handle IDs above the template's existing maximum;
never paste handle IDs from the source vanilla `.ent` into Patch.

For indexed assignment, derive body-frame compatibility from the final mesh
filename, not every directory token: current archives contain PWA meshes below
folders whose names include `pma`. Preview refreshes must stay staged and may
replace cached GLB/cooked/metadata files only after WolvenKit succeeds and the
serialized CR2W metadata shape validates.

Run the female UI by passing the reviewed manifest on the server command line:

```powershell
py -B .\tools\character_ui.py `
  --manifest .\source\characters\female-example.character.json --open
```

The HTTP client may change selections and shape values, but it must never be
allowed to replace the trusted manifest, catalog, template, source, or tool
paths.

Treat index rows as discovery records, not complete appearance bundles: hair
and clothing commonly need control entities, animated components, shadows,
cuffs, chunk masks, visual tags, and other companion data. Indexed head, hair,
arms, player-item resources, material-accurate previews, and complete bundle
resolution are not implemented yet.

Player garment support is transaction/equipment behavior and is not
automatically equivalent for NPC appearance components. Browser fit and a
successful GLB export do not prove in-game deformation or clipping.

## TweakXL Resources

- `source/resources/r6/tweaks` is part of the mod.
- `source/resources/r6/tweaks/ghostline/character_patch.yaml` defines the
  custom NPC.
- `source/resources/r6/tweaks/ghostline/faction_ghostline.yaml` defines the
  custom Ghostline faction.
- TweakXL loads `.yaml` or `.tweak` files from Cyberpunk's `r6/tweaks`; in this
  WolvenKit project, author them under `source/resources/r6/tweaks`.
- Tweak YAML is indentation-sensitive. Use 2 spaces, not tabs.
- Tweak record names must be unique.
- Do not base Ghostline records on generated `inlineX` records, because those
  names can shift between game updates.
- When editing NPC tweak records, prefer copying structure from a working
  base-game example in WolvenKit's Tweak Browser.

Important NPC fields include:

- `entityTemplatePath`
- `displayName`
- `fullDisplayName`
- `voiceTag`
- `baseAttitudeGroup`
- `archetypeData`
- `affiliation`

Useful docs:

- `ROADMAP.md`
- `docs/packaging.md`
- `modding_docs/for-mod-creators-theory/files-and-what-they-do/file-formats/entity-.ent-files`
- `modding_docs/for-mod-creators-theory/files-and-what-they-do/file-formats/appearance-.app-files`
- `modding_docs/for-mod-creators-theory/core-mods-explained/tweakxl`
