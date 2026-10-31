# base-ma-cct-dtn-15

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_15\community\ma_cct_dtn_15_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_15\ma_cct_dtn_15.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_15\ma_cct_dtn_15.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_15\ma_cct_dtn_15_phase.questphase |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_15\ma_cct_dtn_15_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/city_center/downtown/ma_cct_dtn_15/onscreens/ma_cct_dtn_15_onscreen_01`
- `points_of_interest/minor_activities/ma_cct_dtn_15`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 2 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 1 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_15\ma_cct_dtn_15_phase.questphase` / h0 / 41 -> 38 -> 37 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_15\ma_cct_dtn_15_phase.questphase` / h0 / 10 -> 31 -> 21 |
| `1196b65ec43cf9530eeb` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_15\ma_cct_dtn_15_phase.questphase` / h0 / 35 -> 34 -> 26 |
| `16bbbbb5b786ec4e4789` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_15\ma_cct_dtn_15_phase.questphase` / h0 / 2 -> 10 -> 28 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_15\ma_cct_dtn_15_phase.questphase` / h0 / 2 -> 10 -> 31 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_15\ma_cct_dtn_15_phase.questphase` / h0 / 41 -> 40 -> 37 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_15\ma_cct_dtn_15_phase.questphase` / h0 / 17 -> 41 -> 40 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_15\ma_cct_dtn_15_phase.questphase` / h0 / 38 -> 37 -> 23 |
| `4db18aaae4b08d077f4e` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_15\ma_cct_dtn_15_phase.questphase` / h0 / 34 -> 26 -> 27 |
| `52835ecf92cfc4b92621` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_15\ma_cct_dtn_15_phase.questphase` / h0 / 27 -> 30 -> 3 |
| `68f2f28c67095b343e1f` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_15\ma_cct_dtn_15_phase.questphase` / h0 / 24 -> 35 -> 34 |
| `69ac42d59aa43099e19c` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_15\ma_cct_dtn_15_phase.questphase` / h0 / 15 -> 32 -> 22 |
| `6b3e5fe15b7a64a01e21` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_15\ma_cct_dtn_15_phase.questphase` / h0 / 16 -> 17 -> 41 |
| `71892f49b88f7b8bb8be` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_15\ma_cct_dtn_15_phase.questphase` / h0 / 2 -> 10 -> 16 |
| `7616062dec0ebe3473b4` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_15\ma_cct_dtn_15_phase.questphase` / h0 / 41 -> 39 -> 37 |
| `7ab698c317f00ab32676` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_15\ma_cct_dtn_15_phase.questphase` / h0 / 17 -> 41 -> 39 |
| `8d30c0ae448228fc9543` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_15\ma_cct_dtn_15_phase.questphase` / h0 / 10 -> 28 -> 29 |
| `99c738f69bc472a4bcbf` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_15\ma_cct_dtn_15_phase.questphase` / h0 / 23 -> 14 -> 18 |
| `9af8a87f20a910659fa8` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_15\ma_cct_dtn_15_phase.questphase` / h0 / 14 -> 18 -> 19 |
| `9f3dfa03c86adea5087f` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_15\ma_cct_dtn_15_phase.questphase` / h0 / 37 -> 23 -> 14 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
