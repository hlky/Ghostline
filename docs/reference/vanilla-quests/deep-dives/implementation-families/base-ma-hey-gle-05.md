# base-ma-hey-gle-05

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_05\community\ma_hey_gle_05_civilians_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_05\community\ma_hey_gle_05_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_05\ma_hey_gle_05.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_05\ma_hey_gle_05.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\heywood\glen\ma_hey_gle_05\ma_hey_gle_05_phase.questphase |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_05\ma_hey_gle_05_phase.questphase` | content candidate | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/heywood/glen/ma_hey_gle_05/shards/ma_hey_gle_05`
- `points_of_interest/minor_activities/ma_hey_gle_05`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 4 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 4 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 5 |
| `questPhaseNodeDefinition` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 12 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_05\ma_hey_gle_05_phase.questphase` / h0 / 10 -> 37 -> 26 |
| `2c20201f171f754c99e0` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_05\ma_hey_gle_05_phase.questphase` / h0 / 77 -> 78 -> 79 |
| `3ba86c71a70bfb0620a5` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_05\ma_hey_gle_05_phase.questphase` / h0 / 76 -> 77 -> 78 |
| `484f47d527266442c50f` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_05\ma_hey_gle_05_phase.questphase` / h0 / 70 -> 81 -> 76 |
| `543b598a1b2fb7423e72` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_05\ma_hey_gle_05_phase.questphase` / h0 / 80 -> 78 -> 79 |
| `5466f936f30ed8ee354a` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_05\ma_hey_gle_05_phase.questphase` / h0 / 81 -> 76 -> 77 |
| `7373ce40c215f78fb39e` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_05\ma_hey_gle_05_phase.questphase` / h0 / 76 -> 77 -> 80 |
| `7d700b658871d4fd6b45` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_05\ma_hey_gle_05_phase.questphase` / h0 / 24 -> 70 -> 81 |
| `88f5ed16b4aedf0ce68b` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_05\ma_hey_gle_05_phase.questphase` / h0 / 77 -> 80 -> 75 |
| `8cf6277488916d3b7ab5` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_05\ma_hey_gle_05_phase.questphase` / h0 / 81 -> 80 -> 75 |
| `8edf5416ccd8dce9db72` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_05\ma_hey_gle_05_phase.questphase` / h0 / 81 -> 80 -> 78 |
| `c7b377e841e63de88f17` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_05\ma_hey_gle_05_phase.questphase` / h0 / 70 -> 81 -> 80 |
| `cadb89472ec2335d17b1` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_05\ma_hey_gle_05_phase.questphase` / h0 / 77 -> 80 -> 78 |
| `01775a1d01791d2b842b` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_05\ma_hey_gle_05_phase.questphase` / h69 / 10 -> 11 -> 1 |
| `02a5265bcccfc8e3cf77` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_05\ma_hey_gle_05_phase.questphase` / h69 / 13 -> 7 -> 4 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_05\ma_hey_gle_05_phase.questphase` / h0 / 98 -> 96 -> 94 |
| `0976bdf75170c3f46615` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_05\ma_hey_gle_05_phase.questphase` / h0 / 5 -> 92 -> 91 |
| `0985fc78e580f2f10e14` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_05\ma_hey_gle_05_phase.questphase` / h329 / 2 -> 10 -> 9 |
| `0cc371503245695a1ef7` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_05\ma_hey_gle_05_phase.questphase` / h0 / 24 -> 33 -> 35 |
| `1489a2df8e7f98f9c78e` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_05\ma_hey_gle_05_phase.questphase` / h0 / 2 -> 5 -> 92 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
