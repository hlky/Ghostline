# base-ma-wbr-jpn-06

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_06\community\ma_wbr_jpn_06_civs_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_06\community\ma_wbr_jpn_06_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_06\ma_wbr_jpn_06.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_06\ma_wbr_jpn_06.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_06\ma_wbr_jpn_06_phase.questphase |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_06\ma_wbr_jpn_06_phase.questphase` | content candidate | 4 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/westbrook/japantown/ma_wbr_jpn_06/shards/ma_wbr_jpn_06`
- `points_of_interest/minor_activities/ma_wbr_jpn_06`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 4 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 7 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 4 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 4 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questLogicalCondition,questTimeCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 4 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 3 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 13 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 4 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `42d456f68cbe3d8345c3` | 3 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_06\ma_wbr_jpn_06_phase.questphase` / h294 / 2 -> 5 -> 3 |
| `7b44344c01ad5161d3ff` | 3 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_06\ma_wbr_jpn_06_phase.questphase` / h294 / 7 -> 2 -> 5 |
| `987122e5e2fcd167cf6c` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_06\ma_wbr_jpn_06_phase.questphase` / h0 / 16 -> 0 -> 1 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_06\ma_wbr_jpn_06_phase.questphase` / h0 / 68 -> 65 -> 64 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_06\ma_wbr_jpn_06_phase.questphase` / h0 / 12 -> 40 -> 23 |
| `0985fc78e580f2f10e14` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_06\ma_wbr_jpn_06_phase.questphase` / h419 / 20 -> 10 -> 9 |
| `131575528d721251d6a7` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_06\ma_wbr_jpn_06_phase.questphase` / h0 / 16 -> 7 -> 61 |
| `13b3a103bfd4aa1ae513` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_06\ma_wbr_jpn_06_phase.questphase` / h35 / 19 -> 17 -> 22 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_06\ma_wbr_jpn_06_phase.questphase` / h0 / 16 -> 12 -> 40 |
| `204ca9b8b94427c1ef81` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_06\ma_wbr_jpn_06_phase.questphase` / h0 / 60 -> 41 -> 24 |
| `20a77143a898bc753a26` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_06\ma_wbr_jpn_06_phase.questphase` / h35 / 22 -> 23 -> 24 |
| `20e74db83226e46cc202` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_06\ma_wbr_jpn_06_phase.questphase` / h0 / 35 -> 37 -> 34 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_06\ma_wbr_jpn_06_phase.questphase` / h0 / 12 -> 40 -> 19 |
| `257c11bf7c2b1481f8fd` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_06\ma_wbr_jpn_06_phase.questphase` / h35 / 2 -> 7 -> 13 |
| `2cc4f20e16798419f013` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_06\ma_wbr_jpn_06_phase.questphase` / h0 / 20 -> 9 -> 68 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_06\ma_wbr_jpn_06_phase.questphase` / h0 / 68 -> 67 -> 64 |
| `31b17ef6575c70e697eb` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_06\ma_wbr_jpn_06_phase.questphase` / h35 / 17 -> 22 -> 23 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_06\ma_wbr_jpn_06_phase.questphase` / h0 / 65 -> 64 -> 10 |
| `3631db38b0b093f683ed` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_06\ma_wbr_jpn_06_phase.questphase` / h0 / 36 -> 37 -> 32 |
| `390f62c11ddf01069a3f` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_06\ma_wbr_jpn_06_phase.questphase` / h0 / 16 -> 25 -> 62 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
