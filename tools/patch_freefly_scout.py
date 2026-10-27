"""Apply a backed-up local scouting patch to keanuWheeze's installed FreeFly.

The third-party mod stays outside the repository. Its original license applies.
Run: python tools/patch_freefly_scout.py --game "K:/Cyberpunk 2077"
"""

import argparse
from datetime import datetime
import json
from pathlib import Path
import shutil


def replace_once(text, old, new):
    if text.count(old) != 1:
        raise ValueError(f"Unsupported FreeFly version: expected one occurrence of {old[:70]!r}")
    return text.replace(old, new, 1)


def patch(game):
    root = game / "bin/x64/plugins/cyber_engine_tweaks/mods/freefly"
    init_path = root / "init.lua"
    logic_path = root / "modules/utils/logic.lua"
    config_path = root / "config/config.json"
    init = init_path.read_text(encoding="utf-8")
    logic = logic_path.read_text(encoding="utf-8")
    config = json.loads(config_path.read_text(encoding="utf-8-sig"))
    if 'require("modules/utils/scout")' in init:
        raise ValueError("FreeFly Scout is already installed; restore its backup before reapplying")
    init = replace_once(init, 'local GameUI = require("modules/utils/GameUI")',
                        'local GameUI = require("modules/utils/GameUI")\nlocal scout = require("modules/utils/scout")')
    init = replace_once(init, '        self.nUI.setupNative(self)',
                        '        scout.install()\n        self.nUI.setupNative(self)')
    init = replace_once(init, '            self.runtimeData.inGame = false',
                        '            scout.stop(false)\n            self.runtimeData.active = false\n            self.runtimeData.inGame = false')
    init = replace_once(init, '            self.logic.fly(self, deltaTime)',
                        '            scout.update(self)\n            self.logic.fly(self, deltaTime)')
    start = init.index('    registerForEvent("onShutdown", function()')
    end = init.index('\n    registerInput(', start)
    init = init[:start] + '''    registerForEvent("onShutdown", function()
        scout.stop(true)
        self.runtimeData.active = false
    end)
''' + init[end:]
    logic = replace_once(logic, 'local utils = require("modules/utils/miscUtils")',
                         'local utils = require("modules/utils/miscUtils")\nlocal scout = require("modules/utils/scout")')
    start = logic.index('function logic.toggleFlight(mod, state)')
    end = logic.index('\nfunction logic.fly(', start)
    logic = logic[:start] + '''function logic.toggleFlight(mod, state)
        scout.setFlight(mod, state)
end
''' + logic[end:]
    logic = replace_once(logic, '        Game.GetStatPoolsSystem():RequestSettingStatPoolValue(GetPlayer():GetEntityID(), gamedataStatPoolType.Health, 100, nil)',
                         '        -- Named invulnerability replaces the original per-frame health refill.')
    config['noWeapon'] = True
    # Prepare everything before touching installed files; retain originals outside CET mods.
    backup = game / "ghostline-mod-backups" / ("freefly-scout-" + datetime.now().strftime("%Y%m%d-%H%M%S-%f"))
    backup.mkdir(parents=True)
    for path in (init_path, logic_path, config_path):
        target = backup / path.relative_to(root)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
    outputs = {init_path: init, logic_path: logic,
               config_path: json.dumps(config, separators=(',', ':')) + '\n',
               root / 'modules/utils/scout.lua': (Path(__file__).parent / 'freefly_scout_cet/scout.lua').read_text(encoding='utf-8')}
    try:
        for path, text in outputs.items():
            path.write_text(text, encoding='utf-8', newline='\n')
    except Exception:
        for path in (init_path, logic_path, config_path):
            shutil.copy2(backup / path.relative_to(root), path)
        raise
    print(f"Installed FreeFly Scout at {root}")
    print(f"Original files: {backup}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--game', required=True, type=Path)
    patch(parser.parse_args().game)
