# ep1-wst-ep1-11

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `ep1/contacts/bill/wst_ep1_11_bill_invitation`
- `ep1/contacts/bill/wst_ep1_11_bill_invitation/bill_dont_track`
- `ep1/contacts/bill/wst_ep1_11_bill_invitation/bill_invitation`
- `ep1/contacts/bill/wst_ep1_11_bill_invitation/bill_track`
- `ep1/contacts/bill/wst_ep1_11_bill_invitation/v_choice`
- `ep1/contacts/bill/wst_ep1_11_bill_invitation/v_choice/dont_track`
- `ep1/contacts/bill/wst_ep1_11_bill_invitation/v_choice/track`
- `ep1/quests/minor_quest/wst_ep1_11_bill_meeting`
- `ep1/quests/minor_quest/wst_ep1_11_bill_meeting/description`
- `ep1/quests/minor_quest/wst_ep1_11_bill_meeting/wst_ep1_11`
- `ep1/quests/minor_quest/wst_ep1_11_bill_meeting/wst_ep1_11/meet_bill`
- `ep1/quests/minor_quest/wst_ep1_11_bill_meeting/wst_ep1_11/read_message`
- `ep1/quests/minor_quest/wst_ep1_11_bill_meeting/wst_ep1_11/talk_bill`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 3 |
| `questCutControlNodeDefinition` | 2 |
| `questDeletionMarkerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 3 |
| `questInputNodeDefinition` | 2 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 12 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 20 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 4 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentToken_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 7 |
| `questPhaseNodeDefinition` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `0781ef00ea04c05ee418` | 3 | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 50 -> 103 -> 114 |
| `7e7dbbc930b3717fd790` | 3 | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 50 -> 103 -> 59 |
| `21ad9637ecad037e997e` | 2 | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 116 -> 117 -> 127 |
| `2b97bbe6c4d61ccdc588` | 2 | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h329 / 2 -> 4 -> 6 |
| `4060b9bfef9485c64ec7` | 2 | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 75 -> 65 -> 67 |
| `58fcd67b0afde536eb35` | 2 | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 51 -> 108 -> 107 |
| `5a17dff97ddbd2f950e8` | 2 | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 107 -> 115 -> 111 |
| `5c50f779a023d8f8ef07` | 2 | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 106 -> 104 -> 105 |
| `80ea0441e41bca3d56ad` | 2 | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h329 / 0 -> 2 -> 4 |
| `a8c73c321c70bed81c92` | 2 | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 64 -> 65 -> 67 |
| `c7b42897e08961d4eee7` | 2 | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 48 -> 110 -> 109 |
| `ef5bc629af0d7582bdc0` | 2 | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 9 -> 56 -> 63 |
| `166ce14561c4b116d1ac` | 1 | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 56 -> 62 -> 73 |
| `1737436a0cc54670e573` | 1 | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 108 -> 107 -> 25 |
| `1b9da9bf2d5d093c44d8` | 1 | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 113 -> 101 -> 102 |
| `1c114de0cc444dc0d348` | 1 | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 68 -> 71 -> 38 |
| `1fdaa711166fed260f40` | 1 | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 56 -> 94 -> 95 |
| `240148efc76953d1c5d4` | 1 | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 76 -> 79 -> 77 |
| `26031a0637491e1ba782` | 1 | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 83 -> 113 -> 115 |
| `2d63e13b93e78f20f574` | 1 | `ep1\openworld\world_stories\wst_ep1_11\wst_ep1_11.questphase` / h0 / 83 -> 113 -> 101 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
