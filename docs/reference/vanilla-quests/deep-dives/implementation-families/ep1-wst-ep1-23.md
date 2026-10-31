# ep1-wst-ep1-23

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\world_stories\wst_ep1_23\wst_ep1_23.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

- `contacts/muamar_el_capitan_reyes/courier_outro_after/after_courier_outro_muamar_closing`
- `contacts/muamar_el_capitan_reyes/courier_outro_after/after_courier_outro_muamar_thanks_v`
- `contacts/muamar_el_capitan_reyes/courier_outro_after/after_courier_outro_v_responses`
- `contacts/muamar_el_capitan_reyes/courier_outro_after/after_courier_outro_v_responses/after_courier_outro_v_response_var_1`
- `contacts/muamar_el_capitan_reyes/courier_outro_after/after_courier_outro_v_responses/after_courier_outro_v_response_var_2`
- `ep1/contacts/officer_daniels/courier_outro_daniels_saved/daniels_closing_var_01`
- `ep1/contacts/officer_daniels/courier_outro_daniels_saved/daniels_closing_var_02`
- `ep1/contacts/officer_daniels/courier_outro_daniels_saved/daniels_thank_you`
- `ep1/contacts/officer_daniels/courier_outro_daniels_saved/v_response_choice`
- `ep1/contacts/officer_daniels/courier_outro_daniels_saved/v_response_choice/v_response_var_01`
- `ep1/contacts/officer_daniels/courier_outro_daniels_saved/v_response_choice/v_response_var_02`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questInputNodeDefinition` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 4 |
| `questPhoneManagerNodeDefinition[questSendMessage_NodeType]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `694dcc3f01ba46e3e166` | 2 | `ep1\openworld\world_stories\wst_ep1_23\wst_ep1_23.questphase` / h0 / 4 -> 5 -> 8 |
| `78cdbdc6eb5362c7f9b6` | 2 | `ep1\openworld\world_stories\wst_ep1_23\wst_ep1_23.questphase` / h0 / 12 -> 14 -> 15 |
| `97fe69269dae7ae1b83e` | 2 | `ep1\openworld\world_stories\wst_ep1_23\wst_ep1_23.questphase` / h0 / 14 -> 15 -> 13 |
| `c6360c30becfcd41253a` | 2 | `ep1\openworld\world_stories\wst_ep1_23\wst_ep1_23.questphase` / h0 / 3 -> 4 -> 5 |
| `0518bef14a713cd9988b` | 1 | `ep1\openworld\world_stories\wst_ep1_23\wst_ep1_23.questphase` / h0 / 10 -> 12 -> 14 |
| `50842d19c04b79e1e4e7` | 1 | `ep1\openworld\world_stories\wst_ep1_23\wst_ep1_23.questphase` / h0 / 9 -> 10 -> 12 |
| `5aaad1fd7ae8de7dca88` | 1 | `ep1\openworld\world_stories\wst_ep1_23\wst_ep1_23.questphase` / h0 / 0 -> 17 -> 2 |
| `79b1da5db01a5e9833b1` | 1 | `ep1\openworld\world_stories\wst_ep1_23\wst_ep1_23.questphase` / h0 / 0 -> 9 -> 10 |
| `b2502129545bd1ae65f2` | 1 | `ep1\openworld\world_stories\wst_ep1_23\wst_ep1_23.questphase` / h0 / 18 -> 3 -> 4 |
| `c14e9b93367501c460ca` | 1 | `ep1\openworld\world_stories\wst_ep1_23\wst_ep1_23.questphase` / h0 / 2 -> 18 -> 3 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
