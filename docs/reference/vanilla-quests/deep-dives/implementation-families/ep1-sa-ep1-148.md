# ep1-sa-ep1-148

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_148\sa_ep1_148.questphase` | content candidate | 5 / 0 | ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_additional_content_randomizer.questphase; ep1\openworld\sandbox_activities\courier_spot\loop_phases\sa_ep1_courier_police_manager.questphase |

## Journal paths observed in these resources

- `ep1/points_of_interest/sandbox_activities/sa_ep1_51`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 6 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 6 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 8 |
| `questEventManagerNodeDefinition` | 39 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 33 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 8 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 14 |
| `questLogicalXorNodeDefinition` | 8 |
| `questMiscAICommandNode` | 1 |
| `questMovePuppetNodeDefinition[questFollowParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 7 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 18 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 7 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 12 |
| `questPauseConditionNodeDefinition[questGatherTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 24 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 6 |
| `questRandomizerNodeDefinition` | 12 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 38 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 1 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 11 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2e1ee5a1324dbeeb9071` | 18 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_148\sa_ep1_148.questphase` / h0 / 29 -> 26 -> 31 |
| `20a77143a898bc753a26` | 15 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_148\sa_ep1_148.questphase` / h327 / 135 -> 134 -> 139 |
| `4c86e9d12122e122fabf` | 8 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_148\sa_ep1_148.questphase` / h327 / 162 -> 137 -> 135 |
| `415c2c7ab8d34be7e55a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_148\sa_ep1_148.questphase` / h0 / 83 -> 84 -> 79 |
| `97f583e0a8ff557a0b2a` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_148\sa_ep1_148.questphase` / h1157 / 49 -> 82 -> 84 |
| `e6a74d0120b15ec0f02c` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_148\sa_ep1_148.questphase` / h327 / 137 -> 135 -> 134 |
| `f2df22e3cb8f964cb634` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_148\sa_ep1_148.questphase` / h1157 / 49 -> 82 -> 85 |
| `fccbd9cf1c9292c360bf` | 7 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_148\sa_ep1_148.questphase` / h1157 / 49 -> 82 -> 51 |
| `30d6d5448c2b24a092f4` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_148\sa_ep1_148.questphase` / h327 / 41 -> 106 -> 104 |
| `35398687ac04ff110ad0` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_148\sa_ep1_148.questphase` / h327 / 106 -> 102 -> 105 |
| `593e17bd1c9a456e6bde` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_148\sa_ep1_148.questphase` / h327 / 104 -> 105 -> 128 |
| `5c61b1557cd30faef53c` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_148\sa_ep1_148.questphase` / h327 / 55 -> 116 -> 57 |
| `7c781f52e78dc0d251df` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_148\sa_ep1_148.questphase` / h327 / 102 -> 105 -> 128 |
| `8bdf0da350d602cbf970` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_148\sa_ep1_148.questphase` / h327 / 136 -> 144 -> 160 |
| `95098b5ad8804e28c8c4` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_148\sa_ep1_148.questphase` / h327 / 160 -> 146 -> 145 |
| `c9170fb2e5c18a121162` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_148\sa_ep1_148.questphase` / h327 / 140 -> 136 -> 154 |
| `ec56186049f4b470a01a` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_148\sa_ep1_148.questphase` / h327 / 106 -> 104 -> 105 |
| `f36b4271f8b5e18f5d45` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_148\sa_ep1_148.questphase` / h327 / 140 -> 136 -> 144 |
| `fe740361380ffc128c81` | 6 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_148\sa_ep1_148.questphase` / h327 / 41 -> 106 -> 102 |
| `4d51b376e33439a8c9e4` | 5 | `ep1\openworld\sandbox_activities\courier_spot\sa_ep1_148\sa_ep1_148.questphase` / h0 / 84 -> 79 -> 98 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
