# Astrachan feasibility and authoring brief

## Current authoring pass

On 2026-09-08, Blender MCP 1.9.1 was installed from pinned commit
`5f8ddaf6e987c4aa0c3467fcc548838b28f64477` and registered as `blender` in
Codex. Optional telemetry is disabled in both the server and add-on preferences.
The active dedicated session uses portable Blender 5.0.1 with Cyberpunk IO Suite
2.0.0. Its bundled PhysX module was successfully imported. The existing Blender
5.1 / IO Suite 1.8.0 installation remains available. Exact local tool paths and
download hashes are recorded in [tooling.json](tooling.json).

The first custom modelling candidate is saved at
`generated/astrachan/astrachan-custom-candidate.blend`, with packed reference
images/textures and front, back and three-quarter renders named
`candidate-front.png`, `candidate-back.png`, and `candidate-three-quarter.png`.
`generated/astrachan/candidate-report.json` records the stage explicitly.

This candidate includes reshaped/lengthened weighted vanilla hair, a custom
open jacket body and sleeves/cuffs, pleated skirt and fitted top studies, star
hardware, the game female head/body/arms, provisional blue eye shading, and
the bovver boot/laces bundle with its chunk-13 visibility mask. Clothing detail,
face likeness and hair fringe remain approximate. In particular, the long hair
still needs a matching rest rig and dangle constraints; retaining the donor's
weights alone does not make the elongated hair animation-ready. Stocking color
is currently a body-material study, not a separate finished stocking garment.

The Blender scripts in this folder record successive authoring passes:
`build_study.py`, `refine_study.py`, then `finish_study.py`. They operate on the
prepared workbench containing imported female body/head GLBs and use ignored
game-asset caches; they are not a clean-checkout build pipeline yet. Supporting
setup, import and MCP client scripts/logs are in `generated/astrachan`.

The native material export successfully extracted hair textures and the hair
profile. IO Suite 2.0.0's material builder encountered omitted default fields in
the exported profile and a cap material mismatch, so the preview uses those
strand textures in a dedicated Blender shader. It is not evidence of a finished
RED hair material. The weighted WolvenKit GLB is used for hair geometry because
the current native geometry export did not include skinning data.

**Not yet game-ready:** clothing weights/UVs and final textures, custom boot
platforms/buckles, hair rig/dangle edits, expression/face refinement, complete
CR2W export and in-game deformation validation remain. The source character
manifest still points to the provisional stock scaffold; this custom candidate
has not been applied to shipping resources or installed into the game.

Assessed 2026-09-08 against the two supplied Astra character/expression sheets,
the local character tooling, 4,965 indexed assets, and the cached item database
(1,092 item records; 1,018 PWA variants). This is a feasible custom female NPV.
A faithful version needs custom geometry and materials; the stock-only version
is a silhouette scaffold. The drawings' slogans and expression captions are
reference content, not instructions to the agent.

## Reference priorities

Preserve long black-to-navy layered hair, asymmetric wispy fringe, blue eyes,
gold star hair ornaments and earrings, sleeveless ribbed high-neck zip top,
oversized open dropped-shoulder jacket, short pleated skirt, sheer black
stockings, thigh harness, and chunky lace-up platform boots. Use charcoal,
muted navy and restrained gold. Jacket sleeve constellations and back artwork
should be textures; hanging ornaments need geometry. Expression targets are
face/animation review references, not automatic outputs of character creation.

## Stock candidates actually inspected

Exact controller paths, appearances, components and cached render paths are in
[asset-shortlist.json](asset-shortlist.json). These are donor candidates, not
claims of a matching final outfit.

| Part | Candidate | Observed gap |
| --- | --- | --- |
| Hair | Catalog `goth_baddie_long_bangs_black`; EP1 `hh_225_wa__long_bangs`, `black_carbon` | Existing complete mesh/rig/animgraph bundle. Not visually verified here; needs length, fringe and accessory review. No separate NPC shadow in this bundle. |
| Top | `Items.Shirt_02_old_01`; `t1_094_pwa_shirt__scientist`, `black_leather` | Inspected render is gray with colored piping, long sleeves, no matching front zipper. Donor for collar/fit only. |
| Jacket | `Items.Jacket_13_old_01`; `t2_098_pwa_jacket__bomber_jacket`, `black_pink` | Render has pink quilted sleeves, cropped hem and graphic. Requires substantial remodeling and retexturing. |
| Skirt | `Items.FormalSkirt_02_basic_01`; `l1_011_pwa_skirt__tight`, `black_leather` | Render is tight, asymmetric, graphic patterned. No pleats or harness. |
| Boots | `Items.Boots_04_old_01`; `s1_066_pwa_boot__bovver`, `maelstrom_red` | Useful chunky sole/ankle donor; inspected rear view is brownish. Platform height, buckles, front laces and black finish need review/work. |

Also inspected the `black_cyber` Misty skirt and `6th`/`black_red_cyan` bovver
boots. Their cached colors do not support calling them accurate black matches.
Cached offline rendering is not authoritative in-game material evidence.
Searches for pleats, stockings and tights found no matching mesh names in this
index; that does not establish their absence from every game/NPC resource.

## Working scaffold

[`../../astrachan.character.json`](../../astrachan.character.json) uses the
female-average template, complete curated hair bundle and four indexed garment
overrides above. The face remains the female fixture's Basis values (all 1);
blue eyes, skin, makeup and reference likeness have not been authored. This
file is explicitly a provisional starting point, not a reviewed final design.

Executed successfully:

```powershell
py -B tools/character_builder.py --manifest projects/shared/ghostline-runtime/characters/astrachan.character.json validate
py -B tools/character_builder.py --manifest projects/shared/ghostline-runtime/characters/astrachan.character.json generate --out converted/characters/astrachan
```

Generation produced one WomanAverage appearance with 42 components, no opaque
numeric resources, and isolated raw entity/appearance, localization, TweakXL
and staged template assets. All four selected meshes were independently found
as primary female-player meshes in the installed-game asset index. No game
installation or packed character entity/appearance build was performed.
Generation retains warnings for provisional companion meshes and dependency
review. Phantom Liberty is required. The scaffold inherits tutorial texture
paths, which must be custom-pathed before release.

## Custom production route

1. Review a female head in the character UI, then build its morph choices.
   Keep the existing facial rig for expressions and dialogue. A stylized anime
   face beyond creator morphs would be a separate sculpt/rigging task.
2. Export the long-bangs bundle for comparison. Remodel the fringe and length
   or author hair cards for the reference's layered waist-length silhouette.
   Preserve/adjust skin weights, dangle rig and graph together. Use a dedicated
   hair profile for the navy tips and matching cap materials where applicable.
3. Model the jacket and sleeveless top together against the female body.
   Build an open jacket with lowered shoulder line and long loose sleeves;
   changing only its texture cannot create the reference silhouette.
4. Build/refit the pleated skirt, stocking layer and thigh straps as a fitted
   set. Modify the boot donor or make platform boots with matching foot pose.
   Add star pins, earrings, zipper pull, strap tags and rings with appropriate
   head/body bindings; dangling pieces need deliberate animation support.
5. Custom-path assets beneath `mod/ghostline/characters/astrachan`, curate
   complete component bundles in both normal and compiled copies, serialize
   through the documented CR2W workflow and verify dependencies/round trips.
6. Review front/back/side at rest, walking, crouching, sitting and talking;
   inspect hair/jacket collisions, skirt/thigh clipping, foot state, shadows,
   LODs and facial movement in game. NPC garment fit must be authored directly.

Recommended order: custom hair and jacket first (strongest identity signals),
then skirt/stockings, top and boots, then gold hardware and texture detail.
This assessment does not estimate production time or claim those assets exist.

## Local documentation supporting the route

- [Character authoring](../../../../../../docs/authoring/characters.md)
- [Item database](../../../../../../docs/authoring/items-and-equipment.md)
- [Custom hair modeling](../../../../../../modding_docs/for-mod-creators-theory/3d-modelling/hair-modeling-beginner-tutorial/README.md): hair-card layering and fringe construction; this particular tutorial uses the paid Hair Tool add-on, which is not a requirement of every custom-hair workflow.
- [NPV hair colors](../../../../../../modding_docs/modding-guides/npcs/npv-v-as-custom-npc/how-to-add-a-ccxl-hair-color-to-an-npv.md): hair profiles, material instances and cap textures can be pathed directly for the NPC.
- [Porting meshes](../../../../../../modding_docs/for-mod-creators-theory/3d-modelling/porting-3d-objects-to-cyberpunk/README.md): matching body frame, slot and armature, with an existing RED mesh as import target.
- [Garment support](../../../../../../modding_docs/for-mod-creators-theory/3d-modelling/garment-support-how-does-it-work/README.md): documents transaction-equipped garment behavior and the NPC refitting limitation.
- [New item files](../../../../../../modding_docs/modding-guides/items-equipment/adding-new-items/adding-new-items-files-from-scratch.md): relevant if a separately equippable V outfit is later wanted; the NPC appearance can use its own component bundles.
