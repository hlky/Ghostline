# ep1-sts-ep1-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\street_stories\sts_ep1_02\communities\sts_ep1_02_enemies_last_room.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\street_stories\sts_ep1_02\communities\sts_ep1_02_enemies_outside.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\street_stories\sts_ep1_02\communities\sts_ep1_02_enemies_outside_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\street_stories\sts_ep1_02\communities\sts_ep1_02_enemies_room1.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\street_stories\sts_ep1_02\communities\sts_ep1_02_enemies_room_001.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\street_stories\sts_ep1_02\communities\sts_ep1_02_enemies_room_002.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\street_stories\sts_ep1_02\communities\sts_ep1_02_enemies_room_003.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\street_stories\sts_ep1_02\communities\sts_ep1_02_enemies_room_turrets.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\street_stories\sts_ep1_02\communities\sts_ep1_02_enemies_tunnel.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\street_stories\sts_ep1_02\phases\sts_ep1_02_combat.questphase` | content candidate | 9 / 0 | ep1\openworld\street_stories\sts_ep1_02\scenes\sts_ep1_02_chats.scene |

## Journal paths observed in these resources

- `ep1/quests/street_stories/sts_ep1_02/sts_ep1_02/meet_at_gate_002`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 1 |
| `questCutControlNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 2 |
| `questInputNodeDefinition` | 14 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 1 |
| `questMiscAICommandNode` | 18 |
| `questOutputNodeDefinition` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterTriggeredCombatInSecuritySystem_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 6 |
| `questPhaseNodeDefinition` | 8 |
| `questSceneNodeDefinition[scnWorldMarker]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 9 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `95b7458b3ffd83fd4357` | 16 | `ep1\openworld\street_stories\sts_ep1_02\phases\sts_ep1_02_combat.questphase` / h172 / 2 -> 4 -> 9 |
| `987122e5e2fcd167cf6c` | 4 | `ep1\openworld\street_stories\sts_ep1_02\phases\sts_ep1_02_combat.questphase` / h9 / 0 -> 2 -> 3 |
| `f3a269b6a97862bc211c` | 4 | `ep1\openworld\street_stories\sts_ep1_02\phases\sts_ep1_02_combat.questphase` / h172 / 2 -> 4 -> 12 |
| `f802ad66d4ceea2d0aff` | 2 | `ep1\openworld\street_stories\sts_ep1_02\phases\sts_ep1_02_combat.questphase` / h59 / 0 -> 13 -> 9 |
| `0e55e762d8ff58e5ae49` | 1 | `ep1\openworld\street_stories\sts_ep1_02\phases\sts_ep1_02_combat.questphase` / h9 / 15 -> 16 -> 11 |
| `0f41ce87ed388a4089dd` | 1 | `ep1\openworld\street_stories\sts_ep1_02\phases\sts_ep1_02_combat.questphase` / h172 / 4 -> 24 -> 23 |
| `2251a3c44ea8a153bc79` | 1 | `ep1\openworld\street_stories\sts_ep1_02\phases\sts_ep1_02_combat.questphase` / h478 / 2 -> 20 -> 5 |
| `3e6409a613f85e1670aa` | 1 | `ep1\openworld\street_stories\sts_ep1_02\phases\sts_ep1_02_combat.questphase` / h59 / 0 -> 26 -> 27 |
| `3ff43607d17c17b2e0d6` | 1 | `ep1\openworld\street_stories\sts_ep1_02\phases\sts_ep1_02_combat.questphase` / h59 / 0 -> 21 -> 19 |
| `658fe17f8b47d2c016b7` | 1 | `ep1\openworld\street_stories\sts_ep1_02\phases\sts_ep1_02_combat.questphase` / h478 / 2 -> 20 -> 1 |
| `86c6b08a5631dffee988` | 1 | `ep1\openworld\street_stories\sts_ep1_02\phases\sts_ep1_02_combat.questphase` / h172 / 16 -> 12 -> 1 |
| `8d10896873df5c62014e` | 1 | `ep1\openworld\street_stories\sts_ep1_02\phases\sts_ep1_02_combat.questphase` / h172 / 2 -> 4 -> 24 |
| `96d12e2f451fb48e0c50` | 1 | `ep1\openworld\street_stories\sts_ep1_02\phases\sts_ep1_02_combat.questphase` / h9 / 2 -> 3 -> 15 |
| `9cb82fbabfd13bc9dbf8` | 1 | `ep1\openworld\street_stories\sts_ep1_02\phases\sts_ep1_02_combat.questphase` / h478 / 20 -> 5 -> 9 |
| `9d7eb0ead19b2e7036f6` | 1 | `ep1\openworld\street_stories\sts_ep1_02\phases\sts_ep1_02_combat.questphase` / h138 / 0 -> 4 -> 5 |
| `b3396120b0ea52314aa7` | 1 | `ep1\openworld\street_stories\sts_ep1_02\phases\sts_ep1_02_combat.questphase` / h478 / 2 -> 21 -> 22 |
| `e4f4f6f55aa491ef140a` | 1 | `ep1\openworld\street_stories\sts_ep1_02\phases\sts_ep1_02_combat.questphase` / h59 / 0 -> 29 -> 30 |
| `fa5824c0efca270073ba` | 1 | `ep1\openworld\street_stories\sts_ep1_02\phases\sts_ep1_02_combat.questphase` / h9 / 3 -> 15 -> 16 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
