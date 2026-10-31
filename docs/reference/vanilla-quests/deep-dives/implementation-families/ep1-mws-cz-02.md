# ep1-mws-cz-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\community\mws_cz_02_community.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\mws_cz_02.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\mws_cz_02.quest` | content candidate | 1 / 0 | ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\mws_cz_02.questphase |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\mws_cz_02.questphase` | content candidate | 4 / 0 | ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\scenes\mws_cz_02_scene_01.scene |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\scenes\mws_cz_02_scene_01.scene` | content candidate | 0 / 47 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_NodeType,questCharacterManagerCombat_SetDeathDirection]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 3 |
| `questInputNodeDefinition` | 4 |
| `questLogicalAndNodeDefinition` | 3 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 2 |
| `questOutputNodeDefinition` | 5 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 3 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 17 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 7 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 6 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 6 |
| `scnAndNode[scnNodeId]` | 3 |
| `scnEndNode[scnNodeId]` | 1 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 3 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `987122e5e2fcd167cf6c` | 5 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\mws_cz_02.questphase` / h26 / 0 -> 10 -> 15 |
| `0ad9f74a2d370ba01327` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\mws_cz_02.questphase` / h170 / 4 -> 3 -> 11 |
| `20d7e7055b4afb21dd89` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\mws_cz_02.questphase` / h170 / 6 -> 3 -> 11 |
| `380f2153d1639bdd0d26` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\mws_cz_02.questphase` / h170 / 2 -> 3 -> 11 |
| `40b1396595b5dbbfe8ed` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\mws_cz_02.questphase` / h170 / 0 -> 8 -> 3 |
| `4518cc0fb86e98005539` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\scenes\mws_cz_02_scene_01.scene` / scene / 1 -> 301 -> 311 |
| `678965e49d6f7034c7a9` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\mws_cz_02.questphase` / h170 / 0 -> 7 -> 3 |
| `67fc2574104b01640ecf` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\mws_cz_02.questphase` / h170 / 0 -> 5 -> 3 |
| `704db4612860979a8daf` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\mws_cz_02.questphase` / h170 / 0 -> 6 -> 3 |
| `71e2339271c2888089c3` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\mws_cz_02.questphase` / h170 / 7 -> 3 -> 11 |
| `8989317dcc1caeab8582` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\mws_cz_02.questphase` / h170 / 5 -> 3 -> 11 |
| `9d9c15d0d47bc574464c` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\mws_cz_02.questphase` / h170 / 3 -> 11 -> 10 |
| `a5badf9ee5152a2bd797` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\mws_cz_02.questphase` / h170 / 0 -> 4 -> 3 |
| `eb9aa604acd6eee51612` | 2 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\mws_cz_02.questphase` / h170 / 0 -> 2 -> 3 |
| `00fa134e0b12e7b82f04` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\scenes\mws_cz_02_scene_01.scene` / scene / 1 -> 6 -> 171 |
| `02d9368484f4ddedc1e6` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\scenes\mws_cz_02_scene_01.scene` / scene / 24 -> 30 -> 33 |
| `0903cdd6abb05bb38a8b` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\scenes\mws_cz_02_scene_01.scene` / scene / 143 -> 249 -> 246 |
| `0cdc70306b6cca6ecf2a` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\mws_cz_02.questphase` / h26 / 35 -> 31 -> 34 |
| `10ac8cb355f355254ee3` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\mws_cz_02.questphase` / h26 / 16 -> 14 -> 35 |
| `13781663e311e07c2c30` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_02\mws_cz_02.questphase` / h26 / 34 -> 33 -> 1 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
