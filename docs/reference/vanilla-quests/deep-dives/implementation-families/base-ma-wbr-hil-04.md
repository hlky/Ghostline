# base-ma-wbr-hil-04

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\community\ma_wbr_hil_04_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04_phase.questphase |
| `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04_phase.questphase` | content candidate | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/westbrook/charter_hill/ma_wbr_hil_04/onscreens/ma_wbr_hil_04_onscreen_03`
- `points_of_interest/minor_activities/ma_wbr_hil_04`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 3 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 7 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 3 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questLogicalCondition,questTimeCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 4 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 6 |
| `questPhaseNodeDefinition` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 5 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 4 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 6 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `495cb7d9f15a7bc3a11b` | 4 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04_phase.questphase` / h252 / 4 -> 5 -> 3 |
| `0bef3d9d4a4adf2da8cd` | 3 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04_phase.questphase` / h252 / 4 -> 5 -> 11 |
| `6bade9a6171d604fd6d8` | 3 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04_phase.questphase` / h252 / 5 -> 3 -> 11 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04_phase.questphase` / h0 / 32 -> 61 -> 53 |
| `1704e95bd0b374c0e216` | 2 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04_phase.questphase` / h252 / 0 -> 4 -> 7 |
| `2be2aaaa8bc7f9d40730` | 2 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04_phase.questphase` / h252 / 0 -> 18 -> 6 |
| `42d456f68cbe3d8345c3` | 2 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04_phase.questphase` / h252 / 3 -> 11 -> 12 |
| `56c53a847765e20a971f` | 2 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04_phase.questphase` / h252 / 5 -> 11 -> 12 |
| `79f4dddf5c52f6df598a` | 2 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04_phase.questphase` / h0 / 35 -> 44 -> 45 |
| `bfe95df47bd1ca67330f` | 2 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04_phase.questphase` / h0 / 56 -> 57 -> 59 |
| `cf969908af6cc30ed0df` | 2 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04_phase.questphase` / h252 / 2 -> 3 -> 11 |
| `063c0e3538b36ad0971b` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04_phase.questphase` / h252 / 0 -> 2 -> 13 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04_phase.questphase` / h0 / 86 -> 83 -> 82 |
| `0985fc78e580f2f10e14` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04_phase.questphase` / h0 / 6 -> 73 -> 72 |
| `0f91d4d5aa591426add8` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04_phase.questphase` / h0 / 50 -> 3 -> 5 |
| `12208b60f11caf6d936e` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04_phase.questphase` / h0 / 60 -> 71 -> 55 |
| `197d8d3a3df546beea12` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04_phase.questphase` / h48 / 3 -> 5 -> 6 |
| `1f22b00cd5f6b14c601a` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04_phase.questphase` / h252 / 10 -> 18 -> 6 |
| `1ffca1efb50bb622e133` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04_phase.questphase` / h0 / 34 -> 36 -> 37 |
| `251a64d2bd43eb1ef02f` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04_phase.questphase` / h0 / 48 -> 0 -> 58 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
