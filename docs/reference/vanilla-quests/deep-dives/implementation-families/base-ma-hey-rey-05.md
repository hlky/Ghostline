# base-ma-hey-rey-05

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\community\ma_hey_rey_05_civilians_victim_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\community\ma_hey_rey_05_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\community\ma_hey_rey_05_police_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\ma_hey_rey_05.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\ma_hey_rey_05.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\ma_hey_rey_05_phase.questphase |
| `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\ma_hey_rey_05_phase.questphase` | content candidate | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/heywood/vista_del_rey/ma_hey_rey_05/onscreens/ma_hey_rey_05_onscreen_01`
- `points_of_interest/minor_activities/ma_hey_rey_05`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 4 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 1 |
| `questOutputNodeDefinition` | 4 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 8 |
| `questPhaseNodeDefinition` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 11 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\ma_hey_rey_05_phase.questphase` / h0 / 11 -> 37 -> 26 |
| `00c3ca0ac0b55db639ca` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\ma_hey_rey_05_phase.questphase` / h26 / 4 -> 20 -> 6 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\ma_hey_rey_05_phase.questphase` / h0 / 54 -> 51 -> 50 |
| `0976bdf75170c3f46615` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\ma_hey_rey_05_phase.questphase` / h0 / 29 -> 49 -> 48 |
| `0985fc78e580f2f10e14` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\ma_hey_rey_05_phase.questphase` / h294 / 2 -> 10 -> 9 |
| `0d71b48f126267c1b6e3` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\ma_hey_rey_05_phase.questphase` / h26 / 22 -> 9 -> 23 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\ma_hey_rey_05_phase.questphase` / h26 / 29 -> 4 -> 20 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\ma_hey_rey_05_phase.questphase` / h0 / 2 -> 11 -> 37 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\ma_hey_rey_05_phase.questphase` / h0 / 11 -> 37 -> 20 |
| `2cc4f20e16798419f013` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\ma_hey_rey_05_phase.questphase` / h0 / 22 -> 14 -> 54 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\ma_hey_rey_05_phase.questphase` / h0 / 54 -> 53 -> 50 |
| `3473788fa2e021211ee9` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\ma_hey_rey_05_phase.questphase` / h0 / 33 -> 34 -> 35 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\ma_hey_rey_05_phase.questphase` / h0 / 51 -> 50 -> 15 |
| `390f62c11ddf01069a3f` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\ma_hey_rey_05_phase.questphase` / h0 / 2 -> 30 -> 46 |
| `3c6b36e8c01548f18f31` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\ma_hey_rey_05_phase.questphase` / h0 / 21 -> 17 -> 25 |
| `3defb6b5bfe82560078d` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\ma_hey_rey_05_phase.questphase` / h0 / 2 -> 4 -> 9 |
| `4135965421e26f7852e9` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\ma_hey_rey_05_phase.questphase` / h26 / 23 -> 10 -> 25 |
| `423e38da0596af6a3004` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\ma_hey_rey_05_phase.questphase` / h294 / 10 -> 9 -> 6 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\ma_hey_rey_05_phase.questphase` / h0 / 37 -> 26 -> 20 |
| `4d6c55ba26916a1e04f1` | 1 | `base\open_world\minor_activities\heywood\vista_del_rey\ma_hey_rey_05\ma_hey_rey_05_phase.questphase` / h0 / 25 -> 45 -> 3 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
