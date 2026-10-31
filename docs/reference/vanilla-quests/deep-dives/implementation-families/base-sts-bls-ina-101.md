# base-sts-bls-ina-101

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\community\ina_101_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\phases\sts_bls_ina_101_gameplay.questphase` | content candidate | 12 / 0 | base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\scenes\ina_101_chat.scene |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\phases\sts_bls_ina_101_open_world.questphase` | content candidate | 5 / 0 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\phases\sts_bls_ina_101_phase.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\phases\sts_bls_ina_101_gameplay.questphase; base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\phases\sts_bls_ina_101_open_world.questphase |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\scenes\ina_101_chat.scene` | content candidate | 0 / 3 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\sts_bls_ina_101.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\sts_bls_ina_101.quest` | content candidate | 1 / 0 | base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\phases\sts_bls_ina_101_phase.questphase |

## Journal paths observed in these resources

- `contacts/dakota_smith/sts_bls_ina_101_brief`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_101/sts_bls_ina_101`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_101/sts_bls_ina_101/find`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_101/sts_bls_ina_101/get_inside`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_101/sts_bls_ina_101/get_out`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_101/sts_bls_ina_101/leave`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_101/sts_bls_ina_101/take_down`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 2 |
| `questInputNodeDefinition` | 18 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 4 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 13 |
| `questLogicalXorNodeDefinition` | 2 |
| `questMiscAICommandNode` | 7 |
| `questOutputNodeDefinition` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 8 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questSensesCondition,questVision_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 7 |
| `questPhaseNodeDefinition` | 18 |
| `questPhoneManagerNodeDefinition[questOpenMessage_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 4 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 3 |
| `scnEndNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `138cff49923a75e07348` | 4 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\phases\sts_bls_ina_101_open_world.questphase` / h29 / 16 -> 17 -> 18 |
| `3535ee3b356c051e5fe9` | 4 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\phases\sts_bls_ina_101_gameplay.questphase` / h64 / 0 -> 2 -> 3 |
| `a53561b4c002bc02b58a` | 3 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\phases\sts_bls_ina_101_open_world.questphase` / h29 / 14 -> 16 -> 17 |
| `ed2137595a890fc5858c` | 3 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\phases\sts_bls_ina_101_gameplay.questphase` / h133 / 6 -> 7 -> 3 |
| `2f0eea9ff31e1b057178` | 2 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\phases\sts_bls_ina_101_phase.questphase` / h0 / 5 -> 8 -> 3 |
| `6f633a1a8a493edf4436` | 2 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\phases\sts_bls_ina_101_gameplay.questphase` / h133 / 0 -> 2 -> 4 |
| `8bd54738c2c85f70192e` | 2 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\phases\sts_bls_ina_101_open_world.questphase` / h29 / 9 -> 11 -> 13 |
| `9df46c3fb14e034d520b` | 2 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\phases\sts_bls_ina_101_open_world.questphase` / h29 / 12 -> 14 -> 16 |
| `beac811f7dfe2ac38d1a` | 2 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\phases\sts_bls_ina_101_open_world.questphase` / h29 / 11 -> 12 -> 14 |
| `0737207b51fc12c42573` | 1 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\phases\sts_bls_ina_101_open_world.questphase` / h29 / 6 -> 8 -> 27 |
| `1618d8c3e60a5672fe4f` | 1 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\phases\sts_bls_ina_101_open_world.questphase` / h29 / 28 -> 29 -> 4 |
| `2179483c4d9ed5db29c9` | 1 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\phases\sts_bls_ina_101_phase.questphase` / h0 / 0 -> 6 -> 5 |
| `2a18d536739310eb7e61` | 1 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\phases\sts_bls_ina_101_open_world.questphase` / h29 / 27 -> 9 -> 11 |
| `33622e6e4a84447feebf` | 1 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\phases\sts_bls_ina_101_open_world.questphase` / h29 / 7 -> 27 -> 9 |
| `3f08205082c0c7c632d2` | 1 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\phases\sts_bls_ina_101_open_world.questphase` / h29 / 17 -> 18 -> 22 |
| `4724163561c9b50c63e6` | 1 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\phases\sts_bls_ina_101_open_world.questphase` / h29 / 8 -> 27 -> 9 |
| `4e9253a72e6b0134b8dd` | 1 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\phases\sts_bls_ina_101_open_world.questphase` / h29 / 4 -> 5 -> 6 |
| `6c608b5828b20f65d7e2` | 1 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\phases\sts_bls_ina_101_gameplay.questphase` / h7 / 2 -> 4 -> 1 |
| `77e76e66a119b9a4b73f` | 1 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\phases\sts_bls_ina_101_open_world.questphase` / h29 / 20 -> 21 -> 30 |
| `7b28e67428f27a091a2d` | 1 | `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_101\phases\sts_bls_ina_101_phase.questphase` / h0 / 6 -> 5 -> 8 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
