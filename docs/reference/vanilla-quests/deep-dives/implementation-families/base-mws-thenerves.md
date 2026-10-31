# base-mws-thenerves

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\watson\mws_thenerves\characters\mws_thenerves.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\watson\mws_thenerves\characters\mws_thenerves_2.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves.questphase |
| `base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves.questphase` | content candidate | 1 / 0 | base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves_cleanup.questphase; base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves_decoration_spawn.questphase; base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves_enginerevssound.questphase |
| `base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves_cleanup.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves_decoration_spawn.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves_enginerevssound.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves_npcspawn.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\mini_world_stories\watson\mws_thenerves\scenes\mws_thenerves.scene` | content candidate | 0 / 22 |  |

## Journal paths observed in these resources

- `quests/minor_quest/mq032_sacrum/mq032_sacrum`
- `quests/minor_quest/mq032_sacrum/mq032_sacrum/03_monk`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 8 |
| `questAudioNodeDefinition[questAudioParameterNodeType]` | 10 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 10 |
| `questDeletionMarkerNodeDefinition` | 41 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 25 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 2 |
| `questInputNodeDefinition` | 7 |
| `questLogicalAndNodeDefinition` | 5 |
| `questLogicalHubNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 5 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 38 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterQuickHacked_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PuppetSubType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterStatusEffect_CondtionType,questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterStatusEffect_CondtionType]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 8 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInputAction_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTimeCondition,questTimePeriod_ConditionType,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 19 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSectionNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 6 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleQuickHack_ConditionType]` | 1 |
| `questPhaseNodeDefinition` | 9 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 106 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 36 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 3 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 2 |
| `questVehicleNodeDefinition[questJoinTraffic_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 4 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 12 |
| `scnDeletionMarkerNode[scnNodeId]` | 11 |
| `scnEndNode[scnNodeId]` | 1 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 1 |
| `scnXorNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `6e66b967a4e71571e809` | 48 | `base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves_cleanup.questphase` / h0 / 16 -> 104 -> 105 |
| `79ff30ab7464b071eda5` | 30 | `base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves_decoration_spawn.questphase` / h0 / 9 -> 10 -> 11 |
| `e612447c92cb1e217571` | 10 | `base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves.questphase` / h0 / 314 -> 315 -> 595 |
| `f7ae732f504e68ef12b1` | 7 | `base\open_world\mini_world_stories\watson\mws_thenerves\scenes\mws_thenerves.scene` / scene / 257 -> 10 -> 114 |
| `bfe95df47bd1ca67330f` | 4 | `base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves.questphase` / h0 / 40 -> 104 -> 83 |
| `da3f196a1e48a0aec227` | 3 | `base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves.questphase` / h0 / 637 -> 354 -> 314 |
| `0d775ef374b7d7eddf87` | 2 | `base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves_cleanup.questphase` / h0 / 20 -> 21 -> 116 |
| `1cd8e491ead362236880` | 2 | `base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves.questphase` / h0 / 155 -> 576 -> 627 |
| `20a77143a898bc753a26` | 2 | `base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves.questphase` / h0 / 649 -> 652 -> 659 |
| `25aae51001db85d5b1fb` | 2 | `base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves.questphase` / h0 / 659 -> 660 -> 285 |
| `293ea858c258c4b9287c` | 2 | `base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves_decoration_spawn.questphase` / h0 / 18 -> 19 -> 2 |
| `3a31623257fff66fe3e5` | 2 | `base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves.questphase` / h0 / 29 -> 15 -> 5 |
| `3f522da5aafade67772b` | 2 | `base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves_enginerevssound.questphase` / h0 / 7 -> 4 -> 11 |
| `43614d3e2db5dc5f8e81` | 2 | `base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves_enginerevssound.questphase` / h0 / 2 -> 6 -> 4 |
| `45774537e7e190ffe3d6` | 2 | `base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves_decoration_spawn.questphase` / h0 / 1 -> 20 -> 21 |
| `500275dae3c789410eff` | 2 | `base\open_world\mini_world_stories\watson\mws_thenerves\scenes\mws_thenerves.scene` / scene / 287 -> 286 -> 304 |
| `591f2536e7cba145b19b` | 2 | `base\open_world\mini_world_stories\watson\mws_thenerves\scenes\mws_thenerves.scene` / scene / 1 -> 287 -> 286 |
| `6767c1c9bd449c18b359` | 2 | `base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves_cleanup.questphase` / h0 / 4 -> 5 -> 116 |
| `6f8ed7276bb109f88a76` | 2 | `base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves_cleanup.questphase` / h0 / 60 -> 61 -> 119 |
| `a4de1b643a001ff185a6` | 2 | `base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves.questphase` / h0 / 136 -> 318 -> 326 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
