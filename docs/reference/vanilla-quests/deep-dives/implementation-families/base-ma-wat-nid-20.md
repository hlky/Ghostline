# base-ma-wat-nid-20

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_20\community\ma_wat_nid_20_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_20\ma_wat_nid_20_gamedef.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_20\ma_wat_nid_20_phase.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_20\ma_wat_nid_20_quest.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_20\ma_wat_nid_20_phase.questphase |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/norhside_industrial_district/ma_wat_nid_20/onscreens/ma_wat_nid_20_sms_conversation`
- `points_of_interest/minor_activities/ma_wat_nid_20`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questInputNodeDefinition` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 3 |
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
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `95b7458b3ffd83fd4357` | 3 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_20\ma_wat_nid_20_phase.questphase` / h0 / 0 -> 4 -> 24 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_20\ma_wat_nid_20_phase.questphase` / h0 / 47 -> 44 -> 43 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_20\ma_wat_nid_20_phase.questphase` / h0 / 31 -> 36 -> 32 |
| `0c8f031f372a34b54a46` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_20\ma_wat_nid_20_phase.questphase` / h0 / 41 -> 19 -> 42 |
| `1489a2df8e7f98f9c78e` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_20\ma_wat_nid_20_phase.questphase` / h0 / 0 -> 4 -> 47 |
| `1495b1d75b7c2987dca3` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_20\ma_wat_nid_20_phase.questphase` / h0 / 21 -> 23 -> 28 |
| `1ecc1e1f4c4151a3aba0` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_20\ma_wat_nid_20_phase.questphase` / h0 / 31 -> 36 -> 38 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_20\ma_wat_nid_20_phase.questphase` / h0 / 47 -> 46 -> 43 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_20\ma_wat_nid_20_phase.questphase` / h0 / 44 -> 43 -> 9 |
| `36dddd8add8366cb2443` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_20\ma_wat_nid_20_phase.questphase` / h0 / 36 -> 38 -> 41 |
| `3750bdcc2a4bda83d074` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_20\ma_wat_nid_20_phase.questphase` / h0 / 4 -> 47 -> 46 |
| `3a7f8b9c6d709ceceae1` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_20\ma_wat_nid_20_phase.questphase` / h0 / 4 -> 47 -> 44 |
| `3c6b36e8c01548f18f31` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_20\ma_wat_nid_20_phase.questphase` / h0 / 11 -> 17 -> 31 |
| `4e534a24897f81ddee0f` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_20\ma_wat_nid_20_phase.questphase` / h0 / 36 -> 32 -> 38 |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_20\ma_wat_nid_20_phase.questphase` / h0 / 4 -> 2 -> 5 |
| `5870e2fba5607932758d` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_20\ma_wat_nid_20_phase.questphase` / h0 / 4 -> 8 -> 16 |
| `655a5fc4418feddbb4e4` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_20\ma_wat_nid_20_phase.questphase` / h0 / 29 -> 34 -> 12 |
| `75a31805d3e2f9c96e96` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_20\ma_wat_nid_20_phase.questphase` / h0 / 42 -> 18 -> 21 |
| `7616062dec0ebe3473b4` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_20\ma_wat_nid_20_phase.questphase` / h0 / 47 -> 45 -> 43 |
| `7d737e5a0349033850b7` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_20\ma_wat_nid_20_phase.questphase` / h0 / 28 -> 29 -> 34 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
