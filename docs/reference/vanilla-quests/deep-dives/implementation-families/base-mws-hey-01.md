# base-mws-hey-01

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\heywood\mws_hey_01\characters\mws_hey_01.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\heywood\mws_hey_01\mws_hey_01.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\heywood\mws_hey_01\mws_hey_01.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\heywood\mws_hey_01\mws_hey_01.questphase |
| `base\open_world\mini_world_stories\heywood\mws_hey_01\mws_hey_01.questphase` | content candidate | 3 / 0 | base\open_world\mini_world_stories\heywood\mws_hey_01\scenes\mws_hey_01_follow.scene |
| `base\open_world\mini_world_stories\heywood\mws_hey_01\scenes\mws_hey_01_follow.scene` | content candidate | 0 / 56 |  |

## Journal paths observed in these resources

- `quests/minor_quest/mq014_zen/01_hook/01_approach_master`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questCutControlNodeDefinition` | 2 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questInputNodeDefinition` | 5 |
| `questLogicalHubNodeDefinition` | 14 |
| `questMovePuppetNodeDefinition` | 1 |
| `questMovePuppetNodeDefinition[questFollowParams,questUniversalRef]` | 2 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 10 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questCharacterCombat_ConditionType,questCharacterCondition,questContentCondition,questContentLock_ConditionType,questLogicalCondition,questSensesCondition,questSystemCondition,questVision_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 10 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 7 |
| `questPhaseNodeDefinition` | 2 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRandomizerNodeDefinition` | 4 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 5 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 8 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |
| `scnCutControlNode[scnNodeId]` | 4 |
| `scnEndNode[scnNodeId]` | 4 |
| `scnHubNode[scnNodeId]` | 11 |
| `scnRandomizerNode[scnNodeId]` | 3 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 10 |
| `scnStartNode[scnNodeId]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `62270548ca59ef273a9b` | 9 | `base\open_world\mini_world_stories\heywood\mws_hey_01\scenes\mws_hey_01_follow.scene` / scene / 38 -> 126 -> 14 |
| `e354b8fd6f609b8a29e2` | 8 | `base\open_world\mini_world_stories\heywood\mws_hey_01\scenes\mws_hey_01_follow.scene` / scene / 126 -> 14 -> 219 |
| `59b2a535800f1c1b497d` | 7 | `base\open_world\mini_world_stories\heywood\mws_hey_01\mws_hey_01.questphase` / h145 / 30 -> 34 -> 4 |
| `ec728d82d970f30670c0` | 6 | `base\open_world\mini_world_stories\heywood\mws_hey_01\mws_hey_01.questphase` / h145 / 11 -> 15 -> 16 |
| `864b518c28a376ce9236` | 5 | `base\open_world\mini_world_stories\heywood\mws_hey_01\scenes\mws_hey_01_follow.scene` / scene / 91 -> 54 -> 50 |
| `f03db56fa93fc8748f46` | 5 | `base\open_world\mini_world_stories\heywood\mws_hey_01\scenes\mws_hey_01_follow.scene` / scene / 54 -> 181 -> 2 |
| `0e0a15879adbbe767284` | 4 | `base\open_world\mini_world_stories\heywood\mws_hey_01\scenes\mws_hey_01_follow.scene` / scene / 257 -> 280 -> 220 |
| `10e6dec063a478152aa0` | 4 | `base\open_world\mini_world_stories\heywood\mws_hey_01\scenes\mws_hey_01_follow.scene` / scene / 14 -> 219 -> 296 |
| `1c6763dc4f7bebbba4f1` | 4 | `base\open_world\mini_world_stories\heywood\mws_hey_01\scenes\mws_hey_01_follow.scene` / scene / 14 -> 219 -> 257 |
| `1f42567b20d342a50044` | 4 | `base\open_world\mini_world_stories\heywood\mws_hey_01\scenes\mws_hey_01_follow.scene` / scene / 257 -> 280 -> 227 |
| `237ae176433605c5d8b9` | 4 | `base\open_world\mini_world_stories\heywood\mws_hey_01\scenes\mws_hey_01_follow.scene` / scene / 257 -> 280 -> 225 |
| `53211b465a95c52e6571` | 4 | `base\open_world\mini_world_stories\heywood\mws_hey_01\scenes\mws_hey_01_follow.scene` / scene / 14 -> 219 -> 290 |
| `6b13d47ffe5d2c25d345` | 4 | `base\open_world\mini_world_stories\heywood\mws_hey_01\scenes\mws_hey_01_follow.scene` / scene / 14 -> 219 -> 294 |
| `84a7e4dace992eecef6c` | 4 | `base\open_world\mini_world_stories\heywood\mws_hey_01\scenes\mws_hey_01_follow.scene` / scene / 38 -> 126 -> 220 |
| `a737198437424e66c57c` | 4 | `base\open_world\mini_world_stories\heywood\mws_hey_01\scenes\mws_hey_01_follow.scene` / scene / 235 -> 151 -> 191 |
| `2e7bf31036e03d72efe9` | 3 | `base\open_world\mini_world_stories\heywood\mws_hey_01\scenes\mws_hey_01_follow.scene` / scene / 38 -> 126 -> 374 |
| `d2f62476b55deb28e27d` | 3 | `base\open_world\mini_world_stories\heywood\mws_hey_01\scenes\mws_hey_01_follow.scene` / scene / 370 -> 345 -> 359 |
| `f1aa346c60fffbd540e8` | 3 | `base\open_world\mini_world_stories\heywood\mws_hey_01\mws_hey_01.questphase` / h18 / 24 -> 28 -> 27 |
| `05fb15bd4551094b663b` | 2 | `base\open_world\mini_world_stories\heywood\mws_hey_01\mws_hey_01.questphase` / h145 / 14 -> 11 -> 15 |
| `2be70c555d6a95de2942` | 2 | `base\open_world\mini_world_stories\heywood\mws_hey_01\scenes\mws_hey_01_follow.scene` / scene / 96 -> 113 -> 345 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
