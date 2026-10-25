"""Install the CET location chooser or import its complete placement set."""
from __future__ import annotations

import argparse
import copy
import json
import math
from pathlib import Path
import shutil
import sys

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'AGENTS.md').is_file())
sys.path.insert(0, str(ROOT / 'tools'))
WORLD = HERE / 'world/love-actually.world.json'
MOD = 'ghostline_love_actually_scout'
GUIDANCE = {
    'origin': ('Meeting anchor', 'Stand where Velvet will stand, facing V\'s approach. Reuse this position for the meeting group.', 'meeting'),
    '#gq004_mp_velvet': ('Meet Velvet map pin', 'Meeting entrance or Velvet\'s standing position.', 'meeting'),
    '#gq004_sm_velvet': ('Meeting scene anchor', 'Use Velvet\'s standing position and facing.', 'meeting'),
    '#gq004_tr_setup': ('Meeting setup centre (90 m)', 'Broad loading gate; normally the same centre as Velvet.', 'meeting'),
    '#gq004_tr_mood': ('Meeting mood centre (60 m)', 'Normally the same centre as Velvet.', 'meeting'),
    '#gq004_tr_awareness': ('Meeting awareness centre (3 m)', 'Normally the same centre as Velvet.', 'meeting'),
    '#gq004_tr_engage': ('Meeting conversation centre (2.5 m)', 'Normally the same centre as Velvet. Keep the approach unobstructed.', 'meeting'),
    '#gq004_spot_velvet': ('Velvet standing spot', 'Clear, walkable ground with room for a face-to-face conversation.', 'meeting'),
    '#gq004_mp_relay': ('Claw operation map pin', 'An accessible entry to the small Claw operation.', 'operation'),
    '#gq004_tr_operation': ('Operation centre (30 m)', 'Centre of the encounter, covering both sockets and all three guards.', 'operation'),
    '#gq004_tr_cleanup': ('Operation cleanup centre (50 m)', 'Normally the same centre as the operation. Leave space to exit this radius.', 'operation'),
    '#gq004_ap_relay': ('Recovery socket', 'First wall socket: stand at its floor position, face OUT from the wall, then adjust height to the socket centre.', 'device'),
    '#gq004_ap_upload': ('Distribution socket', 'A separate second socket, reachable after recovery. Face OUT from the wall and adjust its mounting height.', 'device'),
    '#gq004_spot_guard_1': ('Guard 1 - ranged', 'Clear walkable floor; face the direction this guard should watch.', 'guard'),
    '#gq004_spot_guard_2': ('Guard 2 - ranged', 'A different clear floor position. Preserve a stealth route past the guards.', 'guard'),
    '#gq004_spot_guard_3': ('Guard 3 - melee', 'A third clear floor position with room to move.', 'guard'),
}


def targets(world: dict) -> list[dict]:
    result = [dict(id='origin', label='Kabuki meeting site origin')]
    for key in ('markers', 'triggers', 'devices'):
        for item in world.get(key, []):
            if item.get('derived_from'):
                continue
            capture_ref = item.get('capture_ref', item['ref'])
            result.append(dict(id=capture_ref, label=capture_ref.lstrip('#')))
    for community in world['communities']:
        if 'spot' in community:
            spots = [community['spot']]
        else:
            spots = [s for entry in community['entries'] for s in entry['spots']]
        for spot in spots:
            result.append(dict(id=spot['ref'], label=spot['ref'].lstrip('#')))
    for row in result:
        label, hint, group = GUIDANCE.get(row['id'], (row['label'], 'Record exact position and facing.', 'other'))
        row.update(label=label, hint=hint, group=group, height=1.2 if group == 'device' else 0.0)
    return result


def snap_socket_to_wall(device: dict) -> None:
    """Mount the socket's rear collider face on its inspected wall plane."""
    mount = device.get('wall_mount')
    if not mount:
        return
    nx, ny = mount['normal']
    px, py = mount['surface_point']
    length = math.hypot(nx, ny)
    if not math.isfinite(length) or abs(length - 1) > 1e-5:
        raise ValueError('Wall mounting normal must be a unit vector')
    position = device['position']
    distance = (position['x'] - px) * nx + (position['y'] - py) * ny
    correction = mount['rear_offset'] + mount['clearance'] - mount.get('render_surface_inset', 0) - distance
    position['x'] += correction * nx
    position['y'] += correction * ny
    device['yaw'] = math.degrees(math.atan2(ny, nx))


def sync_device_markers(world: dict) -> None:
    """Derive quest-pin positions from mounted sockets, without extra captures."""
    markers = {m['ref']: m for m in world['markers']}
    devices = {d['ref']: d for d in world['devices']}
    for device in devices.values():
        snap_socket_to_wall(device)
    for name, device_ref in (('recover', '#gq004_ap_relay_link'), ('upload', '#gq004_ap_upload_link')):
        ref = '#gq004_mp_' + name
        if ref not in markers:
            markers[ref] = dict(ref=ref, sector='always_loaded')
            world['markers'].append(markers[ref])
        device = devices[device_ref]
        markers[ref].update(derived_from=device_ref, position=dict(device['position']), yaw=device['yaw'])


def apply_captures(world: dict, log: dict) -> dict:
    if log.get('schema_version') != 1 or log.get('quest') != 'gq004':
        raise ValueError('Expected the GQ004 scout schema')
    captures = log.get('captures')
    if not isinstance(captures, dict):
        raise ValueError('Expected captures keyed by target ID')
    required = {row['id'] for row in targets(world)}
    if required - captures.keys():
        raise ValueError('Missing captures: ' + ', '.join(sorted(required - captures.keys())))
    for key in required:
        pose = captures[key]
        if not isinstance(pose, dict) or not all(
            isinstance(pose.get(axis), (float, int)) and not isinstance(pose[axis], bool)
            and math.isfinite(pose[axis]) for axis in ('x', 'y', 'z', 'yaw')
        ):
            raise ValueError(f'Invalid finite XYZ/yaw capture: {key}')
    sockets = [captures[item.get('capture_ref', item['ref'])] for item in world.get('devices', [])]
    for index, socket in enumerate(sockets):
        if any(all(socket[axis] == other[axis] for axis in ('x', 'y', 'z')) for other in sockets[index + 1:]):
            raise ValueError('Socket captures coincide; record separate recovery and distribution mounts')
    result = copy.deepcopy(world)
    result['origin'] = {axis: captures['origin'][axis] for axis in ('x', 'y', 'z', 'yaw')}
    for collection in ('markers', 'triggers', 'devices'):
        for item in result.get(collection, []):
            if item.get('derived_from'):
                continue
            pose = captures[item.get('capture_ref', item['ref'])]
            mount = item.get('wall_mount')
            if mount and any(abs(pose[axis] - mount['capture_position'][axis]) > 0.001
                             for axis in ('x', 'y', 'z', 'yaw')):
                # A new location/facing needs a new inspected wall. Never
                # project unrelated future captures onto this old wall plane.
                item.pop('wall_mount')
            item['position'] = {axis: pose[axis] for axis in ('x', 'y', 'z')}
            if collection == 'triggers':
                item['position']['z'] -= item['outline']['height'] / 2
            item['yaw'] = pose['yaw']
            if collection == 'devices':
                # The socket plate faces local +X; player facing is local +Y.
                item['yaw'] = (pose['yaw'] + 90 + 180) % 360 - 180
                setback = item.get('mount_setback', 0.0)
                angle = math.radians(pose['yaw'])
                item['position']['x'] += math.sin(angle) * setback
                item['position']['y'] -= math.cos(angle) * setback
    for community in result['communities']:
        if 'spot' in community:
            spots = [community['spot']]
        else:
            spots = [s for entry in community['entries'] for s in entry['spots']]
        for spot in spots:
            pose = captures[spot['ref']]
            spot['position'] = {axis: pose[axis] for axis in ('x', 'y', 'z')}
            spot['yaw'] = pose['yaw']
        if 'position' in community:
            community['position'] = dict(spots[0]['position'])
    sync_device_markers(result)
    result['_note'] = 'CET-captured coordinates; collision, navmesh, scene facing and vanilla activity review still required.'
    return result


def check_install(game_root: Path, world: dict) -> dict:
    destination = game_root.resolve() / 'bin/x64/plugins/cyber_engine_tweaks/mods' / MOD
    errors = []
    installed = destination / 'init.lua'
    if not (game_root / 'bin/x64/Cyberpunk2077.exe').is_file():
        errors.append('Cyberpunk2077.exe is missing from the selected game root')
    if not (game_root / 'bin/x64/plugins/cyber_engine_tweaks.asi').is_file():
        errors.append('The CET plugin binary is missing')
    if not installed.is_file() or installed.read_bytes() != (HERE / 'cet/init.lua').read_bytes():
        errors.append('Installed scout code is absent or outdated')
    target_path = destination / 'targets.json'
    try:
        if json.loads(target_path.read_text(encoding='utf-8')) != targets(world):
            errors.append('Installed target list is outdated')
    except (OSError, ValueError):
        errors.append('Installed target list is absent or invalid')
    return dict(ready_for_capture=not errors, target_count=len(targets(world)),
                distinct_stops=7, log=str(destination / 'love-actually-locations.json'), errors=errors)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    install = sub.add_parser('install-cet')
    install.add_argument('--game-root', type=Path, required=True)
    check = sub.add_parser('check', help='Verify the installed capture helper matches current authoring inputs')
    check.add_argument('--game-root', type=Path, required=True)
    importer = sub.add_parser('import-log')
    importer.add_argument('--input', type=Path, required=True)
    importer.add_argument('--apply', action='store_true', help='Replace authored world only after the full capture set validates')
    args = parser.parse_args()
    world = json.loads(WORLD.read_text(encoding='utf-8'))
    if args.command == 'install-cet':
        base = args.game_root.resolve() / 'bin/x64/plugins/cyber_engine_tweaks'
        if not base.is_dir():
            parser.error(f'CET is not installed at {base}')
        destination = base / 'mods' / MOD
        destination.mkdir(parents=True, exist_ok=True)
        for source in (HERE / 'cet').glob('*.lua'):
            shutil.copyfile(source, destination / source.name)
        (destination / 'targets.json').write_text(json.dumps(targets(world), indent=2), encoding='utf-8')
        print(destination)
    elif args.command == 'check':
        report = check_install(args.game_root, world)
        print(json.dumps(report, indent=2))
        return 0 if report['ready_for_capture'] else 1
    else:
        log = json.loads(args.input.read_text(encoding='utf-8-sig'))
        updated = apply_captures(world, log)
        from generate_world import build_world_documents
        build_world_documents(updated, ROOT / '.tmp/gq004-placement-check/raw', ROOT / '.tmp/gq004-placement-check/archive')
        target = WORLD if args.apply else WORLD.with_name('love-actually.captured.world.json')
        from artifact_io import publish_json_artifacts
        publish_json_artifacts({target: updated})
        print(f'Validated {len(targets(world))} placements: {target}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
