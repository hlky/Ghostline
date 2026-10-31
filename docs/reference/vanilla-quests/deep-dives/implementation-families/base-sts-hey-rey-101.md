# base-sts-hey-rey-101

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\community\sts_hey_rey_101_corpo.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\community\sts_hey_rey_101_reinforcements.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\community\sts_hey_rey_101_stuff.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\phases\sts_hey_rey_101.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\phases\sts_hey_rey_101_gameplay.questphase; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\phases\sts_hey_rey_101_openworld.questphase |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\phases\sts_hey_rey_101_gameplay.questphase` | content candidate | 8 / 0 | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\scenes\rey_101_bouncer.scene |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\phases\sts_hey_rey_101_openworld.questphase` | content candidate | 7 / 0 | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\scenes\rey_101_phone_call.scene |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\scenes\rey_101_bouncer.scene` | content candidate | 0 / 5 |  |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\scenes\rey_101_phone_call.scene` | content candidate | 0 / 3 |  |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\sts_hey_rey_101.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\sts_hey_rey_101.quest` | content candidate | 1 / 0 | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\phases\sts_hey_rey_101.questphase |

## Journal paths observed in these resources

- `contacts/father_sebastian_perez_aka_padre`
- `contacts/player`
- `contacts/regina_jones`
- `contacts/sebastian_padre_perez/sts_hey_rey_101_brief`
- `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_101`
- `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_101/sts_hey_rey_101/deliver`
- `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_101/sts_hey_rey_101/get_in`
- `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_101/sts_hey_rey_101/get_out`
- `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_101/sts_hey_rey_101/phone`
- `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_101/sts_hey_rey_101/take_down`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questCutControlNodeDefinition` | 4 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 1 |
| `questInputNodeDefinition` | 16 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 3 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 16 |
| `questLogicalAndNodeDefinition` | 3 |
| `questLogicalHubNodeDefinition` | 5 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMappinManagerNodeDefinition` | 2 |
| `questMiscAICommandNode` | 4 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 7 |
| `questOutputNodeDefinition` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 8 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questPhone_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 10 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleTrunk_ConditionType]` | 1 |
| `questPhaseNodeDefinition` | 16 |
| `questPhoneManagerNodeDefinition[questAddRemoveContact_NodeType,questChangeContactList_NodeTypeParams]` | 1 |
| `questPhoneManagerNodeDefinition[questCallContact_NodeType]` | 2 |
| `questPhoneManagerNodeDefinition[questOpenMessage_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 11 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 7 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnEndNode[scnNodeId]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 3 |
| `scnStartNode[scnNodeId]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `138cff49923a75e07348` | 4 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\phases\sts_hey_rey_101_openworld.questphase` / h106 / 34 -> 35 -> 38 |
| `3535ee3b356c051e5fe9` | 3 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\phases\sts_hey_rey_101_gameplay.questphase` / h392 / 0 -> 2 -> 4 |
| `40b362134ec2de8f422b` | 3 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\phases\sts_hey_rey_101_gameplay.questphase` / h137 / 35 -> 11 -> 12 |
| `2f0eea9ff31e1b057178` | 2 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\phases\sts_hey_rey_101.questphase` / h0 / 6 -> 7 -> 9 |
| `443e81765e9f7f224b8f` | 2 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\phases\sts_hey_rey_101_gameplay.questphase` / h137 / 43 -> 4 -> 5 |
| `4e9253a72e6b0134b8dd` | 2 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\phases\sts_hey_rey_101_openworld.questphase` / h106 / 35 -> 38 -> 15 |
| `8bd54738c2c85f70192e` | 2 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\phases\sts_hey_rey_101_openworld.questphase` / h106 / 6 -> 10 -> 11 |
| `9df46c3fb14e034d520b` | 2 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\phases\sts_hey_rey_101_openworld.questphase` / h106 / 11 -> 13 -> 33 |
| `a53561b4c002bc02b58a` | 2 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\phases\sts_hey_rey_101_openworld.questphase` / h106 / 13 -> 33 -> 36 |
| `a929a6882b8777e3d117` | 2 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\phases\sts_hey_rey_101_gameplay.questphase` / h137 / 0 -> 27 -> 9 |
| `beac811f7dfe2ac38d1a` | 2 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\phases\sts_hey_rey_101_openworld.questphase` / h106 / 10 -> 11 -> 13 |
| `dea8e50289b8821c58be` | 2 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\phases\sts_hey_rey_101_openworld.questphase` / h106 / 44 -> 14 -> 1 |
| `0267b0e79efe88bdd513` | 1 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\phases\sts_hey_rey_101_gameplay.questphase` / h54 / 3 -> 2 -> 4 |
| `02e0f2ad30fdd64812ca` | 1 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\phases\sts_hey_rey_101_gameplay.questphase` / h54 / 6 -> 8 -> 9 |
| `081b9dbe9528f984ddca` | 1 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\scenes\rey_101_bouncer.scene` / scene / 4 -> 5 -> 6 |
| `0c45bf12915e990be5f2` | 1 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\phases\sts_hey_rey_101_gameplay.questphase` / h137 / 16 -> 32 -> 2 |
| `0ca9bfdb2b5f53c7f1c8` | 1 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\scenes\rey_101_bouncer.scene` / scene / 5 -> 6 -> 2 |
| `1570fea67d5b7ed933d1` | 1 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\phases\sts_hey_rey_101_gameplay.questphase` / h137 / 3 -> 41 -> 42 |
| `1618d8c3e60a5672fe4f` | 1 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\phases\sts_hey_rey_101_openworld.questphase` / h106 / 57 -> 59 -> 4 |
| `1de31499189203e612c9` | 1 | `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_101\phases\sts_hey_rey_101_openworld.questphase` / h106 / 46 -> 47 -> 56 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
