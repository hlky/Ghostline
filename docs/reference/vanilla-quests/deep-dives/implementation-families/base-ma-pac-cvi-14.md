# base-ma-pac-cvi-14

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_14\community\ma_pac_cvi_14_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_14\ma_pac_cvi_14.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_14\ma_pac_cvi_14.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_14\ma_pac_cvi_14_phase.questphase |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_14\ma_pac_cvi_14_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/pacifica/coastview/ma_pac_cvi_14/onscreens/ma_pac_cvi_14`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 2 |
| `questInputNodeDefinition` | 3 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `0015f21cac33b67104ef` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_14\ma_pac_cvi_14_phase.questphase` / h0 / 17 -> 26 -> 24 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_14\ma_pac_cvi_14_phase.questphase` / h0 / 26 -> 23 -> 22 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_14\ma_pac_cvi_14_phase.questphase` / h0 / 18 -> 21 -> 19 |
| `114d46d19e809cb7d96b` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_14\ma_pac_cvi_14_phase.questphase` / h0 / 20 -> 26 -> 24 |
| `1c8f5db5f76df3ad5f7c` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_14\ma_pac_cvi_14_phase.questphase` / h0 / 12 -> 20 -> 26 |
| `28db20c91b639a09afae` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_14\ma_pac_cvi_14_phase.questphase` / h0 / 22 -> 14 -> 15 |
| `2aa0f3a3b004f071652f` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_14\ma_pac_cvi_14_phase.questphase` / h46 / 6 -> 7 -> 1 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_14\ma_pac_cvi_14_phase.questphase` / h0 / 26 -> 25 -> 22 |
| `4365e94e7169e2520841` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_14\ma_pac_cvi_14_phase.questphase` / h0 / 23 -> 22 -> 1 |
| `4516ea8d7bcf8c04ba50` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_14\ma_pac_cvi_14_phase.questphase` / h0 / 24 -> 22 -> 1 |
| `48b34908ac4ded0af324` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_14\ma_pac_cvi_14_phase.questphase` / h0 / 25 -> 22 -> 1 |
| `4e534a24897f81ddee0f` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_14\ma_pac_cvi_14_phase.questphase` / h0 / 20 -> 17 -> 26 |
| `53e1b61b58de584e4473` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_14\ma_pac_cvi_14_phase.questphase` / h0 / 17 -> 26 -> 25 |
| `71892f49b88f7b8bb8be` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_14\ma_pac_cvi_14_phase.questphase` / h0 / 0 -> 3 -> 12 |
| `7616062dec0ebe3473b4` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_14\ma_pac_cvi_14_phase.questphase` / h0 / 26 -> 24 -> 22 |
| `7b136ed9620da85cbac6` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_14\ma_pac_cvi_14_phase.questphase` / h0 / 23 -> 22 -> 14 |
| `90cf58434e79ce42af1e` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_14\ma_pac_cvi_14_phase.questphase` / h46 / 0 -> 12 -> 11 |
| `9b34cc5e868557ecd600` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_14\ma_pac_cvi_14_phase.questphase` / h0 / 24 -> 22 -> 14 |
| `a3e5f861a4b71433135a` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_14\ma_pac_cvi_14_phase.questphase` / h46 / 11 -> 6 -> 7 |
| `a5478462b081c1e7f114` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_14\ma_pac_cvi_14_phase.questphase` / h0 / 25 -> 22 -> 14 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
