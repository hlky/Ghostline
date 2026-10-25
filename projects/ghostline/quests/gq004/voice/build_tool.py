"""Build ghostline-voice against the checkout matching GQ004's existing artifacts."""
from pathlib import Path
import json
import subprocess

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'AGENTS.md').is_file())


def main() -> int:
    config = json.loads(Path(__file__).with_name('toolchain.json').read_text(encoding='utf-8'))
    checkout = Path(config['dinoml_checkout'])
    revision = subprocess.check_output(['git', '-C', str(checkout), 'rev-parse', 'HEAD'], text=True).strip()
    if revision != config['dinoml_commit']:
        raise ValueError('DinoML checkout changed; review compatibility before replacing the working tool')
    command = ['cargo', 'build', '--release', '--locked', '--manifest-path', 'tools/ghostline-voice/Cargo.toml']
    for name in ('dinoml-qwen3-tts', 'dinoml-runtime'):
        crate = (checkout / 'crates' / name).as_posix()
        command.extend(['--config', f'patch."https://github.com/hlky/dinoml_v2".{name}.path="{crate}"'])
    subprocess.run(command, cwd=ROOT, check=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
