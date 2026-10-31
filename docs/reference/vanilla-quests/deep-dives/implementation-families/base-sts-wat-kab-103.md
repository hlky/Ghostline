# base-sts-wat-kab-103

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_103\community\sts_wat_kab_103_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_103\scenes\sts_wat_kab_103.scene` | content candidate | 0 / 6 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_103\scenes\sts_wat_kab_103_fixer_call.scene` | content candidate | 0 / 6 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_103\scenes\sts_wat_kab_103_johnny_comment.scene` | content candidate | 0 / 4 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_103\sts_wat_kab_103.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_103\sts_wat_kab_103.quest` | content candidate | 1 / 0 | base\open_world\street_stories\watson\kabuki\sts_wat_kab_103\phases\sts_wat_kab_103.questphase |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questEndNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 1 |
| `questPhaseNodeDefinition` | 1 |
| `questStartNodeDefinition` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnEndNode[scnNodeId]` | 4 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 7 |
| `scnStartNode[scnNodeId]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `8cd3b647ae3f592ad947` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_103\scenes\sts_wat_kab_103.scene` / scene / 1 -> 4 -> 2 |
| `1a000c4a2942fdbb978c` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_103\scenes\sts_wat_kab_103_fixer_call.scene` / scene / 4 -> 7 -> 12 |
| `59394a189cb5a316e1d8` | 1 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_103\sts_wat_kab_103.quest` / h0 / 3 -> 2 -> 1 |
| `7e64c6caa0cef1487541` | 1 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_103\scenes\sts_wat_kab_103_fixer_call.scene` / scene / 1 -> 4 -> 7 |
| `d3a2c510dd58a21e697b` | 1 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_103\scenes\sts_wat_kab_103_fixer_call.scene` / scene / 4 -> 7 -> 9 |
| `e5862c59e31014c8499d` | 1 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_103\sts_wat_kab_103.quest` / h0 / 0 -> 3 -> 2 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
