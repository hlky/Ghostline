# base-ma-hey-gle-11

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_11\community\ma_hey_gle_11_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_11\community\ma_hey_gle_11_valentinos_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_11\ma_hey_gle_11.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_11\ma_hey_gle_11.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\heywood\glen\ma_hey_gle_11\ma_hey_gle_11_phase.questphase |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_11\ma_hey_gle_11_phase.questphase` | content candidate | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/heywood/glen/ma_hey_gle_11/shards/ma_hey_gle_11`
- `points_of_interest/minor_activities/ma_hey_gle_11`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_ModifyHealth,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 4 |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition` | 5 |
| `questCombatNodeDefinition[questCombatNodeParams_UseCover]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 4 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalHubNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 2 |
| `questMiscAICommandNode[questCombatNodeParams_RestrictMovementToArea]` | 4 |
| `questOutputNodeDefinition` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 5 |
| `questPhaseNodeDefinition` | 2 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `9ee390ed5172aafc9175` | 5 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_11\ma_hey_gle_11_phase.questphase` / h226 / 42 -> 46 -> 48 |
| `59bbe39d0391262861b9` | 4 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_11\ma_hey_gle_11_phase.questphase` / h0 / 41 -> 44 -> 42 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_11\ma_hey_gle_11_phase.questphase` / h0 / 9 -> 50 -> 27 |
| `987122e5e2fcd167cf6c` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_11\ma_hey_gle_11_phase.questphase` / h0 / 0 -> 2 -> 4 |
| `02692ae3a7624f2dd47d` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_11\ma_hey_gle_11_phase.questphase` / h226 / 49 -> 53 -> 54 |
| `02a5265bcccfc8e3cf77` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_11\ma_hey_gle_11_phase.questphase` / h75 / 10 -> 2 -> 3 |
| `05a1a34a1ecb3c1b73e3` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_11\ma_hey_gle_11_phase.questphase` / h226 / 56 -> 53 -> 54 |
| `0672ae8d2fae884916ec` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_11\ma_hey_gle_11_phase.questphase` / h75 / 2 -> 3 -> 5 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_11\ma_hey_gle_11_phase.questphase` / h0 / 54 -> 55 -> 53 |
| `0997ca74d2d1cd9b37c3` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_11\ma_hey_gle_11_phase.questphase` / h226 / 47 -> 53 -> 54 |
| `1684da3a45630fb3518c` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_11\ma_hey_gle_11_phase.questphase` / h75 / 7 -> 6 -> 8 |
| `1705b5c45728a7f5feb5` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_11\ma_hey_gle_11_phase.questphase` / h226 / 51 -> 53 -> 54 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_11\ma_hey_gle_11_phase.questphase` / h0 / 0 -> 9 -> 50 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_11\ma_hey_gle_11_phase.questphase` / h0 / 9 -> 50 -> 22 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_11\ma_hey_gle_11_phase.questphase` / h0 / 54 -> 52 -> 53 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_11\ma_hey_gle_11_phase.questphase` / h0 / 26 -> 54 -> 52 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_11\ma_hey_gle_11_phase.questphase` / h0 / 55 -> 53 -> 7 |
| `3747c39288db4afd2de7` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_11\ma_hey_gle_11_phase.questphase` / h226 / 46 -> 56 -> 53 |
| `3d325dd074976fcb5b34` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_11\ma_hey_gle_11_phase.questphase` / h226 / 0 -> 24 -> 64 |
| `403d794f01acf7d4e8ce` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_11\ma_hey_gle_11_phase.questphase` / h0 / 53 -> 7 -> 19 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
