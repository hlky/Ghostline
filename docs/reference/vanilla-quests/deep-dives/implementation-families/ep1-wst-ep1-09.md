# ep1-wst-ep1-09

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.quest` | content candidate | 1 / 0 | ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase |
| `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` | content candidate | 1 / 0 |  |
| `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09_enemies_com.community` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `ep1/contacts/nele_spranger`
- `ep1/contacts/nele_spranger/wst_ep1_09/meet_ambush`
- `ep1/contacts/nele_spranger/wst_ep1_09/meet_ambush_after_v_answer`
- `ep1/contacts/nele_spranger/wst_ep1_09/nele_answers_where_are_you`
- `ep1/contacts/nele_spranger/wst_ep1_09/v_answer`
- `ep1/contacts/nele_spranger/wst_ep1_09/v_answer/v_answer_message`
- `ep1/contacts/nele_spranger/wst_ep1_09/v_answer/v_answer_message_ambush_ver2`
- `ep1/contacts/nele_spranger/wst_ep1_09/v_where_are_you`
- `ep1/quests/minor_quest/wst_ep1_09`
- `ep1/quests/minor_quest/wst_ep1_09/description`
- `ep1/quests/minor_quest/wst_ep1_09/meet_nele/find_nele`
- `ep1/quests/minor_quest/wst_ep1_09/meet_nele/find_nele/search_area`
- `ep1/quests/minor_quest/wst_ep1_09/meet_nele/meet_nele`
- `ep1/quests/minor_quest/wst_ep1_09/meet_nele/read_nele_message`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 3 |
| `questCheckpointNodeDefinition` | 1 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 2 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_ActionProperty,questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 2 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 3 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 13 |
| `questLogicalHubNodeDefinition` | 1 |
| `questMappinManagerNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentToken_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 6 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 5 |
| `questPhaseNodeDefinition` | 1 |
| `questPhoneManagerNodeDefinition[questAddRemoveContact_NodeType,questChangeContactList_NodeTypeParams]` | 1 |
| `questPhoneManagerNodeDefinition[questSendMessage_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 8 |
| `questStartNodeDefinition` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `20a77143a898bc753a26` | 3 | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 71 -> 72 -> 73 |
| `3e6f03030764fcc75954` | 2 | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 85 -> 103 -> 105 |
| `8078c6e0e42d42afaed3` | 2 | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 101 -> 108 -> 83 |
| `ac173bb28431bf322da0` | 2 | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 136 -> 135 -> 56 |
| `b54739889d4d9a0745d2` | 2 | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 132 -> 85 -> 103 |
| `e2b1eb99d7aed5f4d239` | 2 | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 135 -> 56 -> 74 |
| `00dbb2682d28855163ba` | 1 | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 129 -> 128 -> 80 |
| `1398ec279d5314c176fb` | 1 | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 111 -> 101 -> 108 |
| `15d558010c9ee43c21c5` | 1 | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 134 -> 132 -> 85 |
| `1d48bd7cbbaeca8257d2` | 1 | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 61 -> 62 -> 102 |
| `207da315ba96f3ea5c8b` | 1 | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 73 -> 57 -> 118 |
| `253ae7a41038cb3a306f` | 1 | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 124 -> 1 -> 96 |
| `31bc1d8a7078e1f15bb2` | 1 | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 0 -> 120 -> 122 |
| `41a5ee696bceec6adb97` | 1 | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 120 -> 122 -> 123 |
| `4366985c0ea874cdca93` | 1 | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 81 -> 61 -> 62 |
| `481bb61cd41815a09fdf` | 1 | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 72 -> 73 -> 57 |
| `59608f91c91ae73a089b` | 1 | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 133 -> 131 -> 134 |
| `62513b1c2fdaf0c74a1c` | 1 | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 58 -> 59 -> 51 |
| `66eaec0f4b47e655b42a` | 1 | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 0 -> 120 -> 121 |
| `6791cbbe6b26cff8e34a` | 1 | `ep1\openworld\world_stories\wst_ep1_09\wst_ep1_09.questphase` / h0 / 63 -> 66 -> 81 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
