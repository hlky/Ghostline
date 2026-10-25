"""Build Love, Actually.exe as an isolated authoring preview."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys

ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'AGENTS.md').is_file())
HERE = Path(__file__).resolve().parent
PROJECT = ROOT / 'projects/ghostline'
sys.path.insert(0, str(ROOT / 'tools'))
from quest_build import publish_build
from quest_compiler import compile_manifest_artifacts, resource_paths, QuestArtifact
from phases import reach, meeting, root, transfer, attempt, reward_repair, ending, finish_and_epilogue, leave


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out-root', type=Path, default=PROJECT / 'generated/love-actually-preview')
    parser.add_argument('--deserialize', action='store_true')
    args = parser.parse_args()
    output = args.out_root.resolve()
    if output == ROOT or output == PROJECT or any(output.is_relative_to(p / 'source') for p in [ROOT, PROJECT]):
        parser.error('Preview output must be outside source and project roots')
    raw, archive = resource_paths(r'mod\gq004\phases\gq004.questphase')
    artifacts = compile_manifest_artifacts(HERE / 'quest.json', raw, archive, allow_planned=True,
                                          stage_overrides={'reach': reach, 'meet': meeting, 'return': meeting,
                                                           'recover': transfer, 'upload': transfer, 'ending': ending,
                                                           'leave': leave},
                                          root_override=root)
    stages = {s['id']: s for s in json.loads((HERE / 'quest.json').read_text())['stages']}
    for stage in ('recover', 'upload'):
        device = stages[stage]['device']
        raw, archive = resource_paths(rf'mod\gq004\phases\gq004_{stage}_attempt.questphase')
        artifacts.append(QuestArtifact(raw, archive, attempt(device, archive,
            'Velvet Crash' if stage == 'upload' else 'Heartbreaker Protocol')))
    raw, archive = resource_paths(r'mod\gq004\phases\gq004_reward_repair.questphase')
    repair = reward_repair(archive)
    from quest_compiler import validate_handle_graph, validate_no_forward_handle_refs
    validate_handle_graph(repair, context='reward repair')
    validate_no_forward_handle_refs(repair, context='reward repair')
    artifacts.append(QuestArtifact(raw, archive, repair))
    raw, archive = resource_paths(r'mod\gq004\phases\gq004_finish_and_epilogue.questphase')
    finish = finish_and_epilogue(archive)
    validate_handle_graph(finish, context='finish and epilogue')
    validate_no_forward_handle_refs(finish, context='finish and epilogue')
    artifacts.append(QuestArtifact(raw, archive, finish))
    # Compile the ordinary phone graph separately; its one-shot wrapper owns
    # dispatch. Quest completion belongs to finish_and_epilogue, not a reply.
    from quest_compiler import build_phone_phase
    # Resolve the composition bindings using the compiled original artifact's
    # authoring spec, exactly as the regular compiler does.
    from quest_compiler import load_spec
    spec, diagnostics = load_spec(HERE / 'quest.json')
    assert spec is not None and not any(d.level == 'error' for d in diagnostics)
    phone_stage = next(s for s in spec.stages if s.id == 'ending')
    raw, archive = resource_paths(r'mod\gq004\phases\gq004_epilogue_messages.questphase')
    phone = build_phone_phase(phone_stage, archive)
    validate_handle_graph(phone, context='epilogue messages')
    validate_no_forward_handle_refs(phone, context='epilogue messages')
    artifacts.append(QuestArtifact(raw, archive, phone))
    publish_build(artifacts, namespace='gq004', output_root=output, deserialize=args.deserialize)
    # Every preview scene points to its own preview binary, never the live source.
    for source in sorted((HERE / 'scenes').glob('*.scene-spec.json')):
        spec = json.loads(source.read_text(encoding='utf-8'))
        for key, tree in [('raw_path', 'raw'), ('archive_path', 'archive')]:
            relative = Path(spec[key]).resolve().relative_to(PROJECT / 'source' / tree)
            spec[key] = str(output / 'source' / tree / relative)
        target = output / 'specs' / source.name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(spec, indent=2) + '\n', encoding='utf-8')
        command = [sys.executable, str(ROOT / 'tools/generate_scene.py'), 'generate', '--spec', str(target)]
        if args.deserialize:
            command.append('--deserialize')
        subprocess.run(command, cwd=ROOT, check=True)
    from generate_world import build_world
    world = json.loads((HERE / 'world/love-actually.world.json').read_text(encoding='utf-8'))
    from scout import sync_device_markers
    sync_device_markers(world)
    build_world(world, output / 'source/raw', output / 'source/archive')
    print(f'Preview: {output}. World is not registered or installed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
