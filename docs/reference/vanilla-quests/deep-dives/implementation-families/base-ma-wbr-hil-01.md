# base-ma-wbr-hil-01

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\community\ma_wbr_hil_01.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.questphase |
| `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.questphase` | content candidate | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/westbrook/charter_hill/ma_wbr_hil_01/onscreens/ma_wbr_hil_01_onscreen_01`
- `points_of_interest/minor_activities/ma_wbr_hil_01`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 6 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 8 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 3 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalHubNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 4 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questLogicalCondition,questTimeCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 4 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 6 |
| `questPhaseNodeDefinition` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 11 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 4 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 6 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2c20201f171f754c99e0` | 4 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.questphase` / h0 / 53 -> 48 -> 49 |
| `3ba86c71a70bfb0620a5` | 4 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.questphase` / h0 / 52 -> 53 -> 48 |
| `484f47d527266442c50f` | 4 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.questphase` / h0 / 56 -> 54 -> 72 |
| `495cb7d9f15a7bc3a11b` | 4 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.questphase` / h239 / 4 -> 5 -> 3 |
| `5466f936f30ed8ee354a` | 4 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.questphase` / h0 / 57 -> 52 -> 53 |
| `7373ce40c215f78fb39e` | 4 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.questphase` / h0 / 52 -> 53 -> 45 |
| `c7b377e841e63de88f17` | 4 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.questphase` / h0 / 56 -> 54 -> 68 |
| `ea9fbda4728c2a1fcedc` | 4 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.questphase` / h0 / 4 -> 56 -> 54 |
| `0bef3d9d4a4adf2da8cd` | 3 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.questphase` / h239 / 4 -> 5 -> 11 |
| `543b598a1b2fb7423e72` | 3 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.questphase` / h0 / 45 -> 48 -> 49 |
| `6bade9a6171d604fd6d8` | 3 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.questphase` / h239 / 5 -> 3 -> 11 |
| `88f5ed16b4aedf0ce68b` | 3 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.questphase` / h0 / 53 -> 45 -> 50 |
| `8cf6277488916d3b7ab5` | 3 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.questphase` / h0 / 57 -> 45 -> 50 |
| `8edf5416ccd8dce9db72` | 3 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.questphase` / h0 / 57 -> 45 -> 48 |
| `cadb89472ec2335d17b1` | 3 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.questphase` / h0 / 53 -> 45 -> 48 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.questphase` / h0 / 8 -> 43 -> 29 |
| `1704e95bd0b374c0e216` | 2 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.questphase` / h239 / 0 -> 4 -> 7 |
| `2be2aaaa8bc7f9d40730` | 2 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.questphase` / h239 / 0 -> 18 -> 6 |
| `42d456f68cbe3d8345c3` | 2 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.questphase` / h239 / 3 -> 11 -> 12 |
| `56c53a847765e20a971f` | 2 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.questphase` / h239 / 5 -> 11 -> 12 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
