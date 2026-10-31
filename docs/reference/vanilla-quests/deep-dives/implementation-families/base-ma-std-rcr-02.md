# base-ma-std-rcr-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_02\community\ma_std_rcr_02_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_02\ma_std_rcr_02.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_02\ma_std_rcr_02.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_02\ma_std_rcr_02_phase.questphase |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_02\ma_std_rcr_02_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_02/onscreens/ma_std_rcr_02_onscreen_02`
- `points_of_interest/minor_activities/ma_std_rcr_02`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 1 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `71892f49b88f7b8bb8be` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_02\ma_std_rcr_02_phase.questphase` / h0 / 0 -> 36 -> 49 |
| `0015f21cac33b67104ef` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_02\ma_std_rcr_02_phase.questphase` / h0 / 57 -> 71 -> 69 |
| `02d878a28a675e881f96` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_02\ma_std_rcr_02_phase.questphase` / h0 / 69 -> 67 -> 50 |
| `06e3382349ceff89de6f` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_02\ma_std_rcr_02_phase.questphase` / h0 / 53 -> 54 -> 59 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_02\ma_std_rcr_02_phase.questphase` / h0 / 71 -> 68 -> 67 |
| `08b800a2169ac0a8b3c2` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_02\ma_std_rcr_02_phase.questphase` / h0 / 37 -> 64 -> 57 |
| `0b387b0e0f2538ab6067` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_02\ma_std_rcr_02_phase.questphase` / h140 / 3 -> 12 -> 13 |
| `114d46d19e809cb7d96b` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_02\ma_std_rcr_02_phase.questphase` / h0 / 64 -> 71 -> 69 |
| `136512a6b340968ce236` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_02\ma_std_rcr_02_phase.questphase` / h0 / 40 -> 65 -> 1 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_02\ma_std_rcr_02_phase.questphase` / h0 / 71 -> 70 -> 67 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_02\ma_std_rcr_02_phase.questphase` / h0 / 68 -> 67 -> 38 |
| `403d794f01acf7d4e8ce` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_02\ma_std_rcr_02_phase.questphase` / h0 / 67 -> 38 -> 40 |
| `425220d8428e981550da` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_02\ma_std_rcr_02_phase.questphase` / h0 / 33 -> 43 -> 32 |
| `42f528821ad39c8630d1` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_02\ma_std_rcr_02_phase.questphase` / h140 / 15 -> 3 -> 14 |
| `43497e272537226eb0cc` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_02\ma_std_rcr_02_phase.questphase` / h0 / 16 -> 33 -> 53 |
| `45a0059a97ab5b10fb49` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_02\ma_std_rcr_02_phase.questphase` / h0 / 68 -> 67 -> 50 |
| `4e534a24897f81ddee0f` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_02\ma_std_rcr_02_phase.questphase` / h0 / 64 -> 57 -> 71 |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_02\ma_std_rcr_02_phase.questphase` / h0 / 33 -> 53 -> 54 |
| `53e1b61b58de584e4473` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_02\ma_std_rcr_02_phase.questphase` / h0 / 57 -> 71 -> 70 |
| `66e17bf07a534afe17b2` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_02\ma_std_rcr_02_phase.questphase` / h140 / 15 -> 3 -> 12 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
