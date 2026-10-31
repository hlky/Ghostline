# base-ma-wbr-jpn-16

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\communities\ma_wbr_jpn_16_after_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\communities\ma_wbr_jpn_16_civilian_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\communities\ma_wbr_jpn_16_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\ma_wbr_jpn_16.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\ma_wbr_jpn_16.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\ma_wbr_jpn_16_phase.questphase |
| `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\ma_wbr_jpn_16_phase.questphase` | content candidate | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/westbrook/japantown/ma_wbr_jpn_16/shards/ma_wbr_jpn_16_a`
- `points_of_interest/minor_activities/ma_wbr_jpn_16`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 5 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 7 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 3 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalAndNodeDefinition` | 3 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterReaction_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 5 |
| `questPhaseNodeDefinition` | 2 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 9 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `66e17bf07a534afe17b2` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\ma_wbr_jpn_16_phase.questphase` / h56 / 20 -> 21 -> 30 |
| `8d10896873df5c62014e` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\ma_wbr_jpn_16_phase.questphase` / h0 / 2 -> 3 -> 6 |
| `987122e5e2fcd167cf6c` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\ma_wbr_jpn_16_phase.questphase` / h0 / 0 -> 2 -> 3 |
| `a3e5f861a4b71433135a` | 2 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\ma_wbr_jpn_16_phase.questphase` / h56 / 20 -> 21 -> 11 |
| `02a5265bcccfc8e3cf77` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\ma_wbr_jpn_16_phase.questphase` / h56 / 20 -> 21 -> 25 |
| `063a411ffe9c7568d9ee` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\ma_wbr_jpn_16_phase.questphase` / h56 / 10 -> 16 -> 18 |
| `06e3382349ceff89de6f` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\ma_wbr_jpn_16_phase.questphase` / h0 / 6 -> 4 -> 30 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\ma_wbr_jpn_16_phase.questphase` / h0 / 54 -> 51 -> 50 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\ma_wbr_jpn_16_phase.questphase` / h0 / 16 -> 38 -> 25 |
| `0985fc78e580f2f10e14` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\ma_wbr_jpn_16_phase.questphase` / h348 / 97 -> 10 -> 9 |
| `0b387b0e0f2538ab6067` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\ma_wbr_jpn_16_phase.questphase` / h56 / 8 -> 12 -> 13 |
| `1198407e25fb6cae0240` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\ma_wbr_jpn_16_phase.questphase` / h0 / 51 -> 50 -> 5 |
| `13b3a103bfd4aa1ae513` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\ma_wbr_jpn_16_phase.questphase` / h56 / 11 -> 27 -> 26 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\ma_wbr_jpn_16_phase.questphase` / h56 / 20 -> 21 -> 23 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\ma_wbr_jpn_16_phase.questphase` / h0 / 0 -> 16 -> 38 |
| `204ca9b8b94427c1ef81` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\ma_wbr_jpn_16_phase.questphase` / h0 / 47 -> 39 -> 26 |
| `23c83f846beb25d06b1d` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\ma_wbr_jpn_16_phase.questphase` / h0 / 3 -> 31 -> 33 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\ma_wbr_jpn_16_phase.questphase` / h0 / 16 -> 38 -> 21 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\ma_wbr_jpn_16_phase.questphase` / h0 / 54 -> 53 -> 50 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\westbrook\japantown\ma_wbr_jpn_16\ma_wbr_jpn_16_phase.questphase` / h0 / 22 -> 54 -> 53 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
