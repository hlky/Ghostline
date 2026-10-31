# ep1-wst-ep1-07

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_07\wst_ep1_07.questphase` | content candidate | 1 / 0 | ep1\openworld\scene\chats\ferronia_downes\cz_ferronia_downes_chat_013.scene; ep1\quest\tertiary_characters\default_dialogs\michael_maldonado_default\michael_maldonado_default.scene |

## Journal paths observed in these resources

- `ep1/contacts/michael_maldonado`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questCutControlNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 3 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 2 |
| `questInputNodeDefinition` | 1 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 7 |
| `questLogicalAndNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 5 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questPhoneManagerNodeDefinition[questAddRemoveContact_NodeType,questChangeContactList_NodeTypeParams]` | 1 |
| `questSceneNodeDefinition[scnInterruptionScenarioId,scnOverrideInterruptionScenario_InterruptionOperation,scnOverrideTalkOnReturn_InterruptionScenarioOperation,scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 4 |
| `questUIManagerNodeDefinition[questSetHUDEntryForcedVisibility_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 8 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `9380dda43f90ecd62efb` | 5 | `ep1\openworld\world_stories\wst_ep1_07\wst_ep1_07.questphase` / h0 / 26 -> 27 -> 28 |
| `bfe95df47bd1ca67330f` | 4 | `ep1\openworld\world_stories\wst_ep1_07\wst_ep1_07.questphase` / h0 / 39 -> 2 -> 51 |
| `29cb69424d0ff586110c` | 3 | `ep1\openworld\world_stories\wst_ep1_07\wst_ep1_07.questphase` / h0 / 69 -> 68 -> 64 |
| `27d63236000f16d8a9a3` | 2 | `ep1\openworld\world_stories\wst_ep1_07\wst_ep1_07.questphase` / h0 / 0 -> 5 -> 12 |
| `76696e728ecd1de1569f` | 2 | `ep1\openworld\world_stories\wst_ep1_07\wst_ep1_07.questphase` / h0 / 68 -> 65 -> 59 |
| `77276effa8df29e8ab90` | 2 | `ep1\openworld\world_stories\wst_ep1_07\wst_ep1_07.questphase` / h0 / 66 -> 58 -> 62 |
| `b48a0de3dd4cd342df90` | 2 | `ep1\openworld\world_stories\wst_ep1_07\wst_ep1_07.questphase` / h0 / 68 -> 58 -> 62 |
| `bd5d9ac85ae8af74b85e` | 2 | `ep1\openworld\world_stories\wst_ep1_07\wst_ep1_07.questphase` / h0 / 60 -> 65 -> 59 |
| `d9cdd14827cb8e3ac949` | 2 | `ep1\openworld\world_stories\wst_ep1_07\wst_ep1_07.questphase` / h0 / 69 -> 68 -> 58 |
| `10de5d2a81ab97879de5` | 1 | `ep1\openworld\world_stories\wst_ep1_07\wst_ep1_07.questphase` / h0 / 33 -> 77 -> 76 |
| `19c2b4ec29b433047073` | 1 | `ep1\openworld\world_stories\wst_ep1_07\wst_ep1_07.questphase` / h0 / 11 -> 69 -> 68 |
| `1a847192f6cd2bcebaf2` | 1 | `ep1\openworld\world_stories\wst_ep1_07\wst_ep1_07.questphase` / h0 / 17 -> 16 -> 20 |
| `216dc4afa1cdff93031c` | 1 | `ep1\openworld\world_stories\wst_ep1_07\wst_ep1_07.questphase` / h0 / 0 -> 5 -> 11 |
| `3420fb9b071ece981c66` | 1 | `ep1\openworld\world_stories\wst_ep1_07\wst_ep1_07.questphase` / h0 / 63 -> 61 -> 66 |
| `3dac218f6b7a359ab572` | 1 | `ep1\openworld\world_stories\wst_ep1_07\wst_ep1_07.questphase` / h0 / 5 -> 26 -> 27 |
| `3e2308cf17c02eba85b4` | 1 | `ep1\openworld\world_stories\wst_ep1_07\wst_ep1_07.questphase` / h0 / 22 -> 38 -> 37 |
| `4f62a97b40f7490e323d` | 1 | `ep1\openworld\world_stories\wst_ep1_07\wst_ep1_07.questphase` / h0 / 5 -> 39 -> 2 |
| `521a3dedf1e2f4f9d6f5` | 1 | `ep1\openworld\world_stories\wst_ep1_07\wst_ep1_07.questphase` / h0 / 5 -> 11 -> 69 |
| `531777d14c35fb07583a` | 1 | `ep1\openworld\world_stories\wst_ep1_07\wst_ep1_07.questphase` / h0 / 16 -> 20 -> 24 |
| `5fe297210a3c11607b9c` | 1 | `ep1\openworld\world_stories\wst_ep1_07\wst_ep1_07.questphase` / h0 / 5 -> 11 -> 58 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
