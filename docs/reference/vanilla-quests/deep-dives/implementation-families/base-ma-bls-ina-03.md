# base-ma-bls-ina-03

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_03\community\ma_bls_ina_se1_03_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_03\ma_bls_ina_se1_03_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/badlands/se1/ma_bls_ina_se1_03/onscreens/ma_bls_ina_se1_03_onscreen_01`
- `points_of_interest/minor_activities/ma_bls_ina_se1_03`
- `quests/minor_activities/badlands/se1/ma_bls_ina_se1_03`
- `quests/minor_activities/badlands/se1/ma_bls_ina_se1_03/description`
- `quests/minor_activities/badlands/se1/ma_bls_ina_se1_03/ma_bls_ina_se1_03/go_to`
- `quests/minor_activities/badlands/se1/ma_bls_ina_se1_03/ma_bls_ina_se1_03/loot`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 6 |
| `questEventManagerNodeDefinition` | 16 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 2 |
| `questInteractiveObjectManagerNodeDefinition[questSetInteractionState_NodeType]` | 1 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 7 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 2 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 3 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `fd6abc96d7197725e3e8` | 3 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_03\ma_bls_ina_se1_03_phase.questphase` / h0 / 63 -> 36 -> 51 |
| `95b7458b3ffd83fd4357` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_03\ma_bls_ina_se1_03_phase.questphase` / h0 / 36 -> 51 -> 79 |
| `02c5a983de890662a298` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_03\ma_bls_ina_se1_03_phase.questphase` / h0 / 38 -> 91 -> 98 |
| `06e3382349ceff89de6f` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_03\ma_bls_ina_se1_03_phase.questphase` / h0 / 39 -> 40 -> 41 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_03\ma_bls_ina_se1_03_phase.questphase` / h0 / 60 -> 83 -> 61 |
| `08a5a2d03b9f559eb4b2` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_03\ma_bls_ina_se1_03_phase.questphase` / h0 / 11 -> 92 -> 100 |
| `0a93050c3b0a04df8de6` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_03\ma_bls_ina_se1_03_phase.questphase` / h0 / 38 -> 91 -> 90 |
| `0b81e5206696faa510d4` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_03\ma_bls_ina_se1_03_phase.questphase` / h0 / 63 -> 36 -> 37 |
| `0d59d5b737ce1451c32f` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_03\ma_bls_ina_se1_03_phase.questphase` / h0 / 117 -> 113 -> 112 |
| `138cff49923a75e07348` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_03\ma_bls_ina_se1_03_phase.questphase` / h0 / 16 -> 17 -> 19 |
| `159599f19533cfcfe918` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_03\ma_bls_ina_se1_03_phase.questphase` / h0 / 91 -> 90 -> 35 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_03\ma_bls_ina_se1_03_phase.questphase` / h224 / 12 -> 2 -> 3 |
| `1c8f5db5f76df3ad5f7c` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_03\ma_bls_ina_se1_03_phase.questphase` / h0 / 34 -> 82 -> 94 |
| `1d48bd7cbbaeca8257d2` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_03\ma_bls_ina_se1_03_phase.questphase` / h0 / 26 -> 49 -> 21 |
| `215ca95d939006973a7d` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_03\ma_bls_ina_se1_03_phase.questphase` / h0 / 21 -> 27 -> 53 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_03\ma_bls_ina_se1_03_phase.questphase` / h0 / 114 -> 111 -> 112 |
| `374c09a5d0cbf6fbf8b5` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_03\ma_bls_ina_se1_03_phase.questphase` / h0 / 106 -> 114 -> 111 |
| `4050a1424e83b44096ff` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_03\ma_bls_ina_se1_03_phase.questphase` / h0 / 93 -> 102 -> 98 |
| `4123636c2b09a02fdc99` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_03\ma_bls_ina_se1_03_phase.questphase` / h224 / 8 -> 9 -> 11 |
| `45384fad45d3768a409d` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_03\ma_bls_ina_se1_03_phase.questphase` / h0 / 113 -> 112 -> 26 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
