"""Install, diagnose and serve the independent Cyberpunk gameplay MCP."""
from __future__ import annotations

import argparse
import atexit
from datetime import datetime
import json
from pathlib import Path
import shutil
import sys

from .core import Bridge, GameplayError, Library, atomic_json, file_lock

REPO = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG = REPO / '.local/cyberpunk-mcp.json'


def install(game, data, config_path):
    game, data = game.resolve(), data.resolve()
    mods = game / 'bin/x64/plugins/cyber_engine_tweaks/mods'
    if not mods.is_dir():
        raise GameplayError(f'No CET installation at {mods}')
    destination = mods / 'cyberpunk_mcp'
    backup = None
    with file_lock(destination / 'runtime/controller.lock'):
        existing = [destination / name for name in ('init.lua', 'engine.lua') if (destination / name).exists()]
        if existing:
            backup = game / 'ghostline-mod-backups' / ('cyberpunk-mcp-' + datetime.now().strftime('%Y%m%d-%H%M%S-%f'))
            backup.mkdir(parents=True)
            for path in existing:
                shutil.copy2(path, backup / path.name)
        for name in ('init.lua', 'engine.lua'):
            shutil.copy2(Path(__file__).parent / 'cet' / name, destination / name)
    config = {'schema_version': 1, 'game_root': str(game), 'data_root': str(data),
              'runtime': str(destination / 'runtime'),
              'competing_locks': [str(mods / name / 'runtime/controller.lock')
                                  for name in ('game_scout', 'world_location_capture')],
              'bindings': {}}
    # Preserve customized bindings on reinstall.
    if config_path.exists():
        config['bindings'] = json.loads(config_path.read_text(encoding='utf-8')).get('bindings', {})
    atomic_json(config_path, config)
    Library(data)
    return {'config': str(config_path.resolve()), 'mod': str(destination),
            'reload_required': True, 'backup': str(backup) if backup else None}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, default=DEFAULT_CONFIG)
    commands = parser.add_subparsers(dest='command', required=True)
    installer = commands.add_parser('install')
    installer.add_argument('--game-root', type=Path, default=Path('K:/Cyberpunk 2077'))
    installer.add_argument('--data-root', type=Path, default=REPO / 'converted/cyberpunk-mcp/library')
    commands.add_parser('doctor')
    commands.add_parser('serve')
    args = parser.parse_args(argv)
    try:
        if args.command == 'install':
            print(json.dumps(install(args.game_root, args.data_root, args.config), indent=2))
            return 0
        config = json.loads(args.config.read_text(encoding='utf-8'))
        if config.get('schema_version') != 1:
            raise GameplayError('Unsupported Cyberpunk MCP configuration')
        bridge = Bridge(Path(config['runtime']), [Path(p) for p in config.get('competing_locks', [])])
        try:
            if args.command == 'doctor':
                state = bridge.state()
                if state.get('product') != 'cyberpunk_mcp':
                    raise GameplayError('Wrong CET runtime')
                print(json.dumps({'connected': True, 'gameplay_ready': state.get('ready', False), 'state': state}, indent=2))
                return 0
            import windows_capture  # noqa: F401 -- initialize native capture on main thread
            from .controller import Gameplay
            from .images import CameraImages
            from .server import make_server
            library = Library(Path(config['data_root']))
            game = Gameplay(bridge, library, CameraImages(library), config.get('bindings'))
            atexit.register(game.stop)
            try:
                make_server(game).run(transport='stdio')
            finally:
                game.stop()
        finally:
            bridge.close()
        return 0
    except (GameplayError, OSError, ValueError, KeyError) as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
