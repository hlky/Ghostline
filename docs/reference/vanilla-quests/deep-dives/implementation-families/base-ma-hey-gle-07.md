# base-ma-hey-gle-07

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_07\community\ma_hey_gle_07_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_07\ma_hey_gle_07.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_07\ma_hey_gle_07.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\heywood\glen\ma_hey_gle_07\ma_hey_gle_07_phase.questphase |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_07\ma_hey_gle_07_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/heywood/glen/ma_hey_gle_07/shards/ma_hey_gle_07_a`
- `points_of_interest/minor_activities/ma_hey_gle_07`
- `quests/minor_activities/heywood/glen/ma_hey_gle_07`
- `quests/minor_activities/heywood/glen/ma_hey_gle_07/description`
- `quests/minor_activities/heywood/glen/ma_hey_gle_07/ma_hey_gle_07/go_to_spot`
- `quests/minor_activities/heywood/glen/ma_hey_gle_07/ma_hey_gle_07/loot`
- `quests/minor_activities/heywood/glen/ma_hey_gle_07/ma_hey_gle_07/read_shard`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 3 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 3 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 7 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 7 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_07\ma_hey_gle_07_phase.questphase` / h0 / 10 -> 51 -> 37 |
| `58cccf416254fa380803` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_07\ma_hey_gle_07_phase.questphase` / h0 / 44 -> 46 -> 47 |
| `bee1f62dab6be5337bda` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_07\ma_hey_gle_07_phase.questphase` / h85 / 6 -> 9 -> 7 |
| `03981ca41dcdffb72312` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_07\ma_hey_gle_07_phase.questphase` / h0 / 53 -> 28 -> 30 |
| `0781ef00ea04c05ee418` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_07\ma_hey_gle_07_phase.questphase` / h0 / 29 -> 31 -> 58 |
| `0d59d5b737ce1451c32f` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_07\ma_hey_gle_07_phase.questphase` / h0 / 61 -> 60 -> 56 |
| `138cff49923a75e07348` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_07\ma_hey_gle_07_phase.questphase` / h0 / 28 -> 30 -> 29 |
| `1618785f459ae761ab44` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_07\ma_hey_gle_07_phase.questphase` / h0 / 18 -> 34 -> 8 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_07\ma_hey_gle_07_phase.questphase` / h85 / 12 -> 6 -> 9 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_07\ma_hey_gle_07_phase.questphase` / h0 / 0 -> 10 -> 51 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_07\ma_hey_gle_07_phase.questphase` / h0 / 10 -> 51 -> 16 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_07\ma_hey_gle_07_phase.questphase` / h0 / 58 -> 57 -> 56 |
| `334d3d5e9292145cac5a` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_07\ma_hey_gle_07_phase.questphase` / h85 / 7 -> 8 -> 1 |
| `34bfe3a351fe83270da3` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_07\ma_hey_gle_07_phase.questphase` / h0 / 33 -> 35 -> 12 |
| `3f522da5aafade67772b` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_07\ma_hey_gle_07_phase.questphase` / h0 / 10 -> 44 -> 46 |
| `4365e94e7169e2520841` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_07\ma_hey_gle_07_phase.questphase` / h0 / 60 -> 56 -> 1 |
| `45384fad45d3768a409d` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_07\ma_hey_gle_07_phase.questphase` / h0 / 60 -> 56 -> 33 |
| `48b34908ac4ded0af324` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_07\ma_hey_gle_07_phase.questphase` / h0 / 57 -> 56 -> 1 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_07\ma_hey_gle_07_phase.questphase` / h0 / 51 -> 37 -> 16 |
| `4e9253a72e6b0134b8dd` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_07\ma_hey_gle_07_phase.questphase` / h0 / 30 -> 29 -> 31 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
