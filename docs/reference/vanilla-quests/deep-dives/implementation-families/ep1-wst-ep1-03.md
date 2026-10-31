# ep1-wst-ep1-03

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03.quest` | content candidate | 1 / 0 | ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03.questphase |
| `ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03.questphase` | content candidate | 1 / 0 | ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03_silverhand.scene |
| `ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03_bugfixing.questphase` | repair | 2 / 0 |  |
| `ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03_silverhand.scene` | content candidate | 0 / 10 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 4 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questTimeManagerNodeDefinition[questSetTime_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnEndNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `0fdad4c8a8b4964c866f` | 1 | `ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03_silverhand.scene` / scene / 4 -> 19 -> 17 |
| `1a3e365fa34d855352fe` | 1 | `ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03_silverhand.scene` / scene / 13 -> 8 -> 4 |
| `28545b5893ed55a6c748` | 1 | `ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03.questphase` / h0 / 11 -> 6 -> 16 |
| `36dfffa993b51ca3c390` | 1 | `ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03.questphase` / h0 / 21 -> 4 -> 18 |
| `43fa485b791b83f1331b` | 1 | `ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03.questphase` / h0 / 9 -> 19 -> 20 |
| `4f210d93383983304c1e` | 1 | `ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03_bugfixing.questphase` / h22 / 5 -> 8 -> 9 |
| `51f8c44d9fad8914cd26` | 1 | `ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03_silverhand.scene` / scene / 19 -> 17 -> 2 |
| `598baf1c7bafcd231abf` | 1 | `ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03.questphase` / h0 / 21 -> 4 -> 5 |
| `5c76d3bf7160f29b884f` | 1 | `ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03_bugfixing.questphase` / h22 / 2 -> 3 -> 4 |
| `6454d67fc8f0a60aadef` | 1 | `ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03_bugfixing.questphase` / h22 / 6 -> 5 -> 8 |
| `69435bb7b4e44374ca53` | 1 | `ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03_silverhand.scene` / scene / 1 -> 37 -> 33 |
| `714f33b0cd4d2ee9c385` | 1 | `ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03_silverhand.scene` / scene / 33 -> 5 -> 13 |
| `7cbe8bf33e57db886e54` | 1 | `ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03_silverhand.scene` / scene / 5 -> 13 -> 8 |
| `82485e35636203d8ca6c` | 1 | `ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03.questphase` / h0 / 5 -> 8 -> 13 |
| `8932aa094f8fb5fef635` | 1 | `ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03_bugfixing.questphase` / h22 / 7 -> 6 -> 5 |
| `8dd5c44ffdb3cb8886ef` | 1 | `ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03_bugfixing.questphase` / h22 / 3 -> 4 -> 7 |
| `9555178c9f24c6404fbe` | 1 | `ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03.questphase` / h0 / 15 -> 11 -> 6 |
| `95a40631bf8ba3a9020c` | 1 | `ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03.questphase` / h0 / 4 -> 18 -> 17 |
| `9c634ff27b9a7aa77918` | 1 | `ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03_bugfixing.questphase` / h0 / 0 -> 4 -> 3 |
| `a1afa7580300ad2ecba4` | 1 | `ep1\openworld\world_stories\wst_ep1_03\wst_ep1_03_silverhand.scene` / scene / 8 -> 4 -> 19 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
