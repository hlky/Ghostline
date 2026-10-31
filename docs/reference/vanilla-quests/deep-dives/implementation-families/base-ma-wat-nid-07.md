# base-ma-wat-nid-07

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_07\community\ma_wat_nid_07_mercenaries.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_07\community\ma_wat_nid_07_wounded_merc.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_07\ma_wat_nid_07_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/norhside_industrial_district/ma_wat_nid_07/onscreens/ma_wat_nid_07_documents`
- `points_of_interest/minor_activities/ma_wat_nid_07`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_ModifyHealth,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 2 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterEquippedItem_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_07\ma_wat_nid_07_phase.questphase` / h0 / 12 -> 49 -> 33 |
| `43497e272537226eb0cc` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_07\ma_wat_nid_07_phase.questphase` / h0 / 15 -> 16 -> 20 |
| `dde3cfc86c1764319bba` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_07\ma_wat_nid_07_phase.questphase` / h0 / 15 -> 16 -> 29 |
| `e28e57fe70562fd64681` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_07\ma_wat_nid_07_phase.questphase` / h0 / 8 -> 15 -> 16 |
| `02d878a28a675e881f96` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_07\ma_wat_nid_07_phase.questphase` / h0 / 59 -> 57 -> 14 |
| `04dd53360cd034415986` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_07\ma_wat_nid_07_phase.questphase` / h0 / 24 -> 56 -> 28 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_07\ma_wat_nid_07_phase.questphase` / h0 / 61 -> 58 -> 57 |
| `0b988ceccf7fcaa3e0e3` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_07\ma_wat_nid_07_phase.questphase` / h0 / 58 -> 57 -> 35 |
| `0c8f031f372a34b54a46` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_07\ma_wat_nid_07_phase.questphase` / h0 / 55 -> 24 -> 56 |
| `1121a7f146103492ac60` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_07\ma_wat_nid_07_phase.questphase` / h0 / 59 -> 57 -> 30 |
| `15703191a3189e1fd363` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_07\ma_wat_nid_07_phase.questphase` / h0 / 57 -> 35 -> 50 |
| `16127f3f2f66b166e252` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_07\ma_wat_nid_07_phase.questphase` / h0 / 32 -> 26 -> 22 |
| `24bdc2839a62528ae410` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_07\ma_wat_nid_07_phase.questphase` / h0 / 56 -> 28 -> 26 |
| `255c3064dfbb8efcc440` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_07\ma_wat_nid_07_phase.questphase` / h0 / 37 -> 26 -> 22 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_07\ma_wat_nid_07_phase.questphase` / h0 / 61 -> 60 -> 57 |
| `2e578fd8f85357f1804f` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_07\ma_wat_nid_07_phase.questphase` / h0 / 12 -> 61 -> 59 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_07\ma_wat_nid_07_phase.questphase` / h0 / 58 -> 57 -> 13 |
| `354e0603fdbd00ceb27b` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_07\ma_wat_nid_07_phase.questphase` / h0 / 57 -> 51 -> 55 |
| `3b9c02e635e0f649e86a` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_07\ma_wat_nid_07_phase.questphase` / h0 / 59 -> 57 -> 35 |
| `429813b3b7383ae126db` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_07\ma_wat_nid_07_phase.questphase` / h0 / 60 -> 57 -> 35 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
