# base-ma-std-rcr-03

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_03\community\ma_std_rcr_03_civilian_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_03\community\ma_std_rcr_03_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_03\ma_std_rcr_03.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_03\ma_std_rcr_03.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_03\ma_std_rcr_03_phase.questphase |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_03\ma_std_rcr_03_phase.questphase` | content candidate | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_03/onscreens/ma_std_rcr_03_onscreen_01`
- `points_of_interest/minor_activities/ma_std_rcr_03`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 3 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 2 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 7 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `5506424829d3f5f3a244` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_03\ma_std_rcr_03_phase.questphase` / h0 / 54 -> 105 -> 119 |
| `64806ebc968ec7d10025` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_03\ma_std_rcr_03_phase.questphase` / h0 / 136 -> 111 -> 134 |
| `987122e5e2fcd167cf6c` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_03\ma_std_rcr_03_phase.questphase` / h0 / 54 -> 108 -> 136 |
| `0015f21cac33b67104ef` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_03\ma_std_rcr_03_phase.questphase` / h0 / 132 -> 150 -> 148 |
| `02d878a28a675e881f96` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_03\ma_std_rcr_03_phase.questphase` / h0 / 148 -> 146 -> 120 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_03\ma_std_rcr_03_phase.questphase` / h0 / 150 -> 147 -> 146 |
| `114d46d19e809cb7d96b` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_03\ma_std_rcr_03_phase.questphase` / h0 / 143 -> 150 -> 148 |
| `136512a6b340968ce236` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_03\ma_std_rcr_03_phase.questphase` / h0 / 117 -> 144 -> 55 |
| `2814aea29b6af3574623` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_03\ma_std_rcr_03_phase.questphase` / h0 / 111 -> 109 -> 130 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_03\ma_std_rcr_03_phase.questphase` / h0 / 150 -> 149 -> 146 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_03\ma_std_rcr_03_phase.questphase` / h0 / 147 -> 146 -> 107 |
| `403d794f01acf7d4e8ce` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_03\ma_std_rcr_03_phase.questphase` / h0 / 146 -> 107 -> 117 |
| `414179f27318cfb189d5` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_03\ma_std_rcr_03_phase.questphase` / h0 / 105 -> 143 -> 132 |
| `423e38da0596af6a3004` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_03\ma_std_rcr_03_phase.questphase` / h277 / 14 -> 17 -> 2 |
| `42d198651597f3c3ac03` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_03\ma_std_rcr_03_phase.questphase` / h277 / 0 -> 4 -> 1 |
| `45a0059a97ab5b10fb49` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_03\ma_std_rcr_03_phase.questphase` / h0 / 147 -> 146 -> 120 |
| `4e534a24897f81ddee0f` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_03\ma_std_rcr_03_phase.questphase` / h0 / 143 -> 132 -> 150 |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_03\ma_std_rcr_03_phase.questphase` / h0 / 111 -> 109 -> 112 |
| `53e1b61b58de584e4473` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_03\ma_std_rcr_03_phase.questphase` / h0 / 132 -> 150 -> 149 |
| `60faf7d04cb945080042` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_03\ma_std_rcr_03_phase.questphase` / h277 / 17 -> 2 -> 3 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
