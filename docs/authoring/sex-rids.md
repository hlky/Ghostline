# Vanilla Sex RID Catalog

`reference/animations/sex` separates the machine-readable structure of
vanilla sex scene RIDs from human review:

- `vanilla-sex-rids.json` is reproducible technical evidence.
- `vanilla-sex-rid-annotations.json` is the small human-owned semantic layer.
- `vanilla-sex-rid-previews.json` is the stable render-job contract.

The current inventory contains 71 resources: all 60 RIDs under
`base\animations\quest\lore\generic_sex` and all 11 bespoke RIDs referenced by
the inspected Panam, Kerry, River, and Judy scenes. Meredith and the inspected
female and male Joytoy scenes select from the generic set rather than a
partner-specific RID family.

## What A RID Contributes

A `.scenerid` is performance data, not a complete scene. The catalog records:

- actor signatures and serial numbers;
- every body, facial, cyberware, and camera clip rather than assuming one clip
  per actor;
- animation name, duration, frame rate, joint/track cardinality, offsets, root
  motion flags, event types, and buffer/source hashes;
- the source `.scene` resources that register each RID, including duplicate
  registrations with different resource IDs;
- conservative path-derived hints such as generic family, intro/loop/outro,
  Maya variant, nominal duration, and `_f`/`_m` authored player-gender suffix.

The `.scene` still owns performers, appearances, section order, dialogue,
playback events, camera selection, interruption, exits, and cleanup. This is
why a sex RID resembles a braindance performance resource but is not itself a
braindance or a reusable quest scene.

The `inferred` object is never presented as observed pose semantics. Labels
such as position, body contact, standing/lying posture, direction, transition
quality, and safe loop points belong in the annotation layer after visual
review.

### Generic intercourse `_f` / `_m` semantics

For `generic_sex\intercourse`, the suffix identifies the player-gender variant
for which the choreography was authored. It does **not** identify the sex of
the NPC partner and it is not, by itself, a hard compatibility constraint.

The vanilla Meredith scene proves the branch meaning directly. Its
`questCharacterGender_CondtionType` tests `Male` with `isPlayer = 1`: the true
branch selects `_m` RIDs, while the false branch selects `_f` RIDs where they
exist. The female-player branch reuses `_m` resources such as `sex_04_5s_m` and
`sex_06_5s_m` because no corresponding `_f` resource exists. Those reusable
resources supply gender-selected player tracks (`player` and, where required,
`femalePlayerFpp`) through RID animation containers.

This proves the engine's player-gender branch convention; it does not by
itself prove which character-creator choice supplies that runtime gender flag.
Voice/body romance eligibility is separate scene or quest logic.

Partner sex is an independent binding. The female Joytoy scene binds the NPC
to `female_average`; the male Joytoy scene binds the NPC to `male_average`,
including when both scenes use the same intercourse RID. A mod should therefore
choose the intended `_f`/`_m` player choreography first, then verify that the
RID contains the required partner signature and player/FPP tracks.

## Rebuild Workflow

Extract the selected vanilla RIDs into one depot-mirrored scratch tree. Then
serialize them without flattening duplicate Maya/non-Maya basenames:

```powershell
py -B .\tools\sex_rid_catalog.py serialize `
  --input .\.tmp\vanilla-sex-rids `
  --output .\.tmp\vanilla-sex-rids-json `
  --wolvenkit-cli H:\WolvenKit.Console-8.17.4\WolvenKit.CLI.exe
```

The command uses the native `ghostline-red` serializer first. Some nested
facial/camera buffers are reflected as opaque `$rawData`; those files are
detected and batch-reserialized with the supplied WolvenKit CLI. The command
fails if an opaque animation buffer survives either path.

Build the technical catalog and merge scene usage:

```powershell
py -B .\tools\sex_rid_catalog.py build `
  --rid-json-root .\.tmp\vanilla-sex-rids-json `
  --binary-root .\.tmp\vanilla-sex-rids `
  --scene-json-root .\.tmp\vanilla-sex-scenes-json `
  --output .\reference\animations\sex\vanilla-sex-rids.json
```

`summary.referenced_not_in_catalog` must be empty. A non-empty value means a
source scene names a RID which was not extracted, so the inventory is not
complete.

Refresh the human layer and preview plan:

```powershell
py -B .\tools\sex_rid_catalog.py annotations `
  --catalog .\reference\animations\sex\vanilla-sex-rids.json `
  --output .\reference\animations\sex\vanilla-sex-rid-annotations.json

py -B .\tools\sex_rid_catalog.py preview-plan `
  --catalog .\reference\animations\sex\vanilla-sex-rids.json `
  --output .\reference\animations\sex\vanilla-sex-rid-previews.json
```

Refreshing annotations preserves reviewed values, drops rows no longer in the
catalog, adds new rows, and maintains conservative seeds for the 11
human-readable bespoke names.

## Review Contract

`generated/sex-rid-review/intercourse-observations.md` is the main combined
human-readable observation sheet for the 25 generic intercourse RIDs. It keeps
the role descriptions separate from technical catalog evidence and does not
use `_f`/`_m` as a compatibility filter.

Generate the ignored, portable review page:

```powershell
py -B .\tools\sex_rid_catalog.py review `
  --catalog .\reference\animations\sex\vanilla-sex-rids.json `
  --annotations .\reference\animations\sex\vanilla-sex-rid-annotations.json `
  --preview-plan .\reference\animations\sex\vanilla-sex-rid-previews.json `
  --output .\generated\sex-rid-review\index.html
```

The page filters by path, family, actors, labels, and tags. Reviewers edit the
semantic fields in the browser and use **Download annotations** to export the
human-owned JSON for review before replacing the checked file.

Every preview job has a deterministic MP4 and contact-sheet name, 960x540 at
30 FPS, neutral color-coded actors, the RID camera where present, an overview
fallback, and an identifying slate. `tools/sex_rid_preview.py` now ports the
pinned WolvenKit SIMD and compressed body-track decoders and renders
role-colored neutral proxies through Blender. Generate the first
generic-intercourse review sample with:

```powershell
py -B .\tools\sex_rid_preview.py `
  --rid-json .\.tmp\vanilla-sex-rids-json\sex_01_5s_f.scenerid.json `
  --rid-id 'base\animations\quest\lore\generic_sex\intercourse\sex_01_5s_f.scenerid' `
  --output-dir .\generated\sex-rid-review\previews `
  --actor female_average --actor player `
  --blender 'C:\Program Files\Blender Foundation\Blender 5.1\blender.exe'
```

Re-running the review-page command detects complete MP4/contact-sheet pairs
and embeds them without changing the checked preview manifest. The current
bridge covers SIMD and compressed body motion and uses the 71-bone `man_base`
hierarchy as an approximate core-bone contract for the player proxy.
`tools/sex_rid_preview_batch.py` provides resumable catalog rendering and
automatic uncluttered human-role selection. Facial tracks, RID cameras, props,
and complete multi-take scene assembly still need decoder/render support;
unrendered jobs therefore remain `decoder_required`. Pose metadata must not be
guessed from filenames while visual evidence is absent.

## Reuse Decisions

For a generic RID, prefer the authored player-gender hint and match the exact
actor signatures. An NPV created with Ghostline's vanilla-compatible character
tooling can satisfy an ordinary `female_average` or `male_average` partner
slot, but that does not make every player/FPP or prop rig interchangeable.
Cross-gender reuse is demonstrably possible for some RIDs, but must be proven
from the available `player`/`femalePlayerFpp` tracks and scene bindings rather
than assumed from the suffix alone.

For bespoke romance RIDs, treat all extra signatures as dependencies. Panam's
set includes Basilisk and personal-link rigs; River's bedroom RID includes
doors and a bottle; Judy includes cigarette/lighter tracks; Kerry includes a
lighter. Reuse is possible only after retargeting or supplying the same rig,
offset, prop, camera, and scene-orchestration contract.
