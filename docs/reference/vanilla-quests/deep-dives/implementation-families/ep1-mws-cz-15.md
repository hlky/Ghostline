# ep1-mws-cz-15

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_15\mws_cz_15_best_dressed.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_15\mws_cz_15_best_dressed.quest` | content candidate | 1 / 0 | ep1\openworld\mini_world_stories\combat_zone\mws_cz_15\phases\mws_cz_15_questphase.questphase |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_15\phases\mws_cz_15_questphase.questphase` | content candidate | 3 / 0 | ep1\openworld\mini_world_stories\combat_zone\mws_cz_15\scenes\mws_cz_15_best_dressed_device.scene |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_15\scenes\mws_cz_15_best_dressed_device.scene` | content candidate | 0 / 58 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questConditionNodeDefinition[questCharacterBodyType_CondtionType,questCharacterCondition]` | 4 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterEquippedItem_ConditionType,questLogicalCondition]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 3 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 1 |
| `questInputNodeDefinition` | 3 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 3 |
| `questPhaseNodeDefinition` | 3 |
| `questSceneNodeDefinition[scnWorldMarker]` | 2 |
| `questSpawnManagerNodeDefinition[questScene_NodeType,questSpawnManagerNodeActionEntry]` | 12 |
| `questStartNodeDefinition` | 1 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questWarningMessage_NodeType]` | 2 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotPlayerParams,scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 1 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 5 |
| `scnChoiceNode[scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnHubNode[scnNodeId]` | 4 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 10 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `18ecba01435e453780a5` | 3 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_15\scenes\mws_cz_15_best_dressed_device.scene` / scene / 10 -> 23 -> 26 |
| `1ec7305600f4beb07494` | 3 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_15\scenes\mws_cz_15_best_dressed_device.scene` / scene / 169 -> 160 -> 162 |
| `57648e42baaf0bf443e3` | 3 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_15\scenes\mws_cz_15_best_dressed_device.scene` / scene / 10 -> 23 -> 25 |
| `b4df9ad44e9b1d5b5d8b` | 3 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_15\scenes\mws_cz_15_best_dressed_device.scene` / scene / 169 -> 160 -> 164 |
| `16d1d6a285a08b87cd77` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_15\scenes\mws_cz_15_best_dressed_device.scene` / scene / 409 -> 24 -> 46 |
| `178f79d29289e946444b` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_15\scenes\mws_cz_15_best_dressed_device.scene` / scene / 409 -> 24 -> 203 |
| `2ecf6cf4ecb2e5b5dd21` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_15\scenes\mws_cz_15_best_dressed_device.scene` / scene / 144 -> 130 -> 285 |
| `324b952c3c23f239dbdb` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_15\scenes\mws_cz_15_best_dressed_device.scene` / scene / 310 -> 145 -> 144 |
| `4bce0d1a0328be704289` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_15\scenes\mws_cz_15_best_dressed_device.scene` / scene / 201 -> 275 -> 78 |
| `54d804aa48f81c058798` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_15\scenes\mws_cz_15_best_dressed_device.scene` / scene / 28 -> 409 -> 24 |
| `a38c649a9ad91a4ffa5f` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_15\scenes\mws_cz_15_best_dressed_device.scene` / scene / 25 -> 28 -> 409 |
| `dfd4d7249953e7dc9b66` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_15\scenes\mws_cz_15_best_dressed_device.scene` / scene / 308 -> 145 -> 144 |
| `e3b808d5b58b06b9dc89` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_15\scenes\mws_cz_15_best_dressed_device.scene` / scene / 203 -> 270 -> 78 |
| `e580484d82b60eb728fb` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_15\scenes\mws_cz_15_best_dressed_device.scene` / scene / 144 -> 130 -> 368 |
| `eeaedcb26fefc87febc3` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_15\scenes\mws_cz_15_best_dressed_device.scene` / scene / 409 -> 24 -> 39 |
| `119d8760e546de03d955` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_15\scenes\mws_cz_15_best_dressed_device.scene` / scene / 78 -> 169 -> 244 |
| `16856885e6a1d5bebd86` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_15\scenes\mws_cz_15_best_dressed_device.scene` / scene / 169 -> 176 -> 6 |
| `19fe0a74e57469e5c20f` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_15\phases\mws_cz_15_questphase.questphase` / h56 / 0 -> 4 -> 2 |
| `1ae94ee872986dd79c0d` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_15\phases\mws_cz_15_questphase.questphase` / h16 / 0 -> 3 -> 4 |
| `208bcf520befcd7c4d03` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_15\scenes\mws_cz_15_best_dressed_device.scene` / scene / 130 -> 368 -> 308 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
