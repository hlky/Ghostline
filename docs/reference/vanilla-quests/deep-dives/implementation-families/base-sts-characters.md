# base-sts-characters

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\scenes\sts_characters\aaron_mccarlson_default.scene` | content candidate | 0 / 53 |  |
| `base\open_world\scenes\sts_characters\anna_hamill_default.questphase` | content candidate | 2 / 0 | base\open_world\scenes\sts_characters\anna_hamill_default.scene |
| `base\open_world\scenes\sts_characters\anna_hamill_default.scene` | content candidate | 0 / 57 |  |
| `base\open_world\scenes\sts_characters\benedict_mcadams_default.scene` | content candidate | 0 / 4 |  |
| `base\open_world\scenes\sts_characters\bugbear_default.scene` | content candidate | 0 / 11 |  |
| `base\open_world\scenes\sts_characters\dan_default.scene` | content candidate | 0 / 16 |  |
| `base\open_world\scenes\sts_characters\hal_cantos_default.scene` | content candidate | 0 / 4 |  |
| `base\open_world\scenes\sts_characters\lucy_thackery_default.scene` | content candidate | 0 / 28 |  |
| `base\open_world\scenes\sts_characters\max_jones_default.scene` | content candidate | 0 / 30 |  |
| `base\open_world\scenes\sts_characters\rihanna_kumar_default.scene` | content candidate | 0 / 5 |  |
| `base\open_world\scenes\sts_characters\robert_tanner_default.scene` | content candidate | 0 / 11 |  |
| `base\open_world\scenes\sts_characters\sergei_karasinsky_default.scene` | content candidate | 0 / 8 |  |
| `base\open_world\scenes\sts_characters\tiny_mike_default.scene` | content candidate | 0 / 50 |  |
| `base\open_world\voicesets\sts_characters\vset_aaron_mccarlson.scene` | content candidate | 0 / 28 |  |
| `base\open_world\voicesets\sts_characters\vset_anna_hamill.scene` | content candidate | 0 / 58 |  |
| `base\open_world\voicesets\sts_characters\vset_bruce_welby.scene` | content candidate | 0 / 30 |  |
| `base\open_world\voicesets\sts_characters\vset_chang_hoon_nam.scene` | content candidate | 0 / 30 |  |
| `base\open_world\voicesets\sts_characters\vset_corporal_hare.scene` | content candidate | 0 / 70 |  |
| `base\open_world\voicesets\sts_characters\vset_el_gallo.scene` | content candidate | 0 / 56 |  |
| `base\open_world\voicesets\sts_characters\vset_hal_cantos.scene` | content candidate | 0 / 30 |  |
| `base\open_world\voicesets\sts_characters\vset_hwangbo_dong_gun.scene` | content candidate | 0 / 30 |  |
| `base\open_world\voicesets\sts_characters\vset_lauren_costigan.scene` | content candidate | 0 / 30 |  |
| `base\open_world\voicesets\sts_characters\vset_max_jones.scene` | content candidate | 0 / 58 |  |
| `base\open_world\voicesets\sts_characters\vset_red_thunder.scene` | content candidate | 0 / 70 |  |
| `base\open_world\voicesets\sts_characters\vset_ron_chi_won.scene` | content candidate | 0 / 30 |  |
| `base\open_world\voicesets\sts_characters\vset_ted_fox.scene` | content candidate | 0 / 18 |  |
| `base\open_world\voicesets\sts_characters\vset_tiny_mike.scene` | content candidate | 0 / 46 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 1 |
| `questConditionNodeDefinition` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 17 |
| `questInputNodeDefinition` | 2 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 4 |
| `questOutputNodeDefinition` | 4 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 5 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSectionNode_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 21 |
| `questUIManagerNodeDefinition[questVendorPanel_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 22 |
| `questUseWorkspotNodeDefinition[questUseWorkspotPlayerParams,scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 5 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 48 |
| `scnAndNode[scnNodeId]` | 2 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnReferencePointId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 8 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 7 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 4 |
| `scnEndNode[scnNodeId]` | 10 |
| `scnHubNode[scnNodeId]` | 15 |
| `scnInterruptManagerNode[scnNodeId,scnToggleInterruption_InterruptionOperation]` | 2 |
| `scnRandomizerNode[scnNodeId]` | 88 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 159 |
| `scnSectionNode[scnNodeId,scnSceneTime]` | 108 |
| `scnStartNode[scnNodeId]` | 308 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `cc06aff3e3b17ec38339` | 51 | `base\open_world\voicesets\sts_characters\vset_aaron_mccarlson.scene` / scene / 40 -> 41 -> 43 |
| `5044a5fbccba69772268` | 44 | `base\open_world\voicesets\sts_characters\vset_aaron_mccarlson.scene` / scene / 40 -> 41 -> 42 |
| `4fcad87865f924474a76` | 43 | `base\open_world\voicesets\sts_characters\vset_aaron_mccarlson.scene` / scene / 54 -> 55 -> 56 |
| `3af95a0b36868c686aaa` | 36 | `base\open_world\voicesets\sts_characters\vset_aaron_mccarlson.scene` / scene / 54 -> 55 -> 57 |
| `27faccd7b30abbc3add2` | 8 | `base\open_world\scenes\sts_characters\bugbear_default.scene` / scene / 36 -> 4 -> 6 |
| `c1b6601d2f647c8a694d` | 8 | `base\open_world\scenes\sts_characters\bugbear_default.scene` / scene / 36 -> 4 -> 21 |
| `7f90556fa6e058039d36` | 7 | `base\open_world\voicesets\sts_characters\vset_aaron_mccarlson.scene` / scene / 46 -> 47 -> 79 |
| `bdba7ed59b6db80b79ec` | 6 | `base\open_world\scenes\sts_characters\aaron_mccarlson_default.scene` / scene / 14 -> 20 -> 88 |
| `5e0fdd5c991cc4718977` | 5 | `base\open_world\scenes\sts_characters\anna_hamill_default.scene` / scene / 205 -> 10 -> 248 |
| `1b4f5e876c8109d5a852` | 4 | `base\open_world\scenes\sts_characters\benedict_mcadams_default.scene` / scene / 1 -> 4 -> 5 |
| `276aca4a2dc348a877d5` | 4 | `base\open_world\scenes\sts_characters\aaron_mccarlson_default.scene` / scene / 14 -> 20 -> 276 |
| `300323a534d1166f0705` | 4 | `base\open_world\scenes\sts_characters\anna_hamill_default.scene` / scene / 205 -> 10 -> 249 |
| `4d0b89400e09faa05792` | 4 | `base\open_world\scenes\sts_characters\aaron_mccarlson_default.scene` / scene / 14 -> 20 -> 152 |
| `afbc348d6f0f691e60f3` | 4 | `base\open_world\scenes\sts_characters\robert_tanner_default.scene` / scene / 4 -> 17 -> 2 |
| `d5bca3987352b6bf4122` | 4 | `base\open_world\scenes\sts_characters\anna_hamill_default.scene` / scene / 205 -> 10 -> 250 |
| `0ca9bfdb2b5f53c7f1c8` | 3 | `base\open_world\scenes\sts_characters\benedict_mcadams_default.scene` / scene / 4 -> 5 -> 2 |
| `47d2d60daf4a94e81e2f` | 3 | `base\open_world\scenes\sts_characters\lucy_thackery_default.scene` / scene / 41 -> 68 -> 69 |
| `4d64d6162c8281c013fc` | 3 | `base\open_world\scenes\sts_characters\dan_default.scene` / scene / 5 -> 6 -> 8 |
| `93c10f5cd335e961264a` | 3 | `base\open_world\scenes\sts_characters\robert_tanner_default.scene` / scene / 9 -> 12 -> 22 |
| `a515c16b5d15bd03fa23` | 3 | `base\open_world\scenes\sts_characters\anna_hamill_default.scene` / scene / 6 -> 8 -> 205 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
