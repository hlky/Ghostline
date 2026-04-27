# Ghostline

Cyberpunk 2077 quest mod (WIP)

## Questphase Explorer

Use `tools/explore_questphase.py` to inspect deserialized questphase JSON without
dumping the whole CR2W-JSON file into context.

The default target is
`source/raw/mod/gq000/phases/gq000_patch_meet.questphase.json`:

```powershell
py .\tools\explore_questphase.py summary
py .\tools\explore_questphase.py nodes --sockets
py .\tools\explore_questphase.py edges
py .\tools\explore_questphase.py refs
py .\tools\explore_questphase.py handles --type TriggerCondition
py .\tools\explore_questphase.py search gq000_01_tr
py .\tools\explore_questphase.py node id:11
py .\tools\explore_questphase.py handle 13
py .\tools\explore_questphase.py dot > questphase.dot
```

Pass another raw questphase with `--file`:

```powershell
py .\tools\explore_questphase.py --file .\source\raw\mod\gq000\phases\other.questphase.json summary
```

Large lists are bounded by default. Use `--limit`, `--offset`, or `--limit 0`
on list commands when you need more rows.

## Scene Explorer

Use `tools/explore_scene.py` to inspect deserialized `.scene` CR2W-JSON.

The default target is `source/raw/mod/gq000/scenes/gq000_patch_meet.scene.json`:

```powershell
py .\tools\explore_scene.py summary
py .\tools\explore_scene.py actors
py .\tools\explore_scene.py nodes
py .\tools\explore_scene.py edges
py .\tools\explore_scene.py events
py .\tools\explore_scene.py lines
py .\tools\explore_scene.py choices
py .\tools\explore_scene.py refs --kind NodeRef
py .\tools\explore_scene.py handles --type TriggerCondition
py .\tools\explore_scene.py node 8
py .\tools\explore_scene.py handle 41
py .\tools\explore_scene.py search gq000_01_tr
py .\tools\explore_scene.py dot > scene.dot
```

Pass another raw scene with `--file`:

```powershell
py .\tools\explore_scene.py --file .\source\raw\mod\gq000\scenes\other.scene.json summary
```

## Localization Explorer

Use `tools/explore_localization.py` to inspect subtitle and VO-map CR2W-JSON.
By default it loads the current `gq000_01` subtitle and VO raw JSON files
together, then cross-checks entries by `stringId`.

```powershell
py .\tools\explore_localization.py summary
py .\tools\explore_localization.py entries
py .\tools\explore_localization.py check
py .\tools\explore_localization.py search Arasaka
py .\tools\explore_localization.py entry 6099223344158574223
py .\tools\explore_localization.py refs
py .\tools\explore_localization.py types
```

Pass one or more localization files with repeated `--file` arguments:

```powershell
py .\tools\explore_localization.py --file .\source\raw\mod\gq000\localization\en-us\subtitles\gq000_01.json.json --file .\source\raw\mod\gq000\localization\en-us\vo\gq000_01.json.json check
```
