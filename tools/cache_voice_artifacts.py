"""Copy or verify the pinned voice bundle under the ignored repository-local cache."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'tools/voice-artifacts.json'
LOCK = ROOT / 'tools/voice-artifacts.lock.json'
CACHE = ROOT / '.local/voice'


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(8 * 1024 * 1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def files(path: Path, excluded: set[str]):
    """Exclude regenerable debug/HF caches and refuse linked directories."""
    if path.is_file():
        yield Path(path.name), path
        return
    if not path.is_dir():
        raise FileNotFoundError(path)

    def walk(directory: Path):
        for child in sorted(directory.iterdir()):
            if child.name in excluded:
                continue
            if child.is_symlink() or child.is_junction():
                raise ValueError(f'Linked input requires an explicit concrete source: {child}')
            if child.is_dir():
                yield from walk(child)
            elif child.is_file():
                yield child.relative_to(path), child

    yield from walk(path)


def destination(relative: str) -> Path:
    path = (CACHE / relative).resolve()
    if not path.is_relative_to(CACHE.resolve()) or path == CACHE.resolve():
        raise ValueError(f'Cache destination escapes its bundle: {relative}')
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['plan', 'copy', 'verify'])
    args = parser.parse_args()
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    if args.mode == 'verify':
        lock = json.loads(LOCK.read_text(encoding='utf-8'))
        total = 0
        for entry in lock['entries']:
            for record in entry['files']:
                path = destination(record['path'])
                if not path.is_file() or path.stat().st_size != record['bytes'] or sha256(path) != record['sha256']:
                    raise ValueError(f'Cached file missing or changed: {path}')
                total += 1
            print(f"Verified {entry['id']}: {len(entry['files'])} files", flush=True)
        print(json.dumps({'verified_files': total}))
        return 0

    planned = []
    destinations = set()
    for entry in manifest['entries']:
        source = ROOT / entry['source']
        target = destination(entry['destination'])
        rows = list(files(source, set(entry.get('exclude_names', []))))
        if not rows:
            raise ValueError(f'Empty source: {source}')
        for relative, item in rows:
            output = target if source.is_file() else target / relative
            if output in destinations:
                raise ValueError(f'Duplicate cache destination: {output}')
            destinations.add(output)
        planned.append((entry, source, target, rows))
        print(f"{entry['id']}: {len(rows)} files, {sum(p.stat().st_size for _, p in rows):,} bytes", flush=True)
    required = sum(p.stat().st_size for _, source, target, rows in planned for rel, p in rows
                   if not (target if source.is_file() else target / rel).exists())
    if required > shutil.disk_usage(ROOT).free:
        raise ValueError(f'Insufficient free space for {required:,} additional bytes')
    if args.mode == 'plan':
        return 0

    lock_entries = []
    for entry, source, target, rows in planned:
        records = []
        for relative, item in rows:
            output = target if source.is_file() else target / relative
            before = item.stat()
            digest = sha256(item)
            output.parent.mkdir(parents=True, exist_ok=True)
            if output.exists():
                if not output.is_file() or sha256(output) != digest:
                    raise ValueError(f'Existing cache differs; preserve it and use a new bundle: {output}')
            else:
                temporary = output.with_name(output.name + '.copying')
                if temporary.exists():
                    raise ValueError(f'Interrupted copy exists; inspect before retrying: {temporary}')
                shutil.copy2(item, temporary)
                if sha256(temporary) != digest:
                    raise ValueError(f'Copy verification failed: {temporary}')
                temporary.rename(output)
            after = item.stat()
            if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
                raise ValueError(f'Source changed while copying: {item}')
            records.append({'path': output.relative_to(CACHE).as_posix(),
                            'bytes': after.st_size, 'sha256': digest})
        lock_entries.append({'id': entry['id'], 'source': entry['source'], 'files': records})
        print(f"Copied and verified {entry['id']}", flush=True)
    lock = {'schema_version': 1, 'bundle': manifest['bundle'],
            'compatibility': manifest['compatibility'], 'entries': lock_entries}
    LOCK.write_text(json.dumps(lock, indent=2) + '\n', encoding='utf-8')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
