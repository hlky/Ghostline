# base-ma-hey-gle-03

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_03\community\ma_hey_gle_03_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_03\ma_hey_gle_03.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_03\ma_hey_gle_03.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\heywood\glen\ma_hey_gle_03\ma_hey_gle_03_phase.questphase |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_03\ma_hey_gle_03_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/heywood/glen/ma_hey_gle_03/shards/ma_hey_gle_03`
- `points_of_interest/minor_activities/ma_hey_gle_03`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 6 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 3 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 4 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_03\ma_hey_gle_03_phase.questphase` / h0 / 27 -> 61 -> 38 |
| `808c42396a9735fe3a65` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_03\ma_hey_gle_03_phase.questphase` / h0 / 3 -> 49 -> 42 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_03\ma_hey_gle_03_phase.questphase` / h0 / 68 -> 69 -> 66 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_03\ma_hey_gle_03_phase.questphase` / h61 / 11 -> 6 -> 3 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_03\ma_hey_gle_03_phase.questphase` / h0 / 3 -> 27 -> 61 |
| `1e8ddd4b176ae3d7c402` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_03\ma_hey_gle_03_phase.questphase` / h0 / 49 -> 42 -> 44 |
| `210435623f63af100570` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_03\ma_hey_gle_03_phase.questphase` / h0 / 44 -> 45 -> 41 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_03\ma_hey_gle_03_phase.questphase` / h0 / 27 -> 61 -> 31 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_03\ma_hey_gle_03_phase.questphase` / h0 / 68 -> 67 -> 66 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_03\ma_hey_gle_03_phase.questphase` / h0 / 32 -> 68 -> 67 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_03\ma_hey_gle_03_phase.questphase` / h0 / 69 -> 66 -> 25 |
| `3c6b36e8c01548f18f31` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_03\ma_hey_gle_03_phase.questphase` / h0 / 33 -> 30 -> 40 |
| `42ca878854c6b758165e` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_03\ma_hey_gle_03_phase.questphase` / h61 / 3 -> 2 -> 9 |
| `4365e94e7169e2520841` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_03\ma_hey_gle_03_phase.questphase` / h0 / 69 -> 66 -> 4 |
| `4516ea8d7bcf8c04ba50` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_03\ma_hey_gle_03_phase.questphase` / h0 / 70 -> 66 -> 4 |
| `48b34908ac4ded0af324` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_03\ma_hey_gle_03_phase.questphase` / h0 / 67 -> 66 -> 4 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_03\ma_hey_gle_03_phase.questphase` / h0 / 61 -> 38 -> 31 |
| `51570397b2f761f6ba4f` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_03\ma_hey_gle_03_phase.questphase` / h0 / 61 -> 31 -> 32 |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_03\ma_hey_gle_03_phase.questphase` / h0 / 7 -> 5 -> 18 |
| `598920ee48558917ab4e` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_03\ma_hey_gle_03_phase.questphase` / h0 / 38 -> 31 -> 32 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
