"""Install, diagnose or serve the independent Game Scout MCP."""
from __future__ import annotations

import argparse
import atexit
from datetime import datetime
import json
from pathlib import Path
import shutil
import sys

from .core import Bridge, Library, ScoutError, atomic_json, file_lock

REPO = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG = REPO/'.local/game-scout.json'


def install(game: Path, data: Path, config_path: Path):
    game, data = game.resolve(), data.resolve()
    mods = game/'bin/x64/plugins/cyber_engine_tweaks/mods'
    if not mods.is_dir():
        raise ScoutError(f'No CET installation at {mods}')
    destination = mods/'game_scout'
    with file_lock(destination/'runtime/controller.lock'):
        backup = game/'ghostline-mod-backups'/('game-scout-'+datetime.now().strftime('%Y%m%d-%H%M%S-%f'))
        existing = [destination/name for name in ('init.lua','engine.lua') if (destination/name).exists()]
        if existing:
            backup.mkdir(parents=True)
            for path in existing:
                shutil.copy2(path,backup/path.name)
        for name in ('init.lua','engine.lua'):
            shutil.copy2(Path(__file__).parent/'cet'/name,destination/name)
    config = {'schema_version':1,'game_root':str(game),'data_root':str(data),
        'runtime':str(destination/'runtime'),
        'competing_lock':str(mods/'world_location_capture/runtime/controller.lock')}
    atomic_json(config_path,config)
    Library(data)
    return {'config':str(config_path.resolve()),'mod':str(destination),'data_root':str(data),
            'reload_required':True,'existing_mod_backup':str(backup) if existing else None}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config',type=Path,default=DEFAULT_CONFIG)
    commands = parser.add_subparsers(dest='command',required=True)
    installer = commands.add_parser('install')
    installer.add_argument('--game-root',type=Path,default=Path('K:/Cyberpunk 2077'))
    installer.add_argument('--data-root',type=Path,default=REPO/'converted/game-scout/library')
    commands.add_parser('doctor')
    commands.add_parser('serve')
    args = parser.parse_args(argv)
    try:
        if args.command == 'install':
            print(json.dumps(install(args.game_root,args.data_root,args.config),indent=2)); return 0
        config = json.loads(args.config.read_text())
        if config.get('schema_version') != 1:
            raise ScoutError('Unsupported scout configuration version')
        bridge = Bridge(Path(config['runtime']),Path(config['competing_lock']) if config.get('competing_lock') else None)
        if args.command == 'doctor':
            try:
                print(json.dumps({'ready':True,'runtime':bridge.state(),'config':config},indent=2)); return 0
            finally:
                bridge.close()
        # The capture backend loads native dependencies; initialize it before worker threads.
        import windows_capture
        from .controller import Scout
        from .images import CameraImages
        from .server import make_server
        library = Library(Path(config['data_root']))
        scout = Scout(bridge,library,CameraImages(library))
        atexit.register(bridge.close)
        try:
            make_server(scout).run(transport='stdio')
        finally:
            scout.stop()
            if scout.job_thread:
                scout.job_thread.join(timeout=2)
            bridge.close()
        return 0
    except (ScoutError,OSError,ValueError) as error:
        print(str(error),file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
