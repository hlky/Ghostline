# base-ma-hey-gle-09

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_09\community\ma_hey_gle_09_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_09\ma_hey_gle_09.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_09\ma_hey_gle_09.quest` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_09\ma_hey_gle_09_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/heywood/glen/ma_hey_gle_09/shards/ma_hey_gle_09`
- `points_of_interest/minor_activities/ma_hey_gle_09`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_09\ma_hey_gle_09_phase.questphase` / h0 / 12 -> 22 -> 19 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_09\ma_hey_gle_09_phase.questphase` / h0 / 25 -> 27 -> 26 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_09\ma_hey_gle_09_phase.questphase` / h57 / 7 -> 4 -> 2 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_09\ma_hey_gle_09_phase.questphase` / h0 / 3 -> 12 -> 22 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_09\ma_hey_gle_09_phase.questphase` / h0 / 12 -> 22 -> 15 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_09\ma_hey_gle_09_phase.questphase` / h0 / 25 -> 24 -> 26 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_09\ma_hey_gle_09_phase.questphase` / h0 / 16 -> 25 -> 24 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_09\ma_hey_gle_09_phase.questphase` / h0 / 27 -> 26 -> 10 |
| `403d794f01acf7d4e8ce` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_09\ma_hey_gle_09_phase.questphase` / h0 / 26 -> 10 -> 14 |
| `4365e94e7169e2520841` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_09\ma_hey_gle_09_phase.questphase` / h0 / 27 -> 26 -> 4 |
| `4516ea8d7bcf8c04ba50` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_09\ma_hey_gle_09_phase.questphase` / h0 / 28 -> 26 -> 4 |
| `48b34908ac4ded0af324` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_09\ma_hey_gle_09_phase.questphase` / h0 / 24 -> 26 -> 4 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_09\ma_hey_gle_09_phase.questphase` / h0 / 22 -> 19 -> 15 |
| `51570397b2f761f6ba4f` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_09\ma_hey_gle_09_phase.questphase` / h0 / 22 -> 15 -> 16 |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_09\ma_hey_gle_09_phase.questphase` / h0 / 7 -> 5 -> 8 |
| `598920ee48558917ab4e` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_09\ma_hey_gle_09_phase.questphase` / h0 / 19 -> 15 -> 16 |
| `60a306c2bf9dcf430a17` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_09\ma_hey_gle_09_phase.questphase` / h0 / 10 -> 14 -> 18 |
| `6b3e5fe15b7a64a01e21` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_09\ma_hey_gle_09_phase.questphase` / h0 / 15 -> 16 -> 25 |
| `7616062dec0ebe3473b4` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_09\ma_hey_gle_09_phase.questphase` / h0 / 25 -> 28 -> 26 |
| `79b539118540b151bff5` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_09\ma_hey_gle_09_phase.questphase` / h57 / 3 -> 6 -> 1 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
