# ep1-sa-ep1-3

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\sa_ep1_3\communities\sa_ep1_3_av_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_3\communities\sa_ep1_3_barghest_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_3\communities\sa_ep1_3_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_3\communities\sa_ep1_3_voodoo_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_3\sa_ep1_3_phase.questphase` | content candidate | 5 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 4 |
| `questCheckpointNodeDefinition` | 1 |
| `questCombatNodeDefinition` | 51 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questEventManagerNodeDefinition` | 6 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 7 |
| `questInputNodeDefinition` | 5 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 8 |
| `questLogicalAndNodeDefinition` | 3 |
| `questLogicalHubNodeDefinition` | 12 |
| `questLogicalXorNodeDefinition` | 4 |
| `questOutputNodeDefinition` | 5 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questCharacterCondition,questCharacterHit_ConditionType,questLogicalCondition,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 9 |
| `questPauseConditionNodeDefinition[questTickDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 10 |
| `questPhaseNodeDefinition` | 4 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 10 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 7 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `402758845f86d6dd89dc` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_3\sa_ep1_3_phase.questphase` / h721 / 3 -> 11 -> 5 |
| `e239bb3187912262f96a` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_3\sa_ep1_3_phase.questphase` / h721 / 14 -> 15 -> 16 |
| `39986b4fbf68ce432047` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_3\sa_ep1_3_phase.questphase` / h311 / 9 -> 64 -> 59 |
| `9890c704bd8503fd1750` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_3\sa_ep1_3_phase.questphase` / h721 / 13 -> 14 -> 15 |
| `cd52eac716a61cdc5d27` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_3\sa_ep1_3_phase.questphase` / h311 / 10 -> 64 -> 59 |
| `f3a893ca94c828b1cfe3` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_3\sa_ep1_3_phase.questphase` / h0 / 2 -> 228 -> 231 |
| `00c3ca0ac0b55db639ca` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_3\sa_ep1_3_phase.questphase` / h0 / 7 -> 22 -> 23 |
| `115d8a1b79379ecc48b1` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_3\sa_ep1_3_phase.questphase` / h311 / 64 -> 59 -> 11 |
| `20677d15c85394700dd9` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_3\sa_ep1_3_phase.questphase` / h311 / 3 -> 60 -> 5 |
| `21b0f05f7b119dae8d9c` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_3\sa_ep1_3_phase.questphase` / h846 / 2 -> 11 -> 13 |
| `35aa2c304f78db7500fe` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_3\sa_ep1_3_phase.questphase` / h0 / 2 -> 176 -> 220 |
| `35afb5e39d6bdeba1128` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_3\sa_ep1_3_phase.questphase` / h311 / 63 -> 2 -> 61 |
| `3de2ce4ad6ce1db5e797` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_3\sa_ep1_3_phase.questphase` / h846 / 2 -> 11 -> 14 |
| `509bab2eef74ab39d4ae` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_3\sa_ep1_3_phase.questphase` / h311 / 61 -> 4 -> 9 |
| `66465a7fcc9af212839a` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_3\sa_ep1_3_phase.questphase` / h311 / 0 -> 63 -> 2 |
| `821306dbfe294d459b38` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_3\sa_ep1_3_phase.questphase` / h311 / 6 -> 70 -> 62 |
| `98e727f9f695ef36a1aa` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_3\sa_ep1_3_phase.questphase` / h846 / 2 -> 11 -> 15 |
| `a20faa215d2ac1943486` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_3\sa_ep1_3_phase.questphase` / h846 / 2 -> 11 -> 17 |
| `b1927920d0dd4e9ba9e2` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_3\sa_ep1_3_phase.questphase` / h846 / 2 -> 11 -> 18 |
| `bd4bb68e151a5a63deb7` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_3\sa_ep1_3_phase.questphase` / h0 / 104 -> 119 -> 4 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
