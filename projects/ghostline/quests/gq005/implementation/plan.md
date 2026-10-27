# Implementation plan and first playable gate

Status: authoring/preproduction. No compiled GQ005 graph, installed quest,
delivery locations, generated VO or verified performance yet. The story project
owns GQ005 and Leena depot paths. Registering ownership does not activate a quest
in a packaging profile.

## First playable route

After surveying one real delivery spot, implement the smallest complete route:
Leena offer/accept → acquire parcel A → controlled handover → return → base pay
→ completed journal. Use provisional voice/presentation and the working AKPP
office. A temporary one-stop route is explicitly a development milestone, not
the finished three-stop quest. Preserve its accepted-state and reward semantics
when adding B/C.

Review `docs/authoring/native-quest-template.md`, local `modding_docs`, working
GQ004 scenes and compiler block examples before choosing native implementations.
Do not alter the current GQ000 root/child handoff merely to add this side quest.
If integration needs that handoff, read its runtime-flow contract first.

Gate: installed named package; accept, defer/return, interrupt, deliver, return,
reward and reload all observed in game. Only then bulk-produce performance.

## Block mapping

These map desired behaviour onto existing building-block concepts. They are not
a claim that arbitrary scene interactions compile directly from this table.

| Behaviour | Block / contract | Binding still needed |
| --- | --- | --- |
| Pickup three parcels | `acquire_item`, one identity per parcel | Authored item records and one-shot grant |
| Handover A/B/C | `deliver_drop_point` with correct item/receipt | Surveyed drop nodes; inspect block transfer semantics |
| Security code | Scene choices plus access fact | Door/device controller and both converging choices |
| Lift notice, buzzer | `interact_device` where native precedent fits | Exact entity/controller and completion signal |
| Read policy | Native computer file read fact | Quest-specific readable identity on existing terminal |
| Kitchen courtesy | `optional_condition` | Explicitly no rating/reward penalty |
| Final three choices | `choice_gate`, exclusive facts | Confirmation scenes/device actions and idempotent reward |

Before coding, inspect `tools/quest_authoring_schema.py`,
`tools/quest-schema-v1.json`, `quests/examples/direct_building_blocks.quest.json`
and `quests/examples/template_building_blocks.quest.json`. Do not invent a
ready-to-compile manifest with unresolved locations or unsupported stage fields.

## Proposed facts and ownership

| Fact (prefix `gq005_`) | Owner / meaning |
| --- | --- |
| accepted | Briefing acceptance transaction committed |
| parcels_issued | Inventory grant completed, not simply offer displayed |
| access_a | Either access dialogue provided the valid code |
| delivered_a / delivered_b / delivered_c | Correct parcel consumed and receipt accepted |
| kitchen_courtesy | Optional B action; flavour only |
| score_shown | Fixed 4.59 message delivered once |
| policy_read | Named policy file selected/read |
| ending_accept / ending_expose / ending_correct | Exclusive committed resolution |
| base_paid / bonus_paid | Separate one-shot payment receipts |
| complete | Ending, required payment and journal completion settled |

Only handover logic consumes parcels. Only settlement logic grants money. UI
actions request a transaction; replay/reload must not duplicate its effects.
Do not write a paid flag before a failed grant or grant again after an interrupted
response. Confirm native transaction/save behaviour in the route prototype.

Timed notifications and waits need persisted stage/cooldown ownership and clean
teardown. Dialogue entry checks active quest stage and actor readiness. No
elapsed-time target locks rewards or causes failure.

## Leena and office integration

`characters/leena.character.json` uses the female-average neutral shell and
reviewed component catalogue. Generated candidate is isolated under
`projects/ghostline/generated/gq005/leena-candidate`. It is not applied to source
or installed. Keep the generic worker until the new character is visually and
mechanically validated. Never change only a male worker's appearance to a female
asset; bind the new character record/entity and matching seated workspot.

Replace the Building Lab worker through an explicit integration/export change.
Give Leena a stable actor identity for scene acquisition. Check sitting fit,
scene entry, interruption, return to workspot, speech/eyes and save/load. Own the
terminal's policy read fact separately from its existing workstation test fact.

Leena belongs to `Factions.AKPPLogistics`, a custom neutral faction based on
`Factions.Unaffiliated`, with localized display name AKPP Logistics. Its authored
TweakXL record is `source/resources/r6/tweaks/ghostline/faction_akpp_logistics.yaml`.
The character's localization template includes the matching faction label. The NPV candidate declares Phantom Liberty and retains donor
dependencies. Asset closure, original tutorial texture references, both normal
and compiled component copies, shadow/cuff companions and overlays need review.

## Delivery and ending milestones

1. Survey A/B and select exact actor/drop/access positions.
2. Prove one-stop route and reward lifecycle with provisional presentation.
3. Add B/C, access choices, app order, receipts and the optional kitchen branch.
4. Add policy read gate and three explicit settlement confirmations. Verify
   exposure redaction and local-batch scope in text and simulated effects.
5. Review the complete walkthrough/dialogue with user feedback; revise before
   voice auditions and full synthesis. Use the voice environment preflight.
6. Finish Leena appearance, customer/guard casting, scenes, VO and lipsync.
7. Full timed run, all endings, interruptions, save/load and accessibility check.

## Evidence and handoff

Record authoring/serialization checks, archive/install checks and observed
gameplay separately. Name candidate hash and save state for every playtest.
Required scenarios include defer/return, early future-stop visit, both security
solutions, both customer branches, skipped C wait, unread policy, all endings,
interrupted payment, missing parcel recovery, and no duplicate manager on load.

No auto-install is part of this planning pass. No bulk VO until readable review;
no new tower construction before checking existing retrofits.
