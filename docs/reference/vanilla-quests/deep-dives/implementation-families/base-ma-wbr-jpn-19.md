# base-ma-wbr-jpn-19

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_19\community\ma_wbr_jpn_19.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_19\community\ma_wbr_jpn_19_tyger_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_19\ma_wbr_jpn_19.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_19\ma_wbr_jpn_19.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_19\ma_wbr_jpn_19_phase.questphase |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_19\ma_wbr_jpn_19_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/westbrook/japantown/ma_wbr_jpn_19/shards/ma_wbr_jpn_19_a`
- `points_of_interest/minor_activities/ma_wbr_jpn_19`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questInputNodeDefinition` | 2 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalHubNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 5 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `51d78876d4b7cc3025b7` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_19\ma_wbr_jpn_19_phase.questphase` / h0 / 3 -> 6 -> 4 |
| `99c738f69bc472a4bcbf` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_19\ma_wbr_jpn_19_phase.questphase` / h0 / 12 -> 20 -> 21 |
| `9b747524cfea0c0bc013` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_19\ma_wbr_jpn_19_phase.questphase` / h50 / 14 -> 4 -> 10 |
| `aecd5a3ed323a981c85d` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_19\ma_wbr_jpn_19_phase.questphase` / h0 / 0 -> 2 -> 31 |
| `05741704b94ee3af2e8c` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_19\ma_wbr_jpn_19_phase.questphase` / h0 / 2 -> 29 -> 41 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_19\ma_wbr_jpn_19_phase.questphase` / h0 / 61 -> 58 -> 57 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_19\ma_wbr_jpn_19_phase.questphase` / h0 / 15 -> 48 -> 26 |
| `0f660f7484731cdb671e` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_19\ma_wbr_jpn_19_phase.questphase` / h0 / 48 -> 12 -> 20 |
| `13130c9dd4ee6035a364` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_19\ma_wbr_jpn_19_phase.questphase` / h50 / 12 -> 13 -> 1 |
| `189631309abfbdbf5486` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_19\ma_wbr_jpn_19_phase.questphase` / h50 / 11 -> 12 -> 13 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_19\ma_wbr_jpn_19_phase.questphase` / h0 / 0 -> 15 -> 48 |
| `204ca9b8b94427c1ef81` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_19\ma_wbr_jpn_19_phase.questphase` / h0 / 52 -> 49 -> 27 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_19\ma_wbr_jpn_19_phase.questphase` / h0 / 61 -> 60 -> 57 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_19\ma_wbr_jpn_19_phase.questphase` / h0 / 21 -> 61 -> 60 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_19\ma_wbr_jpn_19_phase.questphase` / h0 / 58 -> 57 -> 13 |
| `45ebbca5a69e9668631c` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_19\ma_wbr_jpn_19_phase.questphase` / h0 / 32 -> 35 -> 34 |
| `4a93fa18bd8c04cc0e0e` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_19\ma_wbr_jpn_19_phase.questphase` / h0 / 15 -> 48 -> 12 |
| `4b4a7657f49a6c8435c2` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_19\ma_wbr_jpn_19_phase.questphase` / h50 / 7 -> 2 -> 14 |
| `4d2899bd368a655696af` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_19\ma_wbr_jpn_19_phase.questphase` / h0 / 2 -> 44 -> 45 |
| `4e9e44d7ce1c1377e58e` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_19\ma_wbr_jpn_19_phase.questphase` / h0 / 17 -> 47 -> 52 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
