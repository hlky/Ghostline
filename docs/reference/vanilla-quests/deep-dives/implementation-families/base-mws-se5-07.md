# base-mws-se5-07

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\community\mws_se5_07_gang.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase; base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07_chicken_test.scene |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` | content candidate | 1 / 0 | base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07.scene; base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07_camp.scene |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07.scene` | content candidate | 0 / 10 |  |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07_camp.scene` | content candidate | 0 / 10 |  |
| `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07_chicken_test.scene` | test/debug | 0 / 16 |  |

## Journal paths observed in these resources

- `codex/glossary/vehicles/porsche_turbo_911_cabrio`
- `contacts/muamar_el_capitan_reyes/car_dealership/porsche_911_cabrio_hook`
- `contacts/muamar_el_capitan_reyes/car_dealership/porsche_911_cabrio_message1_response_a/porsche_911_cabrio_message1_response_a`
- `contacts/muamar_el_capitan_reyes/car_dealership/porsche_911_cabrio_message1_response_a/porsche_911_cabrio_message1_response_b`
- `contacts/muamar_el_capitan_reyes/mws_se5_07/porsche_911_cabrio_message1`
- `contacts/muamar_el_capitan_reyes/mws_se5_07/porsche_911_cabrio_message1_response_a`
- `contacts/muamar_el_capitan_reyes/mws_se5_07/porsche_911_cabrio_message1_response_a/porsche_911_cabrio_message1_response_a`
- `contacts/muamar_el_capitan_reyes/mws_se5_07/porsche_911_cabrio_message1_response_a/porsche_911_cabrio_message1_response_b`
- `contacts/muamar_el_capitan_reyes/mws_se5_07/porsche_911_cabrio_message2`
- `contacts/muamar_el_capitan_reyes/mws_se5_07/porsche_911_cabrio_message3`
- `contacts/muamar_el_capitan_reyes/mws_se5_07/porsche_911_cabrio_message3_job_done`
- `contacts/muamar_el_capitan_reyes/mws_se5_07/porsche_911_cabrio_message3_job_done/job_done`
- `contacts/muamar_el_capitan_reyes/mws_se5_07/porsche_911_cabrio_message3_response`
- `contacts/muamar_el_capitan_reyes/mws_se5_07/porsche_911_cabrio_message3_response/porsche_911_cabrio_message3_response_a`
- `contacts/muamar_el_capitan_reyes/mws_se5_07/porsche_911_cabrio_message3_response/porsche_911_cabrio_message3_response_b`
- `contacts/muamar_el_capitan_reyes/mws_se5_07/porsche_911_cabrio_message4`
- `onscreens/emails/quests/minor_activities/badlands/se5/mws_se5_07/shards1/gps`
- `quests/minor_quest/mws_se5_07`
- `quests/minor_quest/mws_se5_07/description`
- `quests/minor_quest/mws_se5_07/mws_se5_07/corpse`
- `quests/minor_quest/mws_se5_07/mws_se5_07/corpse1`
- `quests/minor_quest/mws_se5_07/mws_se5_07a/objective`
- `quests/minor_quest/mws_se5_07/mws_se5_07c/objective`
- `quests/minor_quest/mws_se5_07/mws_se5_07c/objective1`
- `quests/minor_quest/mws_se5_07/mws_se5_07c/objective2`
- `quests/minor_quest/mws_se5_07/mws_se5_07c/objective3`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questCutControlNodeDefinition` | 3 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 8 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 8 |
| `questInputNodeDefinition` | 2 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 2 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 33 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questInventory_ConditionType,questJournalCondition,questJournalEntryVisited_ConditionType,questLogicalCondition,questObjectCondition,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance,questVehicleCondition,questVehicleDestruction_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questInventory_ConditionType,questLogicalCondition,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questGameTimeDelay_ConditionType,questLogicalCondition,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questGameTimeDelay_ConditionType,questLogicalCondition,questObjectDistance,questTimeCondition,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questJournalCondition,questJournalEntryVisited_ConditionType,questLogicalCondition,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questTimeCondition,questTimePeriod_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 9 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 4 |
| `questPhaseNodeDefinition` | 1 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 3 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 4 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType,questSpawner_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 3 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 5 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 4 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 2 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 5 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 2 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 2 |
| `questVehicleNodeDefinition[questEnablePlayerVehicle_NodeType]` | 2 |
| `questVehicleNodeDefinition[questSpawnPlayerVehicle_NodeType,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 7 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnEndNode[scnNodeId]` | 4 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 5 |
| `scnStartNode[scnNodeId]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `9353bff92035396e0fc6` | 5 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 12 -> 97 -> 156 |
| `b54739889d4d9a0745d2` | 5 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 106 -> 107 -> 191 |
| `3e6f03030764fcc75954` | 4 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 107 -> 191 -> 180 |
| `5c5e9486af30e2f834ec` | 3 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 31 -> 50 -> 52 |
| `7e7dbbc930b3717fd790` | 3 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 179 -> 106 -> 107 |
| `138cff49923a75e07348` | 2 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 29 -> 50 -> 52 |
| `30d34adedee6f73fb995` | 2 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 11 -> 13 -> 14 |
| `4355c750bffd48a2a3be` | 2 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 148 -> 48 -> 26 |
| `4e9253a72e6b0134b8dd` | 2 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 50 -> 52 -> 53 |
| `6e29597821655a1718b1` | 2 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07_chicken_test.scene` / scene / 35 -> 22 -> 2 |
| `764330de4badaff6be27` | 2 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 146 -> 148 -> 48 |
| `77690ca882ef81d7aaab` | 2 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07.scene` / scene / 50 -> 6 -> 44 |
| `956a18e11770fe167253` | 2 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 146 -> 148 -> 50 |
| `9791d641ee7ee2d5b2e7` | 2 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\scenes\mws_se5_07.scene` / scene / 50 -> 6 -> 8 |
| `a0f78d5365726d8a66f2` | 2 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 48 -> 26 -> 141 |
| `a53561b4c002bc02b58a` | 2 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 27 -> 29 -> 50 |
| `a5f6ff0df46f7043f2b5` | 2 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 76 -> 134 -> 207 |
| `b4d4aca04dc8f419d68d` | 2 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 142 -> 143 -> 144 |
| `b7a66bd86175315617dd` | 2 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 10 -> 11 -> 13 |
| `b7e863bd58c0072f3308` | 2 | `base\open_world\mini_world_stories\badlands\se5\mws_se5_07\mws_se5_07.questphase` / h0 / 149 -> 150 -> 151 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
