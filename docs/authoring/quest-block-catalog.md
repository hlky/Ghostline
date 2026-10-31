# Quest block catalog

Registry-derived capabilities; recorded evidence is valid only for its listed hashes and scope, never every configuration of a block.

Use `docs/authoring/quest-composition.md` for authoring patterns. Fields and implementation limits below come from the compiler registry.

## `meet_contact`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `accept_exit` | no | yes |
| `accepted_fact` | no | yes |
| `appearance` | no | yes |
| `checkpoint` | no | yes |
| `community` | yes | yes |
| `community_phase` | no | yes |
| `contact` | yes | yes |
| `contract` | no | yes |
| `defer_exit` | no | yes |
| `defer_policy` | no | yes |
| `description_entry` | yes | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `mappin` | yes | yes |
| `meeting_checkpoint` | no | yes |
| `notes` | no | yes |
| `objective` | yes | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `opening_message` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `rearm_trigger` | no | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `scene` | yes | yes |
| `scene_entry` | no | yes |
| `scene_origin` | no | yes |
| `setup_trigger` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `projects/ghostline/quests/gq001/implementation/quest.json` → `meet_patch` (ready).
- `projects/ghostline/quests/gq001/implementation/quest.json` → `meet_iris` (ready).
- `projects/ghostline/quests/gq002/implementation/quest.json` → `meet_cinder` (ready).
- `projects/ghostline/quests/gq003/implementation/quest.json` → `meet_iris_briefing` (planned).
- `projects/ghostline/quests/gq003/implementation/quest.json` → `meet_iris_safe_site` (planned).
- `projects/ghostline/quests/gq004/implementation/quest.json` → `meet` (ready).
- `projects/ghostline/quests/gq004/implementation/quest.json` → `return` (ready).
- `projects/test-quests/gqt005/gqt005_braindance_analysis.quest.json` → `meet_patch` (ready).
- `projects/test-quests/gqt006/gqt006_goth_baddie_cyberpsycho.quest.json` → `challenge_goth_baddie` (ready).
- `projects/test-quests/gqt007/gqt007_barry_lipsync.quest.json` → `compare_barry_lipsync` (ready).
- `quests/examples/generated-block-variants.quest.json` → `meet_contact` (planned).
- `quests/examples/generated-building-blocks.quest.json` → `meet_contact` (planned).
- `quests/examples/recipes/investigation.quest.json` → `meeting` (planned).

## `cyberpsycho_encounter`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `activate` | no | yes |
| `activation_mode` | no | yes |
| `activation_trigger` | yes | yes |
| `alerted_path` | no | yes |
| `alerted_spots` | no | yes |
| `arena_mode` | no | yes |
| `arena_trigger` | no | yes |
| `authoring` | no | yes |
| `boss_character` | yes | yes |
| `boss_entry` | yes | yes |
| `checkpoint` | no | yes |
| `cleanup` | no | yes |
| `community` | yes | yes |
| `completion_fact` | no | yes |
| `contract` | no | yes |
| `description_entry` | no | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `mappin` | no | yes |
| `notes` | no | yes |
| `objective` | no | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `player_defeat_scene` | no | yes |
| `postfight_scene` | no | yes |
| `required_assets` | no | yes |
| `resolution` | yes | yes |
| `retry_checkpoint` | no | yes |
| `reveal` | yes | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `projects/test-quests/gqt006/gqt006_goth_baddie_cyberpsycho.quest.json` → `neutralize_goth_baddie` (ready).
- `quests/examples/cyberpsycho_encounter.quest.json` → `face_cyberpsycho` (planned).

## `phone_job_offer`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `accept_choice` | yes | yes |
| `accepted_fact` | yes | yes |
| `checkpoint` | no | yes |
| `choice_group` | yes | yes |
| `contact` | yes | yes |
| `contract` | no | yes |
| `delay_game_hours` | no | yes |
| `delay_seconds` | no | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `message` | yes | yes |
| `notes` | no | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `prerequisite_fact` | no | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `start_fact` | yes | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `projects/ghostline/quests/gq001/implementation/quest.json` → `patch_job_offer` (ready).
- `projects/ghostline/quests/gq002/implementation/quest.json` → `patch_job_offer` (ready).
- `projects/ghostline/quests/gq003/implementation/quest.json` → `patch_job_offer` (planned).
- `projects/ghostline/quests/gq004/implementation/quest.json` → `offer` (ready).
- `quests/examples/recipes/investigation.quest.json` → `offer` (planned).

## `hack_access_point`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `action` | no | yes |
| `checkpoint` | no | yes |
| `completion_function` | no | yes |
| `contract` | no | yes |
| `controller_class` | no | yes |
| `description_entry` | no | yes |
| `device` | yes | yes |
| `grants` | no | yes |
| `guard_community` | no | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `mappin` | no | yes |
| `notes` | no | yes |
| `objective` | no | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `send_action` | no | yes |
| `status` | no | yes |
| `success_fact` | yes | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `projects/ghostline/quests/gq001/implementation/quest.json` → `hack_relay` (ready).
- `projects/ghostline/quests/gq003/implementation/quest.json` → `breach_dispatch_relay` (planned).
- `projects/ghostline/quests/gq004/implementation/quest.json` → `recover` (ready).
- `quests/examples/generated-building-blocks.quest.json` → `hack_access_point` (planned).

## `deliver_drop_point`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `checkpoint` | no | yes |
| `contract` | no | yes |
| `deposit_fact` | yes | yes |
| `description_entry` | no | yes |
| `drop_point` | yes | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `item` | no | yes |
| `item_branches` | no | yes |
| `mappin` | no | yes |
| `notes` | no | yes |
| `objective` | no | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `projects/ghostline/quests/gq001/implementation/quest.json` → `deliver_cache` (ready).
- `projects/ghostline/quests/gq003/implementation/quest.json` → `deliver_black_lantern_package` (planned).
- `quests/examples/generated-building-blocks.quest.json` → `deliver_drop_point` (planned).

## `phone_conversation`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `checkpoint` | no | yes |
| `choice_group` | yes | yes |
| `choices` | yes | yes |
| `complete_quest` | no | yes |
| `completion_fact` | no | yes |
| `conditional_message_groups` | no | yes |
| `contact` | yes | yes |
| `contract` | no | yes |
| `delay_seconds` | no | yes |
| `description_entry` | no | yes |
| `final_message` | yes | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `messages` | yes | yes |
| `notes` | no | yes |
| `objective` | no | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `opening_branches` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `postscript_messages` | no | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `reward` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `thread` | yes | yes |
| `type` | yes | yes |

Examples:

- `projects/ghostline/quests/gq002/implementation/quest.json` → `relay_decision` (ready).
- `projects/ghostline/quests/gq002/implementation/quest.json` → `cinder_debrief` (ready).
- `projects/ghostline/quests/gq003/implementation/quest.json` → `receive_yard_identifier` (planned).
- `projects/ghostline/quests/gq003/implementation/quest.json` → `clinic_location_call` (planned).
- `projects/ghostline/quests/gq003/implementation/quest.json` → `patch_confession` (planned).
- `projects/ghostline/quests/gq003/implementation/quest.json` → `argue_relay_outcome` (planned).
- `projects/ghostline/quests/gq003/implementation/quest.json` → `black_lantern_debrief` (planned).
- `projects/ghostline/quests/gq004/implementation/quest.json` → `ending` (ready).
- `projects/test-quests/gqt001/gqt001_signal_delay.quest.json` → `confirm_result` (ready).
- `projects/test-quests/gqt006/gqt006_goth_baddie_cyberpsycho.quest.json` → `report_goth_baddie_outcome` (ready).
- `quests/examples/phone_conversation.quest.json` → `morrow_followup` (ready).
- `quests/examples/recipes/encounter.quest.json` → `report` (planned).
- `quests/examples/recipes/investigation.quest.json` → `debrief` (planned).

## `reach_area`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `checkpoint` | no | yes |
| `contract` | no | yes |
| `description_entry` | yes | yes |
| `disable_previous_mappins` | no | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `mappin` | yes | yes |
| `notes` | no | yes |
| `objective` | yes | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `start_fact` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `trigger` | yes | yes |
| `type` | yes | yes |

Examples:

- `projects/experiments/npc-runtime/implementation/jobs/data-theft.quest.json` → `reach_target` (ready).
- `projects/ghostline/quests/gq002/implementation/quest.json` → `reach_relay` (ready).
- `projects/ghostline/quests/gq002/implementation/quest.json` → `return_to_relay` (ready).
- `projects/ghostline/quests/gq003/implementation/quest.json` → `reach_freight_yard` (planned).
- `projects/ghostline/quests/gq003/implementation/quest.json` → `reach_memory_clinic` (planned).
- `projects/ghostline/quests/gq003/implementation/quest.json` → `enter_reconstruction_relay` (planned).
- `projects/ghostline/quests/gq004/implementation/quest.json` → `reach` (ready).
- `projects/test-quests/gqt001/gqt001_signal_delay.quest.json` → `reach_terminal` (ready).
- `projects/test-quests/gqt003/gqt003_extract_and_hold.quest.json` → `reach_extraction_relay` (ready).
- `projects/test-quests/gqt005/gqt005_braindance_analysis.quest.json` → `approach_patch` (ready).
- `quests/examples/direct_building_blocks.quest.json` → `reach_relay` (ready).

Evidence:

- `gq_blocks_direct-structural-build`: build, stale, passed=True. Compiled raw phase graphs in memory and passed compiler graph/socket checks. No native serialization, resource/world audit, packaging, or game execution.
  - Changed bound resource: quests/templates/journal/catalog.json
  - Changed bound resource: tools/generate_advanced_quest_block_templates.py
  - Changed bound resource: tools/quest-schema-v1.json
  - Changed bound resource: tools/quest_authoring.py
  - Changed bound resource: tools/quest_compiler.py
  - Changed bound resource: tools/quest_flow.py
  - Changed bound resource: tools/quest_stage_validation.py
  - Changed bound resource: tools/quest_stages.py

## `leave_area`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `checkpoint` | no | yes |
| `cleanup_community` | no | yes |
| `completion_fact` | no | yes |
| `contract` | no | yes |
| `description_entry` | yes | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `mappin` | no | yes |
| `notes` | no | yes |
| `objective` | yes | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `trigger` | yes | yes |
| `type` | yes | yes |

Examples:

- `projects/ghostline/quests/gq002/implementation/quest.json` → `leave_relay` (ready).
- `projects/ghostline/quests/gq003/implementation/quest.json` → `leave_freight_yard` (planned).
- `projects/ghostline/quests/gq003/implementation/quest.json` → `leave_reconstruction_relay` (planned).
- `projects/ghostline/quests/gq004/implementation/quest.json` → `leave` (ready).
- `projects/test-quests/gqt006/gqt006_goth_baddie_cyberpsycho.quest.json` → `leave_goth_baddie_site` (ready).
- `quests/examples/direct_building_blocks.quest.json` → `leave_relay` (ready).
- `quests/examples/recipes/rescue.quest.json` → `extraction` (planned).

Evidence:

- `gq_blocks_direct-structural-build`: build, stale, passed=True. Compiled raw phase graphs in memory and passed compiler graph/socket checks. No native serialization, resource/world audit, packaging, or game execution.
  - Changed bound resource: quests/templates/journal/catalog.json
  - Changed bound resource: tools/generate_advanced_quest_block_templates.py
  - Changed bound resource: tools/quest-schema-v1.json
  - Changed bound resource: tools/quest_authoring.py
  - Changed bound resource: tools/quest_compiler.py
  - Changed bound resource: tools/quest_flow.py
  - Changed bound resource: tools/quest_stage_validation.py
  - Changed bound resource: tools/quest_stages.py

## `acquire_item`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `acquisition_fact` | no | yes |
| `checkpoint` | no | yes |
| `contract` | no | yes |
| `description_entry` | no | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `item` | yes | yes |
| `mappin` | no | yes |
| `notes` | no | yes |
| `objective` | no | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `quantity` | no | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `source` | yes | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `projects/test-quests/gqt006/gqt006_goth_baddie_cyberpsycho.quest.json` → `recover_goth_baddie_shard` (ready).
- `quests/examples/direct_building_blocks.quest.json` → `acquire_datacache` (ready).

Evidence:

- `gq_blocks_direct-structural-build`: build, stale, passed=True. Compiled raw phase graphs in memory and passed compiler graph/socket checks. No native serialization, resource/world audit, packaging, or game execution.
  - Changed bound resource: quests/templates/journal/catalog.json
  - Changed bound resource: tools/generate_advanced_quest_block_templates.py
  - Changed bound resource: tools/quest-schema-v1.json
  - Changed bound resource: tools/quest_authoring.py
  - Changed bound resource: tools/quest_compiler.py
  - Changed bound resource: tools/quest_flow.py
  - Changed bound resource: tools/quest_stage_validation.py
  - Changed bound resource: tools/quest_stages.py

## `read_shard`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `acquisition_fact` | no | yes |
| `activate_entry` | no | yes |
| `checkpoint` | no | yes |
| `completion_fact` | no | yes |
| `contract` | no | yes |
| `description_entry` | no | yes |
| `file_entry_index` | yes | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `item` | yes | yes |
| `journal_entry` | yes | yes |
| `notes` | no | yes |
| `objective` | no | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `presentation_delay_seconds` | no | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `projects/ghostline/quests/gq002/implementation/quest.json` → `read_hostage_circuit` (ready).
- `projects/ghostline/quests/gq003/implementation/quest.json` → `read_expedited_handoff` (planned).
- `projects/test-quests/gqt006/gqt006_goth_baddie_cyberpsycho.quest.json` → `read_goth_baddie_shard` (ready).
- `quests/examples/direct_building_blocks.quest.json` → `read_datacache` (ready).

Evidence:

- `gq_blocks_direct-structural-build`: build, stale, passed=True. Compiled raw phase graphs in memory and passed compiler graph/socket checks. No native serialization, resource/world audit, packaging, or game execution.
  - Changed bound resource: quests/templates/journal/catalog.json
  - Changed bound resource: tools/generate_advanced_quest_block_templates.py
  - Changed bound resource: tools/quest-schema-v1.json
  - Changed bound resource: tools/quest_authoring.py
  - Changed bound resource: tools/quest_compiler.py
  - Changed bound resource: tools/quest_flow.py
  - Changed bound resource: tools/quest_stage_validation.py
  - Changed bound resource: tools/quest_stages.py

## `interact_device`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `action` | yes | yes |
| `checkpoint` | no | yes |
| `completion_function` | yes | yes |
| `contract` | no | yes |
| `controller_class` | yes | yes |
| `description_entry` | no | yes |
| `device` | yes | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `mappin` | no | yes |
| `notes` | no | yes |
| `objective` | no | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcome_branches` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `send_action` | no | yes |
| `status` | no | yes |
| `success_fact` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `projects/experiments/npc-runtime/implementation/jobs/data-theft.quest.json` → `steal_credentials` (ready).
- `projects/ghostline/quests/gq002/implementation/quest.json` → `operate_relay` (ready).
- `projects/ghostline/quests/gq003/implementation/quest.json` → `disable_neural_jammer` (planned).
- `projects/ghostline/quests/gq003/implementation/quest.json` → `operate_reconstruction_core` (planned).
- `projects/ghostline/quests/gq004/implementation/quest.json` → `upload` (ready).
- `quests/examples/template_building_blocks.quest.json` → `use_terminal` (ready).

## `combat_encounter`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `activate` | no | yes |
| `checkpoint` | no | yes |
| `cleanup_on_exit` | no | yes |
| `community` | yes | yes |
| `completion` | yes | yes |
| `completion_fact` | no | yes |
| `contract` | no | yes |
| `description_entry` | no | yes |
| `entries` | no | yes |
| `hostility` | yes | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `nonlethal_allowed` | no | yes |
| `notes` | no | yes |
| `objective` | no | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `threat_duration_seconds` | no | yes |
| `threat_function` | no | yes |
| `trigger` | no | yes |
| `type` | yes | yes |

Examples:

- `projects/ghostline/quests/gq002/implementation/quest.json` → `relay_security` (ready).
- `projects/ghostline/quests/gq003/implementation/quest.json` → `clear_clinic_security` (planned).
- `projects/ghostline/quests/gq003/implementation/quest.json` → `defeat_retrieval_team` (planned).
- `quests/examples/recipes/encounter.quest.json` → `encounter` (planned).
- `quests/examples/template_building_blocks.quest.json` → `clear_guards` (ready).

## `investigate_clues`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `checkpoint` | no | yes |
| `clues` | yes | yes |
| `completion_fact` | no | yes |
| `contract` | no | yes |
| `description_entry` | yes | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `notes` | no | yes |
| `objective` | yes | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `required_assets` | no | yes |
| `required_count` | no | yes |
| `retry_checkpoint` | no | yes |
| `scan_order` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `projects/ghostline/quests/gq002/implementation/quest.json` → `investigate_relay` (ready).
- `projects/ghostline/quests/gq003/implementation/quest.json` → `investigate_yard` (planned).
- `projects/ghostline/quests/gq003/implementation/quest.json` → `investigate_reconstruction_relay` (planned).
- `quests/examples/recipes/encounter.quest.json` → `evidence` (planned).
- `quests/examples/recipes/investigation.quest.json` → `investigation` (planned).
- `quests/examples/template_building_blocks.quest.json` → `scan_clue` (ready).

## `optional_condition`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `checkpoint` | no | yes |
| `condition` | yes | yes |
| `contract` | no | yes |
| `description_entry` | no | yes |
| `evaluation` | yes | yes |
| `failure_fact` | yes | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `notes` | no | yes |
| `objective` | yes | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `status` | no | yes |
| `success_fact` | yes | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `quests/examples/generated-block-variants.quest.json` → `optional_condition` (planned).
- `quests/examples/generated-building-blocks.quest.json` → `optional_condition` (planned).
- `quests/examples/template_building_blocks.quest.json` → `record_optional_result` (ready).

## `choice_gate`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `branches` | yes | yes |
| `checkpoint` | no | yes |
| `contract` | no | yes |
| `default_branch` | no | yes |
| `evaluation` | no | yes |
| `gate_kind` | yes | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `join` | yes | yes |
| `notes` | no | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `projects/experiments/npc-runtime/implementation/jobs/data-theft.quest.json` → `resolve_delivery` (ready).
- `projects/ghostline/quests/gq002/implementation/quest.json` → `relay_choice` (ready).
- `projects/ghostline/quests/gq003/implementation/quest.json` → `choose_relay_outcome` (planned).
- `quests/examples/generated-building-blocks.quest.json` → `choice_gate` (planned).
- `quests/examples/recipes/investigation.quest.json` → `decision` (planned).
- `quests/examples/template_building_blocks.quest.json` → `resolve_choice` (ready).

## `escort_npc`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `actor_lifecycle` | no | yes |
| `allow_combat_interrupt` | no | yes |
| `cancellation_fact` | no | yes |
| `cancelled_fact` | no | yes |
| `checkpoint` | no | yes |
| `community` | yes | yes |
| `completion_fact` | yes | yes |
| `contract` | no | yes |
| `description_entry` | no | yes |
| `destinations` | yes | yes |
| `entry` | yes | yes |
| `failure_fact` | no | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `mappin` | yes | yes |
| `notes` | no | yes |
| `objective` | yes | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `route_mappins` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `projects/ghostline/quests/gq003/implementation/quest.json` → `escort_mara` (planned).
- `projects/test-quests/gqt003/gqt003_extract_and_hold.quest.json` → `escort_patch` (ready).
- `quests/examples/generated-building-blocks.quest.json` → `escort_npc` (planned).
- `quests/examples/recipes/rescue.quest.json` → `escort` (planned).
- `quests/examples/template_building_blocks.quest.json` → `escort_contact` (ready).
- `quests/examples/timed-defense-retry.quest.json` → `escort_patch` (ready).

## `carry_npc`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `checkpoint` | no | yes |
| `community` | yes | yes |
| `completion_fact` | no | yes |
| `contract` | no | yes |
| `description_entry` | no | yes |
| `destination` | yes | yes |
| `entry` | yes | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `mappin` | no | yes |
| `notes` | no | yes |
| `objective` | yes | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `placement_slot` | no | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |
| `waypoints` | no | yes |

Examples:

- `quests/examples/generated-block-variants.quest.json` → `carry_npc` (planned).
- `quests/examples/generated-building-blocks.quest.json` → `carry_npc` (planned).
- `quests/examples/template_building_blocks.quest.json` → `carry_contact` (ready).

## `deliver_vehicle`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `checkpoint` | no | yes |
| `completion_fact` | no | yes |
| `contract` | no | yes |
| `description_entry` | no | yes |
| `destination` | yes | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `mappin` | no | yes |
| `notes` | no | yes |
| `objective` | yes | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `require_player_exit` | no | yes |
| `require_stop` | no | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |
| `vehicle` | yes | yes |

Examples:

- `quests/examples/generated-block-variants.quest.json` → `deliver_vehicle` (planned).
- `quests/examples/generated-building-blocks.quest.json` → `deliver_vehicle` (planned).
- `quests/examples/template_building_blocks.quest.json` → `deliver_vehicle` (ready).

## `time_gate`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `checkpoint` | no | yes |
| `completion_fact` | no | yes |
| `contract` | no | yes |
| `days` | no | yes |
| `hours` | no | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `minutes` | no | yes |
| `notes` | no | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `seconds` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `projects/ghostline/quests/gq003/implementation/quest.json` → `wait_for_transfer_window` (planned).
- `projects/test-quests/gqt001/gqt001_signal_delay.quest.json` → `wait_for_reply` (ready).

## `read_terminal_document`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `checkpoint` | no | yes |
| `completion_fact` | yes | yes |
| `computer` | yes | yes |
| `contract` | no | yes |
| `description_entry` | no | yes |
| `document_entry` | no | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `notes` | no | yes |
| `objective` | yes | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `output_socket` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `scene` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `projects/ghostline/quests/gq003/implementation/quest.json` → `read_reconstruction_report` (planned).
- `projects/test-quests/gqt001/gqt001_signal_delay.quest.json` → `read_diagnostic` (ready).

## `stealth_monitor`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `additional_failure_facts` | no | yes |
| `checkpoint` | no | yes |
| `contract` | no | yes |
| `description_entry` | no | yes |
| `failure_fact` | yes | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `notes` | no | yes |
| `objective` | yes | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `status` | no | yes |
| `stop_fact` | yes | yes |
| `success_fact` | yes | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `projects/ghostline/quests/gq003/implementation/quest.json` → `remain_undetected` (planned).
- `projects/test-quests/gqt002/gqt002_quiet_install.quest.json` → `remain_undetected` (ready).
- `quests/examples/generated-block-variants.quest.json` → `stealth_monitor` (planned).
- `quests/examples/generated-building-blocks.quest.json` → `stealth_monitor` (planned).

## `plant_item`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `action` | yes | yes |
| `checkpoint` | no | yes |
| `completion_fact` | yes | yes |
| `completion_function` | yes | yes |
| `consume_item` | no | yes |
| `contract` | no | yes |
| `controller_class` | yes | yes |
| `description_entry` | no | yes |
| `device` | yes | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `item` | yes | yes |
| `notes` | no | yes |
| `objective` | yes | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `projects/ghostline/quests/gq003/implementation/quest.json` → `plant_routing_beacon` (planned).
- `projects/test-quests/gqt002/gqt002_quiet_install.quest.json` → `plant_keylogger` (ready).
- `quests/examples/generated-block-variants.quest.json` → `plant_item` (planned).
- `quests/examples/generated-building-blocks.quest.json` → `plant_item` (planned).

## `defend_target`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `actor_lifecycle` | no | yes |
| `attackers` | no | yes |
| `block_on_failure` | no | yes |
| `cancellation_fact` | no | yes |
| `cancelled_fact` | no | yes |
| `checkpoint` | no | yes |
| `community` | yes | yes |
| `completion_fact` | yes | yes |
| `contract` | no | yes |
| `description_entry` | no | yes |
| `duration_seconds` | no | yes |
| `entry` | yes | yes |
| `failure_fact` | yes | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `notes` | no | yes |
| `objective` | yes | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `projects/ghostline/quests/gq003/implementation/quest.json` → `stabilize_mara` (planned).
- `projects/test-quests/gqt003/gqt003_extract_and_hold.quest.json` → `defend_patch` (ready).
- `quests/examples/generated-building-blocks.quest.json` → `defend_target` (planned).
- `quests/examples/recipes/rescue.quest.json` → `defense` (planned).
- `quests/examples/timed-defense-retry.quest.json` → `defend_patch` (ready).

## `release_or_rescue_npc`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `action` | yes | yes |
| `additional_entries` | no | yes |
| `checkpoint` | no | yes |
| `community` | yes | yes |
| `completion_fact` | yes | yes |
| `completion_function` | yes | yes |
| `contract` | no | yes |
| `controller_class` | yes | yes |
| `description_entry` | no | yes |
| `device` | yes | yes |
| `entry` | yes | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `notes` | no | yes |
| `objective` | yes | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `projects/ghostline/quests/gq003/implementation/quest.json` → `release_mara` (planned).
- `projects/test-quests/gqt003/gqt003_extract_and_hold.quest.json` → `release_patch` (ready).
- `quests/examples/generated-block-variants.quest.json` → `release_or_rescue_npc` (planned).
- `quests/examples/generated-building-blocks.quest.json` → `release_or_rescue_npc` (planned).
- `quests/examples/recipes/rescue.quest.json` → `rescue` (planned).
- `quests/examples/timed-defense-retry.quest.json` → `release_patch` (ready).

## `enter_vehicle`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `checkpoint` | no | yes |
| `contract` | no | yes |
| `description_entry` | no | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `mappin` | yes | yes |
| `notes` | no | yes |
| `objective` | yes | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `player_role` | no | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |
| `vehicle_community` | yes | yes |
| `vehicle_entry` | yes | yes |

Examples:

- `projects/ghostline/quests/gq003/implementation/quest.json` → `enter_patch_vehicle` (planned).
- `projects/test-quests/gqt004/gqt004_vehicle_lab.quest.json` → `enter_contact_vehicle` (ready).
- `quests/examples/generated-building-blocks.quest.json` → `enter_vehicle` (planned).

## `ride_with_contact`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `additional_passengers` | no | yes |
| `checkpoint` | no | yes |
| `contact_community` | yes | yes |
| `contact_entry` | yes | yes |
| `contact_role` | no | yes |
| `contact_slot` | no | yes |
| `contract` | no | yes |
| `description_entry` | no | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `notes` | no | yes |
| `objective` | yes | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `player_role` | no | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |
| `vehicle_community` | yes | yes |
| `vehicle_entry` | yes | yes |
| `wait_for_contacts` | no | yes |

Examples:

- `projects/ghostline/quests/gq003/implementation/quest.json` → `ride_with_patch` (planned).
- `projects/test-quests/gqt004/gqt004_vehicle_lab.quest.json` → `ride_with_patch` (ready).
- `quests/examples/generated-block-variants.quest.json` → `ride_with_contact` (planned).
- `quests/examples/generated-building-blocks.quest.json` → `ride_with_contact` (planned).

## `drive_to`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `checkpoint` | no | yes |
| `completion_fact` | yes | yes |
| `contract` | no | yes |
| `description_entry` | no | yes |
| `destination` | yes | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `mappin` | yes | yes |
| `notes` | no | yes |
| `objective` | yes | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |
| `vehicle_community` | yes | yes |
| `vehicle_entry` | yes | yes |
| `waypoints` | no | yes |

Examples:

- `projects/ghostline/quests/gq003/implementation/quest.json` → `drive_patch_to_interchange` (planned).
- `projects/ghostline/quests/gq003/implementation/quest.json` → `drive_carrier_to_relay` (planned).
- `projects/test-quests/gqt004/gqt004_vehicle_lab.quest.json` → `drive_contact_to_destination` (ready).
- `projects/test-quests/gqt004/gqt004_vehicle_lab.quest.json` → `deliver_test_vehicle` (ready).
- `quests/examples/generated-block-variants.quest.json` → `drive_to` (planned).
- `quests/examples/generated-building-blocks.quest.json` → `drive_to` (planned).

## `steal_vehicle`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `checkpoint` | no | yes |
| `completion_fact` | yes | yes |
| `contract` | no | yes |
| `description_entry` | no | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `mappin` | yes | yes |
| `notes` | no | yes |
| `objective` | yes | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `player_role` | no | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |
| `vehicle_community` | yes | yes |
| `vehicle_entry` | yes | yes |

Examples:

- `projects/ghostline/quests/gq003/implementation/quest.json` → `steal_pair_07b` (planned).
- `projects/test-quests/gqt004/gqt004_vehicle_lab.quest.json` → `steal_test_vehicle` (ready).
- `quests/examples/generated-building-blocks.quest.json` → `steal_vehicle` (planned).

## `vehicle_cleanup`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `checkpoint` | no | yes |
| `cleanup_communities` | no | yes |
| `completion_fact` | yes | yes |
| `contract` | no | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `notes` | no | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `player_vehicle_record` | yes | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `projects/ghostline/quests/gq003/implementation/quest.json` → `cleanup_patch_vehicle` (planned).
- `projects/test-quests/gqt004/gqt004_vehicle_lab.quest.json` → `cleanup_test_vehicle` (ready).
- `quests/examples/generated-block-variants.quest.json` → `vehicle_cleanup` (planned).
- `quests/examples/generated-building-blocks.quest.json` → `vehicle_cleanup` (planned).

## `braindance_analysis`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `checkpoint` | no | yes |
| `clue_facts` | yes | yes |
| `completion_fact` | yes | yes |
| `contract` | no | yes |
| `exit_enable_seconds` | no | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `notes` | no | yes |
| `objective` | yes | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `player_anchor` | yes | yes |
| `player_return` | yes | yes |
| `required_assets` | no | yes |
| `retry_checkpoint` | no | yes |
| `scene` | yes | yes |
| `scene_entry` | no | yes |
| `scene_exit_sockets` | no | yes |
| `scene_origin` | yes | yes |
| `settle_seconds` | no | yes |
| `status` | no | yes |
| `teardown_seconds` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `projects/test-quests/gqt005/gqt005_braindance_analysis.quest.json` → `review_braindance` (ready).
- `quests/examples/generated-block-variants.quest.json` → `braindance_analysis` (planned).
- `quests/examples/generated-building-blocks.quest.json` → `braindance_analysis` (planned).

## `owned_scope`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `cancellation_fact` | no | yes |
| `checkpoint` | no | yes |
| `child` | yes | yes |
| `commit_fact` | no | yes |
| `contract` | no | yes |
| `effects` | no | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `notes` | no | yes |
| `notifications` | no | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `required_assets` | no | yes |
| `restore` | no | yes |
| `retry_checkpoint` | no | yes |
| `setup` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `quests/examples/owned-lifecycle-blocks.quest.json` → `owned_scope` (planned).

## `acquire_or_use`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `acquired_fact` | no | yes |
| `application` | yes | yes |
| `cancellation_fact` | no | yes |
| `checkpoint` | no | yes |
| `commit_fact` | no | yes |
| `contract` | no | yes |
| `effects` | no | yes |
| `existing_fact` | no | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `item` | yes | yes |
| `notes` | no | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `quantity` | no | yes |
| `required_assets` | no | yes |
| `restore` | no | yes |
| `retry_checkpoint` | no | yes |
| `setup` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `quests/examples/owned-lifecycle-blocks.quest.json` → `acquire_or_use` (planned).

## `access_routes`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `application` | yes | yes |
| `cancellation_fact` | no | yes |
| `checkpoint` | no | yes |
| `commit_fact` | no | yes |
| `contract` | no | yes |
| `effects` | no | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `notes` | no | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `required_assets` | no | yes |
| `restore` | no | yes |
| `retry_checkpoint` | no | yes |
| `route_facts` | no | yes |
| `routes` | yes | yes |
| `setup` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `quests/examples/owned-lifecycle-blocks.quest.json` → `access_routes` (planned).

## `resolve_and_report`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `cancellation_fact` | no | yes |
| `checkpoint` | no | yes |
| `commit_fact` | no | yes |
| `contract` | no | yes |
| `effects` | no | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `notes` | no | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `report` | yes | yes |
| `reported_fact` | yes | yes |
| `required_assets` | no | yes |
| `resolved_fact` | yes | yes |
| `restore` | no | yes |
| `retry_checkpoint` | no | yes |
| `setup` | no | yes |
| `status` | no | yes |
| `targets` | yes | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `quests/examples/owned-lifecycle-blocks.quest.json` → `resolve_and_report` (planned).

## `observe_lethal`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `cancellation_fact` | no | yes |
| `checkpoint` | no | yes |
| `commit_fact` | no | yes |
| `contract` | no | yes |
| `effects` | no | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `notes` | no | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `required_assets` | no | yes |
| `restore` | no | yes |
| `retry_checkpoint` | no | yes |
| `setup` | no | yes |
| `status` | no | yes |
| `stop_fact` | yes | yes |
| `targets` | yes | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `quests/examples/owned-lifecycle-blocks.quest.json` → `observe_lethal` (planned).

## `reward_commit`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `checkpoint` | no | yes |
| `commit_fact` | yes | yes |
| `contract` | no | yes |
| `effects` | no | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `item` | yes | yes |
| `notes` | no | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `quantity` | no | yes |
| `reported_fact` | yes | yes |
| `required_assets` | no | yes |
| `restore` | no | yes |
| `retry_checkpoint` | no | yes |
| `setup` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `quests/examples/owned-lifecycle-blocks.quest.json` → `reward_commit` (planned).

## `contact_fallback`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `call` | yes | yes |
| `cancellation_fact` | no | yes |
| `checkpoint` | no | yes |
| `connected_fact` | yes | yes |
| `contract` | no | yes |
| `effects` | no | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `message` | yes | yes |
| `message_fact` | yes | yes |
| `notes` | no | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `required_assets` | no | yes |
| `restore` | no | yes |
| `retry_checkpoint` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |
| `unavailable_facts` | no | yes |

Examples:

- `quests/examples/owned-lifecycle-blocks.quest.json` → `contact_fallback` (planned).

## `adaptive_timer`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `busy_fact` | no | yes |
| `cancellation_fact` | no | yes |
| `checkpoint` | no | yes |
| `choices` | yes | yes |
| `clock` | yes | yes |
| `commit_fact` | no | yes |
| `contract` | no | yes |
| `effects` | no | yes |
| `eligibility_fact` | no | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `max_deferral_seconds` | no | yes |
| `notes` | no | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `profiles` | no | yes |
| `required_assets` | no | yes |
| `restore` | no | yes |
| `retry_checkpoint` | no | yes |
| `setup` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `quests/examples/owned-lifecycle-blocks.quest.json` → `adaptive_timer` (planned).
- `quests/examples/owned-lifecycle-variants.quest.json` → `game_clock` (planned).

## `entitlement_reconcile`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `checkpoint` | no | yes |
| `contract` | no | yes |
| `effects` | no | yes |
| `entitled_fact` | no | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `notes` | no | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `owned_fact` | yes | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `required_assets` | no | yes |
| `restore` | no | yes |
| `retire` | yes | yes |
| `retry_checkpoint` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |
| `vehicle_record` | no | yes |

Examples:

- `quests/examples/owned-lifecycle-blocks.quest.json` → `entitlement_reconcile` (planned).
- `quests/examples/owned-lifecycle-variants.quest.json` → `native_vehicle` (planned).

## `investigate_reactions`

Implementation: `generated`. Structural build recorded: **false**. Current in-game pass recorded: **false**.

Inputs: `{"start": "In1"}`. Outcomes: `{"success": "Out1"}`.

| Field | Required | Default-template support |
| --- | --- | --- |
| `cancellation_fact` | no | yes |
| `checkpoint` | no | yes |
| `clues` | yes | yes |
| `commit_fact` | no | yes |
| `contract` | no | yes |
| `discovery_fact` | no | yes |
| `effects` | no | yes |
| `id` | yes | yes |
| `inherit_phase_prefabs` | no | yes |
| `inputs` | no | yes |
| `notes` | no | yes |
| `objective_lifecycle` | no | yes |
| `on` | no | yes |
| `outcomes` | no | yes |
| `phase_prefabs` | no | yes |
| `phase_resource` | yes | yes |
| `phase_template` | no | yes |
| `required_assets` | no | yes |
| `required_count` | no | yes |
| `restore` | no | yes |
| `retry_checkpoint` | no | yes |
| `setup` | no | yes |
| `status` | no | yes |
| `template_bindings` | no | yes |
| `type` | yes | yes |

Examples:

- `quests/examples/owned-lifecycle-blocks.quest.json` → `investigate_reactions` (planned).
