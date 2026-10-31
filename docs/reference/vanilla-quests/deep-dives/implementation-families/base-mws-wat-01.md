# base-mws-wat-01

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\watson\mws_wat_01\characters\mws_wat_01_robot.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\watson\mws_wat_01\mws_wat_01.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\watson\mws_wat_01\mws_wat_01.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\watson\mws_wat_01\mws_wat_01.questphase |
| `base\open_world\mini_world_stories\watson\mws_wat_01\mws_wat_01.questphase` | content candidate | 2 / 0 | base\open_world\mini_world_stories\watson\mws_wat_01\scenes\mws_wat_01.scene |
| `base\open_world\mini_world_stories\watson\mws_wat_01\mws_wat_01_inactive.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\watson\mws_wat_01\scenes\mws_wat_01.scene` | content candidate | 0 / 20 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 4 |
| `questEndNodeDefinition` | 1 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 2 |
| `questInputNodeDefinition` | 4 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_ActionProperty,questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 1 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 2 |
| `questPhaseNodeDefinition` | 1 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 4 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnEndNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 2 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `081b9dbe9528f984ddca` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_01\scenes\mws_wat_01.scene` / scene / 4 -> 13 -> 20 |
| `10883942d8ed42b98d9a` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_01\mws_wat_01.questphase` / h12 / 7 -> 4 -> 3 |
| `11b386a4cb2fc370fa4f` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_01\scenes\mws_wat_01.scene` / scene / 13 -> 20 -> 24 |
| `27ad6c335f3e6566344b` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_01\mws_wat_01.questphase` / h12 / 9 -> 6 -> 8 |
| `488662cf480a01564128` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_01\scenes\mws_wat_01.scene` / scene / 10 -> 4 -> 6 |
| `5228e66f60083982c9af` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_01\scenes\mws_wat_01.scene` / scene / 20 -> 65 -> 2 |
| `5345305d748c8a45459b` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_01\mws_wat_01.questphase` / h0 / 0 -> 9 -> 6 |
| `588819095eb16ec14528` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_01\scenes\mws_wat_01.scene` / scene / 13 -> 20 -> 50 |
| `5c22cbe05ce147d543b4` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_01\mws_wat_01.questphase` / h0 / 10 -> 6 -> 1 |
| `645cc6f9b4ae2c686302` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_01\scenes\mws_wat_01.scene` / scene / 1 -> 10 -> 38 |
| `7a1b13762b649aeb232b` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_01\mws_wat_01.questphase` / h12 / 6 -> 8 -> 1 |
| `7eece6022ec117da8ee6` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_01\mws_wat_01.questphase` / h0 / 9 -> 6 -> 1 |
| `8a7d26f5ef3d55eb0fbb` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_01\scenes\mws_wat_01.scene` / scene / 58 -> 32 -> 34 |
| `b7d6706f12b686ee6ca5` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_01\scenes\mws_wat_01.scene` / scene / 13 -> 20 -> 22 |
| `cc9bf9f879e74e6f1d93` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_01\mws_wat_01.questphase` / h12 / 0 -> 7 -> 4 |
| `e50179a81cb4a91a2171` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_01\scenes\mws_wat_01.scene` / scene / 1 -> 10 -> 14 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
