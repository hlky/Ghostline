# base-ma-wbr-jpn-13

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_13\community\ma_wbr_jpn_013_claws_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_13\ma_wbr_jpn_13.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_13\ma_wbr_jpn_13.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_13\ma_wbr_jpn_13_phase.questphase |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_13\ma_wbr_jpn_13_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/westbrook/japantown/ma_wbr_jpn_13/shards/ma_wbr_jpn_13_002`
- `points_of_interest/minor_activities/ma_wbr_jpn_13`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 2 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 2 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_13\ma_wbr_jpn_13_phase.questphase` / h0 / 68 -> 65 -> 64 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_13\ma_wbr_jpn_13_phase.questphase` / h0 / 8 -> 57 -> 35 |
| `13f01235c2f7a206b430` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_13\ma_wbr_jpn_13_phase.questphase` / h100 / 2 -> 7 -> 9 |
| `1684da3a45630fb3518c` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_13\ma_wbr_jpn_13_phase.questphase` / h100 / 7 -> 9 -> 12 |
| `16bbbbb5b786ec4e4789` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_13\ma_wbr_jpn_13_phase.questphase` / h0 / 2 -> 8 -> 47 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_13\ma_wbr_jpn_13_phase.questphase` / h100 / 13 -> 4 -> 6 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_13\ma_wbr_jpn_13_phase.questphase` / h0 / 2 -> 8 -> 57 |
| `204ca9b8b94427c1ef81` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_13\ma_wbr_jpn_13_phase.questphase` / h0 / 59 -> 58 -> 36 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_13\ma_wbr_jpn_13_phase.questphase` / h0 / 8 -> 57 -> 24 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_13\ma_wbr_jpn_13_phase.questphase` / h0 / 68 -> 67 -> 64 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_13\ma_wbr_jpn_13_phase.questphase` / h0 / 25 -> 68 -> 67 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_13\ma_wbr_jpn_13_phase.questphase` / h0 / 65 -> 64 -> 6 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_13\ma_wbr_jpn_13_phase.questphase` / h0 / 57 -> 35 -> 24 |
| `4e9e44d7ce1c1377e58e` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_13\ma_wbr_jpn_13_phase.questphase` / h0 / 19 -> 56 -> 59 |
| `51570397b2f761f6ba4f` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_13\ma_wbr_jpn_13_phase.questphase` / h0 / 57 -> 24 -> 25 |
| `598920ee48558917ab4e` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_13\ma_wbr_jpn_13_phase.questphase` / h0 / 35 -> 24 -> 25 |
| `6b3e5fe15b7a64a01e21` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_13\ma_wbr_jpn_13_phase.questphase` / h0 / 24 -> 25 -> 68 |
| `75582ae0b4c1620a124c` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_13\ma_wbr_jpn_13_phase.questphase` / h100 / 10 -> 11 -> 1 |
| `7616062dec0ebe3473b4` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_13\ma_wbr_jpn_13_phase.questphase` / h0 / 68 -> 66 -> 64 |
| `7ab698c317f00ab32676` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_13\ma_wbr_jpn_13_phase.questphase` / h0 / 25 -> 68 -> 66 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
