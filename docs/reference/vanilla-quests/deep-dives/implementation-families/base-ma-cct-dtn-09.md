# base-ma-cct-dtn-09

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\community\ma_cct_dtn_09_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\community\ma_cct_dtn_09_com_victims.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\ma_cct_dtn_09.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\ma_cct_dtn_09.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\ma_cct_dtn_09_phase.questphase |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\ma_cct_dtn_09_phase.questphase` | content candidate | 7 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/city_center/downtown/ma_cct_dtn_09/onscreens/ma_cct_dtn_09_onscreen_01`
- `points_of_interest/minor_activities/ma_cct_dtn_09`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 7 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 7 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 2 |
| `questOutputNodeDefinition` | 6 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterReaction_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 6 |
| `questPhaseNodeDefinition` | 7 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 14 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 6 |
| `questStartNodeDefinition` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `658fe17f8b47d2c016b7` | 3 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\ma_cct_dtn_09_phase.questphase` / h272 / 0 -> 2 -> 1 |
| `71892f49b88f7b8bb8be` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\ma_cct_dtn_09_phase.questphase` / h0 / 0 -> 8 -> 21 |
| `79ff30ab7464b071eda5` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\ma_cct_dtn_09_phase.questphase` / h0 / 40 -> 41 -> 42 |
| `86598e02c77b18e76df0` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\ma_cct_dtn_09_phase.questphase` / h298 / 0 -> 2 -> 3 |
| `eaba84fa6e215dfc141d` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\ma_cct_dtn_09_phase.questphase` / h212 / 8 -> 11 -> 12 |
| `0015f21cac33b67104ef` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\ma_cct_dtn_09_phase.questphase` / h0 / 35 -> 59 -> 57 |
| `00c3ca0ac0b55db639ca` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\ma_cct_dtn_09_phase.questphase` / h0 / 14 -> 28 -> 38 |
| `05368f97c1887d1ef26f` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\ma_cct_dtn_09_phase.questphase` / h298 / 3 -> 5 -> 10 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\ma_cct_dtn_09_phase.questphase` / h0 / 59 -> 56 -> 55 |
| `0b81e5206696faa510d4` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\ma_cct_dtn_09_phase.questphase` / h0 / 45 -> 19 -> 26 |
| `114d46d19e809cb7d96b` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\ma_cct_dtn_09_phase.questphase` / h0 / 52 -> 59 -> 57 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\ma_cct_dtn_09_phase.questphase` / h0 / 29 -> 14 -> 28 |
| `1c8f5db5f76df3ad5f7c` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\ma_cct_dtn_09_phase.questphase` / h0 / 22 -> 52 -> 59 |
| `25e95738e237951bd227` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\ma_cct_dtn_09_phase.questphase` / h0 / 58 -> 55 -> 29 |
| `295acc02504244db40db` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\ma_cct_dtn_09_phase.questphase` / h0 / 36 -> 47 -> 15 |
| `2c20201f171f754c99e0` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\ma_cct_dtn_09_phase.questphase` / h298 / 10 -> 7 -> 6 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\ma_cct_dtn_09_phase.questphase` / h0 / 59 -> 58 -> 55 |
| `344a9bb49243e19907c3` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\ma_cct_dtn_09_phase.questphase` / h298 / 2 -> 3 -> 4 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\ma_cct_dtn_09_phase.questphase` / h0 / 56 -> 55 -> 10 |
| `390f62c11ddf01069a3f` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\ma_cct_dtn_09_phase.questphase` / h0 / 0 -> 37 -> 39 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
