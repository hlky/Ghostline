# ep1-sa-ep1-110

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_110\sa_ep1_110.questphase` | content candidate | 2 / 0 | ep1\openworld\sandbox_activities\courier_spot\sa_ep1_109\scenes\sa_ep1_109_vehicle_enter.scene |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_110\sa_ep1_110_combat_community.community` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `ep1/contacts/muamar/courier/sa_ep1_2`
- `ep1/contacts/muamar/courier/sa_ep1_hacking_introduction`
- `ep1/points_of_interest/sandbox_activities/sa_ep1_10`
- `ep1/quests/sandbox_activities/courier_test`
- `ep1/quests/sandbox_activities/courier_test/test`
- `ep1/quests/sandbox_activities/courier_test/test/after_hack_take_car`
- `ep1/quests/sandbox_activities/courier_test/test/chase_and_hack`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 6 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 14 |
| `questFlowControlNodeDefinition` | 2 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 9 |
| `questInputNodeDefinition` | 3 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 7 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 2 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questProximityProgressBar_ConditionType,questUICondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 7 |
| `questPhaseNodeDefinition` | 1 |
| `questPhoneManagerNodeDefinition[questSendMessage_NodeType]` | 2 |
| `questRandomizerNodeDefinition` | 1 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 9 |
| `questTimeManagerNodeDefinition[questShiftTime_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questProximityProgressBar_NodeType]` | 3 |
| `questUIManagerNodeDefinition[questSetHUDEntryForcedVisibility_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questShowOnscreen_NodeType]` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 3 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 7 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 4 |
| `questVehicleNodeDefinition[questStopVehicle_NodeType]` | 1 |
| `questVehicleNodeDefinition[questTeleportPuppetParams,questTeleport_NodeType,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 10 |
| `questVehicleNodeDefinition[questToggleForceBrake_NodeType]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `46f6e677d95f49d38652` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_110\sa_ep1_110.questphase` / h12 / 221 -> 222 -> 223 |
| `9af8a87f20a910659fa8` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_110\sa_ep1_110.questphase` / h0 / 25 -> 23 -> 8 |
| `beb0324add70d3ab4316` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_110\sa_ep1_110.questphase` / h12 / 137 -> 157 -> 174 |
| `fb8bb9c8f7b20bef3e3d` | 3 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_110\sa_ep1_110.questphase` / h12 / 236 -> 133 -> 233 |
| `2e1ee5a1324dbeeb9071` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_110\sa_ep1_110.questphase` / h12 / 135 -> 134 -> 162 |
| `35fc9c9ed3035dd850a8` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_110\sa_ep1_110.questphase` / h12 / 169 -> 171 -> 166 |
| `3fecf5d780775a6f2a61` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_110\sa_ep1_110.questphase` / h12 / 138 -> 137 -> 139 |
| `7881fbadf67ef1ff5c0d` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_110\sa_ep1_110.questphase` / h0 / 6 -> 12 -> 1 |
| `7c7062e6c1de3aafaf9d` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_110\sa_ep1_110.questphase` / h12 / 168 -> 259 -> 169 |
| `827cf5a0b3e00306bbae` | 2 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_110\sa_ep1_110.questphase` / h12 / 136 -> 137 -> 139 |
| `05da58ffa41a47aeb533` | 1 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_110\sa_ep1_110.questphase` / h12 / 175 -> 189 -> 188 |
| `0bfdcc18a8f2568dc213` | 1 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_110\sa_ep1_110.questphase` / h12 / 169 -> 171 -> 263 |
| `10ce0db372ef19128a6f` | 1 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_110\sa_ep1_110.questphase` / h12 / 121 -> 221 -> 222 |
| `10de5d2a81ab97879de5` | 1 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_110\sa_ep1_110.questphase` / h0 / 9 -> 12 -> 1 |
| `115fa12835d959ad9b55` | 1 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_110\sa_ep1_110.questphase` / h12 / 170 -> 172 -> 263 |
| `144b77d6eed6dd0be5cf` | 1 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_110\sa_ep1_110.questphase` / h0 / 52 -> 37 -> 59 |
| `1760abb46e61bc4b12dd` | 1 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_110\sa_ep1_110.questphase` / h12 / 138 -> 137 -> 142 |
| `1b825168e18afaa5eb2f` | 1 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_110\sa_ep1_110.questphase` / h12 / 133 -> 233 -> 132 |
| `1d207da50becc4024ea4` | 1 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_110\sa_ep1_110.questphase` / h12 / 122 -> 126 -> 216 |
| `2154e4dfc27be00ccd0a` | 1 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_110\sa_ep1_110.questphase` / h0 / 35 -> 57 -> 13 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
