# ep1-sa-ep1-33

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\sa_ep1_33\community\sa_ep1_33_av_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_33\community\sa_ep1_33_enemies_com_01.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_33\community\sa_ep1_33_enemies_com_02.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_33\community\sa_ep1_33_var_01_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_33\sa_ep1_33.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_33\sa_ep1_33.quest` | content candidate | 1 / 0 | ep1\openworld\sandbox_activities\sa_ep1_30\scenes\sa_ep1_30_chicken_test.scene; ep1\openworld\sandbox_activities\sa_ep1_33\sa_ep1_33.questphase |
| `ep1\openworld\sandbox_activities\sa_ep1_33\sa_ep1_33.questphase` | content candidate | 7 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 8 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerVisuals_ChangeEntityAppearance,questCharacterManagerVisuals_EntityAppearanceOperationBaseEntityAppearanceEntry,questCharacterManagerVisuals_NodeType]` | 2 |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition` | 19 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 5 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 4 |
| `questCutControlNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 8 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 8 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 18 |
| `questInputNodeDefinition` | 10 |
| `questItemManagerNodeDefinition[questReInitContainers_NodeType,questReInitContainers_NodeTypeParams]` | 1 |
| `questLogicalAndNodeDefinition` | 4 |
| `questLogicalHubNodeDefinition` | 9 |
| `questLogicalXorNodeDefinition` | 3 |
| `questMiscAICommandNode` | 11 |
| `questOutputNodeDefinition` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 13 |
| `questPauseConditionNodeDefinition[questTickDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 12 |
| `questPhaseNodeDefinition` | 7 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 16 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 22 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questUIManagerNodeDefinition[questDisplayMessageBox_NodeType]` | 1 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 4 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 6 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `42d456f68cbe3d8345c3` | 5 | `ep1\openworld\sandbox_activities\sa_ep1_33\sa_ep1_33.questphase` / h507 / 6 -> 10 -> 3 |
| `05c7a2151e0cd17400d5` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_33\sa_ep1_33.questphase` / h323 / 26 -> 30 -> 3 |
| `3e6653e916afcf7cc2e1` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_33\sa_ep1_33.questphase` / h323 / 26 -> 30 -> 21 |
| `7b44344c01ad5161d3ff` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_33\sa_ep1_33.questphase` / h507 / 8 -> 2 -> 9 |
| `fc910f43d5ff9aabecc6` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_33\sa_ep1_33.questphase` / h323 / 2 -> 26 -> 30 |
| `95b7458b3ffd83fd4357` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_33\sa_ep1_33.questphase` / h962 / 92 -> 99 -> 102 |
| `bb07e30a5fd078f99b61` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_33\sa_ep1_33.questphase` / h962 / 99 -> 102 -> 146 |
| `01cc762cd06f16743b1c` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_33\sa_ep1_33.questphase` / h7 / 69 -> 90 -> 47 |
| `0307c8e1c2bd71322d7d` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_33\sa_ep1_33.questphase` / h7 / 103 -> 84 -> 131 |
| `0f6060800f34fba21084` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_33\sa_ep1_33.questphase` / h7 / 97 -> 103 -> 84 |
| `115d8a1b79379ecc48b1` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_33\sa_ep1_33.questphase` / h7 / 115 -> 157 -> 132 |
| `151afe4cc6b87955b4b5` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_33\sa_ep1_33.questphase` / h7 / 58 -> 184 -> 194 |
| `1553ea49805c9d5b4f24` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_33\sa_ep1_33.questphase` / h7 / 74 -> 72 -> 73 |
| `181f231b641eba46ad3b` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_33\sa_ep1_33.questphase` / h323 / 30 -> 3 -> 29 |
| `1f2c7c3fe2e1f24e893f` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_33\sa_ep1_33.questphase` / h7 / 57 -> 58 -> 184 |
| `1f53069a6ddb1130d5ef` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_33\sa_ep1_33.questphase` / h7 / 61 -> 118 -> 49 |
| `20a77143a898bc753a26` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_33\sa_ep1_33.questphase` / h7 / 65 -> 105 -> 62 |
| `2165c31c38fd80af8cdc` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_33\sa_ep1_33.questphase` / h323 / 41 -> 42 -> 39 |
| `2765fcbe8f4e745fbc8e` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_33\sa_ep1_33.questphase` / h323 / 31 -> 36 -> 38 |
| `2dfa184e3774a4a8c13b` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_33\sa_ep1_33.questphase` / h7 / 61 -> 67 -> 74 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
