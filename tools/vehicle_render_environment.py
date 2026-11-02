"""Process-local AMD driver environment for the existing Blender HIP renderer."""
from __future__ import annotations

import hashlib
import os
from pathlib import Path


def blender_environment():
    env = dict(os.environ)
    if os.name != 'nt':
        return env
    system = Path(os.environ.get('SystemRoot', 'C:/Windows')) / 'System32'
    runtime = system / 'amdhip64_6.dll'
    driver = None
    if runtime.is_file():
        signature = hashlib.sha256(runtime.read_bytes()).digest()
        for candidate in (system / 'DriverStore/FileRepository').glob('amdocl.inf_amd64_*/amdhip64_6.dll'):
            if hashlib.sha256(candidate.read_bytes()).digest() == signature:
                driver = candidate.parent
                break
    # Development ROCm SDK dependencies can conflict with the installed display
    # driver's HIP runtime. Scope this correction to the Blender child process.
    entries = [p for p in env.get('PATH', '').split(';') if 'rocm' not in p.lower() and 'dinoml' not in p.lower()]
    env['PATH'] = ';'.join([*([str(driver)] if driver else []), str(system), *entries])
    for name in ('HIP_PATH', 'ROCM_PATH', 'ROCM_HOME', 'HIP_DEVICE_LIB_PATH', 'HIP_PLATFORM'):
        env.pop(name, None)
    return env
