# ep1-wst-ep1-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

- `ep1/contacts/alan_noel/wst_ep1_02/wst_ep1_02`
- `ep1/contacts/alan_noel/wst_ep1_02/wst_ep1_02_alan_rep`
- `ep1/contacts/alan_noel/wst_ep1_02/wst_ep1_02_corpo_blueline`
- `ep1/contacts/alan_noel/wst_ep1_02/wst_ep1_02_reply`
- `ep1/contacts/alan_noel/wst_ep1_02/wst_ep1_02_reply/wst_ep1_02_reply_a`
- `ep1/contacts/alan_noel/wst_ep1_02/wst_ep1_02_reply/wst_ep1_02_reply_b`
- `ep1/quests/minor_quest/sts_ep1_12_pickup`
- `ep1/quests/minor_quest/sts_ep1_12_pickup/alan_codex`
- `ep1/quests/minor_quest/sts_ep1_12_pickup/alan_message`
- `ep1/quests/minor_quest/sts_ep1_12_pickup/description`
- `ep1/quests/minor_quest/sts_ep1_12_pickup/sts_ep1_12_pickup/read_message`
- `ep1/quests/minor_quest/sts_ep1_12_pickup/sts_ep1_12_pickup/take_reward`
- `ep1/quests/minor_quest/sts_ep1_12_pickup/sts_ep1_12_pickup/take_reward/mp`
- `ep1/quests/minor_quest/sts_ep1_12_pickup/sts_ep1_12_pickup/take_reward/mp2`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 3 |
| `questInputNodeDefinition` | 1 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_ActionProperty,questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 1 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 12 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMappinManagerNodeDefinition` | 2 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentToken_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 4 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `7e7dbbc930b3717fd790` | 4 | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 6 -> 35 -> 57 |
| `ff3adc95658d38e3e68e` | 2 | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 2 -> 8 -> 24 |
| `014ed7f2034fbb1d68ee` | 1 | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 60 -> 61 -> 62 |
| `08924a89ae010060d9a9` | 1 | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 47 -> 5 -> 36 |
| `1258cee37e98f0ae14fe` | 1 | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 8 -> 24 -> 40 |
| `21302dda76be240f6c56` | 1 | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 45 -> 47 -> 5 |
| `240148efc76953d1c5d4` | 1 | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 59 -> 34 -> 33 |
| `31bc1d8a7078e1f15bb2` | 1 | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 0 -> 48 -> 50 |
| `3e6f03030764fcc75954` | 1 | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 26 -> 27 -> 28 |
| `479fea450b4d7ec01b0c` | 1 | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 55 -> 7 -> 23 |
| `4c22b4607e21dec08dc5` | 1 | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 7 -> 23 -> 53 |
| `600aabee3d30a71963f2` | 1 | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 34 -> 33 -> 9 |
| `66eaec0f4b47e655b42a` | 1 | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 0 -> 48 -> 49 |
| `70cdd8ca93455e047152` | 1 | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 33 -> 9 -> 60 |
| `80c436c3f41257230312` | 1 | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 47 -> 5 -> 2 |
| `85ba174646d56b45d66c` | 1 | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 44 -> 45 -> 47 |
| `8852f0dbd6d859b59497` | 1 | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 23 -> 53 -> 20 |
| `96b8a4f304e892d0412b` | 1 | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 9 -> 60 -> 61 |
| `a0ab42bf8e079a08b7d0` | 1 | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 36 -> 6 -> 35 |
| `a0f32b652b7e50e9d29a` | 1 | `ep1\openworld\world_stories\wst_ep1_02\wst_ep1_02.questphase` / h0 / 58 -> 59 -> 34 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
