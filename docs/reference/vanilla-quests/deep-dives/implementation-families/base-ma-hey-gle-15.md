# base-ma-hey-gle-15

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\community\ma_hey_gle_15_6th_street_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\community\ma_hey_gle_15_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\community\ma_hey_gle_15_com_002.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\ma_hey_gle_15.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\ma_hey_gle_15.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\ma_hey_gle_15_phase.questphase |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\ma_hey_gle_15_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/heywood/glen/ma_hey_gle_15/shards/ma_hey_gle_15_b`
- `points_of_interest/minor_activities/ma_hey_gle_15`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 3 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 3 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 9 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\ma_hey_gle_15_phase.questphase` / h0 / 10 -> 46 -> 23 |
| `47cc5074c53050699ba3` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\ma_hey_gle_15_phase.questphase` / h0 / 43 -> 45 -> 5 |
| `56c53a847765e20a971f` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\ma_hey_gle_15_phase.questphase` / h0 / 32 -> 28 -> 27 |
| `7214221ab5d271ce1333` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\ma_hey_gle_15_phase.questphase` / h0 / 31 -> 32 -> 28 |
| `721dd253f632c98c4268` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\ma_hey_gle_15_phase.questphase` / h0 / 4 -> 45 -> 5 |
| `8d10896873df5c62014e` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\ma_hey_gle_15_phase.questphase` / h0 / 2 -> 3 -> 4 |
| `00c3ca0ac0b55db639ca` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\ma_hey_gle_15_phase.questphase` / h66 / 4 -> 2 -> 9 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\ma_hey_gle_15_phase.questphase` / h0 / 55 -> 52 -> 51 |
| `0b81e5206696faa510d4` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\ma_hey_gle_15_phase.questphase` / h66 / 10 -> 11 -> 12 |
| `0e0b0ec1add4154b2d49` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\ma_hey_gle_15_phase.questphase` / h66 / 12 -> 3 -> 5 |
| `102d400f63aec732f66b` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\ma_hey_gle_15_phase.questphase` / h0 / 49 -> 48 -> 39 |
| `12b102391853a0e26cba` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\ma_hey_gle_15_phase.questphase` / h66 / 9 -> 10 -> 11 |
| `178ff9eba50354aed786` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\ma_hey_gle_15_phase.questphase` / h0 / 0 -> 26 -> 2 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\ma_hey_gle_15_phase.questphase` / h66 / 14 -> 4 -> 2 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\ma_hey_gle_15_phase.questphase` / h0 / 0 -> 10 -> 46 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\ma_hey_gle_15_phase.questphase` / h0 / 10 -> 46 -> 17 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\ma_hey_gle_15_phase.questphase` / h0 / 55 -> 54 -> 51 |
| `2e1ee5a1324dbeeb9071` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\ma_hey_gle_15_phase.questphase` / h0 / 26 -> 2 -> 3 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\ma_hey_gle_15_phase.questphase` / h0 / 14 -> 55 -> 54 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_15\ma_hey_gle_15_phase.questphase` / h0 / 52 -> 51 -> 8 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
