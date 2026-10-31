# ep1-wst-ep1-04

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.quest` | content candidate | 1 / 0 | ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase |
| `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` | content candidate | 1 / 0 |  |
| `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04_bugfixing.questphase` | repair | 2 / 0 |  |

## Journal paths observed in these resources

- `ep1/quests/minor_quest/wst_ep1_04`
- `ep1/quests/minor_quest/wst_ep1_04/description`
- `ep1/quests/minor_quest/wst_ep1_04/wst_ep1_04/enter_the_code`
- `ep1/quests/minor_quest/wst_ep1_04/wst_ep1_04/go_to_rinders_garage`
- `ep1/quests/minor_quest/wst_ep1_04/wst_ep1_04/loot_the_box`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questDeletionMarkerNodeDefinition` | 5 |
| `questEventManagerNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 4 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_ActionProperty,questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 1 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 9 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 9 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questRealtimeDelay_ConditionType,questTimeCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTickDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questPhaseNodeDefinition` | 2 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `bf9c73a58053b668d2fb` | 4 | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` / h0 / 0 -> 20 -> 6 |
| `9380dda43f90ecd62efb` | 3 | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` / h0 / 39 -> 40 -> 53 |
| `6cbd4aaf3157582f705c` | 2 | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` / h0 / 29 -> 38 -> 43 |
| `0781ef00ea04c05ee418` | 1 | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` / h0 / 8 -> 29 -> 38 |
| `19a35d27ae1aaa1f92ef` | 1 | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` / h0 / 3 -> 10 -> 14 |
| `256f5695ecda8ef528d7` | 1 | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04_bugfixing.questphase` / h31 / 4 -> 5 -> 6 |
| `2c086284fbf257114744` | 1 | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` / h0 / 6 -> 13 -> 19 |
| `2face0cc90a9b0fee909` | 1 | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` / h0 / 35 -> 8 -> 29 |
| `4bd64eac2ef7a8cc2f2c` | 1 | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` / h0 / 37 -> 31 -> 1 |
| `5c76d3bf7160f29b884f` | 1 | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04_bugfixing.questphase` / h31 / 2 -> 3 -> 8 |
| `7a88801c0d5664236a9c` | 1 | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` / h0 / 9 -> 46 -> 45 |
| `88c85d9bbfa1b9735715` | 1 | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04_bugfixing.questphase` / h31 / 9 -> 4 -> 5 |
| `8a4f596250b8a523b4ca` | 1 | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04_bugfixing.questphase` / h31 / 8 -> 9 -> 4 |
| `8c0231ff341cea704782` | 1 | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` / h0 / 46 -> 47 -> 48 |
| `8dd5c44ffdb3cb8886ef` | 1 | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04_bugfixing.questphase` / h31 / 3 -> 8 -> 9 |
| `8ecf570bca7d76168ecc` | 1 | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` / h0 / 45 -> 3 -> 10 |
| `9890c704bd8503fd1750` | 1 | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` / h0 / 11 -> 36 -> 35 |
| `9ecad89a3912aae53f47` | 1 | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` / h0 / 32 -> 9 -> 46 |
| `b3205573f616e5f366a7` | 1 | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` / h0 / 45 -> 24 -> 22 |
| `b5032542f6cc4ccd2d26` | 1 | `ep1\openworld\world_stories\wst_ep1_04\wst_ep1_04.questphase` / h0 / 20 -> 6 -> 13 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
