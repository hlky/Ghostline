# base-ma-pac-cvi-10

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\community\ma_pac_cvi_10_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\community\ma_pac_cvi_10_drone_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\ma_pac_cvi_10.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\ma_pac_cvi_10.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\ma_pac_cvi_10_phase.questphase |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\ma_pac_cvi_10_bugfixing.questphase` | repair | 3 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\ma_pac_cvi_10_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/pacifica/coastview/ma_pac_cvi_10/onscreens/ma_pac_cvi_10`
- `onscreens/emails/quests/minor_activities/pacifica/coastview/ma_pac_cvi_10/onscreens/ma_pac_cvi_10_b`
- `points_of_interest/minor_activities/ma_pac_cvi_10`
- `quests/minor_activities/pacifica/coastview/ma_pac_cvi_10`
- `quests/minor_activities/pacifica/coastview/ma_pac_cvi_10/description`
- `quests/minor_activities/pacifica/coastview/ma_pac_cvi_10/ma_pac_cvi_10/go_to_spot`
- `quests/minor_activities/pacifica/coastview/ma_pac_cvi_10/ma_pac_cvi_10/loot`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 4 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 5 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 10 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 9 |
| `questInputNodeDefinition` | 6 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 6 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 2 |
| `questOutputNodeDefinition` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 4 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 5 |
| `questPhaseNodeDefinition` | 4 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 5 |
| `questStartNodeDefinition` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `fa0334f4ccd47150ee96` | 3 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\ma_pac_cvi_10_bugfixing.questphase` / h73 / 8 -> 12 -> 11 |
| `237687944a84dd96b7b5` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\ma_pac_cvi_10_bugfixing.questphase` / h7 / 0 -> 2 -> 3 |
| `05741704b94ee3af2e8c` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\ma_pac_cvi_10_phase.questphase` / h0 / 83 -> 90 -> 84 |
| `0781ef00ea04c05ee418` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\ma_pac_cvi_10_phase.questphase` / h0 / 49 -> 50 -> 118 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\ma_pac_cvi_10_phase.questphase` / h0 / 118 -> 115 -> 114 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\ma_pac_cvi_10_phase.questphase` / h0 / 79 -> 102 -> 80 |
| `08fb7fe6e6763ea8028e` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\ma_pac_cvi_10_bugfixing.questphase` / h73 / 3 -> 4 -> 10 |
| `09d5b307996c34df9907` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\ma_pac_cvi_10_phase.questphase` / h0 / 56 -> 108 -> 104 |
| `0a7b874d042b698fee86` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\ma_pac_cvi_10_bugfixing.questphase` / h7 / 7 -> 10 -> 6 |
| `138cff49923a75e07348` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\ma_pac_cvi_10_phase.questphase` / h0 / 47 -> 48 -> 49 |
| `159599f19533cfcfe918` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\ma_pac_cvi_10_phase.questphase` / h0 / 111 -> 55 -> 62 |
| `1972a0532f20a107c8bb` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\ma_pac_cvi_10_phase.questphase` / h0 / 98 -> 99 -> 100 |
| `1d48bd7cbbaeca8257d2` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\ma_pac_cvi_10_phase.questphase` / h0 / 53 -> 54 -> 65 |
| `2aa0f3a3b004f071652f` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\ma_pac_cvi_10_phase.questphase` / h134 / 6 -> 7 -> 1 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\ma_pac_cvi_10_phase.questphase` / h0 / 118 -> 117 -> 114 |
| `2ea6dc8eef48b1cfc585` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\ma_pac_cvi_10_phase.questphase` / h0 / 101 -> 78 -> 77 |
| `34258c330674aba088d3` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\ma_pac_cvi_10_phase.questphase` / h0 / 22 -> 81 -> 44 |
| `37309720032dc96c0dd4` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\ma_pac_cvi_10_bugfixing.questphase` / h73 / 9 -> 8 -> 12 |
| `4050a1424e83b44096ff` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\ma_pac_cvi_10_phase.questphase` / h0 / 77 -> 112 -> 110 |
| `4365e94e7169e2520841` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_10\ma_pac_cvi_10_phase.questphase` / h0 / 115 -> 114 -> 1 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
