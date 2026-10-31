# base-ma-wat-nid-09

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_09\community\ma_wat_nid_09.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_09\ma_wat_nid_09_gamedef.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_09\ma_wat_nid_09_phase.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_09\ma_wat_nid_09_quest.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_09\ma_wat_nid_09_phase.questphase |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/norhside_industrial_district/ma_wat_nid_09/onscreens/ma_wat_nid_09_alvin`
- `points_of_interest/minor_activities/ma_wat_nid_09`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 4 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalAndNodeDefinition` | 1 |
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
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 1 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `50c0101882435d977f36` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_09\ma_wat_nid_09_phase.questphase` / h0 / 37 -> 61 -> 46 |
| `04dd53360cd034415986` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_09\ma_wat_nid_09_phase.questphase` / h0 / 37 -> 61 -> 38 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_09\ma_wat_nid_09_phase.questphase` / h0 / 66 -> 63 -> 62 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_09\ma_wat_nid_09_phase.questphase` / h0 / 51 -> 54 -> 50 |
| `0b988ceccf7fcaa3e0e3` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_09\ma_wat_nid_09_phase.questphase` / h0 / 63 -> 62 -> 51 |
| `0c8f031f372a34b54a46` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_09\ma_wat_nid_09_phase.questphase` / h0 / 60 -> 37 -> 61 |
| `12ec4d2b63164a705dfa` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_09\ma_wat_nid_09_phase.questphase` / h0 / 5 -> 47 -> 23 |
| `15703191a3189e1fd363` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_09\ma_wat_nid_09_phase.questphase` / h0 / 62 -> 51 -> 54 |
| `16127f3f2f66b166e252` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_09\ma_wat_nid_09_phase.questphase` / h0 / 46 -> 41 -> 2 |
| `163c2cd0d219f09e80f6` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_09\ma_wat_nid_09_phase.questphase` / h0 / 52 -> 41 -> 2 |
| `24bdc2839a62528ae410` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_09\ma_wat_nid_09_phase.questphase` / h0 / 61 -> 38 -> 41 |
| `255c3064dfbb8efcc440` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_09\ma_wat_nid_09_phase.questphase` / h0 / 48 -> 41 -> 2 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_09\ma_wat_nid_09_phase.questphase` / h0 / 66 -> 65 -> 62 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_09\ma_wat_nid_09_phase.questphase` / h0 / 63 -> 62 -> 24 |
| `3b9c02e635e0f649e86a` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_09\ma_wat_nid_09_phase.questphase` / h0 / 64 -> 62 -> 51 |
| `429813b3b7383ae126db` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_09\ma_wat_nid_09_phase.questphase` / h0 / 65 -> 62 -> 51 |
| `45774537e7e190ffe3d6` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_09\ma_wat_nid_09_phase.questphase` / h0 / 1 -> 44 -> 45 |
| `4e9e44d7ce1c1377e58e` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_09\ma_wat_nid_09_phase.questphase` / h0 / 32 -> 43 -> 59 |
| `5d73a2f49ed5d74832e0` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_09\ma_wat_nid_09_phase.questphase` / h0 / 26 -> 32 -> 57 |
| `61d3418beee2f95947c8` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_09\ma_wat_nid_09_phase.questphase` / h0 / 39 -> 41 -> 2 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
