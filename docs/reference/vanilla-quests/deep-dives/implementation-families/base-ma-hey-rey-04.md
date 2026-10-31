# base-ma-hey-rey-04

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_04\community\ma_hey_rey_04_civilian_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_04\community\ma_hey_rey_04_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_04\ma_hey_rey_04.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_04\ma_hey_rey_04.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_04\ma_hey_rey_04_phase.questphase |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_04\ma_hey_rey_04_phase.questphase` | content candidate | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/heywood/vista_del_rey/ma_hey_rey_04/onscreens/ma_hey_rey_04_onscreen_01`
- `points_of_interest/minor_activities/ma_hey_rey_04`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 9 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 3 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 4 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 2 |
| `questOutputNodeDefinition` | 4 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 4 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 14 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `987122e5e2fcd167cf6c` | 5 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_04\ma_hey_rey_04_phase.questphase` / h0 / 7 -> 0 -> 32 |
| `2c20201f171f754c99e0` | 3 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_04\ma_hey_rey_04_phase.questphase` / h0 / 51 -> 52 -> 53 |
| `3ba86c71a70bfb0620a5` | 3 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_04\ma_hey_rey_04_phase.questphase` / h0 / 50 -> 51 -> 52 |
| `543b598a1b2fb7423e72` | 3 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_04\ma_hey_rey_04_phase.questphase` / h0 / 54 -> 52 -> 53 |
| `5466f936f30ed8ee354a` | 3 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_04\ma_hey_rey_04_phase.questphase` / h0 / 55 -> 50 -> 51 |
| `5a1e5eb45e2acdebe80e` | 3 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_04\ma_hey_rey_04_phase.questphase` / h0 / 22 -> 55 -> 54 |
| `7373ce40c215f78fb39e` | 3 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_04\ma_hey_rey_04_phase.questphase` / h0 / 50 -> 51 -> 54 |
| `88f5ed16b4aedf0ce68b` | 3 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_04\ma_hey_rey_04_phase.questphase` / h0 / 51 -> 54 -> 49 |
| `8cf6277488916d3b7ab5` | 3 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_04\ma_hey_rey_04_phase.questphase` / h0 / 55 -> 54 -> 49 |
| `8d10896873df5c62014e` | 3 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_04\ma_hey_rey_04_phase.questphase` / h0 / 22 -> 55 -> 50 |
| `8edf5416ccd8dce9db72` | 3 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_04\ma_hey_rey_04_phase.questphase` / h0 / 55 -> 54 -> 52 |
| `cadb89472ec2335d17b1` | 3 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_04\ma_hey_rey_04_phase.questphase` / h0 / 51 -> 54 -> 52 |
| `d864a6aee629e2bd85fa` | 3 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_04\ma_hey_rey_04_phase.questphase` / h0 / 55 -> 54 -> 73 |
| `f1c09c9f02e5dc183b08` | 3 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_04\ma_hey_rey_04_phase.questphase` / h0 / 9 -> 80 -> 76 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_04\ma_hey_rey_04_phase.questphase` / h0 / 10 -> 41 -> 35 |
| `95b7458b3ffd83fd4357` | 2 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_04\ma_hey_rey_04_phase.questphase` / h0 / 0 -> 32 -> 31 |
| `00c3ca0ac0b55db639ca` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_04\ma_hey_rey_04_phase.questphase` / h21 / 4 -> 6 -> 9 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_04\ma_hey_rey_04_phase.questphase` / h0 / 86 -> 89 -> 87 |
| `0985fc78e580f2f10e14` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_04\ma_hey_rey_04_phase.questphase` / h407 / 2 -> 10 -> 9 |
| `0f3377684c4e80349213` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_04\ma_hey_rey_04_phase.questphase` / h0 / 0 -> 9 -> 80 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
