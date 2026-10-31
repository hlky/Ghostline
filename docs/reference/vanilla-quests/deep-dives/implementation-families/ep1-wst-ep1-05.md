# ep1-wst-ep1-05

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.quest` | content candidate | 1 / 0 | ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase |
| `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` | content candidate | 1 / 0 | ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.questphase |

## Journal paths observed in these resources

- `contacts/mr_hands/sts_ep1_04/sts_ep1_04_sms_hasan_alive`
- `contacts/mr_hands/sts_ep1_04/sts_ep1_04_sms_hasan_alive_hands_answer_01`
- `contacts/mr_hands/sts_ep1_04/sts_ep1_04_sms_hasan_alive_hands_answer_02`
- `contacts/mr_hands/sts_ep1_04/sts_ep1_04_sms_hasan_alive_v_response`
- `contacts/mr_hands/sts_ep1_04/sts_ep1_04_sms_hasan_alive_v_response/sts_ep1_04_sms_hasan_alive_v_response_01`
- `contacts/mr_hands/sts_ep1_04/sts_ep1_04_sms_hasan_alive_v_response/sts_ep1_04_sms_hasan_alive_v_response_02`
- `ep1/quests/minor_quest/wst_ep1_05`
- `ep1/quests/minor_quest/wst_ep1_05/description`
- `ep1/quests/minor_quest/wst_ep1_05/wst_ep1_05/go_to_hasan_apartment`
- `ep1/quests/minor_quest/wst_ep1_05/wst_ep1_05/read_message_from_hands`
- `ep1/quests/minor_quest/wst_ep1_05/wst_ep1_05/speak_with_hasan`
- `ep1/quests/minor_quest/wst_ep1_05/wst_ep1_05/take_the_gun`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questEventManagerNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 7 |
| `questInputNodeDefinition` | 2 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 13 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentToken_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questLogicalCondition,questObjectCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPhaseNodeDefinition` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `34a94443e680a228f2ef` | 2 | `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 38 -> 61 -> 63 |
| `be95ed609c623423854c` | 2 | `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 3 -> 38 -> 61 |
| `02717b267d8bde2dbade` | 1 | `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 43 -> 44 -> 3 |
| `07a508d9181a1ec44ac6` | 1 | `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 43 -> 44 -> 41 |
| `1094980783b061bb3393` | 1 | `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 49 -> 50 -> 74 |
| `113b12d2ff4928232882` | 1 | `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 10 -> 23 -> 25 |
| `1666d7526b9bab74f2e2` | 1 | `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 24 -> 48 -> 55 |
| `190afe6d31978a672ef7` | 1 | `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 47 -> 33 -> 34 |
| `1a9b8893087e174a603f` | 1 | `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 48 -> 55 -> 56 |
| `1d48bd7cbbaeca8257d2` | 1 | `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 56 -> 28 -> 27 |
| `1d719a6baa0016981693` | 1 | `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 73 -> 45 -> 70 |
| `1fdaa711166fed260f40` | 1 | `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 34 -> 75 -> 76 |
| `20d0683a7148dd226b26` | 1 | `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 0 -> 47 -> 33 |
| `240148efc76953d1c5d4` | 1 | `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 70 -> 72 -> 71 |
| `31979c59a519504cbef2` | 1 | `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 76 -> 78 -> 3 |
| `3411c04c289ccac5ebe2` | 1 | `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 34 -> 75 -> 77 |
| `3568a94944398919d9f7` | 1 | `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 22 -> 10 -> 23 |
| `41a5ee696bceec6adb97` | 1 | `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 75 -> 77 -> 78 |
| `54cc447b02347895f5d3` | 1 | `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 23 -> 25 -> 24 |
| `5cd775fe045e92b72670` | 1 | `ep1\openworld\world_stories\wst_ep1_05\wst_ep1_05.questphase` / h0 / 28 -> 27 -> 59 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
