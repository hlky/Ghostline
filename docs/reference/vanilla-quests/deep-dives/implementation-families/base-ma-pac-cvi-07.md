# base-ma-pac-cvi-07

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_07\community\ma_pac_cvi_07_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_07\community\ma_pac_cvi_07_com_civilians.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_07\ma_pac_cvi_07.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_07\ma_pac_cvi_07.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_07\ma_pac_cvi_07_phase.questphase |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_07\ma_pac_cvi_07_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/pacifica/coastview/ma_pac_cvi_07/onscreens/ma_pac_cvi_07`
- `points_of_interest/minor_activities/ma_pac_cvi_07`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 8 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 3 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 6 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 4 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `808c42396a9735fe3a65` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_07\ma_pac_cvi_07_phase.questphase` / h0 / 0 -> 11 -> 30 |
| `d30dec206567a53c3ede` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_07\ma_pac_cvi_07_phase.questphase` / h0 / 11 -> 30 -> 29 |
| `d91a9f204f2f2c336b02` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_07\ma_pac_cvi_07_phase.questphase` / h0 / 35 -> 33 -> 34 |
| `0015f21cac33b67104ef` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_07\ma_pac_cvi_07_phase.questphase` / h0 / 25 -> 64 -> 63 |
| `034e4ec70e5e541255d2` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_07\ma_pac_cvi_07_phase.questphase` / h84 / 11 -> 12 -> 1 |
| `05741704b94ee3af2e8c` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_07\ma_pac_cvi_07_phase.questphase` / h0 / 40 -> 39 -> 49 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_07\ma_pac_cvi_07_phase.questphase` / h0 / 27 -> 55 -> 26 |
| `0b387b0e0f2538ab6067` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_07\ma_pac_cvi_07_phase.questphase` / h84 / 6 -> 7 -> 14 |
| `0e0b0ec1add4154b2d49` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_07\ma_pac_cvi_07_phase.questphase` / h84 / 7 -> 14 -> 13 |
| `114d46d19e809cb7d96b` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_07\ma_pac_cvi_07_phase.questphase` / h0 / 54 -> 64 -> 63 |
| `1258cee37e98f0ae14fe` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_07\ma_pac_cvi_07_phase.questphase` / h0 / 16 -> 23 -> 27 |
| `1c8f5db5f76df3ad5f7c` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_07\ma_pac_cvi_07_phase.questphase` / h0 / 22 -> 54 -> 64 |
| `28853014c883178ad822` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_07\ma_pac_cvi_07_phase.questphase` / h84 / 13 -> 10 -> 11 |
| `28db20c91b639a09afae` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_07\ma_pac_cvi_07_phase.questphase` / h0 / 62 -> 20 -> 24 |
| `403d794f01acf7d4e8ce` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_07\ma_pac_cvi_07_phase.questphase` / h0 / 62 -> 5 -> 16 |
| `43504be6c050709c9a10` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_07\ma_pac_cvi_07_phase.questphase` / h0 / 63 -> 62 -> 41 |
| `48ef5781867fbe61b8b0` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_07\ma_pac_cvi_07_phase.questphase` / h0 / 61 -> 62 -> 5 |
| `4e534a24897f81ddee0f` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_07\ma_pac_cvi_07_phase.questphase` / h0 / 54 -> 25 -> 64 |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_07\ma_pac_cvi_07_phase.questphase` / h0 / 8 -> 9 -> 10 |
| `53e1b61b58de584e4473` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_07\ma_pac_cvi_07_phase.questphase` / h0 / 25 -> 64 -> 61 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
