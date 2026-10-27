# Environmental damage feasibility

Environmental destruction is possible in Ghostline using native Cyberpunk 2077
systems. Reusing existing destructible props is the strongest starting point.
Selected breakable architecture and deliberately staged collapses are plausible
extensions. Arbitrary destruction of ordinary buildings has not been established.

Research date: 26 October 2026. This investigation inspected local references,
world-sector data, WolvenKit schemas, a cached script decompilation and World
Builder source, and freshly serialized five meshes from the installed base-game
archives. It did not install a mod or observe new gameplay. Evidence is in
[`environmental-damage-research.json`](../../reference/world/environmental-damage-research.json).

## Feasibility by intended result

| Intended result | Assessment | Necessary work |
| --- | --- | --- |
| Breakable glass, clutter and existing destructible props | Strong native reuse path | Preserve the donor mesh, node settings, filters and effects; validate a new placement in game. |
| Explosive machinery that hurts nearby characters | Native gameplay path exists | Clone a complete explosive device and attack setup, including controller state and instigator handling. |
| Fire, electricity or another persistent hazard | Native mechanisms exist | Pair visuals with an appropriate attack/status-effect setup and explicit activation/cleanup. |
| Break a selected wall panel to open a route | Feasible design; integration unproven | Use a compatible destructible donor or authored intact/broken states; coordinate collision and navigation. |
| A scripted collapse or destroyed room state | Feasible design; integration unproven | Author the before/after layout and transition, with controlled debris, effects and durable quest state. |
| Newly modeled objects that fracture physically | Engine supports the representation; authoring pipeline unproven | Generate compatible geometry, physics and destruction mappings together. |
| Make arbitrary existing buildings fully destructible | No supported general solution established | Would require much more than changing node type or a destructibility flag. |

## What the vanilla resources prove

The earlier building investigation scanned 16,256 serialized Night City sectors.
Its lexical type counts include 458,351 occurrences of
`worldInstancedDestructibleMeshNode`, 17,548 of `worldPhysicalDestructionNode`,
1,817 of `worldBakedDestructionNode`, and 16,798 of
`worldFoliageDestructionNode`. These are serialized type occurrences, not a
verified placed-instance count or an exhaustive survey of expansion content.
This investigation reused those counts and independently inspected three concrete
node definitions from the corpus.

The five fresh archive reads all serialized successfully:

| Resource | Observed structure |
| --- | --- |
| `wat_kab_shack_a_wall_window_l300_ab_glass_dst.mesh` | Physics, destruction steps with 74 offsets, 105 destruction bonds, 74 bone/chunk masks, and destruction chunk/index tables. |
| `trash_packaging_c.mesh` | Physics data; its sector places it as an instanced destructible with a specific fracturing effect. |
| `blockade_d.mesh` | Intact roadblock with physics and occluder data. |
| `blockade_d_dst_dynamic.mesh` | Broken roadblock with baked destruction region/index data, physics and a GPU buffer. |
| `cinder_block.mesh` | Physics data; the earlier sector inspection identifies its native instanced-destructible use and effect. |

Full depot paths, sector filenames, node indices, settings, hashes and the fresh
serialization outcomes are retained in the evidence file. The raw fresh reads
and job manifest are under `generated/environmental-damage`.

The Kabuki glass node uses multiple destruction levels with different physics
filters and fracture effects. The roadblock node references both intact and
fractured meshes and specifies 90 frames. These are authored asset packages,
not ordinary meshes that the engine automatically cuts into arbitrary pieces.

## Three different destruction mechanisms

**Instanced destructible meshes** provide a lightweight world representation for
many props. Relevant settings include `isDestructible`, damage endurance,
accumulated damage, impulse conversion, physics filters and fracture effects.
Some donors have no multi-chunk destruction parameters: a destruction reaction
can involve effects and object removal rather than a detailed fracture hierarchy.
Do not infer a particular visual result from the node type alone.

**Physical destruction** uses `worldPhysicalDestructionNode` or
`entPhysicalDestructionComponent`. The inspected window demonstrates the mesh-side
destruction tables. Node/component settings control damage thresholds, endurance,
bonds, impulse propagation, debris lifetime and per-level effects/filters.
These settings tune compatible assets; they do not supply missing fracture data.
The [fork's implementation](https://github.com/Akiway/CP77_entSpawner/blob/de6fa54b6a892df142f014963c287e1cfc1a544e/resources/bin/x64/plugins/cyber_engine_tweaks/mods/entSpawner/modules/classes/spawn/physics/physicalDestruction.lua)
also explicitly requires a mesh with a fracture hierarchy.

**Baked destruction** uses `worldBakedDestructionNode` or
`entBakedDestructionComponent`. It plays authored destruction rather than
simulating every break dynamically. The schema exposes frame count/rate,
restart behavior, collider disabling, effects and an optional fractured mesh.
This is a promising mechanism for controlled set pieces when suitable assets
exist. The [fork's implementation](https://github.com/Akiway/CP77_entSpawner/blob/de6fa54b6a892df142f014963c287e1cfc1a544e/resources/bin/x64/plugins/cyber_engine_tweaks/mods/entSpawner/modules/classes/spawn/physics/bakedDestruction.lua)
states that the mesh needs baked destruction animation data.

An ordinary `worldDynamicMeshNode` supplies rigid-body movement, not destruction.
The [supported-node documentation](https://wiki.redmodding.org/cyberpunk-2077-modding/modding-guides/world-editing/object-spawner/supported-nodes)
makes that distinction explicitly.

## Explosions and damage to characters

The cached decompiled scripts supply more specific evidence than class names:

- `ExplosiveDevice.Explode` calls an attack, a physics pulse and visual effects
  separately, then sets exploded state. `DoAttack` resolves the configured attack
  record through `RPGManager.PrepareGameEffectAttack` and starts it. Instigator
  handling distinguishes player involvement, friendly-fire flags and quickhacks.
- `EnvironmentDamageReceiverComponent.DealDamageFromParticle` resolves particle
  damage records to attack records and starts attacks against its owning object.
  Records also contribute cooldown. This establishes a particle-to-gameplay
  damage path; it does not make every fire or spark particle damaging.
- `AOEArea.ActivateEffect` creates and starts an attack from the configured area
  effect. Its shutdown path terminates the effect and can remove active status
  effects from overlapping entities.

The script dump's version/freshness was not independently established here.
These are concrete implementation leads, not a substitute for testing the
installed runtime. A visual explosion, physics impulse, damaging attack and AI
hazard stimulus must be evaluated separately. Falling debris is not proven to
damage V or an NPC merely because it has collision.

For production, start with a complete native donor. Target filters, damage
scaling, friendly fire, attribution, line of sight and repeated damage all need
to be tested for the particular attack selected. Prefer a bounded native area
effect or attack over an unrestricted script polling every nearby object.

## Quest integration and persistence

WolvenKit exposes `questEntityManagerSetDestructionState_NodeType`, targeting
objects by reference/tag. Its action enum contains `Undefined` and `Trigger`;
this is not evidence of a general repair/reset API.
`questDestruction_ConditionType` exposes an object reference and threshold.
Those schemas suggest a native trigger/observation route, but compatible target
classes and threshold semantics still require a donor example and gameplay test.

The cached scripts also show `DestructibleMasterDevice` reacting to
`PhysicalDestructionEvent` and its controller notifying connected slave devices.
That is a useful lead for equipment destruction disabling connected systems.
It does not establish that every raw world mesh emits a quest-addressable event.

Do not assume debris persistence, streamed object destruction state and quest
progress have identical lifetimes. Record durable story consequences in quest
state and explicitly restore the intended scene state after reload. Test saves
before impact, after partial damage and after destruction, then stream the area
out/in and reload. Avoid treating a generic world-node handle as a permanent
entity identity.

## Ghostline's current authoring gap

`tools/building_builder.py:native_documents` currently emits regular
`worldMeshNode` visuals and separate `worldCollisionNode` solids. It does not
emit the destruction node families discussed above. A wall created by the
building editor therefore does not become breakable by choosing a destructive
looking mesh or effect.

The installed World Builder physics directory contains only `dynamicMesh.lua`.
The cached Akiway fork at `de6fa54b6a892df142f014963c287e1cfc1a544e`
has dedicated instanced, physical and baked destruction classes and native
export paths. Both physical and baked implementations explicitly say destruction
is not played in their editor preview. Source support is stronger than the
installed editor's current feature set, but neither establishes an observed
Ghostline gameplay result. The fork's optional per-mesh defaults catalogs also
need checking before relying on automatic donor settings.

For a breakable wall, author the whole transition:

1. Preserve the intact panel's collision and damage-receiving behavior.
2. Break or replace the visible panel at the chosen threshold.
3. Remove the correct blocking collision without removing structural neighbors.
4. Ensure existing occlusion/proxies do not hide the opening or restore an intact
   wall at distance.
5. Prove player traversal and separately prove NPC navigation through the opening.
6. Persist the chosen state and define what reload/re-entry should reconstruct.

Disabling a destruction object's own colliders does not remove an independent
wall collider. Similarly, a navigation setting on a node is not proof of runtime
navmesh regeneration. A route can be visually open yet remain physically or
AI-inaccessible. Existing-city retrofits must also account for the original
sector's collision, occluders and distant proxies.

## A useful first proof

Use an isolated experiment project with its own depot prefix and package profile.
Place the native Kabuki glass donor, one instanced prop, the baked roadblock pair
and one complete explosive-device donor. Preserve donor settings first. Add a
plain static mesh as a control. This tests each mechanism independently before
combining them into a quest route.

For each, observe bullets, melee, an explosion and physical impact where
applicable; distinguish visual breakage, collision changes, actual character
health loss and quest notification. Check repeated triggering, partial damage,
save/reload, streaming and debris cleanup. Then test a single breakable panel in
a two-room layout, including an NPC crossing the resulting opening.

Only after that proof should the building schema gain a destruction specification
covering mechanism, donor, thresholds, effects, collision ownership and durable
state. Custom fracture-data generation and unrestricted structural collapse
remain separate research tasks. A deliberately authored breach or collapsed-room
variant offers a credible path without depending on those unsolved capabilities.
