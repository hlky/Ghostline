# ep1-ma-prototypes

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\minor_activities\ma_prototypes\courier\ep1_courier_minor_activity_test.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\minor_activities\ma_prototypes\courier\ep1_courier_minor_activity_test.quest` | content candidate | 1 / 0 | ep1\openworld\minor_activities\ma_prototypes\courier\ep1_courier_minor_activity_test.questphase |
| `ep1\openworld\minor_activities\ma_prototypes\courier\ep1_courier_minor_activity_test.questphase` | content candidate | 1 / 0 |  |
| `ep1\openworld\minor_activities\ma_prototypes\courier\ep1_courier_minor_activity_test_damage_obstacles_com.community` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `contacts/mr_hands/mr_hands_global_msg/sts_warning_fail_001`
- `ep1/quests/minor_activities/courier_test/courier_enemies/01_steal`
- `ep1/quests/minor_activities/courier_test/courier_enemies/04_leave`
- `ep1/quests/minor_activities/courier_test/courier_enemies/2_bring`
- `ep1/quests/minor_activities/courier_test/courier_enemies/3_defeat`
- `ep1/quests/minor_activities/courier_test/courier_no_damage/01_steal`
- `ep1/quests/minor_activities/courier_test/courier_no_damage/02_bring`
- `ep1/quests/minor_activities/courier_test/courier_no_damage/03_leave`
- `ep1/quests/minor_activities/courier_test/courier_no_damage/no_damage`
- `ep1/quests/minor_activities/courier_test/courier_test/01_steal_vehicle`
- `ep1/quests/minor_activities/courier_test/courier_test/02_bring_to_destination`
- `ep1/quests/minor_activities/courier_test/courier_test/02_bring_to_destination/destination_mappin`
- `ep1/quests/minor_activities/courier_test/courier_test/02_bring_to_destination/waypoint_001`
- `ep1/quests/minor_activities/courier_test/courier_test/02_bring_to_destination/waypoint_002`
- `ep1/quests/minor_activities/courier_test/courier_test/02_bring_to_destination/waypoint_003`
- `ep1/quests/minor_activities/courier_test/courier_test/02_bring_to_destination/waypoint_004`
- `ep1/quests/minor_activities/courier_test/courier_test/02_bring_to_destination/waypoint_005`
- `ep1/quests/minor_activities/courier_test/courier_test/02_bring_to_destination/waypoint_006`
- `ep1/quests/minor_activities/courier_test/courier_test/02_bring_to_destination/waypoint_007`
- `ep1/quests/minor_activities/courier_test/courier_test/02_bring_to_destination/waypoint_008`
- `ep1/quests/minor_activities/courier_test/courier_test/02_bring_to_destination/waypoint_009`
- `ep1/quests/minor_activities/courier_test/courier_test/02_bring_to_destination/waypoint_010`
- `ep1/quests/minor_activities/courier_test/courier_test/02_bring_to_destination/waypoint_011`
- `ep1/quests/minor_activities/courier_test/courier_test/03_leav_in_the_garage`
- `ep1/quests/minor_activities/courier_test/courier_test/return`
- `ep1/quests/minor_activities/courier_test/courier_test/time`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCombatNodeDefinition[questCombatNodeParams_ShootAt]` | 2 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questCutControlNodeDefinition` | 3 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questInputNodeDefinition` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 38 |
| `questMappinManagerNodeDefinition` | 22 |
| `questMovePuppetNodeDefinition[questFollowParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 13 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 12 |
| `questPhaseNodeDefinition` | 1 |
| `questPhoneManagerNodeDefinition[questSendMessage_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 12 |
| `questStartNodeDefinition` | 1 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 2 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 3 |
| `questVehicleNodeDefinition[questStopVehicle_NodeType]` | 3 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `7068575ab5cd93557703` | 11 | `ep1\openworld\minor_activities\ma_prototypes\courier\ep1_courier_minor_activity_test.questphase` / h0 / 128 -> 141 -> 142 |
| `a53561b4c002bc02b58a` | 6 | `ep1\openworld\minor_activities\ma_prototypes\courier\ep1_courier_minor_activity_test.questphase` / h0 / 8 -> 11 -> 12 |
| `5111887e4ac7cd4f477f` | 4 | `ep1\openworld\minor_activities\ma_prototypes\courier\ep1_courier_minor_activity_test.questphase` / h0 / 21 -> 121 -> 122 |
| `79ff30ab7464b071eda5` | 4 | `ep1\openworld\minor_activities\ma_prototypes\courier\ep1_courier_minor_activity_test.questphase` / h0 / 98 -> 104 -> 105 |
| `0e147d9e68a4074ab8c6` | 3 | `ep1\openworld\minor_activities\ma_prototypes\courier\ep1_courier_minor_activity_test.questphase` / h0 / 33 -> 43 -> 83 |
| `138cff49923a75e07348` | 3 | `ep1\openworld\minor_activities\ma_prototypes\courier\ep1_courier_minor_activity_test.questphase` / h0 / 11 -> 12 -> 13 |
| `2f58adf3c7b612392871` | 3 | `ep1\openworld\minor_activities\ma_prototypes\courier\ep1_courier_minor_activity_test.questphase` / h0 / 5 -> 4 -> 28 |
| `874f244bd7a185c32851` | 3 | `ep1\openworld\minor_activities\ma_prototypes\courier\ep1_courier_minor_activity_test.questphase` / h0 / 9 -> 10 -> 17 |
| `0de4f0f3a61a46ff6cf2` | 2 | `ep1\openworld\minor_activities\ma_prototypes\courier\ep1_courier_minor_activity_test.questphase` / h0 / 44 -> 42 -> 115 |
| `21f5393e225c307d7082` | 2 | `ep1\openworld\minor_activities\ma_prototypes\courier\ep1_courier_minor_activity_test.questphase` / h0 / 59 -> 76 -> 77 |
| `2bec64b328d17e5e4e23` | 2 | `ep1\openworld\minor_activities\ma_prototypes\courier\ep1_courier_minor_activity_test.questphase` / h0 / 122 -> 23 -> 117 |
| `37b6e288b0b1e2537f5f` | 2 | `ep1\openworld\minor_activities\ma_prototypes\courier\ep1_courier_minor_activity_test.questphase` / h0 / 14 -> 2 -> 81 |
| `44defd9e9af08691e474` | 2 | `ep1\openworld\minor_activities\ma_prototypes\courier\ep1_courier_minor_activity_test.questphase` / h0 / 18 -> 117 -> 118 |
| `5668d482b8ec8c4e4a5a` | 2 | `ep1\openworld\minor_activities\ma_prototypes\courier\ep1_courier_minor_activity_test.questphase` / h0 / 18 -> 119 -> 120 |
| `70d2fc6c016be01c9c32` | 2 | `ep1\openworld\minor_activities\ma_prototypes\courier\ep1_courier_minor_activity_test.questphase` / h0 / 115 -> 51 -> 35 |
| `7e7dbbc930b3717fd790` | 2 | `ep1\openworld\minor_activities\ma_prototypes\courier\ep1_courier_minor_activity_test.questphase` / h0 / 4 -> 28 -> 88 |
| `a728f2402dc75a1596f9` | 2 | `ep1\openworld\minor_activities\ma_prototypes\courier\ep1_courier_minor_activity_test.questphase` / h0 / 6 -> 18 -> 117 |
| `ed8fd50367e82fde25bb` | 2 | `ep1\openworld\minor_activities\ma_prototypes\courier\ep1_courier_minor_activity_test.questphase` / h0 / 0 -> 14 -> 2 |
| `00dcd95c58bd6418a1dd` | 1 | `ep1\openworld\minor_activities\ma_prototypes\courier\ep1_courier_minor_activity_test.questphase` / h0 / 31 -> 82 -> 123 |
| `0f07fa9ad0fdb30edaaf` | 1 | `ep1\openworld\minor_activities\ma_prototypes\courier\ep1_courier_minor_activity_test.questphase` / h0 / 88 -> 128 -> 141 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
