# base-ma-hey-spr-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\community\ma_hey_spr_02_civilian_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\community\ma_hey_spr_02_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02.quest` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/heywood/wellsprings/ma_hey_spr_02/onscreens/ma_hey_spr_02_onscreen_01`
- `points_of_interest/minor_activities/ma_hey_spr_02`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questInputNodeDefinition` | 2 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 2 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 5 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 4 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 5 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `a3e5f861a4b71433135a` | 3 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02_phase.questphase` / h26 / 15 -> 2 -> 5 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02_phase.questphase` / h0 / 7 -> 75 -> 61 |
| `987122e5e2fcd167cf6c` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02_phase.questphase` / h0 / 0 -> 13 -> 60 |
| `02a5265bcccfc8e3cf77` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02_phase.questphase` / h26 / 15 -> 2 -> 3 |
| `0669a9bd5e6c7e6c51dd` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02_phase.questphase` / h26 / 2 -> 8 -> 13 |
| `06e3382349ceff89de6f` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02_phase.questphase` / h0 / 14 -> 21 -> 71 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02_phase.questphase` / h0 / 79 -> 81 -> 80 |
| `0b387b0e0f2538ab6067` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02_phase.questphase` / h26 / 2 -> 9 -> 12 |
| `1198407e25fb6cae0240` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02_phase.questphase` / h0 / 81 -> 80 -> 4 |
| `12208b60f11caf6d936e` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02_phase.questphase` / h0 / 42 -> 77 -> 62 |
| `163c2cd0d219f09e80f6` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02_phase.questphase` / h26 / 10 -> 13 -> 14 |
| `1972a0532f20a107c8bb` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02_phase.questphase` / h0 / 13 -> 14 -> 21 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02_phase.questphase` / h0 / 0 -> 7 -> 75 |
| `20666b4559fcce2dfa8f` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02_phase.questphase` / h26 / 2 -> 10 -> 13 |
| `20e74db83226e46cc202` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02_phase.questphase` / h0 / 65 -> 68 -> 66 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02_phase.questphase` / h0 / 7 -> 75 -> 37 |
| `24cb2d011f83f1d98c37` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02_phase.questphase` / h26 / 9 -> 12 -> 13 |
| `2c3d4d4eb6c82c8f1261` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02_phase.questphase` / h26 / 3 -> 7 -> 6 |
| `2cc4f20e16798419f013` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02_phase.questphase` / h0 / 33 -> 8 -> 79 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02_phase.questphase` / h0 / 79 -> 78 -> 80 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
