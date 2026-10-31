# base-ma-wat-nid-12

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_12\community\ma_wat_nid_12_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_12\ma_wat_nid_12_gamedef.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_12\ma_wat_nid_12_phase.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_12\ma_wat_nid_12_quest.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_12\ma_wat_nid_12_phase.questphase |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/norhside_industrial_district/ma_wat_nid_12/onscreens/ma_wat_nid_12_guideline`
- `onscreens/emails/quests/minor_activities/watson/norhside_industrial_district/ma_wat_nid_12/onscreens/ma_wat_nid_12_tc`
- `points_of_interest/minor_activities/ma_wat_nid_12`
- `quests/minor_activities/watson/northside_industrial_district/ma_wat_nid_12`
- `quests/minor_activities/watson/northside_industrial_district/ma_wat_nid_12/description`
- `quests/minor_activities/watson/northside_industrial_district/ma_wat_nid_12/ma_wat_nid_12/ma_wat_nid_12`
- `quests/minor_activities/watson/northside_industrial_district/ma_wat_nid_12/ma_wat_nid_12/ma_wat_nid_12_loot`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 3 |
| `questInteractiveObjectManagerNodeDefinition[questSetInteractionState_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 7 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 2 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_12\ma_wat_nid_12_phase.questphase` / h0 / 12 -> 69 -> 58 |
| `a732a0cf44ff0251be89` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_12\ma_wat_nid_12_phase.questphase` / h0 / 23 -> 82 -> 24 |
| `f3a269b6a97862bc211c` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_12\ma_wat_nid_12_phase.questphase` / h0 / 0 -> 1 -> 12 |
| `02d878a28a675e881f96` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_12\ma_wat_nid_12_phase.questphase` / h0 / 91 -> 89 -> 14 |
| `0781ef00ea04c05ee418` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_12\ma_wat_nid_12_phase.questphase` / h0 / 24 -> 25 -> 93 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_12\ma_wat_nid_12_phase.questphase` / h0 / 93 -> 90 -> 89 |
| `0c8f031f372a34b54a46` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_12\ma_wat_nid_12_phase.questphase` / h0 / 75 -> 53 -> 76 |
| `0ea39c90296b8c8c526e` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_12\ma_wat_nid_12_phase.questphase` / h0 / 58 -> 64 -> 68 |
| `16127f3f2f66b166e252` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_12\ma_wat_nid_12_phase.questphase` / h0 / 57 -> 55 -> 3 |
| `178360ac35259ce804ee` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_12\ma_wat_nid_12_phase.questphase` / h0 / 2 -> 66 -> 0 |
| `1dc89cfc6ae4d329b522` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_12\ma_wat_nid_12_phase.questphase` / h0 / 28 -> 60 -> 70 |
| `1ecc1e1f4c4151a3aba0` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_12\ma_wat_nid_12_phase.questphase` / h0 / 60 -> 70 -> 72 |
| `255c3064dfbb8efcc440` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_12\ma_wat_nid_12_phase.questphase` / h0 / 67 -> 55 -> 3 |
| `2802f18cf340a2b946ff` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_12\ma_wat_nid_12_phase.questphase` / h0 / 12 -> 69 -> 64 |
| `2a18d536739310eb7e61` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_12\ma_wat_nid_12_phase.questphase` / h0 / 82 -> 24 -> 25 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_12\ma_wat_nid_12_phase.questphase` / h0 / 93 -> 92 -> 89 |
| `2ea6dc8eef48b1cfc585` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_12\ma_wat_nid_12_phase.questphase` / h0 / 69 -> 58 -> 64 |
| `36dddd8add8366cb2443` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_12\ma_wat_nid_12_phase.questphase` / h0 / 70 -> 72 -> 75 |
| `3cdedab83545367ce112` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_12\ma_wat_nid_12_phase.questphase` / h0 / 88 -> 23 -> 82 |
| `45384fad45d3768a409d` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_12\ma_wat_nid_12_phase.questphase` / h0 / 90 -> 89 -> 27 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
