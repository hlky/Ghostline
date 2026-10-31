# base-ma-wbr-jpn-08

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_08\community\ma_wbr_jpn_08_civs_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_08\community\ma_wbr_jpn_08_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_08\ma_wbr_jpn_08.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_08\ma_wbr_jpn_08.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_08\ma_wbr_jpn_08_phase.questphase |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_08\ma_wbr_jpn_08_phase.questphase` | content candidate | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/westbrook/japantown/ma_wbr_jpn_08/shards/ma_wbr_jpn_08`
- `points_of_interest/minor_activities/ma_wbr_jpn_08`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 7 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 3 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterReaction_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 2 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 11 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `12b102391853a0e26cba` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_08\ma_wbr_jpn_08_phase.questphase` / h41 / 6 -> 7 -> 11 |
| `4a1ea25221f47a7c1e8c` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_08\ma_wbr_jpn_08_phase.questphase` / h0 / 52 -> 41 -> 35 |
| `51d78876d4b7cc3025b7` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_08\ma_wbr_jpn_08_phase.questphase` / h0 / 5 -> 3 -> 40 |
| `987122e5e2fcd167cf6c` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_08\ma_wbr_jpn_08_phase.questphase` / h0 / 1 -> 0 -> 5 |
| `00c3ca0ac0b55db639ca` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_08\ma_wbr_jpn_08_phase.questphase` / h41 / 5 -> 9 -> 6 |
| `03ee75d431e872139e2e` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_08\ma_wbr_jpn_08_phase.questphase` / h41 / 26 -> 23 -> 24 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_08\ma_wbr_jpn_08_phase.questphase` / h0 / 78 -> 82 -> 64 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_08\ma_wbr_jpn_08_phase.questphase` / h0 / 30 -> 52 -> 41 |
| `0985fc78e580f2f10e14` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_08\ma_wbr_jpn_08_phase.questphase` / h339 / 56 -> 10 -> 9 |
| `1147edd5e6b4ca5fc8a1` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_08\ma_wbr_jpn_08_phase.questphase` / h41 / 24 -> 20 -> 21 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_08\ma_wbr_jpn_08_phase.questphase` / h41 / 33 -> 5 -> 9 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_08\ma_wbr_jpn_08_phase.questphase` / h0 / 1 -> 30 -> 52 |
| `20e74db83226e46cc202` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_08\ma_wbr_jpn_08_phase.questphase` / h0 / 48 -> 50 -> 47 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_08\ma_wbr_jpn_08_phase.questphase` / h0 / 30 -> 52 -> 35 |
| `257c11bf7c2b1481f8fd` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_08\ma_wbr_jpn_08_phase.questphase` / h41 / 11 -> 23 -> 24 |
| `2cc4f20e16798419f013` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_08\ma_wbr_jpn_08_phase.questphase` / h0 / 36 -> 27 -> 78 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_08\ma_wbr_jpn_08_phase.questphase` / h0 / 78 -> 77 -> 64 |
| `32ad69d9a9b4b54f12c3` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_08\ma_wbr_jpn_08_phase.questphase` / h41 / 21 -> 25 -> 3 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_08\ma_wbr_jpn_08_phase.questphase` / h0 / 82 -> 64 -> 28 |
| `3631db38b0b093f683ed` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_08\ma_wbr_jpn_08_phase.questphase` / h0 / 49 -> 50 -> 45 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
