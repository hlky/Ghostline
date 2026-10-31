# base-ma-hey-rey-03

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_03\community\ma_hey_rey_03_after_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_03\community\ma_hey_rey_03_civilian_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_03\community\ma_hey_rey_03_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_03\ma_hey_rey_03.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_03\ma_hey_rey_03.quest` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_03\ma_hey_rey_03_phase.questphase` | content candidate | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/heywood/vista_del_rey/ma_hey_rey_03/onscreens/ma_hey_rey_03_onscreen_01`
- `points_of_interest/minor_activities/ma_hey_rey_03`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 4 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 3 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 3 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 7 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 5 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 5 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 23 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `18be198845c90c6bb3c8` | 4 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_03\ma_hey_rey_03_phase.questphase` / h38 / 14 -> 8 -> 2 |
| `2c20201f171f754c99e0` | 4 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_03\ma_hey_rey_03_phase.questphase` / h0 / 45 -> 46 -> 47 |
| `3ba86c71a70bfb0620a5` | 4 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_03\ma_hey_rey_03_phase.questphase` / h0 / 44 -> 45 -> 46 |
| `484f47d527266442c50f` | 4 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_03\ma_hey_rey_03_phase.questphase` / h0 / 42 -> 49 -> 44 |
| `543b598a1b2fb7423e72` | 4 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_03\ma_hey_rey_03_phase.questphase` / h0 / 48 -> 46 -> 47 |
| `5466f936f30ed8ee354a` | 4 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_03\ma_hey_rey_03_phase.questphase` / h0 / 49 -> 44 -> 45 |
| `7373ce40c215f78fb39e` | 4 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_03\ma_hey_rey_03_phase.questphase` / h0 / 44 -> 45 -> 48 |
| `88f5ed16b4aedf0ce68b` | 4 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_03\ma_hey_rey_03_phase.questphase` / h0 / 45 -> 48 -> 43 |
| `8cf6277488916d3b7ab5` | 4 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_03\ma_hey_rey_03_phase.questphase` / h0 / 49 -> 48 -> 43 |
| `8edf5416ccd8dce9db72` | 4 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_03\ma_hey_rey_03_phase.questphase` / h0 / 49 -> 48 -> 46 |
| `c7b377e841e63de88f17` | 4 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_03\ma_hey_rey_03_phase.questphase` / h0 / 42 -> 49 -> 48 |
| `cadb89472ec2335d17b1` | 4 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_03\ma_hey_rey_03_phase.questphase` / h0 / 45 -> 48 -> 46 |
| `20a77143a898bc753a26` | 3 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_03\ma_hey_rey_03_phase.questphase` / h38 / 9 -> 16 -> 17 |
| `95b7458b3ffd83fd4357` | 3 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_03\ma_hey_rey_03_phase.questphase` / h0 / 0 -> 33 -> 34 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_03\ma_hey_rey_03_phase.questphase` / h0 / 10 -> 41 -> 30 |
| `7e96257d321df1ad0991` | 2 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_03\ma_hey_rey_03_phase.questphase` / h0 / 21 -> 42 -> 49 |
| `987122e5e2fcd167cf6c` | 2 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_03\ma_hey_rey_03_phase.questphase` / h0 / 7 -> 0 -> 33 |
| `ce7f1e757edb842cbfa0` | 2 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_03\ma_hey_rey_03_phase.questphase` / h0 / 42 -> 57 -> 71 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_03\ma_hey_rey_03_phase.questphase` / h0 / 84 -> 85 -> 82 |
| `0985fc78e580f2f10e14` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_03\ma_hey_rey_03_phase.questphase` / h546 / 2 -> 10 -> 9 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
