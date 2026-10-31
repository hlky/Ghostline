# base-sts-std-rcr-104

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_104\scenes\sts_std_rcr_104_ben_and_carride.scene` | content candidate | 0 / 6 |  |
| `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_104\scenes\sts_std_rcr_104_militech_chats.scene` | content candidate | 0 / 6 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnEndNode[scnNodeId]` | 3 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 5 |
| `scnStartNode[scnNodeId]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `8cd3b647ae3f592ad947` | 2 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_104\scenes\sts_std_rcr_104_militech_chats.scene` / scene / 1 -> 4 -> 2 |
| `c1b6601d2f647c8a694d` | 2 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_104\scenes\sts_std_rcr_104_ben_and_carride.scene` / scene / 4 -> 6 -> 10 |
| `27faccd7b30abbc3add2` | 1 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_104\scenes\sts_std_rcr_104_ben_and_carride.scene` / scene / 4 -> 6 -> 8 |
| `3300202aa48a37eea8e1` | 1 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_104\scenes\sts_std_rcr_104_ben_and_carride.scene` / scene / 1 -> 4 -> 6 |
| `afbc348d6f0f691e60f3` | 1 | `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_104\scenes\sts_std_rcr_104_ben_and_carride.scene` / scene / 6 -> 10 -> 2 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
