# ep1-mws-cz-16

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_16\mws_cz_16_locker.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_16\mws_cz_16_locker.quest` | content candidate | 1 / 0 | ep1\openworld\mini_world_stories\combat_zone\mws_cz_16\phases\mws_cz_16.questphase |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_16\phases\mws_cz_16.questphase` | content candidate | 2 / 0 | ep1\openworld\mini_world_stories\combat_zone\mws_cz_16\scenes\mws_cz_16_device.scene |
| `ep1\openworld\mini_world_stories\combat_zone\mws_cz_16\scenes\mws_cz_16_device.scene` | content candidate | 0 / 3 |  |

## Journal paths observed in these resources

- `ep1/points_of_interest/service_points/cz_mws_cz_16_locker`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCutControlNodeDefinition` | 1 |
| `questEndNodeDefinition` | 1 |
| `questInputNodeDefinition` | 2 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 128 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 2 |
| `questLogicalHubNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 4 |
| `questPhaseNodeDefinition` | 2 |
| `questRandomizerNodeDefinition` | 5 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questUIManagerNodeDefinition[questWarningMessage_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |
| `scnChoiceNode[questPaymentCondition,questPaymentFixedAmount_ConditionType,scnChoiceNodeNsAttachToPropParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnPropId,scnscreenplayItemId]` | 1 |
| `scnEndNode[scnNodeId]` | 1 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `1ae94ee872986dd79c0d` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_16\phases\mws_cz_16.questphase` / h0 / 0 -> 8 -> 9 |
| `26fed350cd7b76c8a677` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_16\phases\mws_cz_16.questphase` / h0 / 17 -> 15 -> 4 |
| `291c141e890402cc28d8` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_16\phases\mws_cz_16.questphase` / h37 / 0 -> 147 -> 144 |
| `3654595c4c69efca4b35` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_16\phases\mws_cz_16.questphase` / h0 / 4 -> 5 -> 3 |
| `48f71b371ce727fba597` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_16\phases\mws_cz_16.questphase` / h0 / 5 -> 3 -> 4 |
| `4c52f83512e72ae88287` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_16\phases\mws_cz_16.questphase` / h0 / 3 -> 4 -> 5 |
| `4d6e41e9f926f452ecdb` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_16\phases\mws_cz_16.questphase` / h37 / 0 -> 148 -> 146 |
| `5975080c56e62cc2b457` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_16\phases\mws_cz_16.questphase` / h37 / 147 -> 144 -> 4 |
| `a92ce5126e9872f7219d` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_16\phases\mws_cz_16.questphase` / h37 / 148 -> 146 -> 6 |
| `ecbb206e9bb4f3b3007e` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_16\phases\mws_cz_16.questphase` / h37 / 147 -> 144 -> 45 |
| `f17e722bc3349eb411a6` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_16\phases\mws_cz_16.questphase` / h0 / 0 -> 2 -> 16 |
| `f7645eda6995b616936e` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_16\phases\mws_cz_16.questphase` / h0 / 15 -> 4 -> 5 |
| `fbb2a7d084364182b791` | 1 | `ep1\openworld\mini_world_stories\combat_zone\mws_cz_16\phases\mws_cz_16.questphase` / h0 / 9 -> 17 -> 15 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
