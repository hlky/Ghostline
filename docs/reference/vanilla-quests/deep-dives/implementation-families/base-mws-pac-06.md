# base-mws-pac-06

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\pacifica\mws_pac_06\communities\mws_pac_06.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\pacifica\mws_pac_06\communities\mws_pac_06_enemies.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\pacifica\mws_pac_06\mws_pac_06.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\pacifica\mws_pac_06\mws_pac_06.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\pacifica\mws_pac_06\mws_pac_06.questphase |
| `base\open_world\mini_world_stories\pacifica\mws_pac_06\mws_pac_06.questphase` | content candidate | 7 / 0 | base\open_world\mini_world_stories\pacifica\mws_pac_06\scenes\mws_pac_06.scene |
| `base\open_world\mini_world_stories\pacifica\mws_pac_06\scenes\mws_pac_06.scene` | content candidate | 0 / 13 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 6 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 4 |
| `questCombatNodeDefinition` | 4 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 4 |
| `questCombatNodeDefinition[questCombatNodeParams_ShootAt]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questCutControlNodeDefinition` | 7 |
| `questDeletionMarkerNodeDefinition` | 5 |
| `questEndNodeDefinition` | 1 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 8 |
| `questEventManagerNodeDefinition` | 4 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 9 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 4 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 2 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 3 |
| `questLogicalAndNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 6 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questLogicalCondition,questObservableUniversalRef]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questRealtimeDelay_ConditionType,questTimeCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 6 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 4 |
| `questStartNodeDefinition` | 1 |
| `questUIManagerNodeDefinition[questDisplayMessageBox_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |
| `scnEndNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 3 |
| `scnStartNode[scnNodeId]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `f9e272dca03d7feb8114` | 4 | `base\open_world\mini_world_stories\pacifica\mws_pac_06\mws_pac_06.questphase` / h66 / 20 -> 18 -> 21 |
| `861397e266b66f740beb` | 3 | `base\open_world\mini_world_stories\pacifica\mws_pac_06\mws_pac_06.questphase` / h26 / 6 -> 13 -> 32 |
| `30e16a0e63a824307d36` | 2 | `base\open_world\mini_world_stories\pacifica\mws_pac_06\mws_pac_06.questphase` / h66 / 2 -> 4 -> 11 |
| `42d198651597f3c3ac03` | 2 | `base\open_world\mini_world_stories\pacifica\mws_pac_06\mws_pac_06.questphase` / h226 / 0 -> 30 -> 1 |
| `6968bac5d084c2142470` | 2 | `base\open_world\mini_world_stories\pacifica\mws_pac_06\mws_pac_06.questphase` / h66 / 0 -> 2 -> 4 |
| `844196b6c9c48c869bed` | 2 | `base\open_world\mini_world_stories\pacifica\mws_pac_06\mws_pac_06.questphase` / h26 / 113 -> 48 -> 112 |
| `8ba2f1ff405051c02e75` | 2 | `base\open_world\mini_world_stories\pacifica\mws_pac_06\mws_pac_06.questphase` / h26 / 48 -> 112 -> 53 |
| `987122e5e2fcd167cf6c` | 2 | `base\open_world\mini_world_stories\pacifica\mws_pac_06\mws_pac_06.questphase` / h500 / 0 -> 16 -> 18 |
| `d6d5eeaf164748a0d23d` | 2 | `base\open_world\mini_world_stories\pacifica\mws_pac_06\mws_pac_06.questphase` / h26 / 13 -> 48 -> 112 |
| `01851cd592743a0d6b6d` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_06\mws_pac_06.questphase` / h0 / 18 -> 3 -> 4 |
| `056f65b5401e52f37bc4` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_06\mws_pac_06.questphase` / h659 / 0 -> 2 -> 3 |
| `09d4b2d9f039dfb81eeb` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_06\mws_pac_06.questphase` / h659 / 6 -> 10 -> 5 |
| `15f9f7716322b29b1372` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_06\mws_pac_06.questphase` / h26 / 117 -> 97 -> 1 |
| `270065e70ddcf1c96b20` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_06\mws_pac_06.questphase` / h0 / 19 -> 18 -> 3 |
| `2ff7d455af443987753a` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_06\scenes\mws_pac_06.scene` / scene / 4 -> 20 -> 23 |
| `30c005b838f18668560f` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_06\mws_pac_06.questphase` / h26 / 6 -> 13 -> 119 |
| `3cb5bb88329334568432` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_06\scenes\mws_pac_06.scene` / scene / 22 -> 21 -> 5 |
| `3f6b9e253f28c15ec2b3` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_06\mws_pac_06.questphase` / h226 / 0 -> 30 -> 59 |
| `47fffffb2b2de5f2871e` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_06\mws_pac_06.questphase` / h387 / 14 -> 34 -> 33 |
| `48fbfd49617fbdae2512` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_06\mws_pac_06.questphase` / h659 / 3 -> 6 -> 10 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
