# ep1-wst-ep1-08

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_08\wst_ep1_08.questphase` | content candidate | 2 / 0 | ep1\openworld\world_stories\wst_ep1_08\wst_ep1_08_scene.scene |
| `ep1\openworld\world_stories\wst_ep1_08\wst_ep1_08_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\world_stories\wst_ep1_08\wst_ep1_08_scene.scene` | content candidate | 0 / 20 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCutControlNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 3 |
| `questInputNodeDefinition` | 2 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 5 |
| `questMovePuppetNodeDefinition[questJoinCrowdParams]` | 3 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterAim_ConditionType,questCharacterCondition,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterReaction_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questSensesCondition,questStimuli_ConditionType,questTriggerCondition]` | 6 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 13 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 6 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 4 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |
| `scnAndNode[scnNodeId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 1 |
| `scnEndNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 2 |
| `scnStartNode[scnNodeId]` | 1 |
| `scnXorNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `7394ada0cd2462de909b` | 6 | `ep1\openworld\world_stories\wst_ep1_08\wst_ep1_08.questphase` / h237 / 0 -> 10 -> 2 |
| `cd362676c46d8f6c7955` | 3 | `ep1\openworld\world_stories\wst_ep1_08\wst_ep1_08.questphase` / h0 / 76 -> 61 -> 33 |
| `d7ead75d7ae1166ddbe8` | 3 | `ep1\openworld\world_stories\wst_ep1_08\wst_ep1_08.questphase` / h0 / 87 -> 22 -> 79 |
| `c8dd86e59dcccf53ce1a` | 2 | `ep1\openworld\world_stories\wst_ep1_08\wst_ep1_08.questphase` / h0 / 5 -> 13 -> 4 |
| `e735e23a5cafaa15e972` | 2 | `ep1\openworld\world_stories\wst_ep1_08\wst_ep1_08.questphase` / h0 / 7 -> 10 -> 9 |
| `002497598bd7357b3842` | 1 | `ep1\openworld\world_stories\wst_ep1_08\wst_ep1_08_scene.scene` / scene / 10 -> 50 -> 26 |
| `10043e2a44d2719a6d7b` | 1 | `ep1\openworld\world_stories\wst_ep1_08\wst_ep1_08.questphase` / h0 / 51 -> 55 -> 6 |
| `19665e3783f6f51a7337` | 1 | `ep1\openworld\world_stories\wst_ep1_08\wst_ep1_08_scene.scene` / scene / 1 -> 6 -> 118 |
| `215a811f84fe46cd3cac` | 1 | `ep1\openworld\world_stories\wst_ep1_08\wst_ep1_08.questphase` / h0 / 51 -> 55 -> 87 |
| `2e1ee5a1324dbeeb9071` | 1 | `ep1\openworld\world_stories\wst_ep1_08\wst_ep1_08.questphase` / h0 / 13 -> 4 -> 51 |
| `30c49e2f12c404211c65` | 1 | `ep1\openworld\world_stories\wst_ep1_08\wst_ep1_08.questphase` / h0 / 87 -> 22 -> 76 |
| `35ad944a07e384ee88e6` | 1 | `ep1\openworld\world_stories\wst_ep1_08\wst_ep1_08.questphase` / h0 / 55 -> 87 -> 22 |
| `4046f7e0ed1087267da3` | 1 | `ep1\openworld\world_stories\wst_ep1_08\wst_ep1_08.questphase` / h0 / 12 -> 16 -> 15 |
| `41adb25f27e3abdf9e4c` | 1 | `ep1\openworld\world_stories\wst_ep1_08\wst_ep1_08_scene.scene` / scene / 50 -> 26 -> 6 |
| `4518cc0fb86e98005539` | 1 | `ep1\openworld\world_stories\wst_ep1_08\wst_ep1_08_scene.scene` / scene / 1 -> 6 -> 120 |
| `481bb61cd41815a09fdf` | 1 | `ep1\openworld\world_stories\wst_ep1_08\wst_ep1_08.questphase` / h0 / 13 -> 4 -> 12 |
| `4cd7ebd61a91c4e8cab4` | 1 | `ep1\openworld\world_stories\wst_ep1_08\wst_ep1_08.questphase` / h0 / 17 -> 11 -> 7 |
| `72456e8dd927fd679172` | 1 | `ep1\openworld\world_stories\wst_ep1_08\wst_ep1_08.questphase` / h0 / 4 -> 51 -> 55 |
| `7a1b13762b649aeb232b` | 1 | `ep1\openworld\world_stories\wst_ep1_08\wst_ep1_08.questphase` / h0 / 14 -> 86 -> 84 |
| `8370c76cbc0899b84848` | 1 | `ep1\openworld\world_stories\wst_ep1_08\wst_ep1_08.questphase` / h0 / 16 -> 15 -> 17 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
