# base-ma-wbr-jpn-15

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_15\community\ma_wbr_jpn_15_civilians_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_15\community\ma_wbr_jpn_15_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_15\ma_wbr_jpn_15.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_15\ma_wbr_jpn_15.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_15\ma_wbr_jpn_15_phase.questphase |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_15\ma_wbr_jpn_15_phase.questphase` | content candidate | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/westbrook/japantown/ma_wbr_jpn_15/shards/ma_wbr_jpn_15`
- `points_of_interest/minor_activities/ma_wbr_jpn_15`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 12 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 4 |
| `questCutControlNodeDefinition` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 8 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 3 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterReaction_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 2 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 12 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `34078b1414fbd02571bc` | 36 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_15\ma_wbr_jpn_15_phase.questphase` / h0 / 76 -> 77 -> 95 |
| `43cf485fc04a1247428e` | 6 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_15\ma_wbr_jpn_15_phase.questphase` / h0 / 2 -> 75 -> 76 |
| `a5b0274d8a2b7c5b6fe3` | 6 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_15\ma_wbr_jpn_15_phase.questphase` / h0 / 75 -> 76 -> 77 |
| `8d10896873df5c62014e` | 3 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_15\ma_wbr_jpn_15_phase.questphase` / h0 / 0 -> 1 -> 15 |
| `5466f936f30ed8ee354a` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_15\ma_wbr_jpn_15_phase.questphase` / h0 / 1 -> 66 -> 67 |
| `58c7e757cd8df0c755d4` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_15\ma_wbr_jpn_15_phase.questphase` / h0 / 66 -> 67 -> 53 |
| `987122e5e2fcd167cf6c` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_15\ma_wbr_jpn_15_phase.questphase` / h0 / 2 -> 0 -> 1 |
| `04d78f5a272f905e31eb` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_15\ma_wbr_jpn_15_phase.questphase` / h0 / 26 -> 101 -> 102 |
| `05368f97c1887d1ef26f` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_15\ma_wbr_jpn_15_phase.questphase` / h0 / 102 -> 105 -> 107 |
| `06e3382349ceff89de6f` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_15\ma_wbr_jpn_15_phase.questphase` / h0 / 15 -> 4 -> 60 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_15\ma_wbr_jpn_15_phase.questphase` / h0 / 122 -> 119 -> 118 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_15\ma_wbr_jpn_15_phase.questphase` / h0 / 31 -> 73 -> 46 |
| `0985fc78e580f2f10e14` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_15\ma_wbr_jpn_15_phase.questphase` / h476 / 76 -> 10 -> 9 |
| `0e0b0ec1add4154b2d49` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_15\ma_wbr_jpn_15_phase.questphase` / h50 / 16 -> 17 -> 11 |
| `10404eeeedb7a70b4598` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_15\ma_wbr_jpn_15_phase.questphase` / h50 / 2 -> 8 -> 5 |
| `1198407e25fb6cae0240` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_15\ma_wbr_jpn_15_phase.questphase` / h0 / 119 -> 118 -> 5 |
| `19a65852eae5fe9769e8` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_15\ma_wbr_jpn_15_phase.questphase` / h50 / 3 -> 2 -> 8 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_15\ma_wbr_jpn_15_phase.questphase` / h0 / 2 -> 31 -> 73 |
| `204ca9b8b94427c1ef81` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_15\ma_wbr_jpn_15_phase.questphase` / h0 / 115 -> 74 -> 47 |
| `23c83f846beb25d06b1d` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_15\ma_wbr_jpn_15_phase.questphase` / h0 / 1 -> 65 -> 67 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
