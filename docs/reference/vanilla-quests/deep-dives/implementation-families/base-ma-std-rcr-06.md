# base-ma-std-rcr-06

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\community\ma_std_rcr_06_civilian_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\community\ma_std_rcr_06_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\ma_std_rcr_06.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\ma_std_rcr_06.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\ma_std_rcr_06_phase.questphase |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\ma_std_rcr_06_phase.questphase` | content candidate | 3 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\phases\ma_std_rcr_06_bugfixing.questphase` | repair | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_06/onscreens/ma_std_rcr_06_onscreen_01`
- `points_of_interest/minor_activities/ma_std_rcr_06`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 5 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterReaction_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 3 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 8 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 7 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `ef828624d48b06bf49f2` | 7 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\ma_std_rcr_06_phase.questphase` / h0 / 26 -> 27 -> 54 |
| `2e1ee5a1324dbeeb9071` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\ma_std_rcr_06_phase.questphase` / h0 / 75 -> 26 -> 27 |
| `a3e5f861a4b71433135a` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\ma_std_rcr_06_phase.questphase` / h43 / 22 -> 7 -> 19 |
| `f2131c5a08e332cc3af8` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\ma_std_rcr_06_phase.questphase` / h0 / 45 -> 47 -> 64 |
| `02a5265bcccfc8e3cf77` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\ma_std_rcr_06_phase.questphase` / h43 / 22 -> 7 -> 3 |
| `04d78f5a272f905e31eb` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\ma_std_rcr_06_phase.questphase` / h0 / 26 -> 76 -> 80 |
| `0672ae8d2fae884916ec` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\ma_std_rcr_06_phase.questphase` / h43 / 7 -> 3 -> 2 |
| `06e3382349ceff89de6f` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\ma_std_rcr_06_phase.questphase` / h0 / 2 -> 73 -> 74 |
| `08b800a2169ac0a8b3c2` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\ma_std_rcr_06_phase.questphase` / h0 / 48 -> 82 -> 71 |
| `096aaeff70ca3d46fc79` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\ma_std_rcr_06_phase.questphase` / h0 / 0 -> 45 -> 47 |
| `136512a6b340968ce236` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\ma_std_rcr_06_phase.questphase` / h0 / 62 -> 83 -> 1 |
| `178360ac35259ce804ee` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\ma_std_rcr_06_phase.questphase` / h0 / 0 -> 52 -> 75 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\phases\ma_std_rcr_06_bugfixing.questphase` / h7 / 5 -> 4 -> 2 |
| `20e74db83226e46cc202` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\ma_std_rcr_06_phase.questphase` / h0 / 79 -> 81 -> 78 |
| `23c83f846beb25d06b1d` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\ma_std_rcr_06_phase.questphase` / h0 / 76 -> 79 -> 81 |
| `27aa719598304363c84e` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\ma_std_rcr_06_phase.questphase` / h0 / 88 -> 87 -> 86 |
| `2d5e5fbbc83bb6335e36` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\ma_std_rcr_06_phase.questphase` / h0 / 76 -> 80 -> 81 |
| `37a0764f953c91e596dd` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\ma_std_rcr_06_phase.questphase` / h0 / 87 -> 86 -> 65 |
| `3c2d3d76cbc21af939f6` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\phases\ma_std_rcr_06_bugfixing.questphase` / h7 / 0 -> 3 -> 5 |
| `403d794f01acf7d4e8ce` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_06\ma_std_rcr_06_phase.questphase` / h0 / 86 -> 49 -> 62 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
