# base-ma-hey-spr-10

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\community\ma_hey_spr_10_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10.quest` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10_bugfixing.questphase` | repair | 2 / 0 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10_phase.questphase` | content candidate | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/heywood/wellsprings/ma_hey_spr_10/onscreens/ma_hey_spr_10_onscreen_01`
- `points_of_interest/minor_activities/ma_hey_spr_10`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 4 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 8 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 5 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalXorNodeDefinition` | 2 |
| `questMiscAICommandNode` | 2 |
| `questOutputNodeDefinition` | 5 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 7 |
| `questPhaseNodeDefinition` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 9 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `987122e5e2fcd167cf6c` | 4 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10_phase.questphase` / h0 / 0 -> 2 -> 30 |
| `95b7458b3ffd83fd4357` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10_phase.questphase` / h0 / 2 -> 45 -> 46 |
| `019c7a73ec12a81d4f73` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10_phase.questphase` / h0 / 66 -> 70 -> 68 |
| `06f33295980af9fc0010` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10_phase.questphase` / h154 / 6 -> 8 -> 1 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10_phase.questphase` / h0 / 79 -> 81 -> 71 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10_phase.questphase` / h0 / 20 -> 62 -> 51 |
| `0ac3861e63d8cec0e6af` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10_phase.questphase` / h0 / 2 -> 64 -> 63 |
| `12208b60f11caf6d936e` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10_phase.questphase` / h0 / 40 -> 65 -> 53 |
| `178360ac35259ce804ee` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10_phase.questphase` / h0 / 0 -> 32 -> 60 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10_bugfixing.questphase` / h22 / 4 -> 5 -> 6 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10_phase.questphase` / h0 / 0 -> 20 -> 62 |
| `1dff7f84bcc367b07eb4` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10_phase.questphase` / h0 / 69 -> 70 -> 68 |
| `216dc4afa1cdff93031c` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10_bugfixing.questphase` / h22 / 0 -> 2 -> 3 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10_phase.questphase` / h0 / 20 -> 62 -> 39 |
| `2cc4f20e16798419f013` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10_phase.questphase` / h0 / 37 -> 21 -> 79 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10_phase.questphase` / h0 / 79 -> 77 -> 71 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10_phase.questphase` / h0 / 81 -> 71 -> 23 |
| `423e38da0596af6a3004` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10_phase.questphase` / h269 / 6 -> 5 -> 11 |
| `42d198651597f3c3ac03` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10_phase.questphase` / h269 / 0 -> 10 -> 1 |
| `47ffed2303c429a10bea` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10_phase.questphase` / h0 / 67 -> 69 -> 70 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
