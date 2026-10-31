# ep1-wst-ep1-10

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_10\wst_ep1_10.questphase` | content candidate | 1 / 0 | ep1\openworld\world_stories\wst_ep1_10\wst_ep1_10_scavengers_chat.scene |
| `ep1\openworld\world_stories\wst_ep1_10\wst_ep1_10_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\world_stories\wst_ep1_10\wst_ep1_10_scavengers_chat.scene` | content candidate | 0 / 3 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 2 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questMiscAICommandNode` | 2 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 6 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 5 |
| `scnEndNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `20a77143a898bc753a26` | 3 | `ep1\openworld\world_stories\wst_ep1_10\wst_ep1_10.questphase` / h0 / 1 -> 36 -> 37 |
| `163b243e32c0bb8c4eb7` | 2 | `ep1\openworld\world_stories\wst_ep1_10\wst_ep1_10.questphase` / h0 / 41 -> 40 -> 4 |
| `2e1ee5a1324dbeeb9071` | 2 | `ep1\openworld\world_stories\wst_ep1_10\wst_ep1_10.questphase` / h0 / 36 -> 37 -> 28 |
| `00c3ca0ac0b55db639ca` | 1 | `ep1\openworld\world_stories\wst_ep1_10\wst_ep1_10.questphase` / h0 / 5 -> 1 -> 36 |
| `16d77bd449bf9f18d921` | 1 | `ep1\openworld\world_stories\wst_ep1_10\wst_ep1_10.questphase` / h0 / 0 -> 6 -> 25 |
| `18be198845c90c6bb3c8` | 1 | `ep1\openworld\world_stories\wst_ep1_10\wst_ep1_10.questphase` / h0 / 9 -> 8 -> 10 |
| `20e35486dce84a4318f3` | 1 | `ep1\openworld\world_stories\wst_ep1_10\wst_ep1_10.questphase` / h0 / 41 -> 40 -> 30 |
| `215ca95d939006973a7d` | 1 | `ep1\openworld\world_stories\wst_ep1_10\wst_ep1_10.questphase` / h0 / 24 -> 27 -> 57 |
| `450070a422af0dc83c00` | 1 | `ep1\openworld\world_stories\wst_ep1_10\wst_ep1_10.questphase` / h0 / 43 -> 44 -> 45 |
| `4798537ca16e1216226c` | 1 | `ep1\openworld\world_stories\wst_ep1_10\wst_ep1_10.questphase` / h0 / 38 -> 55 -> 47 |
| `4c4ed316b40e2958b53f` | 1 | `ep1\openworld\world_stories\wst_ep1_10\wst_ep1_10.questphase` / h0 / 55 -> 33 -> 54 |
| `4fe64daeff05e511ddfb` | 1 | `ep1\openworld\world_stories\wst_ep1_10\wst_ep1_10.questphase` / h0 / 4 -> 9 -> 8 |
| `699a715a7edd9668a32e` | 1 | `ep1\openworld\world_stories\wst_ep1_10\wst_ep1_10.questphase` / h0 / 11 -> 24 -> 27 |
| `6e3b35557bcc40a5d957` | 1 | `ep1\openworld\world_stories\wst_ep1_10\wst_ep1_10.questphase` / h0 / 10 -> 35 -> 11 |
| `6e9d673e1e846e4cff4c` | 1 | `ep1\openworld\world_stories\wst_ep1_10\wst_ep1_10.questphase` / h0 / 35 -> 11 -> 24 |
| `83a3757c3e54bd269e2e` | 1 | `ep1\openworld\world_stories\wst_ep1_10\wst_ep1_10.questphase` / h0 / 40 -> 4 -> 16 |
| `85d7311426e632fa016e` | 1 | `ep1\openworld\world_stories\wst_ep1_10\wst_ep1_10.questphase` / h0 / 40 -> 4 -> 9 |
| `8cd3b647ae3f592ad947` | 1 | `ep1\openworld\world_stories\wst_ep1_10\wst_ep1_10_scavengers_chat.scene` / scene / 1 -> 4 -> 2 |
| `8f977cf6ceec0bf5cd5f` | 1 | `ep1\openworld\world_stories\wst_ep1_10\wst_ep1_10.questphase` / h0 / 55 -> 47 -> 41 |
| `bee1f62dab6be5337bda` | 1 | `ep1\openworld\world_stories\wst_ep1_10\wst_ep1_10.questphase` / h0 / 8 -> 10 -> 35 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
