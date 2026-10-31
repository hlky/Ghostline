# base-ma-hey-spr-12

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_12\community\ma_hey_spr_12_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_12\ma_hey_spr_12.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_12\ma_hey_spr_12.quest` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_12\ma_hey_spr_12_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/heywood/wellsprings/ma_hey_spr_12/onscreens/ma_hey_spr_12_onscreen_01`
- `points_of_interest/minor_activities/ma_hey_spr_12`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 4 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `95b7458b3ffd83fd4357` | 3 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_12\ma_hey_spr_12_phase.questphase` / h0 / 2 -> 16 -> 34 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_12\ma_hey_spr_12_phase.questphase` / h0 / 6 -> 40 -> 29 |
| `bfe95df47bd1ca67330f` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_12\ma_hey_spr_12_phase.questphase` / h33 / 8 -> 10 -> 11 |
| `02a5265bcccfc8e3cf77` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_12\ma_hey_spr_12_phase.questphase` / h33 / 13 -> 4 -> 7 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_12\ma_hey_spr_12_phase.questphase` / h0 / 44 -> 47 -> 45 |
| `1094980783b061bb3393` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_12\ma_hey_spr_12_phase.questphase` / h33 / 10 -> 11 -> 6 |
| `12208b60f11caf6d936e` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_12\ma_hey_spr_12_phase.questphase` / h0 / 22 -> 42 -> 30 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_12\ma_hey_spr_12_phase.questphase` / h0 / 0 -> 6 -> 40 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_12\ma_hey_spr_12_phase.questphase` / h0 / 6 -> 40 -> 21 |
| `2c3d4d4eb6c82c8f1261` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_12\ma_hey_spr_12_phase.questphase` / h33 / 7 -> 3 -> 12 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_12\ma_hey_spr_12_phase.questphase` / h0 / 44 -> 43 -> 45 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_12\ma_hey_spr_12_phase.questphase` / h0 / 19 -> 44 -> 43 |
| `334d3d5e9292145cac5a` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_12\ma_hey_spr_12_phase.questphase` / h33 / 11 -> 6 -> 1 |
| `3473788fa2e021211ee9` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_12\ma_hey_spr_12_phase.questphase` / h0 / 38 -> 39 -> 37 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_12\ma_hey_spr_12_phase.questphase` / h0 / 47 -> 45 -> 9 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_12\ma_hey_spr_12_phase.questphase` / h0 / 40 -> 29 -> 21 |
| `4b4a7657f49a6c8435c2` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_12\ma_hey_spr_12_phase.questphase` / h33 / 3 -> 12 -> 2 |
| `4d6c55ba26916a1e04f1` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_12\ma_hey_spr_12_phase.questphase` / h0 / 30 -> 41 -> 1 |
| `51570397b2f761f6ba4f` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_12\ma_hey_spr_12_phase.questphase` / h0 / 40 -> 21 -> 19 |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_12\ma_hey_spr_12_phase.questphase` / h0 / 16 -> 28 -> 4 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
