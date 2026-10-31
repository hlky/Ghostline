# base-ma-wbr-hil-06

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_06\communities\ma_wbr_hil_06_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_06\ma_wbr_hil_06.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_06\ma_wbr_hil_06.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_06\ma_wbr_hil_06_phase.questphase |
| `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_06\ma_wbr_hil_06_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/westbrook/charter_hill/ma_wbr_hil_06/onscreens/ma_wbr_hil_06_onscreen_01`
- `points_of_interest/minor_activities/ma_wbr_hil_06`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 2 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
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
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 6 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_06\ma_wbr_hil_06_phase.questphase` / h0 / 27 -> 48 -> 41 |
| `79f4dddf5c52f6df598a` | 2 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_06\ma_wbr_hil_06_phase.questphase` / h0 / 31 -> 36 -> 37 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_06\ma_wbr_hil_06_phase.questphase` / h0 / 61 -> 62 -> 58 |
| `114f40d1eb963a3eb753` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_06\ma_wbr_hil_06_phase.questphase` / h29 / 15 -> 13 -> 6 |
| `12208b60f11caf6d936e` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_06\ma_wbr_hil_06_phase.questphase` / h0 / 47 -> 50 -> 43 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_06\ma_wbr_hil_06_phase.questphase` / h0 / 0 -> 27 -> 48 |
| `1ffca1efb50bb622e133` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_06\ma_wbr_hil_06_phase.questphase` / h0 / 29 -> 32 -> 33 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_06\ma_wbr_hil_06_phase.questphase` / h0 / 27 -> 48 -> 40 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_06\ma_wbr_hil_06_phase.questphase` / h0 / 61 -> 60 -> 58 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_06\ma_wbr_hil_06_phase.questphase` / h0 / 62 -> 58 -> 29 |
| `43562a5823373c0258f8` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_06\ma_wbr_hil_06_phase.questphase` / h0 / 23 -> 45 -> 46 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_06\ma_wbr_hil_06_phase.questphase` / h0 / 48 -> 41 -> 40 |
| `4c4ed316b40e2958b53f` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_06\ma_wbr_hil_06_phase.questphase` / h0 / 30 -> 23 -> 45 |
| `4d6c55ba26916a1e04f1` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_06\ma_wbr_hil_06_phase.questphase` / h0 / 43 -> 49 -> 20 |
| `51570397b2f761f6ba4f` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_06\ma_wbr_hil_06_phase.questphase` / h0 / 48 -> 40 -> 34 |
| `598920ee48558917ab4e` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_06\ma_wbr_hil_06_phase.questphase` / h0 / 41 -> 40 -> 34 |
| `59da0294f1ac40648bea` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_06\ma_wbr_hil_06_phase.questphase` / h0 / 52 -> 53 -> 54 |
| `660db7250eff17f0889d` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_06\ma_wbr_hil_06_phase.questphase` / h0 / 32 -> 33 -> 36 |
| `6dd0626e07e5fefdbfd5` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_06\ma_wbr_hil_06_phase.questphase` / h0 / 46 -> 21 -> 22 |
| `6ef20747166d5182d55e` | 1 | `base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_06\ma_wbr_hil_06_phase.questphase` / h0 / 46 -> 21 -> 24 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
