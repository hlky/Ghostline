# ep1-wst-ep1-06

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.quest` | content candidate | 1 / 0 | ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.questphase |
| `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.questphase` | content candidate | 1 / 0 | ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.questphase |
| `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06_bugfixing.questphase` | repair | 2 / 0 |  |

## Journal paths observed in these resources

- `contacts/mr_hands/sts_ep1_04/sts_ep1_04_sms_hasan_dead`
- `contacts/mr_hands/sts_ep1_04/sts_ep1_04_sms_hasan_dead_hands_answer_01`
- `contacts/mr_hands/sts_ep1_04/sts_ep1_04_sms_hasan_dead_hands_answer_02`
- `contacts/mr_hands/sts_ep1_04/sts_ep1_04_sms_hasan_dead_response`
- `contacts/mr_hands/sts_ep1_04/sts_ep1_04_sms_hasan_dead_response/v_response_sts_ep1_04_sms_hasan_dead_01`
- `contacts/mr_hands/sts_ep1_04/sts_ep1_04_sms_hasan_dead_response/v_response_sts_ep1_04_sms_hasan_dead_02`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 5 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questInputNodeDefinition` | 4 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 2 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentToken_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questPhaseNodeDefinition` | 3 |
| `questStartNodeDefinition` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `34a94443e680a228f2ef` | 2 | `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.questphase` / h0 / 11 -> 26 -> 28 |
| `3c92ff23000bff9fb9b4` | 2 | `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.questphase` / h0 / 17 -> 38 -> 24 |
| `60260fcd07467839d333` | 2 | `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.questphase` / h0 / 11 -> 12 -> 14 |
| `95a40631bf8ba3a9020c` | 2 | `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.questphase` / h0 / 38 -> 24 -> 10 |
| `be95ed609c623423854c` | 2 | `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.questphase` / h0 / 1 -> 11 -> 26 |
| `07a508d9181a1ec44ac6` | 1 | `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.questphase` / h0 / 19 -> 21 -> 22 |
| `190afe6d31978a672ef7` | 1 | `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.questphase` / h0 / 4 -> 8 -> 39 |
| `1fdaa711166fed260f40` | 1 | `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.questphase` / h0 / 8 -> 39 -> 40 |
| `20d0683a7148dd226b26` | 1 | `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.questphase` / h0 / 0 -> 4 -> 8 |
| `3411c04c289ccac5ebe2` | 1 | `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.questphase` / h0 / 8 -> 39 -> 41 |
| `408520bc6e291e2f901f` | 1 | `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.questphase` / h0 / 1 -> 11 -> 12 |
| `41a5ee696bceec6adb97` | 1 | `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.questphase` / h0 / 39 -> 41 -> 42 |
| `5c76d3bf7160f29b884f` | 1 | `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06_bugfixing.questphase` / h22 / 2 -> 3 -> 6 |
| `62ae9ec47ec7dbbf48de` | 1 | `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.questphase` / h0 / 14 -> 16 -> 13 |
| `7bfcd8df5888d6d0d606` | 1 | `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06_bugfixing.questphase` / h22 / 3 -> 6 -> 1 |
| `9af8a87f20a910659fa8` | 1 | `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.questphase` / h0 / 19 -> 21 -> 17 |
| `9c634ff27b9a7aa77918` | 1 | `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06_bugfixing.questphase` / h0 / 0 -> 4 -> 3 |
| `9c66ea906b584c015259` | 1 | `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.questphase` / h0 / 42 -> 17 -> 38 |
| `a979720eeb9c7a590667` | 1 | `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.questphase` / h0 / 39 -> 40 -> 42 |
| `ba386cef3b4bb2bcd6b2` | 1 | `ep1\openworld\world_stories\wst_ep1_06\wst_ep1_06.questphase` / h0 / 21 -> 17 -> 38 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
