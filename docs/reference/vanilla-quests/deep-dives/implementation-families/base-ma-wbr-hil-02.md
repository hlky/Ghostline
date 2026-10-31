# base-ma-wbr-hil-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\community\ma_wbr_hil_02_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02_phase.questphase |
| `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/westbrook/charter_hill/ma_wbr_hil_02/onscreens/ma_wbr_hil_02_onscreen_02`
- `points_of_interest/minor_activities/ma_wbr_hil_02`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 2 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questLogicalCondition,questTimeCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 2 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02_phase.questphase` / h0 / 32 -> 69 -> 62 |
| `79f4dddf5c52f6df598a` | 2 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02_phase.questphase` / h0 / 52 -> 59 -> 60 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02_phase.questphase` / h0 / 73 -> 77 -> 74 |
| `12208b60f11caf6d936e` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02_phase.questphase` / h0 / 68 -> 71 -> 64 |
| `178360ac35259ce804ee` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02_phase.questphase` / h0 / 1 -> 61 -> 35 |
| `1b89a735937e920c2637` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02_phase.questphase` / h14 / 6 -> 2 -> 8 |
| `1ffca1efb50bb622e133` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02_phase.questphase` / h0 / 34 -> 53 -> 54 |
| `2b1c798017b4cbce938c` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02_phase.questphase` / h14 / 11 -> 12 -> 1 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02_phase.questphase` / h0 / 73 -> 72 -> 74 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02_phase.questphase` / h0 / 77 -> 74 -> 34 |
| `3de51e6fe8bd91ef54c9` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02_phase.questphase` / h0 / 6 -> 55 -> 65 |
| `47702cacaf495c0f305d` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02_phase.questphase` / h14 / 15 -> 14 -> 6 |
| `4a93fa18bd8c04cc0e0e` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02_phase.questphase` / h0 / 32 -> 69 -> 33 |
| `4d6c55ba26916a1e04f1` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02_phase.questphase` / h0 / 64 -> 70 -> 2 |
| `5648e2e2624f112b60fd` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02_phase.questphase` / h0 / 55 -> 65 -> 66 |
| `660db7250eff17f0889d` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02_phase.questphase` / h0 / 53 -> 54 -> 59 |
| `6da75727e3bbd6d0eafd` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02_phase.questphase` / h14 / 8 -> 10 -> 11 |
| `6dd0626e07e5fefdbfd5` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02_phase.questphase` / h0 / 66 -> 67 -> 5 |
| `6ef20747166d5182d55e` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02_phase.questphase` / h0 / 66 -> 67 -> 28 |
| `704bdb5ad20f56d5e3d7` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02_phase.questphase` / h0 / 74 -> 34 -> 53 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
