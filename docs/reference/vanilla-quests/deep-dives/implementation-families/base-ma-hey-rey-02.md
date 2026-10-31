# base-ma-hey-rey-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_02\community\ma_hey_rey_02_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_02\ma_hey_rey_02.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_02\ma_hey_rey_02.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_02\ma_hey_rey_02_phase.questphase |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_02\ma_hey_rey_02_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/heywood/vista_del_rey/ma_hey_rey_02/onscreens/ma_hey_rey_02_onscreen_03`
- `points_of_interest/minor_activities/ma_hey_rey_02`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 5 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 8 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 3 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 3 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `987122e5e2fcd167cf6c` | 5 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_02\ma_hey_rey_02_phase.questphase` / h0 / 2 -> 4 -> 58 |
| `95b7458b3ffd83fd4357` | 3 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_02\ma_hey_rey_02_phase.questphase` / h0 / 4 -> 101 -> 102 |
| `36e8af907951eefb860d` | 2 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_02\ma_hey_rey_02_phase.questphase` / h0 / 10 -> 6 -> 9 |
| `ebf923273db7cf158f68` | 2 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_02\ma_hey_rey_02_phase.questphase` / h0 / 4 -> 58 -> 60 |
| `06e3382349ceff89de6f` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_02\ma_hey_rey_02_phase.questphase` / h0 / 6 -> 64 -> 65 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_02\ma_hey_rey_02_phase.questphase` / h0 / 118 -> 116 -> 114 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_02\ma_hey_rey_02_phase.questphase` / h0 / 18 -> 107 -> 72 |
| `0c5acabadd2c6d7f6dd6` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_02\ma_hey_rey_02_phase.questphase` / h0 / 99 -> 98 -> 87 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_02\ma_hey_rey_02_phase.questphase` / h49 / 22 -> 15 -> 8 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_02\ma_hey_rey_02_phase.questphase` / h0 / 2 -> 18 -> 107 |
| `234740de04d3a2934680` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_02\ma_hey_rey_02_phase.questphase` / h0 / 58 -> 60 -> 99 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_02\ma_hey_rey_02_phase.questphase` / h0 / 18 -> 107 -> 45 |
| `27989a991fbce5b0fc5c` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_02\ma_hey_rey_02_phase.questphase` / h0 / 81 -> 11 -> 12 |
| `295acc02504244db40db` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_02\ma_hey_rey_02_phase.questphase` / h49 / 12 -> 21 -> 9 |
| `2cc4f20e16798419f013` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_02\ma_hey_rey_02_phase.questphase` / h0 / 47 -> 25 -> 118 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_02\ma_hey_rey_02_phase.questphase` / h0 / 118 -> 115 -> 114 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_02\ma_hey_rey_02_phase.questphase` / h0 / 116 -> 114 -> 26 |
| `3defb6b5bfe82560078d` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_02\ma_hey_rey_02_phase.questphase` / h0 / 2 -> 4 -> 10 |
| `44001c669afc743ed647` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_02\ma_hey_rey_02_phase.questphase` / h49 / 11 -> 12 -> 21 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_02\ma_hey_rey_02_phase.questphase` / h0 / 107 -> 72 -> 45 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
