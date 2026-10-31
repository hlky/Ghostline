# base-mws-hey-04

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\mini_world_stories\heywood\mws_hey_04\communities\mws_hey_04_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\heywood\mws_hey_04\mws_hey_04.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\mini_world_stories\heywood\mws_hey_04\mws_hey_04.quest` | content candidate | 1 / 0 | base\open_world\mini_world_stories\heywood\mws_hey_04\mws_hey_04.questphase |
| `base\open_world\mini_world_stories\heywood\mws_hey_04\mws_hey_04.questphase` | content candidate | 3 / 0 | base\open_world\mini_world_stories\heywood\mws_hey_04\scenes\mws_hey_04_rave.scene |
| `base\open_world\mini_world_stories\heywood\mws_hey_04\scenes\mws_hey_04_rave.scene` | content candidate | 0 / 15 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetProgressionBuild]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 1 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 2 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 2 |
| `questInputNodeDefinition` | 5 |
| `questLogicalHubNodeDefinition` | 3 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInputAction_ConditionType,questLogicalCondition,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTimeCondition,questTimePeriod_ConditionType,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 5 |
| `questPhaseNodeDefinition` | 1 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questTimeManagerNodeDefinition[questSetTime_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questSetHUDEntryForcedVisibility_NodeType]` | 2 |
| `questUseWorkspotNodeDefinition[questUseWorkspotPlayerParams,scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |
| `scnChoiceNode[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnEndNode[scnNodeId]` | 1 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `056f65b5401e52f37bc4` | 2 | `base\open_world\mini_world_stories\heywood\mws_hey_04\mws_hey_04.questphase` / h0 / 27 -> 25 -> 26 |
| `1cfa47eb6d677e74c588` | 2 | `base\open_world\mini_world_stories\heywood\mws_hey_04\mws_hey_04.questphase` / h25 / 0 -> 13 -> 4 |
| `8586b7023506a09ec198` | 2 | `base\open_world\mini_world_stories\heywood\mws_hey_04\mws_hey_04.questphase` / h25 / 10 -> 11 -> 3 |
| `94bd37224ec39a782b98` | 2 | `base\open_world\mini_world_stories\heywood\mws_hey_04\mws_hey_04.questphase` / h0 / 25 -> 26 -> 1 |
| `093da0188bed59bca86c` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_04\mws_hey_04.questphase` / h39 / 2 -> 7 -> 18 |
| `0e8c677d30317a375773` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_04\scenes\mws_hey_04_rave.scene` / scene / 18 -> 16 -> 22 |
| `1db904feef82c399e944` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_04\mws_hey_04.questphase` / h0 / 0 -> 23 -> 19 |
| `2f405bf7bde94e442568` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_04\scenes\mws_hey_04_rave.scene` / scene / 6 -> 24 -> 2 |
| `3ba6ff1212d10dbe9c9b` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_04\mws_hey_04.questphase` / h39 / 7 -> 18 -> 12 |
| `483d5d9a21bd5685671d` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_04\scenes\mws_hey_04_rave.scene` / scene / 1 -> 6 -> 24 |
| `4ca78070c1b450131886` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_04\mws_hey_04.questphase` / h39 / 18 -> 25 -> 30 |
| `4fe64daeff05e511ddfb` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_04\mws_hey_04.questphase` / h25 / 4 -> 5 -> 6 |
| `5716a3aa6484ab053fc1` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_04\scenes\mws_hey_04_rave.scene` / scene / 20 -> 14 -> 8 |
| `725301e3e54e6fd5ecb0` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_04\scenes\mws_hey_04_rave.scene` / scene / 1 -> 6 -> 26 |
| `8094755f378783ee76ca` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_04\mws_hey_04.questphase` / h39 / 25 -> 30 -> 26 |
| `99a277b74a720d7c2eb6` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_04\scenes\mws_hey_04_rave.scene` / scene / 20 -> 14 -> 18 |
| `9b7ac01bf5c019199b38` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_04\scenes\mws_hey_04_rave.scene` / scene / 1 -> 6 -> 30 |
| `a9ce553d425d4caa2701` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_04\scenes\mws_hey_04_rave.scene` / scene / 14 -> 18 -> 16 |
| `ac1182ad78ceb7da585f` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_04\scenes\mws_hey_04_rave.scene` / scene / 16 -> 22 -> 28 |
| `af2b9babe620555dc517` | 1 | `base\open_world\mini_world_stories\heywood\mws_hey_04\mws_hey_04.questphase` / h0 / 20 -> 25 -> 26 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
