# base-ma-wbr-hil-03

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\community\ma_wbr_hil_03_community.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03_phase.questphase |
| `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/westbrook/charter_hill/ma_wbr_hil_03/onscreens/ma_wbr_hil_03_onscreen_01`
- `points_of_interest/minor_activities/ma_wbr_hil_03`

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
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questLogicalCondition,questTimeCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 2 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 5 |
| `questStartNodeDefinition` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 6 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03_phase.questphase` / h0 / 21 -> 52 -> 45 |
| `79f4dddf5c52f6df598a` | 2 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03_phase.questphase` / h0 / 27 -> 32 -> 35 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03_phase.questphase` / h0 / 59 -> 56 -> 55 |
| `0f91d4d5aa591426add8` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03_phase.questphase` / h0 / 34 -> 3 -> 5 |
| `12208b60f11caf6d936e` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03_phase.questphase` / h0 / 51 -> 54 -> 47 |
| `197d8d3a3df546beea12` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03_phase.questphase` / h44 / 3 -> 5 -> 6 |
| `1ffca1efb50bb622e133` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03_phase.questphase` / h0 / 23 -> 28 -> 29 |
| `20a77143a898bc753a26` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03_phase.questphase` / h0 / 41 -> 0 -> 39 |
| `24c2709a06ce310ae2d1` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03_phase.questphase` / h44 / 7 -> 8 -> 13 |
| `25aae51001db85d5b1fb` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03_phase.questphase` / h44 / 6 -> 7 -> 8 |
| `27c531f102f7b09ac9df` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03_phase.questphase` / h0 / 48 -> 49 -> 34 |
| `2af1b9066204f282e3a4` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03_phase.questphase` / h44 / 18 -> 17 -> 3 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03_phase.questphase` / h0 / 59 -> 58 -> 55 |
| `2e1ee5a1324dbeeb9071` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03_phase.questphase` / h0 / 0 -> 39 -> 1 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03_phase.questphase` / h0 / 56 -> 55 -> 23 |
| `43562a5823373c0258f8` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03_phase.questphase` / h0 / 1 -> 50 -> 48 |
| `4a91c91d8b9eed8c99ce` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03_phase.questphase` / h0 / 33 -> 24 -> 31 |
| `4a93fa18bd8c04cc0e0e` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03_phase.questphase` / h0 / 21 -> 52 -> 22 |
| `4c4ed316b40e2958b53f` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03_phase.questphase` / h0 / 39 -> 1 -> 50 |
| `4d6c55ba26916a1e04f1` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03_phase.questphase` / h0 / 47 -> 53 -> 30 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
