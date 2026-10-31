# base-ma-hey-rey-01

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\community\ma_hey_rey_01_after_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\community\ma_hey_rey_01_civilian_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\community\ma_hey_rey_01_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\ma_hey_rey_01.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\ma_hey_rey_01.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\ma_hey_rey_01_phase.questphase |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\ma_hey_rey_01_phase.questphase` | content candidate | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/heywood/vista_del_rey/ma_hey_rey_01/onscreens/ma_hey_rey_01_onscreen_01`
- `points_of_interest/minor_activities/ma_hey_rey_01`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 4 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 2 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 4 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 5 |
| `questPhaseNodeDefinition` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 15 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `987122e5e2fcd167cf6c` | 4 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\ma_hey_rey_01_phase.questphase` / h0 / 7 -> 0 -> 28 |
| `8d10896873df5c62014e` | 3 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\ma_hey_rey_01_phase.questphase` / h0 / 0 -> 40 -> 2 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\ma_hey_rey_01_phase.questphase` / h0 / 11 -> 45 -> 30 |
| `2c20201f171f754c99e0` | 2 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\ma_hey_rey_01_phase.questphase` / h0 / 48 -> 49 -> 50 |
| `3ba86c71a70bfb0620a5` | 2 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\ma_hey_rey_01_phase.questphase` / h0 / 47 -> 48 -> 49 |
| `543b598a1b2fb7423e72` | 2 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\ma_hey_rey_01_phase.questphase` / h0 / 51 -> 49 -> 50 |
| `5466f936f30ed8ee354a` | 2 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\ma_hey_rey_01_phase.questphase` / h0 / 52 -> 47 -> 48 |
| `5a1e5eb45e2acdebe80e` | 2 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\ma_hey_rey_01_phase.questphase` / h0 / 26 -> 52 -> 51 |
| `7373ce40c215f78fb39e` | 2 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\ma_hey_rey_01_phase.questphase` / h0 / 47 -> 48 -> 51 |
| `88f5ed16b4aedf0ce68b` | 2 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\ma_hey_rey_01_phase.questphase` / h0 / 48 -> 51 -> 46 |
| `8cf6277488916d3b7ab5` | 2 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\ma_hey_rey_01_phase.questphase` / h0 / 52 -> 51 -> 46 |
| `8edf5416ccd8dce9db72` | 2 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\ma_hey_rey_01_phase.questphase` / h0 / 52 -> 51 -> 49 |
| `901d299850eb5392fd72` | 2 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\ma_hey_rey_01_phase.questphase` / h0 / 55 -> 53 -> 54 |
| `95b7458b3ffd83fd4357` | 2 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\ma_hey_rey_01_phase.questphase` / h0 / 0 -> 40 -> 43 |
| `cadb89472ec2335d17b1` | 2 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\ma_hey_rey_01_phase.questphase` / h0 / 48 -> 51 -> 49 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\ma_hey_rey_01_phase.questphase` / h0 / 74 -> 79 -> 77 |
| `0985fc78e580f2f10e14` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\ma_hey_rey_01_phase.questphase` / h415 / 2 -> 10 -> 9 |
| `1236b824035f3d3d10f6` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\ma_hey_rey_01_phase.questphase` / h38 / 8 -> 10 -> 9 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\ma_hey_rey_01_phase.questphase` / h0 / 7 -> 11 -> 45 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_01\ma_hey_rey_01_phase.questphase` / h0 / 11 -> 45 -> 22 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
