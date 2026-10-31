# base-ma-hey-gle-13

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_13\community\ma_hey_gle_13_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_13\community\ma_hey_gle_13_valentinos_victim_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_13\ma_hey_gle_13.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_13\ma_hey_gle_13.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\heywood\glen\ma_hey_gle_13\ma_hey_gle_13_phase.questphase |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_13\ma_hey_gle_13_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/heywood/glen/ma_hey_gle_13/shards/ma_hey_gle_13`
- `points_of_interest/minor_activities/ma_hey_gle_13`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 3 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 5 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_13\ma_hey_gle_13_phase.questphase` / h0 / 12 -> 35 -> 20 |
| `6b6ee30811d0a6650bfd` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_13\ma_hey_gle_13_phase.questphase` / h0 / 26 -> 27 -> 32 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_13\ma_hey_gle_13_phase.questphase` / h0 / 42 -> 44 -> 43 |
| `102d400f63aec732f66b` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_13\ma_hey_gle_13_phase.questphase` / h0 / 39 -> 37 -> 31 |
| `18cc4b1d18f29dc832a8` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_13\ma_hey_gle_13_phase.questphase` / h0 / 0 -> 23 -> 32 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_13\ma_hey_gle_13_phase.questphase` / h0 / 0 -> 12 -> 35 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_13\ma_hey_gle_13_phase.questphase` / h0 / 12 -> 35 -> 18 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_13\ma_hey_gle_13_phase.questphase` / h0 / 42 -> 41 -> 43 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_13\ma_hey_gle_13_phase.questphase` / h0 / 19 -> 42 -> 41 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_13\ma_hey_gle_13_phase.questphase` / h0 / 44 -> 43 -> 10 |
| `3963ee548ac42b0325e9` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_13\ma_hey_gle_13_phase.questphase` / h0 / 0 -> 26 -> 27 |
| `403d794f01acf7d4e8ce` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_13\ma_hey_gle_13_phase.questphase` / h0 / 43 -> 10 -> 15 |
| `42b38abb0e011712fe92` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_13\ma_hey_gle_13_phase.questphase` / h0 / 26 -> 27 -> 24 |
| `4365e94e7169e2520841` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_13\ma_hey_gle_13_phase.questphase` / h0 / 44 -> 43 -> 1 |
| `4516ea8d7bcf8c04ba50` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_13\ma_hey_gle_13_phase.questphase` / h0 / 45 -> 43 -> 1 |
| `48b34908ac4ded0af324` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_13\ma_hey_gle_13_phase.questphase` / h0 / 41 -> 43 -> 1 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_13\ma_hey_gle_13_phase.questphase` / h0 / 35 -> 20 -> 18 |
| `51570397b2f761f6ba4f` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_13\ma_hey_gle_13_phase.questphase` / h0 / 35 -> 18 -> 19 |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_13\ma_hey_gle_13_phase.questphase` / h0 / 3 -> 4 -> 5 |
| `598920ee48558917ab4e` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_13\ma_hey_gle_13_phase.questphase` / h0 / 20 -> 18 -> 19 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
