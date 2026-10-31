# base-mq009

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq009\mq009_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq009\mq009_quest_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\minor_quests\mq009\communities\mq009_com_homeless.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq009\mq009.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq009\mq009.quest` | content candidate | 2 / 0 | base\quest\minor_quests\mq009\mq009.questphase; base\quest\minor_quests\mq009\test\mq009_chicken_test.scene |
| `base\quest\minor_quests\mq009\mq009.questphase` | content candidate | 6 / 0 | base\quest\minor_quests\mq009\scenes\mq009_01_hook.scene; base\quest\minor_quests\mq009\scenes\mq009_02_second_meeting.scene; base\quest\minor_quests\mq009\scenes\mq009_03_execution.scene |
| `base\quest\minor_quests\mq009\scenes\mq009_01_hook.scene` | content candidate | 0 / 47 |  |
| `base\quest\minor_quests\mq009\scenes\mq009_02_second_meeting.scene` | content candidate | 0 / 54 |  |
| `base\quest\minor_quests\mq009\scenes\mq009_03_execution.scene` | content candidate | 0 / 33 |  |
| `base\quest\minor_quests\mq009\test\mq009_chicken_test.scene` | test/debug | 0 / 13 |  |

## Journal paths observed in these resources

- `quests/minor_quest/mq009_loser`
- `quests/minor_quest/mq009_loser/mq009_2nd_meeting/01_approach_loser`
- `quests/minor_quest/mq009_loser/mq009_2nd_meeting/02_sit_loser`
- `quests/minor_quest/mq009_loser/mq009_2nd_meeting/03_drive_loser`
- `quests/minor_quest/mq009_loser/mq009_2nd_meeting/03_get_in_car`
- `quests/minor_quest/mq009_loser/mq009_2nd_meeting/04_shoot`
- `quests/minor_quest/mq009_loser/mq009_2nd_meeting/05_follow`
- `quests/minor_quest/mq009_loser/mq009_2nd_meeting/07_come_back`
- `quests/minor_quest/mq009_loser/mq009_2nd_meeting/08_talk`
- `quests/minor_quest/mq009_loser/mq009_hook/01_beat`
- `quests/minor_quest/mq009_loser/mq009_hook/02_talk_loser`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetProgressionBuild]` | 3 |
| `questCheckpointNodeDefinition` | 11 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questCutControlNodeDefinition` | 3 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 10 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 18 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 26 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMovePuppetNodeDefinition[questFollowParams,questUniversalRef]` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 3 |
| `questOutputNodeDefinition` | 10 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 11 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 13 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpeed_ConditionType]` | 2 |
| `questPhaseNodeDefinition` | 5 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 3 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 3 |
| `questSceneNodeDefinition[scnWorldMarker]` | 19 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 15 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 6 |
| `questUIManagerNodeDefinition[questDisplayMessageBox_NodeType]` | 2 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 3 |
| `questVehicleNodeDefinition[questSpawnPlayerVehicle_NodeType,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleForceBrake_NodeType]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questLifePath_ConditionType,questStatsCondition,questUniversalRef,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questLifePath_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 10 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnEndNode[scnNodeId]` | 29 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 62 |
| `scnStartNode[scnNodeId]` | 20 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `c1b6601d2f647c8a694d` | 15 | `base\quest\minor_quests\mq009\scenes\mq009_01_hook.scene` / scene / 98 -> 110 -> 101 |
| `27faccd7b30abbc3add2` | 13 | `base\quest\minor_quests\mq009\scenes\mq009_01_hook.scene` / scene / 98 -> 110 -> 103 |
| `8cd3b647ae3f592ad947` | 9 | `base\quest\minor_quests\mq009\scenes\mq009_01_hook.scene` / scene / 12 -> 14 -> 13 |
| `1fa539921730278ef7fb` | 5 | `base\quest\minor_quests\mq009\scenes\mq009_01_hook.scene` / scene / 110 -> 101 -> 118 |
| `2b8291b6d86672a1ab66` | 5 | `base\quest\minor_quests\mq009\scenes\mq009_01_hook.scene` / scene / 156 -> 66 -> 50 |
| `3300202aa48a37eea8e1` | 4 | `base\quest\minor_quests\mq009\scenes\mq009_01_hook.scene` / scene / 49 -> 123 -> 137 |
| `6d05e754f27f02e18922` | 4 | `base\quest\minor_quests\mq009\scenes\mq009_01_hook.scene` / scene / 146 -> 57 -> 156 |
| `de490f1a1f721f57a0ec` | 4 | `base\quest\minor_quests\mq009\scenes\mq009_01_hook.scene` / scene / 110 -> 103 -> 118 |
| `04fb03b4c5741c214e48` | 3 | `base\quest\minor_quests\mq009\scenes\mq009_01_hook.scene` / scene / 146 -> 57 -> 153 |
| `313f1b6d65d6d4b38ebe` | 3 | `base\quest\minor_quests\mq009\mq009.questphase` / h357 / 100 -> 95 -> 1 |
| `6126c325391320783d86` | 3 | `base\quest\minor_quests\mq009\scenes\mq009_01_hook.scene` / scene / 82 -> 84 -> 91 |
| `65e99f81f409743aebe3` | 3 | `base\quest\minor_quests\mq009\scenes\mq009_01_hook.scene` / scene / 123 -> 137 -> 143 |
| `da2ac967a03e5be61267` | 3 | `base\quest\minor_quests\mq009\scenes\mq009_01_hook.scene` / scene / 146 -> 57 -> 175 |
| `0c62c4715b51113108ae` | 2 | `base\quest\minor_quests\mq009\mq009.questphase` / h357 / 9 -> 10 -> 4 |
| `0facabbf270476d95d07` | 2 | `base\quest\minor_quests\mq009\scenes\mq009_03_execution.scene` / scene / 25 -> 33 -> 65 |
| `19775f0069af02d420b8` | 2 | `base\quest\minor_quests\mq009\mq009.questphase` / h357 / 8 -> 4 -> 6 |
| `1a000c4a2942fdbb978c` | 2 | `base\quest\minor_quests\mq009\scenes\mq009_02_second_meeting.scene` / scene / 185 -> 187 -> 189 |
| `1b0db5c4fac161a6187c` | 2 | `base\quest\minor_quests\mq009\scenes\mq009_02_second_meeting.scene` / scene / 187 -> 191 -> 84 |
| `247fad5d0bb5f3d680ba` | 2 | `base\quest\minor_quests\mq009\scenes\mq009_01_hook.scene` / scene / 135 -> 146 -> 57 |
| `32047358d4351d6c29a7` | 2 | `base\quest\minor_quests\mq009\scenes\mq009_02_second_meeting.scene` / scene / 189 -> 84 -> 92 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
