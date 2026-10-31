# base-ma-wbr-jpn-01

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_01\community\ma_wbr_jpn_01_civs_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_01\community\ma_wbr_jpn_01_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_01\ma_wbr_jpn_01.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_01\ma_wbr_jpn_01.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_01\ma_wbr_jpn_01_phase.questphase |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_01\ma_wbr_jpn_01_phase.questphase` | content candidate | 4 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/westbrook/japantown/ma_wbr_jpn_01/shards/ma_wbr_jpn_01`
- `points_of_interest/minor_activities/ma_wbr_jpn_01`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 3 |
| `questCutControlNodeDefinition` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 7 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 4 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 4 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 3 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 2 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 12 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `987122e5e2fcd167cf6c` | 3 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_01\ma_wbr_jpn_01_phase.questphase` / h0 / 2 -> 0 -> 1 |
| `18be198845c90c6bb3c8` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_01\ma_wbr_jpn_01_phase.questphase` / h46 / 16 -> 7 -> 2 |
| `5a1e5eb45e2acdebe80e` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_01\ma_wbr_jpn_01_phase.questphase` / h0 / 35 -> 37 -> 40 |
| `8d10896873df5c62014e` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_01\ma_wbr_jpn_01_phase.questphase` / h0 / 0 -> 1 -> 4 |
| `01775a1d01791d2b842b` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_01\ma_wbr_jpn_01_phase.questphase` / h46 / 9 -> 8 -> 1 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_01\ma_wbr_jpn_01_phase.questphase` / h0 / 74 -> 76 -> 75 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_01\ma_wbr_jpn_01_phase.questphase` / h0 / 11 -> 44 -> 32 |
| `09342269699c12a2e008` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_01\ma_wbr_jpn_01_phase.questphase` / h0 / 4 -> 15 -> 20 |
| `0985fc78e580f2f10e14` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_01\ma_wbr_jpn_01_phase.questphase` / h406 / 2 -> 10 -> 9 |
| `0f660f7484731cdb671e` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_01\ma_wbr_jpn_01_phase.questphase` / h0 / 44 -> 8 -> 21 |
| `1147edd5e6b4ca5fc8a1` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_01\ma_wbr_jpn_01_phase.questphase` / h126 / 7 -> 21 -> 10 |
| `16127f3f2f66b166e252` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_01\ma_wbr_jpn_01_phase.questphase` / h46 / 15 -> 8 -> 1 |
| `1b6f9e73ee4262299fe8` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_01\ma_wbr_jpn_01_phase.questphase` / h0 / 1 -> 4 -> 15 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_01\ma_wbr_jpn_01_phase.questphase` / h0 / 2 -> 11 -> 44 |
| `204ca9b8b94427c1ef81` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_01\ma_wbr_jpn_01_phase.questphase` / h0 / 70 -> 45 -> 33 |
| `20e74db83226e46cc202` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_01\ma_wbr_jpn_01_phase.questphase` / h0 / 40 -> 42 -> 39 |
| `23c83f846beb25d06b1d` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_01\ma_wbr_jpn_01_phase.questphase` / h0 / 37 -> 40 -> 42 |
| `2b297fd0a98b850556ae` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_01\ma_wbr_jpn_01_phase.questphase` / h46 / 4 -> 8 -> 1 |
| `2c20201f171f754c99e0` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_01\ma_wbr_jpn_01_phase.questphase` / h0 / 63 -> 62 -> 49 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_01\ma_wbr_jpn_01_phase.questphase` / h0 / 74 -> 73 -> 75 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
