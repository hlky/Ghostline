# base-ma-hey-spr-03

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\community\ma_hey_spr_03_civilian_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\community\ma_hey_spr_03_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03.quest` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03_phase.questphase` | content candidate | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/heywood/wellsprings/ma_hey_spr_03/onscreens/ma_hey_spr_03_onscreen_02`
- `points_of_interest/minor_activities/ma_hey_spr_03`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 7 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 3 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalAndNodeDefinition` | 3 |
| `questLogicalXorNodeDefinition` | 3 |
| `questMiscAICommandNode` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 2 |
| `questOutputNodeDefinition` | 4 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 6 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 10 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `987122e5e2fcd167cf6c` | 3 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03_phase.questphase` / h0 / 0 -> 18 -> 27 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03_phase.questphase` / h0 / 7 -> 66 -> 43 |
| `11d01d01a3598fe0b256` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03_phase.questphase` / h0 / 51 -> 57 -> 52 |
| `a3e5f861a4b71433135a` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03_phase.questphase` / h60 / 13 -> 2 -> 6 |
| `02a5265bcccfc8e3cf77` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03_phase.questphase` / h60 / 13 -> 2 -> 3 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03_phase.questphase` / h0 / 92 -> 94 -> 93 |
| `080b445bc4090d559039` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03_phase.questphase` / h0 / 0 -> 7 -> 51 |
| `0c05428861b4359e61e0` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03_phase.questphase` / h0 / 62 -> 64 -> 63 |
| `12208b60f11caf6d936e` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03_phase.questphase` / h0 / 34 -> 76 -> 44 |
| `163c2cd0d219f09e80f6` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03_phase.questphase` / h60 / 8 -> 11 -> 12 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03_phase.questphase` / h60 / 13 -> 2 -> 5 |
| `1972a0532f20a107c8bb` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03_phase.questphase` / h0 / 18 -> 19 -> 25 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03_phase.questphase` / h0 / 0 -> 7 -> 66 |
| `1dff7f84bcc367b07eb4` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03_phase.questphase` / h0 / 89 -> 90 -> 80 |
| `20666b4559fcce2dfa8f` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03_phase.questphase` / h60 / 2 -> 8 -> 11 |
| `20744a237dcc75c6f578` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03_phase.questphase` / h0 / 93 -> 17 -> 74 |
| `22043c7532e33463a91b` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03_phase.questphase` / h0 / 60 -> 62 -> 64 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03_phase.questphase` / h0 / 7 -> 66 -> 33 |
| `2cc4f20e16798419f013` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03_phase.questphase` / h0 / 31 -> 8 -> 92 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03_phase.questphase` / h0 / 92 -> 91 -> 93 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
