"""Pin native decoder inputs for a long appearance-render batch."""
from __future__ import annotations

import hashlib
from pathlib import Path
import shutil


def snapshot_tools(output, red, schema):
    red_hash = hashlib.sha256(red.read_bytes()).hexdigest()
    schema_hash = hashlib.sha256(schema.read_bytes()).hexdigest()
    folder = output / 'cache/tool-snapshot' / (red_hash[:12] + '-' + schema_hash[:12])
    folder.mkdir(parents=True, exist_ok=True)
    targets = (folder / 'ghostline-red.exe', folder / 'red-schema.json')
    for source, target, digest in zip((red, schema), targets, (red_hash, schema_hash)):
        if not target.exists():
            shutil.copy2(source, target)
        if hashlib.sha256(target.read_bytes()).hexdigest() != digest:
            raise RuntimeError(f'Native tool snapshot does not match {Path(source).name}')
    return targets
