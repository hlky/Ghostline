# base-mws-hey-07

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\heywood\mws_hey_07\communities\mws_hey_07.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\heywood\mws_hey_07\communities\mws_hey_07_dead.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\heywood\mws_hey_07\communities\mws_hey_07_tygers.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\heywood\mws_hey_07\communities\mws_hey_07_tygers_reinforcements.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\heywood\mws_hey_07\communities\mws_hey_07_vehicles.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\heywood\mws_hey_07\communities\mws_hey_07_vehicles_reinforcements.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\heywood\mws_hey_07\mws_hey_07.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\heywood\mws_hey_07\mws_hey_07.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\heywood\mws_hey_07\mws_hey_07.questphase |
| `base\open_world\mini_world_stories\heywood\mws_hey_07\mws_hey_07.questphase` | content candidate | 7 / 0 | base\open_world\mini_world_stories\heywood\mws_hey_07\phases\mws_hey_07_combat.questphase |
| `base\open_world\mini_world_stories\heywood\mws_hey_07\phases\mws_hey_07_combat.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `contacts/dustbunny/mws_hey_07/mws_hey_thank_you_message_01`
- `contacts/dustbunny/mws_hey_07/mws_hey_thank_you_message_03_optional`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 15 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 32 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 13 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 34 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 1 |
| `questCombatNodeDefinition` | 7 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 54 |
| `questConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 27 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 6 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 2 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 6 |
| `questEventManagerNodeDefinition` | 6 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 9 |
| `questInputNodeDefinition` | 10 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 3 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 2 |
| `questLogicalAndNodeDefinition` | 23 |
| `questLogicalHubNodeDefinition` | 13 |
| `questLogicalXorNodeDefinition` | 2 |
| `questMiscAICommandNode` | 1 |
| `questOutputNodeDefinition` | 9 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questGameTimeDelay_ConditionType,questLogicalCondition,questSystemCondition,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questCharacterHit_ConditionType,questCharacterQuickHackUploadBegin_ConditionType,questCharacterStatusEffect_CondtionType,questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType,questCharacterQuickHackUploadBegin_ConditionType,questCharacterStatusEffect_CondtionType,questLogicalCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType,questCharacterStatusEffect_CondtionType,questLogicalCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questLogicalCondition,questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questLogicalCondition]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 10 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 24 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questRealtimeDelay_ConditionType,questTimeCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 21 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpeed_ConditionType]` | 2 |
| `questPhaseNodeDefinition` | 7 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 34 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 2 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 17 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 2 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 4 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 4 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 15 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 15 |
| `questVehicleNodeDefinition[questUnassignAll_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `54c439fb8332e3c50b87` | 24 | `base\open_world\mini_world_stories\heywood\mws_hey_07\mws_hey_07.questphase` / h234 / 163 -> 28 -> 78 |
| `a94dfa0a863488e27f45` | 24 | `base\open_world\mini_world_stories\heywood\mws_hey_07\mws_hey_07.questphase` / h234 / 52 -> 100 -> 200 |
| `e2a53bd4c0984d114638` | 24 | `base\open_world\mini_world_stories\heywood\mws_hey_07\mws_hey_07.questphase` / h234 / 170 -> 157 -> 29 |
| `55bd509a3f9e32bd1d36` | 23 | `base\open_world\mini_world_stories\heywood\mws_hey_07\mws_hey_07.questphase` / h234 / 52 -> 100 -> 149 |
| `a5f6ff0df46f7043f2b5` | 13 | `base\open_world\mini_world_stories\heywood\mws_hey_07\mws_hey_07.questphase` / h268 / 11 -> 12 -> 13 |
| `ae33ab1bf8ac86afe702` | 13 | `base\open_world\mini_world_stories\heywood\mws_hey_07\mws_hey_07.questphase` / h268 / 9 -> 10 -> 16 |
| `b2b049d57541c50e8634` | 12 | `base\open_world\mini_world_stories\heywood\mws_hey_07\mws_hey_07.questphase` / h234 / 133 -> 151 -> 103 |
| `ce0a2a780fffa5d5098e` | 12 | `base\open_world\mini_world_stories\heywood\mws_hey_07\mws_hey_07.questphase` / h234 / 63 -> 151 -> 103 |
| `0c4a984fae982a30b3b1` | 10 | `base\open_world\mini_world_stories\heywood\mws_hey_07\phases\mws_hey_07_combat.questphase` / h39 / 118 -> 28 -> 19 |
| `273bf2a3ea88be4da7df` | 10 | `base\open_world\mini_world_stories\heywood\mws_hey_07\phases\mws_hey_07_combat.questphase` / h39 / 151 -> 28 -> 19 |
| `5dbb4bd9b50cbcc437f1` | 10 | `base\open_world\mini_world_stories\heywood\mws_hey_07\phases\mws_hey_07_combat.questphase` / h39 / 28 -> 19 -> 164 |
| `bab52ba888e325a257fa` | 9 | `base\open_world\mini_world_stories\heywood\mws_hey_07\phases\mws_hey_07_combat.questphase` / h39 / 146 -> 19 -> 164 |
| `6babc5386a30099b5bdb` | 6 | `base\open_world\mini_world_stories\heywood\mws_hey_07\mws_hey_07.questphase` / h234 / 31 -> 80 -> 169 |
| `20a77143a898bc753a26` | 4 | `base\open_world\mini_world_stories\heywood\mws_hey_07\mws_hey_07.questphase` / h115 / 7 -> 19 -> 20 |
| `72bce75ffbe6c3a90b9a` | 4 | `base\open_world\mini_world_stories\heywood\mws_hey_07\phases\mws_hey_07_combat.questphase` / h0 / 193 -> 199 -> 211 |
| `76a00a4b3c6fce6282ab` | 4 | `base\open_world\mini_world_stories\heywood\mws_hey_07\phases\mws_hey_07_combat.questphase` / h0 / 185 -> 186 -> 187 |
| `8aa35a7dedf842c10876` | 4 | `base\open_world\mini_world_stories\heywood\mws_hey_07\phases\mws_hey_07_combat.questphase` / h0 / 199 -> 211 -> 207 |
| `b2249e16afc167a6e89a` | 4 | `base\open_world\mini_world_stories\heywood\mws_hey_07\phases\mws_hey_07_combat.questphase` / h0 / 186 -> 187 -> 188 |
| `b8f09713a92dfeee1bac` | 4 | `base\open_world\mini_world_stories\heywood\mws_hey_07\mws_hey_07.questphase` / h234 / 143 -> 59 -> 153 |
| `f7a8d023e74ef0a4a53c` | 4 | `base\open_world\mini_world_stories\heywood\mws_hey_07\phases\mws_hey_07_combat.questphase` / h0 / 54 -> 17 -> 63 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
