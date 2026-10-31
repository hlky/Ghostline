# base-ma-bls-ina-07

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\community\ma_bls_ina_se1_07_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\test\ma_bls_ina_07_chicken.scene; base\open_world\phases\open_world_content.questphase |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase` | content candidate | 6 / 0 | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\test\ma_bls_ina_07_chicken.scene` | test/debug | 0 / 5 |  |

## Journal paths observed in these resources

- `contacts/player`
- `contacts/regina_jones`
- `contacts/regina_jones/ma_bls_ina_se1_07/00_msg_rejected_call`
- `contacts/regina_jones/ma_bls_ina_se1_07/00_msg_start`
- `contacts/regina_jones/ma_bls_ina_se1_07/01_ch_info/01_ch_info`
- `contacts/regina_jones/ma_bls_ina_se1_07/01_ch_info/01_ch_info_killed`
- `contacts/regina_jones/ma_bls_ina_se1_07/01_ch_info_no_saul/01_ch_info_no_saul`
- `contacts/regina_jones/ma_bls_ina_se1_07/01_ch_info_no_saul/01_ch_info_no_saul_killed`
- `contacts/regina_jones/ma_bls_ina_se1_07/02_msg_regina`
- `contacts/regina_jones/ma_bls_ina_se1_07/02_msg_regina_killed`
- `contacts/regina_jones/ma_bls_ina_se1_07/02_msg_regina_killed_no_saul`
- `contacts/regina_jones/ma_bls_ina_se1_07/02_msg_regina_no_saul`
- `onscreens/emails/quests/minor_activities/badlands/se1/ma_bls_ina_se1_07/shards/ma_bls_ina_se1_07`
- `onscreens/emails/quests/minor_activities/badlands/se1/ma_bls_ina_se1_07/shards/ma_bls_ina_se1_07_onscreen_02`
- `points_of_interest/minor_quests/ma_bls_ina_se1_07`
- `quests/minor_activities/badlands/se1/ma_bls_ina_se1_07/ma_bls_ina_se1_07/kill_psycho`
- `quests/minor_quest/ma_bls_ina_se1_07`
- `quests/minor_quest/ma_bls_ina_se1_07/description`
- `quests/minor_quest/ma_bls_ina_se1_07/ma_bls_ina_se1_07/check_shard`
- `quests/minor_quest/ma_bls_ina_se1_07/ma_bls_ina_se1_07/clues`
- `quests/minor_quest/ma_bls_ina_se1_07/ma_bls_ina_se1_07/clues/mp_clue`
- `quests/minor_quest/ma_bls_ina_se1_07/ma_bls_ina_se1_07/clues/wreck_area`
- `quests/minor_quest/ma_bls_ina_se1_07/ma_bls_ina_se1_07/find_psycho`
- `quests/minor_quest/ma_bls_ina_se1_07/ma_bls_ina_se1_07/follow_trail`
- `quests/minor_quest/ma_bls_ina_se1_07/ma_bls_ina_se1_07/follow_trail/mp_clue`
- `quests/minor_quest/ma_bls_ina_se1_07/ma_bls_ina_se1_07/follow_trail/mp_trail_02`
- `quests/minor_quest/ma_bls_ina_se1_07/ma_bls_ina_se1_07/follow_trail/mp_trail_03`
- `quests/minor_quest/ma_bls_ina_se1_07/ma_bls_ina_se1_07/follow_trail/mp_trail_04`
- `quests/minor_quest/ma_bls_ina_se1_07/ma_bls_ina_se1_07/follow_trail/mp_trail_05`
- `quests/minor_quest/ma_bls_ina_se1_07/ma_bls_ina_se1_07/kill_psycho`
- `quests/minor_quest/ma_bls_ina_se1_07/ma_bls_ina_se1_07/send_info`
- `quests/minor_quest/ma_bls_ina_se1_07/ma_bls_ina_se1_07/send_info/contact`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 8 |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition` | 1 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questLogicalCondition,questTriggerCondition]` | 10 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questPhoneMuted_ConditionType,questSystemCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType,questLogicalCondition,questObjectCondition,questScan_ConditionType]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 3 |
| `questConditionNodeDefinition[questPhone_ConditionType,questSystemCondition]` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 3 |
| `questDeletionMarkerNodeDefinition` | 7 |
| `questEventManagerNodeDefinition` | 5 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 24 |
| `questInputNodeDefinition` | 7 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 30 |
| `questLogicalHubNodeDefinition` | 5 |
| `questLogicalXorNodeDefinition` | 8 |
| `questMappinManagerNodeDefinition` | 7 |
| `questMiscAICommandNode` | 1 |
| `questMiscAICommandNode[questCombatNodeParams_RestrictMovementToArea]` | 10 |
| `questOutputNodeDefinition` | 5 |
| `questPauseConditionNodeDefinition[questCharacterAttack_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questUICondition,questUIElement_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 16 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 17 |
| `questPauseConditionNodeDefinition[questSensesCondition,questVision_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 15 |
| `questPhaseNodeDefinition` | 7 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 3 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 1 |
| `scnDeletionMarkerNode[scnNodeId]` | 1 |
| `scnEndNode[scnNodeId]` | 4 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `15d970f1a757b10d5d36` | 6 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase` / h229 / 76 -> 74 -> 88 |
| `f850020e1406588f80f8` | 5 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase` / h1278 / 0 -> 2 -> 3 |
| `78e88f68d189adafe388` | 4 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase` / h0 / 215 -> 267 -> 214 |
| `caba80ba05338541aa18` | 4 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase` / h0 / 175 -> 129 -> 132 |
| `f1cab9108d90f7f5b3df` | 4 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase` / h0 / 107 -> 116 -> 109 |
| `2a86daf910e379a86de4` | 3 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase` / h0 / 247 -> 248 -> 261 |
| `ac306d4a83a2d9a78d1e` | 3 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase` / h0 / 246 -> 106 -> 108 |
| `0608e609d2123f6d6b19` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase` / h0 / 144 -> 145 -> 143 |
| `08d0cfbab5cb71581bcc` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase` / h0 / 248 -> 261 -> 260 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene` / scene / 280 -> 262 -> 268 |
| `22b8ff11e7e49798423b` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase` / h0 / 162 -> 163 -> 42 |
| `26fbda44b69d810a8c38` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase` / h0 / 172 -> 215 -> 267 |
| `5c36562b0d3ec0c3ad85` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase` / h0 / 129 -> 132 -> 180 |
| `6f0da1a5e37968f05cf8` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase` / h0 / 168 -> 41 -> 40 |
| `75dda43d08b47491d0ed` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase` / h0 / 172 -> 215 -> 171 |
| `7a73985443b4c4c17563` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase` / h0 / 215 -> 171 -> 116 |
| `88e5c865a8bbe5d8736c` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase` / h0 / 215 -> 213 -> 267 |
| `9af8a87f20a910659fa8` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase` / h0 / 133 -> 134 -> 51 |
| `a5ba871bf92eb584e50a` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase` / h0 / 175 -> 129 -> 92 |
| `a9e261308e780b6ee281` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase` / h0 / 180 -> 201 -> 208 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
