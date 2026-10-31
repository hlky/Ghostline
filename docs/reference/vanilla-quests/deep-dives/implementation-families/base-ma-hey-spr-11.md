# base-ma-hey-spr-11

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_11\community\ma_hey_spr_11_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_11\ma_hey_spr_11.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_11\ma_hey_spr_11.quest` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_11\ma_hey_spr_11_phase.questphase` | content candidate | 1 / 0 | base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_11\scenes\ma_hey_spr_11_holocall_brief.scene |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_11\scenes\ma_hey_spr_11_holocall_brief.scene` | content candidate | 0 / 15 |  |

## Journal paths observed in these resources

- `contacts/ncpd_dispatcher/outposts/ma_hey_spr_11`
- `points_of_interest/minor_activities/ma_hey_spr_11`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 4 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 14 |
| `questInputNodeDefinition` | 1 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 1 |
| `questLogicalHubNodeDefinition` | 1 |
| `questMiscAICommandNode` | 5 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `scnEndNode[scnNodeId]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `987122e5e2fcd167cf6c` | 6 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_11\ma_hey_spr_11_phase.questphase` / h0 / 0 -> 5 -> 45 |
| `95b7458b3ffd83fd4357` | 5 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_11\ma_hey_spr_11_phase.questphase` / h0 / 5 -> 45 -> 46 |
| `e5742f9794e6583c67cb` | 3 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_11\scenes\ma_hey_spr_11_holocall_brief.scene` / scene / 78 -> 258 -> 256 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_11\ma_hey_spr_11_phase.questphase` / h0 / 3 -> 85 -> 49 |
| `9e5e28ecb38ea2a53a15` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_11\scenes\ma_hey_spr_11_holocall_brief.scene` / scene / 254 -> 78 -> 75 |
| `d6b7c21f5d2d0ab76fc6` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_11\scenes\ma_hey_spr_11_holocall_brief.scene` / scene / 258 -> 256 -> 260 |
| `06e3382349ceff89de6f` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_11\ma_hey_spr_11_phase.questphase` / h0 / 75 -> 30 -> 43 |
| `0bc8f68e59c0b883af0d` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_11\ma_hey_spr_11_phase.questphase` / h0 / 96 -> 74 -> 83 |
| `0e0605a4b943506ff6fd` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_11\ma_hey_spr_11_phase.questphase` / h0 / 76 -> 74 -> 83 |
| `101b60945ddf6f25f378` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_11\scenes\ma_hey_spr_11_holocall_brief.scene` / scene / 29 -> 87 -> 88 |
| `12208b60f11caf6d936e` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_11\ma_hey_spr_11_phase.questphase` / h0 / 41 -> 87 -> 50 |
| `1520ebe4ea0bf9451321` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_11\ma_hey_spr_11_phase.questphase` / h0 / 75 -> 76 -> 73 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_11\ma_hey_spr_11_phase.questphase` / h0 / 0 -> 3 -> 85 |
| `1d933adb5a617880c93e` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_11\scenes\ma_hey_spr_11_holocall_brief.scene` / scene / 87 -> 88 -> 85 |
| `22adbd10519df5772f7c` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_11\ma_hey_spr_11_phase.questphase` / h0 / 96 -> 74 -> 84 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_11\ma_hey_spr_11_phase.questphase` / h0 / 3 -> 85 -> 21 |
| `26762f051e7728f090ca` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_11\scenes\ma_hey_spr_11_holocall_brief.scene` / scene / 76 -> 77 -> 29 |
| `2beeeaa3b4da5300c035` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_11\scenes\ma_hey_spr_11_holocall_brief.scene` / scene / 74 -> 254 -> 78 |
| `2c3d4d4eb6c82c8f1261` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_11\ma_hey_spr_11_phase.questphase` / h0 / 53 -> 57 -> 80 |
| `2e946768962b95c7dd40` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_11\ma_hey_spr_11_phase.questphase` / h0 / 73 -> 96 -> 97 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
