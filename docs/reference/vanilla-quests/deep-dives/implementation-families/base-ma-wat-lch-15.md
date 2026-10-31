# base-ma-wat-lch-15

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_15\communities\ma_wat_lch_15.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_15\ma_wat_lch_15.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_15\ma_wat_lch_15.quest` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_15\phases\ma_wat_lch_15.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/little_china/ma_wat_lch_15/onscreens/ma_wat_lch_15_01`
- `points_of_interest/minor_activities/ma_wat_lch_15`
- `quests/minor_activities/watson/little_china/ma_wat_lch_15`
- `quests/minor_activities/watson/little_china/ma_wat_lch_15/description`
- `quests/minor_activities/watson/little_china/ma_wat_lch_15/ma_wat_lch_15/go_to_point`
- `quests/minor_activities/watson/little_china/ma_wat_lch_15/ma_wat_lch_15/loot_the_loot`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 5 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 6 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_15\phases\ma_wat_lch_15.questphase` / h0 / 4 -> 57 -> 31 |
| `06e3382349ceff89de6f` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_15\phases\ma_wat_lch_15.questphase` / h0 / 43 -> 44 -> 45 |
| `0781ef00ea04c05ee418` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_15\phases\ma_wat_lch_15.questphase` / h0 / 22 -> 23 -> 63 |
| `0b988ceccf7fcaa3e0e3` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_15\phases\ma_wat_lch_15.questphase` / h0 / 60 -> 59 -> 37 |
| `0d59d5b737ce1451c32f` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_15\phases\ma_wat_lch_15.questphase` / h0 / 65 -> 60 -> 59 |
| `1094980783b061bb3393` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_15\phases\ma_wat_lch_15.questphase` / h188 / 8 -> 11 -> 5 |
| `12933bc7add8cc0324cd` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_15\phases\ma_wat_lch_15.questphase` / h188 / 2 -> 4 -> 9 |
| `138cff49923a75e07348` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_15\phases\ma_wat_lch_15.questphase` / h0 / 18 -> 21 -> 22 |
| `15703191a3189e1fd363` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_15\phases\ma_wat_lch_15.questphase` / h0 / 59 -> 37 -> 58 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_15\phases\ma_wat_lch_15.questphase` / h0 / 0 -> 4 -> 57 |
| `1d48bd7cbbaeca8257d2` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_15\phases\ma_wat_lch_15.questphase` / h0 / 25 -> 26 -> 9 |
| `215ca95d939006973a7d` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_15\phases\ma_wat_lch_15.questphase` / h0 / 9 -> 11 -> 1 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_15\phases\ma_wat_lch_15.questphase` / h0 / 4 -> 57 -> 10 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_15\phases\ma_wat_lch_15.questphase` / h0 / 63 -> 62 -> 59 |
| `35693c84b9d73befcebd` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_15\phases\ma_wat_lch_15.questphase` / h188 / 0 -> 2 -> 4 |
| `3575eb74602f5e5f696d` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_15\phases\ma_wat_lch_15.questphase` / h0 / 56 -> 18 -> 21 |
| `429813b3b7383ae126db` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_15\phases\ma_wat_lch_15.questphase` / h0 / 62 -> 59 -> 37 |
| `45384fad45d3768a409d` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_15\phases\ma_wat_lch_15.questphase` / h0 / 60 -> 59 -> 25 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_15\phases\ma_wat_lch_15.questphase` / h0 / 57 -> 31 -> 10 |
| `4c86e9d12122e122fabf` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_15\phases\ma_wat_lch_15.questphase` / h188 / 5 -> 6 -> 7 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
