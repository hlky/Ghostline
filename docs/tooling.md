# Ghostline Tooling

This document keeps helper command usage out of `README.md` and `ROADMAP.md`.
Use these tools to inspect focused slices of CR2W-JSON instead of loading large
files into context.

Run the regression suite after changing the production scene, meeting phase,
world spec, or world generator:

```powershell
py -B -m unittest discover -s tests -v
```

## Native Archive And CR2W Inspection

`tools/ghostline-red` is a submodule of the independently maintained
[hlky/ghostline-red](https://github.com/hlky/ghostline-red) Rust CLI. Initialize
it after cloning Ghostline, then build and test it with:

```powershell
git submodule update --init --recursive .\tools\ghostline-red
cargo test --manifest-path .\tools\ghostline-red\Cargo.toml
cargo build --release --manifest-path .\tools\ghostline-red\Cargo.toml
```

List the current archive index and resolve every hash from the authored depot
tree:

```powershell
.\tools\ghostline-red\target\release\ghostline-red.exe archive-list `
  .\packed\archive\pc\mod\Ghostline.archive `
  --paths-root .\source\archive
```

Pack and extract the authored depot tree:

```powershell
.\tools\ghostline-red\target\release\ghostline-red.exe pack `
  .\source\archive -o H:\Ghostline-builds\native-candidate

.\tools\ghostline-red\target\release\ghostline-red.exe extract `
  H:\Ghostline-builds\native-candidate\archive.archive `
  -o H:\Ghostline-builds\native-candidate\extracted
```

The native packer uses ghostline-red's clean-room Kraken encoder and decoder;
no proprietary DLL is required for normal archive workflows. The current
301-file archive extracts every payload byte-identically, and WolvenKit remains
useful as an independent interoperability oracle.

Inspect the structural tables of a packed CR2W resource:

```powershell
.\tools\ghostline-red\target\release\ghostline-red.exe cr2w-inspect `
  .\source\archive\mod\gq000\phases\gq000.questphase
```

Both commands accept `--json`. Generic reflected CR2W conversion uses the
schema generated from the pinned WolvenKit submodule:

```powershell
.\tools\ghostline-red\target\release\ghostline-red.exe schema-generate `
  .\WolvenKit .\red-schema.json

.\tools\ghostline-red\target\release\ghostline-red.exe cr2w-serialize `
  .\source\archive\mod\gq000\phases\gq000_patch_meet.questphase `
  --schema .\red-schema.json .\converted\gq000_patch_meet.questphase.json

.\tools\ghostline-red\target\release\ghostline-red.exe cr2w-deserialize `
  .\converted\gq000_patch_meet.questphase.json `
  --template .\source\archive\mod\gq000\phases\gq000_patch_meet.questphase `
  --schema .\red-schema.json .\converted\gq000_patch_meet.questphase
```

The writer supports shifted strings and arrays, new CName/import entries,
typed world-node data, and typed RedPackage edits across all package-bearing
authored resources. Template-backed packages can grow existing non-empty
arrays, allocate new chunks and nested handles from an existing class
template, rebuild handle indices, and preserve untouched package chunks.
The current 80-resource binary-to-native-JSON corpus rebuilds byte-identically.
Novel class layouts still require a matching template or WolvenKit.

On the base-game `03_night_city.streamingworld` fixture, three warm CLI runs
averaged 85.5 ms serialize and 81.2 ms deserialize, versus WolvenKit 8.17.4 at
18.69 s and 17.81 s. Both native JSON and WolvenKit JSON rebuilt to the
original CR2W byte-for-byte.

The specialized localization commands remain available:

```powershell
.\tools\ghostline-red\target\release\ghostline-red.exe `
  cr2w-serialize-localization `
  .\source\archive\mod\gq000\localization\en-us\onscreens\gq000.json `
  .\converted\gq000.json.json

.\tools\ghostline-red\target\release\ghostline-red.exe `
  cr2w-deserialize-localization `
  .\converted\gq000.json.json `
  --template `
  .\source\archive\mod\gq000\localization\en-us\onscreens\gq000.json `
  .\converted\gq000.json
```

The GQ000 fixture round-trips byte-identically.

The suite covers the 15-node scene contract, phase-owned community activation
and spawn-readiness gate, the scene-local engage gate, restored trigger radii,
distinct community registry node identity, numerically sorted choice locStore
descriptor blocks, and synchronization between the generated fixture and the
checked-in raw scene.
It also rejects forward `HandleRefId` use in the meeting phase because
WolvenKit's CR2W-JSON resolver requires a handle definition to appear first.

## Character Builder And UI

`tools/character_builder.py` is the shared engine for the schema-v1 character
manifest and local UI. It writes only to the output directory supplied by the
caller. Validate and generate Patch's reviewed design with:

```powershell
py -B .\tools\character_builder.py validate
py -B .\tools\character_builder.py generate --out .\converted\characters\patch
py -B .\tools\character_builder.py compare --generated .\converted\characters\patch
```

The final `compare` is expected to report all four documents as equivalent to
their applied shipping source paths. Patch's immutable original appearance is
kept at `source/characters/templates/patch-original.app.json`, and its original
catalog selections' semantic equivalence remains covered by
`tests/test_character_builder.py`.

Validate and generate the checked female-average example with the tutorial path
recorded in its reviewed manifest:

```powershell
py -B .\tools\character_builder.py `
  --manifest .\source\characters\female-example.character.json validate
py -B .\tools\character_builder.py `
  --manifest .\source\characters\female-example.character.json generate `
  --out .\converted\characters\female_example
```

Generation rewrites the female tutorial's 18 numeric mesh resource IDs to
explicit `mod\ghostline\characters\female_example\...` paths and stages only
the referenced meshes. Four body/head texture dependencies are also staged at
their existing tutorial depot paths because those paths are embedded inside the
source meshes. The manifest currently declares Phantom Liberty because the
female root retains EP1 references.

Patch's checked-in manifest intentionally leaves its five head-shape values
unset because the original preset is unknown. Check the head toolchain without
building by supplying temporary values:

```powershell
py -B .\tools\character_builder.py head `
  --workspace .\converted\characters\patch\head-build `
  --dry-run `
  --shape eyes=21 --shape nose=21 --shape mouth=21 `
  --shape jaw=21 --shape ears=21
```

Remove `--dry-run` to run the complete selected-morphtarget export, background
Blender shape application, GLB export, and WolvenKit CR2W mesh rebuild. Outputs
remain isolated under the chosen workspace. Do not apply temporary shape values
to Patch's checked-in meshes.

The current male head GLBs contain Basis plus named target variants `h01`
through `h20`. That makes creator values 1 through 21 mechanically available:
value 1 is Basis, and values 2 through 21 map to those named targets. Although
the character-creator cheat sheet documents value 22, the exported GLBs have no
`h21` target. The builder blocks 22 until the offset is resolved; the earlier
shape-22 smoke run was a successful toolchain pass but a geometry no-op.

The female PWA core contains 21 named variants for each of five facial regions,
including `h21`; female-average creator values 1 through 22 are therefore
available. For example, this checks the female shape-22 build without invoking
Blender:

```powershell
py -B .\tools\character_builder.py `
  --manifest .\source\characters\female-example.character.json head `
  --workspace .\converted\characters\female_example\head-build `
  --dry-run `
  --shape eyes=22 --shape nose=22 --shape mouth=22 `
  --shape jaw=22 --shape ears=22
```

Prepare the morph-preserving browser source without running Blender:

```powershell
py -B .\tools\character_builder.py preview `
  --out .\converted\characters\patch\preview
```

Use the same command with `--manifest` before `preview` for the female PWA
source:

```powershell
py -B .\tools\character_builder.py `
  --manifest .\source\characters\female-example.character.json preview `
  --out .\converted\characters\female_example\preview
```

Add `--all-head-parts` only when testing overlays. The default exports the
25.7-MiB core head; all 13 current layers are roughly 109 MiB and are not needed
to select the five facial shapes.

Generate the installed-game asset index with:

```powershell
py -B .\tools\character_asset_index.py
```

The default pass queries `basegame_4_appearance.archive` and
`ep1_2_gamedata.archive`, writes ignored
`converted/character-index/assets.json`, and currently yields 4,965 head, body,
hair, clothing, and player-item records. It records source archive, expansion,
slot, family, body-frame tokens, resource role, and preview warnings. Use
`--archive` repeatedly or `--regex` to change the scope.

Start the local creator with:

```powershell
npm install --prefix .\tools\character_ui --ignore-scripts
py -B .\tools\character_ui.py --open
py -B .\tools\character_ui.py `
  --manifest .\source\characters\female-example.character.json --open
```

Without `--manifest`, the UI and CLI use
`source/characters/patch.character.json` and `source/characters/catalog.json`.
The manifest option switches the trusted server-side manifest and its declared
catalog; client requests cannot replace either path. UI generation and head
builds are isolated under ignored `converted/characters`. The pinned Three.js
dependency stays local to `tools/character_ui/node_modules`. The browser
renders the real frame-specific morph-target head, updates facial shapes
client-side, searches the generated installed-game index, and uncooks a
selected `.mesh` to an isolated GLB on demand. Supported PMA primary meshes in
the `torso`, `legs`, and `feet` slots and PWA primary meshes in `torso` and
`legs` expose the real appearance names read from the cooked mesh: choose an
appearance and click `Use in outfit`. The selection is stored under
`appearance.indexed_overrides`, summarized above the curated controls, and
applied during source generation. PWA feet remain preview-only until the female
catalog has a reviewed garment anchor. Use the `Head` toolbar button to return
from an asset preview.

The server intentionally accepts loopback hosts only. Browser requests may
change identity, selections, and head values, but template paths, source roots,
morphtarget lists, output definitions, WolvenKit, Blender, and game paths are
reloaded from the reviewed server-side manifest. Build/index operations are
serialized and JSON reports are replaced atomically.

The Python server does not hot-reload backend changes. After updating the
character tooling, stop and restart `tools/character_ui.py` before reloading the
page; otherwise a newer frontend can be paired with an older bootstrap API. The
UI detects that mismatch and reports `Restart required` instead of failing with
a JavaScript property-access error.

Preview caches are fingerprinted. Head entries include the source CR2W hash and
tool/game identities; installed meshes include their provider-archive identity,
tool/game identities, depot path, and exporter settings. A source, game, or
tool update therefore regenerates the selected GLB instead of silently serving
an old preview. Mesh refreshes and CR2W metadata serialization run in a fresh
staging directory and replace cache files only after both commands and metadata
shape validation succeed. Assignment compatibility uses frame tokens from the
mesh filename; path-wide tokens remain discovery metadata and cannot make a
PWA mesh assignable merely because a parent folder contains `pma`.

The curated catalogs remain deliberately small: Patch's original visible
hair/clothing bundles, the complete `hh_146` dread-undercut topology, and the
female tutorial's casual hair/torso/legs/boots anchors, with disable choices.
Catalog hair bindings can rebuild component type, skinning, parent transforms,
animgraph, rig, and NPC shadow in both CR2W component copies; new handle IDs are
allocated above the template's existing maximum. An indexed supported-slot
selection replaces only the primary mesh in the corresponding curated bundle,
in both the normal and `compiledData` copies, while retaining its existing
cuff/shadow companion. This makes index rows usable now but is not a complete
NPC bundle resolver. Browser materials are currently neutral, the appearance
dropdown does not recolor the GLB yet, and exact RED materials, component
dependencies, garment behavior, and runtime fit still require separate
validation. Other indexed categories remain preview-only.

## Questphase Explorer

### World Asset Catalog

`tools/world_asset_catalog.py` discovers reusable world families in extracted
binary streaming sectors, serializes a deterministic bounded candidate set
with WolvenKit, builds a normalized placement catalog, and performs safe
deterministic selection by category, tag, district, area, radius, and seed.
Default selection excludes every record not explicitly reviewed as accessible
and quest-safe.

See `docs/world-asset-catalog.md` for the discovery/build/curation workflow,
the generated coverage summary, and test-quest selection examples.

### Vanilla Quest Reference

`tools/build_quest_reference.py` reads IGN's Main Jobs, Side Jobs, and Gigs
indexes, matches their quest links to `H:\projects\quest.json`, and generates
structural Markdown references under `docs/vanilla-quest-reference`. Each
matched quest includes its vanilla type, journal hash/path, premise, ordered
objective paths, map-pin references, and automatically tagged candidate quest
building blocks. Machine-readable IGN-to-journal linkage is written to
`reference/quests/ign-link-map.json`.

```powershell
py -B .\tools\build_quest_reference.py
```

The generator stores links and locally exported journal structure; it does not
copy IGN walkthrough prose.

### Typed Quest Composition

`tools/quest_compiler.py` validates typed linear quest manifests and emits a
deterministic orchestration questphase, instantiated child questphases, and a
normalized build plan. Simple objective, item, shard, and phone blocks are
generated directly. Meeting, hacking, delivery, device, combat, investigation,
branching, escort, carry, and vehicle blocks use reduced raw CR2W-JSON
templates with strict scalar bindings. Nineteen reusable template-backed
blocks have compiler-owned defaults, so normal manifests do not expose
template placeholders. Scene, world, journal, localization, community AI, and
device placement remain separate stage-owned build products.

```powershell
py -B .\tools\quest_compiler.py validate `
  .\source\quests\gq001.quest.json

py -B .\tools\quest_compiler.py compile `
  .\source\quests\gq001.quest.json `
  --out .\converted\quests\gq001\gq001.questphase.json `
  --allow-planned
```

See `tools/quest_spec.md` for the schema, readiness rules, and current
meet-hack-meet-deliver acceptance manifest.

The standalone generated-phone example is:

```powershell
py -B .\tools\quest_compiler.py compile `
  .\source\quests\examples\phone_conversation.quest.json `
  --out .\converted\quests\examples\phone_conversation.questphase.json
```

The complete building-block acceptance examples are:

```powershell
py -B .\tools\quest_compiler.py compile `
  .\source\quests\examples\direct_building_blocks.quest.json `
  --out .\converted\quest-blocks\gq_blocks_direct.questphase.json

py -B .\tools\quest_compiler.py compile `
  .\source\quests\examples\template_building_blocks.quest.json `
  --out .\converted\quest-blocks\gq_blocks_template.questphase.json
```

Regenerate the eight checked-in reduced templates with:

```powershell
py -B .\tools\generate_quest_block_templates.py
py -B .\tools\generate_ai_vehicle_block_templates.py
```

Their vanilla provenance and deliberately supported shapes are documented in
`reference/vanilla_quest_blocks/README.md`.

`tools/explore_questphase.py` inspects deserialized questphase JSON. The
default target is
`source/raw/mod/gq000/phases/gq000_patch_meet.questphase.json`.

```powershell
py .\tools\explore_questphase.py summary
py .\tools\explore_questphase.py nodes --sockets
py .\tools\explore_questphase.py edges
py .\tools\explore_questphase.py refs
py .\tools\explore_questphase.py handles --type TriggerCondition
py .\tools\explore_questphase.py search gq000_01_tr
py .\tools\explore_questphase.py node id:11
py .\tools\explore_questphase.py handle 13
py .\tools\explore_questphase.py dot > questphase.dot
```

Pass another raw questphase with `--file`:

```powershell
py .\tools\explore_questphase.py --file .\source\raw\mod\gq000\phases\gq000.questphase.json summary
```

Large lists are bounded by default. Use `--limit`, `--offset`, or `--limit 0`
when more rows are needed.

### Post-Accept Cache Phase Generator

`tools/generate_cache_phase.py` is the source of truth for
`gq000_post_accept.questphase.json`. It deterministically emits the current
linear cache flow and validates handle definitions, references, unique quest
IDs, the prefab root, and node count.

```powershell
py -B .\tools\generate_cache_phase.py --dry-run
py -B .\tools\generate_cache_phase.py
py -B -m unittest tests.test_generate_cache_phase -v
py -B .\tools\explore_questphase.py `
  --file .\source\raw\mod\gq000\phases\gq000_post_accept.questphase.json `
  summary
```

Do not hand-patch the generated raw phase. Change the generator and its focused
tests, regenerate, then run the WolvenKit deserialize/serialize round trip.

### Delivery Phase Generator

`tools/generate_delivery_phase.py` is the source of truth for
`gq000_delivery.questphase.json`. It emits the native drop-point reservation,
deposit-fact gate, Morrow phone branches, completion reward, and quest success
flow. Validation covers deterministic output, graph topology, the exact live
Kabuki NodeRef, item/fact names, journal path classes and file indexes, both
phone replies, reward record, and handle resolution.

```powershell
py -B .\tools\generate_delivery_phase.py --dry-run
py -B .\tools\generate_delivery_phase.py
py -B -m unittest tests.test_generate_delivery_phase -v
py -B .\tools\explore_questphase.py `
  -f .\source\raw\mod\gq000\phases\gq000_delivery.questphase.json `
  summary
```

The reserve event is intentionally a side branch after the package inventory
gate. Do not put the deposit fact wait behind the EventManager output: the
vanilla delivery graphs do not consume that output.

## Scene Explorer

`tools/explore_scene.py` inspects deserialized `.scene` CR2W-JSON. The default
target is `source/raw/mod/gq000/scenes/gq000_patch_meet.scene.json`.

```powershell
py .\tools\explore_scene.py summary
py .\tools\explore_scene.py actors
py .\tools\explore_scene.py nodes
py .\tools\explore_scene.py edges
py .\tools\explore_scene.py events
py .\tools\explore_scene.py lines
py .\tools\explore_scene.py choices
py .\tools\explore_scene.py refs --kind NodeRef
py .\tools\explore_scene.py refs --kind journal_path
py .\tools\explore_scene.py handles --type TriggerCondition
py .\tools\explore_scene.py node 8
py .\tools\explore_scene.py handle 41
py .\tools\explore_scene.py search gq000_01_tr
py .\tools\explore_scene.py dot > scene.dot
```

Pass another raw scene with `--file`:

```powershell
py .\tools\explore_scene.py --file .\reference\vanilla_extract_json\mq007\mq007_01_gun_found.scene.json summary
```

## Scene Generator

`tools/generate_scene.py` creates fresh `.scene` CR2W-JSON from a compact JSON
spec. The production fixture is
`tools/gq000_patch_meet.scene-spec.json`, and the spec reference is
`tools/scene_spec.md`.

```powershell
py .\tools\generate_scene.py example
py .\tools\generate_scene.py audit --spec .\tools\gq000_patch_meet.scene-spec.json
py .\tools\generate_scene.py generate --spec .\tools\gq000_patch_meet.scene-spec.json --dry-run
py .\tools\generate_scene.py generate --spec .\tools\gq000_patch_meet.scene-spec.json
py .\tools\generate_scene.py validate --file .\source\raw\mod\gq000\scenes\gq000_patch_meet.scene.json --spec .\tools\gq000_patch_meet.scene-spec.json
py -B -m unittest discover -s tests -v
py .\tools\generate_scene.py generate --spec .\tools\gq000_patch_meet.scene-spec.json --deserialize
```

The generator uses audited vanilla shells under `reference/vanilla_extract_json`
and local WolvenKit source assumptions. It does not use `template.scene.json`,
`generated`, or `GraphEditorStates` as scene source of truth. V1 covers
dialogue sections, padded choice nodes, actor acquisition, embedded choice
locStore coverage, and the scene-local quest wrappers used by
`gq000_patch_meet`.

## Localization Explorer

`tools/explore_localization.py` inspects subtitle and VO-map CR2W-JSON. By
default it loads the current `gq000_01` subtitle and VO raw JSON files together
and cross-checks entries by `stringId`.

```powershell
py .\tools\explore_localization.py summary
py .\tools\explore_localization.py entries
py .\tools\explore_localization.py check
py .\tools\explore_localization.py search Arasaka
py .\tools\explore_localization.py entry 67568872890781206
py .\tools\explore_localization.py refs
py .\tools\explore_localization.py types
```

Pass one or more localization files with repeated `--file` arguments:

```powershell
py .\tools\explore_localization.py --file .\source\raw\mod\gq000\localization\en-us\subtitles\gq000_01.json.json --file .\source\raw\mod\gq000\localization\en-us\vo\gq000_01.json.json check
```

## Entity And Appearance Explorer

`tools/explore_ent_app.py` inspects deserialized `.ent` and `.app` CR2W-JSON.
By default it loads Patch's root entity and app files together.

```powershell
py .\tools\explore_ent_app.py summary
py .\tools\explore_ent_app.py appearances
py .\tools\explore_ent_app.py components --resources-only
py .\tools\explore_ent_app.py components --type SkinnedMesh
py .\tools\explore_ent_app.py component c124
py .\tools\explore_ent_app.py refs --kind ResourcePath
py .\tools\explore_ent_app.py handles
py .\tools\explore_ent_app.py search patch
py .\tools\explore_ent_app.py types
```

Pass one or more raw entity/app files with repeated `--file` arguments:

```powershell
py .\tools\explore_ent_app.py --file .\source\raw\mod\ghostline\characters\patch\patch.ent.json --file .\source\raw\mod\ghostline\characters\patch\patch.app.json summary
```

## Journal Explorer

`tools/explore_journal.py` inspects deserialized `.journal` CR2W-JSON. By
default it loads the mq003 quest journal reference from `reference/journal`.

```powershell
py .\tools\explore_journal.py summary
py .\tools\explore_journal.py prefixes --with-types
py .\tools\explore_journal.py -f .\source\raw\mod\gq000\journal\gq000.journal.json tree --max-depth 6
py .\tools\explore_journal.py -f .\source\raw\mod\gq000\journal\gq000.journal.json refs
```

Pass a different reference directory to the prefix command with
`--reference-dir`.

## World Reference Tools

`tools/serialize_reference_world.ps1` serializes CR2W binary world references
under `reference/world` into CR2W-JSON companions.

```powershell
.\tools\serialize_reference_world.ps1
```

`tools/index_drop_points.py` queries the checked 103-device native drop-point
catalog and defaults to the separately reviewed safe pool:

```powershell
py -B .\tools\index_drop_points.py list
py -B .\tools\index_drop_points.py choose --seed gq001
py -B .\tools\index_drop_points.py list `
  --include-unvetted --region watson --area kabuki
```

See `docs/drop-points.md` for rebuild provenance, curation rules, and the
runtime-branching requirement.

`tools/explore_world.py` inspects deserialized `.streamingblock` and
`.streamingsector` CR2W-JSON.

`tools/index_world_assets.py` turns exact vanilla depot paths into a reusable
placement index. First binary-filter the extracted Night City sectors for the
path and serialize only the matching sectors, then build the index:

```powershell
py .\tools\index_world_assets.py build `
  --sectors H:\Ghostline-audits\antenna-access-points `
  --resource 'base\gameplay\devices\masters\access_points\antenna_access_point_small.ent' `
  --output .\reference\world\antenna-access-points.json

py .\tools\index_world_assets.py list `
  --manifest .\reference\world\antenna-access-points.json `
  --near=-1111.060,1456.400,16.360 `
  --radius 100
```

The checked Ghostline references currently cover 82 small antenna access
points, 161 large gameplay antenna placements, and 387 decorative satellite
dish placements. Exact transforms are discovery evidence, not proof of
walkable access or a safe quest lifecycle; quest-owned devices and communities
should be placed at a reviewed terrain candidate rather than mutating a vanilla
activity.

Loot containers are also useful as dense, city-wide sampling anchors when a
quest needs a pseudo-random contact, encounter, or prop location. Index an
exact container template such as
`base\gameplay\loot\containers\weapon_cases\weapon_case_small.ent`, choose a
deterministic random candidate using the quest/save seed, then place the
quest-owned object at a reviewed nearby offset. Do not place a character at the
container transform itself: first verify walking access, navmesh, clearance,
ground height, streaming ownership, and conflicts with the vanilla encounter.
The Kabuki World Inspector capture at
`-1082.949, 1412.400, 21.773` (`weapon_case_small`) is the initial reference
for this location-sampling pattern.

```powershell
py .\tools\explore_world.py summary
py .\tools\explore_world.py blocks
py .\tools\explore_world.py nodes --type TriggerArea --limit 0
py .\tools\explore_world.py nodes --type AISpot --limit 0
py .\tools\explore_world.py noderefs --contains mq003_tr --limit 0
py .\tools\explore_world.py communities
py .\tools\explore_world.py search gq000
```

Pass one or more files or directories with repeated `--file` arguments:

```powershell
py .\tools\explore_world.py --file .\reference\world\001\sectors summary
py .\tools\explore_world.py --file .\source\raw\mod\gq000\world summary
py .\tools\explore_world.py --file .\source\raw\mod\gq000\world noderefs --limit 0
py .\tools\explore_world.py --file .\source\raw\mod\gq000\world communities
```

`tools/find_collision_instances.py` fingerprints a World Inspector collision
actor by its shape hash and lists matching actors in a serialized sector. This
is useful when the selected object is baked into a composite collision node
rather than represented by a standalone mesh or entity node. Actor indices are
zero-based.

```powershell
py .\tools\find_collision_instances.py `
  --file H:\Ghostline-analysis\gq000-cache-20260722\node-cabinet-raw\exterior_-8_11_0_1.streamingsector.json `
  --debug-name NormalCollisionNode_087 `
  --actor 36 `
  --source-prefab-hash 8325780084261042030

py .\tools\find_collision_instances.py `
  --file .\another.streamingsector.json `
  --shape-hash 12135205187229491652 `
  --json
```

## World Generator

`tools/generate_world.py` turns captured in-game coordinates into raw
`.streamingsector.json` and `.streamingblock.json` files. The production
meeting source is `tools/gq000_patch_meet.world.json`. The checked-in
`tools/gq000_world_spec.example.json` uses placeholder/reference coordinates
and is tutorial input only. The full spec reference is `tools/world_spec.md`.

The generator now supports several communities, several entries/spots per
community, and native access-point devices. The production spec uses those
features for three inactive Tyger Claw guards and the dormant Quiet Spine
relay. Access-point entity-instance buffers must use a nonzero ID distinct
from the sector node-data buffer; the production device reserves buffer `1`.

Distances in specs are world-coordinate units: local `forward`, `right`,
`distance`, trigger widths/depths, and radii all use the same scale as captured
CET/WolvenKit coordinates. Current evidence points to roughly 1 coordinate unit
per in-game meter, but final placement still needs in-game validation against
HUD/objective distance display.

```powershell
py .\tools\generate_world.py example
py .\tools\generate_world.py hash "$/mod/npcac/#npcac_spot"
py .\tools\generate_world.py measure -- "origin=-287.155151,-1950.40015,8.960001" "target=-280.087708,-1943.4187,8.960001"
py .\tools\generate_world.py generate --spec .\tools\gq000_world_spec.example.json --dry-run
py .\tools\generate_world.py generate --spec .\tools\gq000_patch_meet.world.json --dry-run
```

For an intentional production update, generate the raw files first, run the
regression suite, inspect the generated world, then register and deserialize
the same reviewed spec:

```powershell
py .\tools\generate_world.py generate --spec .\tools\gq000_patch_meet.world.json
py -B -m unittest discover -s tests -v
py .\tools\explore_world.py --file .\source\raw\mod\gq000\world summary
py .\tools\explore_world.py --file .\source\raw\mod\gq000\world nodes --type Device --limit 0
py .\tools\explore_world.py --file .\source\raw\mod\gq000\world communities
py .\tools\generate_world.py generate --spec .\tools\gq000_patch_meet.world.json --register --deserialize
```

## Voiceover WEM Conversion

`tools/convert_wavs_to_wem.ps1` converts the current quest WAV voiceover files
into Wwise `.wem` files. The authored WAVs presently live in `generated`
alongside legacy duplicates; the script reads `source/raw/gq000_01_manifest.json`
and selects only the 13 referenced basenames. It normalizes those WAVs into
`wwise_conversion\ExternalSources`, writes `external_sources.wsources`, runs
Wwise external-source conversion, and copies the results to
`source/archive/mod/gq000/localization/en-us/vo` without deleting the WAVs.

```powershell
.\tools\convert_wavs_to_wem.ps1 -NoCopy
```

Inspect the conversion output and compare it with the runtime-proven WEMs. Run
the command without `-NoCopy` only when intentionally replacing the 13 active
files under `source/archive`. Use `-SourceDir`, `-DestinationDir`, and
`-Manifest` only when deliberately working on a different dialogue set. A
nonempty manifest is mandatory. Its filter converts and copies only the 13
referenced files; it does not prune the 13 unreferenced WEMs already retained
for archive-baseline parity.

By default it uses:

```powershell
C:\Audiokinetic\Wwise2025.1.7.9143\Authoring\x64\Release\bin\WwiseConsole.exe
```

Override that path with `-WwiseConsole` or the `WWISE_CONSOLE` environment
variable if Wwise is installed elsewhere.
