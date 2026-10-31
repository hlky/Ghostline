# base-mws-wat-08

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\watson\mws_wat_08\communities\mws_trauma_team_av_model_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\watson\mws_wat_08\communities\mws_wat_08_com_trauma_team.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.quest` | content candidate | 2 / 0 | base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.questphase; base\open_world\mini_world_stories\watson\mws_wat_08\scenes\mws_wat_08.scene; base\quest\additional_game_elements.questphase |
| `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.questphase` | content candidate | 8 / 0 | base\open_world\mini_world_stories\watson\mws_wat_08\scenes\mws_wat_08.scene |
| `base\open_world\mini_world_stories\watson\mws_wat_08\scenes\mws_wat_08.scene` | content candidate | 0 / 85 |  |

## Journal paths observed in these resources

- `contacts/arcade_game_manufacturer_trauma_drama`
- `contacts/arcade_game_manufacturer_trauma_drama/trauma_drama/congratulations_for_playing_the_game`
- `contacts/arcade_game_manufacturer_trauma_drama/trauma_drama/congratulations_for_playing_the_game_followup`
- `contacts/arcade_game_manufacturer_trauma_drama/trauma_drama/congratulations_for_reaching_place_01`
- `contacts/arcade_game_manufacturer_trauma_drama/trauma_drama/consolation_prize_is_being_prepared`
- `internet_sites/home/00_home`
- `internet_sites/home/00_home1`
- `internet_sites/home/00_home2`
- `internet_sites/home/00_home3`
- `internet_sites/home/00_mq018_home_bartmoss`
- `internet_sites/traumateam/00_login`
- `internet_sites/traumateam/00_login1`
- `internet_sites/traumateam/01_page_not_found`
- `internet_sites/traumateam/04_inside`
- `internet_sites/traumateam/05_recruitment`
- `internet_sites/traumateam/07_application`
- `internet_sites/traumateam/07_application1`
- `internet_sites/traumateam/07_application2`
- `quests/minor_quest/mws_wat_08_trauma_drama`
- `quests/minor_quest/mws_wat_08_trauma_drama/description`
- `quests/minor_quest/mws_wat_08_trauma_drama/mws_wat_08_trauma_drama/01_check_trauma_team_website`
- `quests/minor_quest/mws_wat_08_trauma_drama/mws_wat_08_trauma_drama/02_read_message_from_game_dev`
- `quests/minor_quest/mws_wat_08_trauma_drama/mws_wat_08_trauma_drama/02_read_message_from_game_dev/contact`
- `quests/minor_quest/mws_wat_08_trauma_drama/mws_wat_08_trauma_drama/04_go_to_reward_location`
- `quests/minor_quest/mws_wat_08_trauma_drama/mws_wat_08_trauma_drama/05_scan_hand`
- `quests/minor_quest/mws_wat_08_trauma_drama/mws_wat_08_trauma_drama/06_take_your_reward`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetProgressionBuild]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 5 |
| `questCutControlNodeDefinition` | 1 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 5 |
| `questEventManagerNodeDefinition` | 5 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 19 |
| `questInputNodeDefinition` | 10 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 3 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 47 |
| `questLogicalHubNodeDefinition` | 5 |
| `questOutputNodeDefinition` | 11 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questInputAction_ConditionType,questSystemCondition]` | 5 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 3 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 10 |
| `questPauseConditionNodeDefinition[questTickDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 5 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 2 |
| `questPhaseNodeDefinition` | 7 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 3 |
| `questPhoneManagerNodeDefinition[questAddRemoveContact_NodeType,questChangeContactList_NodeTypeParams]` | 1 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 1 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 4 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 5 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 7 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Pause]` | 1 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Play]` | 2 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Reset]` | 1 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 2 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 1 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 8 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 3 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 2 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 9 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |
| `scnAndNode[scnNodeId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 3 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 5 |
| `scnHubNode[scnNodeId]` | 3 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 4 |
| `scnStartNode[scnNodeId]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `9af8a87f20a910659fa8` | 6 | `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.quest` / h0 / 4 -> 5 -> 7 |
| `624d47eac987aa67b8fb` | 5 | `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.questphase` / h0 / 102 -> 121 -> 97 |
| `85950fc185447c4a3b16` | 5 | `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.questphase` / h0 / 119 -> 107 -> 102 |
| `f6f4b5b519cf5450f8a6` | 5 | `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.questphase` / h0 / 107 -> 102 -> 121 |
| `7e7dbbc930b3717fd790` | 4 | `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.questphase` / h0 / 88 -> 84 -> 85 |
| `00bee4d1c25f1e548e94` | 2 | `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.questphase` / h328 / 7 -> 2 -> 3 |
| `1c0578433c3aadf0f002` | 2 | `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.questphase` / h328 / 2 -> 3 -> 4 |
| `25c4b5e29cd0009ea282` | 2 | `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.questphase` / h328 / 3 -> 4 -> 5 |
| `350a93ef163cdd76e4ef` | 2 | `base\open_world\mini_world_stories\watson\mws_wat_08\scenes\mws_wat_08.scene` / scene / 217 -> 16 -> 309 |
| `86c7c6ddf152785e79a9` | 2 | `base\open_world\mini_world_stories\watson\mws_wat_08\scenes\mws_wat_08.scene` / scene / 105 -> 107 -> 314 |
| `8ebae96ccbb0172cca1c` | 2 | `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.questphase` / h114 / 2 -> 3 -> 1 |
| `e268727ce99d781b558d` | 2 | `base\open_world\mini_world_stories\watson\mws_wat_08\scenes\mws_wat_08.scene` / scene / 217 -> 16 -> 339 |
| `f04414ad066054b28ac2` | 2 | `base\open_world\mini_world_stories\watson\mws_wat_08\scenes\mws_wat_08.scene` / scene / 205 -> 217 -> 16 |
| `03c68fa756c168cf6c60` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_08\scenes\mws_wat_08.scene` / scene / 366 -> 179 -> 183 |
| `0453d6bea9ad4579c156` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.questphase` / h214 / 12 -> 20 -> 5 |
| `07a508d9181a1ec44ac6` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.quest` / h0 / 50 -> 51 -> 52 |
| `07ffe8d0ddbddefc1025` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_08\scenes\mws_wat_08.scene` / scene / 74 -> 70 -> 98 |
| `097527fb36a42bfd6ea2` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_08\scenes\mws_wat_08.scene` / scene / 6 -> 22 -> 220 |
| `0d08c3cbf1244c06fe57` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.questphase` / h284 / 0 -> 4 -> 7 |
| `0fdad4c8a8b4964c866f` | 1 | `base\open_world\mini_world_stories\watson\mws_wat_08\scenes\mws_wat_08.scene` / scene / 179 -> 196 -> 194 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
