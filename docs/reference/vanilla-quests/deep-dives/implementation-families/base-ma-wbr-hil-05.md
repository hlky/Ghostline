# base-ma-wbr-hil-05

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_05\communities\ma_wbr_hil_05_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_05\ma_wbr_hil_05.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_05\ma_wbr_hil_05.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_05\ma_wbr_hil_05_phase.questphase |
| `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_05\ma_wbr_hil_05_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/westbrook/charter_hill/ma_wbr_hil_05/onscreens/ma_wbr_hil_05_onscreen_01`
- `points_of_interest/minor_activities/ma_wbr_hil_05`
- `quests/minor_activities/westbrook/charter_hill/ma_wbr_hil_05`
- `quests/minor_activities/westbrook/charter_hill/ma_wbr_hil_05/description`
- `quests/minor_activities/westbrook/charter_hill/ma_wbr_hil_05/ma_wbr_hil_05/go_to_spot`
- `quests/minor_activities/westbrook/charter_hill/ma_wbr_hil_05/ma_wbr_hil_05/loot`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 2 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 6 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questLogicalCondition,questTimeCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_05\ma_wbr_hil_05_phase.questphase` / h0 / 23 -> 80 -> 65 |
| `0781ef00ea04c05ee418` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_05\ma_wbr_hil_05_phase.questphase` / h0 / 36 -> 37 -> 87 |
| `0d59d5b737ce1451c32f` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_05\ma_wbr_hil_05_phase.questphase` / h0 / 88 -> 85 -> 84 |
| `101cdd639eee553d361c` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_05\ma_wbr_hil_05_phase.questphase` / h0 / 83 -> 73 -> 34 |
| `12208b60f11caf6d936e` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_05\ma_wbr_hil_05_phase.questphase` / h0 / 79 -> 82 -> 68 |
| `138cff49923a75e07348` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_05\ma_wbr_hil_05_phase.questphase` / h0 / 34 -> 35 -> 36 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_05\ma_wbr_hil_05_phase.questphase` / h0 / 2 -> 23 -> 80 |
| `1d48bd7cbbaeca8257d2` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_05\ma_wbr_hil_05_phase.questphase` / h0 / 39 -> 40 -> 53 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_05\ma_wbr_hil_05_phase.questphase` / h0 / 23 -> 80 -> 51 |
| `2af1b9066204f282e3a4` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_05\ma_wbr_hil_05_phase.questphase` / h45 / 17 -> 16 -> 2 |
| `2bbf5528ada3f00dc747` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_05\ma_wbr_hil_05_phase.questphase` / h45 / 0 -> 9 -> 17 |
| `2bc4ec2388d837bacb1a` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_05\ma_wbr_hil_05_phase.questphase` / h0 / 30 -> 4 -> 5 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_05\ma_wbr_hil_05_phase.questphase` / h0 / 87 -> 86 -> 84 |
| `3575eb74602f5e5f696d` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_05\ma_wbr_hil_05_phase.questphase` / h0 / 73 -> 34 -> 35 |
| `45384fad45d3768a409d` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_05\ma_wbr_hil_05_phase.questphase` / h0 / 85 -> 84 -> 39 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_05\ma_wbr_hil_05_phase.questphase` / h0 / 80 -> 65 -> 51 |
| `4c4ed316b40e2958b53f` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_05\ma_wbr_hil_05_phase.questphase` / h0 / 0 -> 1 -> 71 |
| `4d6c55ba26916a1e04f1` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_05\ma_wbr_hil_05_phase.questphase` / h0 / 68 -> 81 -> 3 |
| `4e9253a72e6b0134b8dd` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_05\ma_wbr_hil_05_phase.questphase` / h0 / 35 -> 36 -> 37 |
| `51570397b2f761f6ba4f` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_05\ma_wbr_hil_05_phase.questphase` / h0 / 80 -> 51 -> 55 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
