# ep1-sa-ep1-30

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\sa_ep1_30\communities\sa_ep1_30_av_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_30\communities\sa_ep1_30_civilians_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_30\communities\sa_ep1_30_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_30\communities\sa_ep1_30_var_01_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_30\communities\sa_ep1_30_var_02_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_30\sa_ep1_30.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_30\sa_ep1_30.quest` | content candidate | 1 / 0 | ep1\openworld\sandbox_activities\sa_ep1_30\sa_ep1_30.questphase; ep1\openworld\sandbox_activities\sa_ep1_30\scenes\sa_ep1_30_chicken_test.scene |
| `ep1\openworld\sandbox_activities\sa_ep1_30\sa_ep1_30.questphase` | content candidate | 10 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_30\scenes\sa_ep1_30_chicken_test.scene` | test/debug | 0 / 5 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 12 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerVisuals_ChangeEntityAppearance,questCharacterManagerVisuals_EntityAppearanceOperationBaseEntityAppearanceEntry,questCharacterManagerVisuals_NodeType]` | 3 |
| `questCheckpointNodeDefinition` | 3 |
| `questCombatNodeDefinition` | 3 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 7 |
| `questCombatNodeDefinition[questCombatNodeParams_UseCover]` | 6 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 11 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 6 |
| `questCutControlNodeDefinition` | 3 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 5 |
| `questEventManagerNodeDefinition` | 9 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 15 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 26 |
| `questInputNodeDefinition` | 13 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 2 |
| `questItemManagerNodeDefinition[questReInitContainers_NodeType,questReInitContainers_NodeTypeParams]` | 3 |
| `questLogicalAndNodeDefinition` | 8 |
| `questLogicalHubNodeDefinition` | 4 |
| `questLogicalXorNodeDefinition` | 3 |
| `questMiscAICommandNode` | 8 |
| `questOutputNodeDefinition` | 14 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 10 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questLogicalCondition,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 3 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 14 |
| `questPauseConditionNodeDefinition[questTickDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 16 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 2 |
| `questPhaseNodeDefinition` | 10 |
| `questRandomizerNodeDefinition` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 32 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 5 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 14 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 8 |
| `questVehicleNodeDefinition[questStopVehicle_NodeType]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 7 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnEndNode[scnNodeId]` | 3 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `95b7458b3ffd83fd4357` | 8 | `ep1\openworld\sandbox_activities\sa_ep1_30\sa_ep1_30.questphase` / h817 / 41 -> 39 -> 38 |
| `057faf6705431d5dcd46` | 7 | `ep1\openworld\sandbox_activities\sa_ep1_30\sa_ep1_30.questphase` / h112 / 11 -> 31 -> 53 |
| `e85b4a6da2c88320c53a` | 7 | `ep1\openworld\sandbox_activities\sa_ep1_30\sa_ep1_30.questphase` / h112 / 4 -> 11 -> 31 |
| `05c7a2151e0cd17400d5` | 6 | `ep1\openworld\sandbox_activities\sa_ep1_30\sa_ep1_30.questphase` / h584 / 26 -> 30 -> 3 |
| `0d1847f63383127a58f1` | 6 | `ep1\openworld\sandbox_activities\sa_ep1_30\sa_ep1_30.questphase` / h306 / 22 -> 2 -> 5 |
| `3e6653e916afcf7cc2e1` | 6 | `ep1\openworld\sandbox_activities\sa_ep1_30\sa_ep1_30.questphase` / h584 / 26 -> 30 -> 21 |
| `fc910f43d5ff9aabecc6` | 6 | `ep1\openworld\sandbox_activities\sa_ep1_30\sa_ep1_30.questphase` / h584 / 2 -> 26 -> 30 |
| `6bf219df807b4759226b` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_30\sa_ep1_30.questphase` / h306 / 2 -> 11 -> 27 |
| `9157e5969454d605a448` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_30\sa_ep1_30.questphase` / h16 / 3 -> 51 -> 50 |
| `987122e5e2fcd167cf6c` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_30\sa_ep1_30.questphase` / h112 / 0 -> 4 -> 11 |
| `01cc762cd06f16743b1c` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_30\sa_ep1_30.questphase` / h16 / 6 -> 28 -> 1 |
| `0307c8e1c2bd71322d7d` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_30\sa_ep1_30.questphase` / h16 / 37 -> 22 -> 45 |
| `099a259d14720a1f55dc` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_30\sa_ep1_30.questphase` / h16 / 24 -> 53 -> 6 |
| `0dd24b433a6ab8bd5c82` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_30\sa_ep1_30.questphase` / h584 / 38 -> 37 -> 41 |
| `0f6060800f34fba21084` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_30\sa_ep1_30.questphase` / h16 / 31 -> 37 -> 22 |
| `1553ea49805c9d5b4f24` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_30\sa_ep1_30.questphase` / h16 / 18 -> 14 -> 15 |
| `181f231b641eba46ad3b` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_30\sa_ep1_30.questphase` / h584 / 30 -> 3 -> 29 |
| `2165c31c38fd80af8cdc` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_30\sa_ep1_30.questphase` / h584 / 46 -> 49 -> 43 |
| `26cc35c85c4ae78da882` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_30\sa_ep1_30.questphase` / h584 / 37 -> 41 -> 32 |
| `2765fcbe8f4e745fbc8e` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_30\sa_ep1_30.questphase` / h584 / 31 -> 38 -> 48 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
