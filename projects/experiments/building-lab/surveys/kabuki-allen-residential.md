# Kabuki Allen-sign building — shell survey

User supplied twelve exterior screenshots on 2026-10-26 for a multi-level
residential retrofit. “Allen” is the visible sign; the canonical building name
and any existing quest ownership are unverified.

Follow-up: the sign's entity is `{AllenSt}`, identifying Allen Street. An
[interior planning draft](allen-street-residential-retrofit.md) now adds a lobby,
two stair connections and upper delivery landings, without runtime changes.

## Recovered

- All eleven inspector selections match installed-world positions to screenshot
  precision. The remaining screenshot is the unobstructed exterior overview.
- Entrance: `[-1063.446533,1782.144653,28.415075]`, entity placement 2176,
  definition 1747 in `exterior_-17_27_0_0.streamingsector`. Its NodeRef ID is
  `16258670866369862865`. Existing entity is `double_door_decorative.ent`, shown
  as FakeDoor, appearance `doors_double_kitsch_f` in the user's inspector.
- Main render shell is in `exterior_-9_13_0_1.streamingsector`, found by broader
  descriptor/placement survey. The screenshots' collision sectors alone would
  not have recovered it. Imported 136 shell placements/instances plus the
  ground-floor shop facade: 137 reference modules, 21 distinct meshes.
- Render bounds in layout-local metres: X `[-0.6002,21.5001]`, Y
  `[-0.5000,21.0327]`, Z `[-0.4338,12.2685]`. About 22.10 × 21.53 × 12.70 m
  including ledges and projecting bays, not habitable dimensions.
- Repeated facade rows at world Z 28.481 and 32.480, further render geometry
  around 36.480 and roof around 40.480, support a provisional three-level model.
  Ground threshold is about Z 28.415. Floor finishes/slabs still need inspection.

## Editor reference

Open **Kabuki Allen · three-level shell survey** in the Project panel.
`../buildings/kabuki-allen-residential-shell.building.json` is the editable
reference. `kabuki-allen-residential-shell-import.json` reproduces the import
from source-pinned sector data. Reimport equality and layout compilation pass.

The three 18 × 18 m rooms are explicitly **planning envelopes**, not measured
usable floors. The editor shows one active level at a time. Upper windows/bays
can span multiple storeys; their reference level is an organisational label,
not a geometry cut. Neutral transparent materials are editor references.

No vanilla patch/deletion is authored, no archive is installed, and there is no
interactive entrance, stair connection or playable interior. The three plan
floors are disconnected until the retrofit is designed. Do not export this
survey as if it were a completed building.

## Scope protections and remaining survey

Collision placement 2704/definition 2606 and placement 2722/definition 2624 each
contain 128 actors. Preserve these groups; only individually confirmed actors
may be replaced when forming an entrance aperture. Several are mesh collisions,
so pivot distance does not measure their occupied space.

The screenshot at placement 2776/definition 2678, actor 104, points to a primitive
box with unit half-extents. Decoding its auxiliary actor scale later established
an effective size of roughly 18 × 21 × 4 m: it fills the upper storey. The earlier
2 m interpretation omitted that scale. The residential retrofit replaces only
this actor with peripheral collision and a roof slab around its new interior.
The far boundary at placement 3691/definition 2615, actor 77
belongs to another prefab and must not be folded into this shell automatically.

Before a playable layout: inspect retained interior geometry and occluders,
ground-floor shop backing, possible existing quest/interior ownership, floor
levels, public approach and stairs footprint. Survey actor clearance and native
navigation separately from exterior shape. Plan a lobby/security desk and two
residential landings only after those checks.

No additional user coordinates required for exterior reconstruction. A player
position just outside the intended entrance and an inside view may be useful
later if extraction cannot resolve the approach or obstructions.

## Evidence

- `kabuki-allen-residential-site.json`: screenshot-to-world matches and source
  hashes.
- `../generated/allen-residential-survey/`: fresh serialization of the four
  primary sectors, nearby surveys, bounds and import verification.
- Finite descriptor discovery encountered 42 uncached sectors and skipped
  unbounded descriptors. This is not an exhaustive quest/occlusion preflight.
  A narrow AABB discovery pass was used because the existing variant parser
  rejected a default-omitted `rangeIndex`; no shared parser was changed.
