# base-mws-pac-01

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\pacifica\mws_pac_01\community\mws_pac_01.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\pacifica\mws_pac_01\mws_pac_01.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\pacifica\mws_pac_01\mws_pac_01.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\pacifica\mws_pac_01\mws_pac_01.questphase |
| `base\open_world\mini_world_stories\pacifica\mws_pac_01\mws_pac_01.questphase` | content candidate | 3 / 0 | base\open_world\mini_world_stories\pacifica\mws_pac_01\scenes\mws_pac_01.scene |
| `base\open_world\mini_world_stories\pacifica\mws_pac_01\scenes\mws_pac_01.scene` | content candidate | 0 / 23 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 1 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 3 |
| `questInputNodeDefinition` | 5 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 5 |
| `questPhaseNodeDefinition` | 2 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questUIManagerNodeDefinition[questDisplayMessageBox_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 4 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 3 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 1 |
| `scnEndNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 3 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `0e3cc17d22ec2e9c1a66` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_01\scenes\mws_pac_01.scene` / scene / 4 -> 144 -> 151 |
| `2be15212938b2a09c6e1` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_01\scenes\mws_pac_01.scene` / scene / 179 -> 1 -> 109 |
| `328b5333583932d21404` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_01\mws_pac_01.questphase` / h7 / 14 -> 13 -> 12 |
| `572bd52467f9b25c536e` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_01\scenes\mws_pac_01.scene` / scene / 4 -> 144 -> 146 |
| `6258d08b4ff3db56955b` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_01\mws_pac_01.questphase` / h7 / 28 -> 30 -> 13 |
| `647ea9ce31c01a3e6527` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_01\mws_pac_01.questphase` / h7 / 2 -> 4 -> 28 |
| `7111d151fcdadbda735b` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_01\scenes\mws_pac_01.scene` / scene / 144 -> 151 -> 160 |
| `724a3b4e8f96b3e6f249` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_01\mws_pac_01.questphase` / h35 / 9 -> 6 -> 7 |
| `80eef33a2f0c64d4d417` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_01\scenes\mws_pac_01.scene` / scene / 174 -> 166 -> 8 |
| `987122e5e2fcd167cf6c` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_01\mws_pac_01.questphase` / h35 / 0 -> 2 -> 8 |
| `9bcefd0d8dbfc24fb456` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_01\mws_pac_01.questphase` / h35 / 0 -> 5 -> 10 |
| `9c5162f63a419a5d6f46` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_01\scenes\mws_pac_01.scene` / scene / 179 -> 1 -> 99 |
| `a12138a3a146a35163df` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_01\mws_pac_01.questphase` / h7 / 30 -> 13 -> 12 |
| `a1404b16fab430ba81cc` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_01\scenes\mws_pac_01.scene` / scene / 179 -> 1 -> 111 |
| `a5ea6f917ed6dbcd90fb` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_01\mws_pac_01.questphase` / h7 / 4 -> 28 -> 30 |
| `a83b22c47fa1d333e4d8` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_01\mws_pac_01.questphase` / h35 / 2 -> 8 -> 9 |
| `ae773aa587365d33cd27` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_01\scenes\mws_pac_01.scene` / scene / 170 -> 116 -> 94 |
| `b4210655ef3333c0f4ed` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_01\mws_pac_01.questphase` / h35 / 9 -> 6 -> 4 |
| `c8b3108c074b0828457d` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_01\scenes\mws_pac_01.scene` / scene / 144 -> 151 -> 159 |
| `ce2753c57175dffe5803` | 1 | `base\open_world\mini_world_stories\pacifica\mws_pac_01\scenes\mws_pac_01.scene` / scene / 146 -> 179 -> 1 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
