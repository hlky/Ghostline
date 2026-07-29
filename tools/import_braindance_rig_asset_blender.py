"""Create a reusable, animation-free Blender rig asset from a WKit GLB.

Run through Blender, for example:

    blender --background --factory-startup --python \
      tools/import_braindance_rig_asset_blender.py -- \
      --input vanilla_rig_and_anims.glb --output man_base.glb

The checked output contains only the armature. Vanilla actions and meshes are
deliberately excluded so normal braindance authoring starts from a clean rig.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import bpy  # type: ignore[import-not-found]


def parse_args() -> argparse.Namespace:
    arguments = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args(arguments)


def main() -> None:
    args = parse_args()
    input_path = args.input.resolve()
    output_path = args.output.resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(input_path))
    armatures = [obj for obj in bpy.context.scene.objects if obj.type == "ARMATURE"]
    if len(armatures) != 1:
        raise RuntimeError(
            f"Expected one armature in {input_path}, found {len(armatures)}"
        )
    armature = armatures[0]
    armature.name = "man_base"
    armature.data.name = "man_base"
    for obj in list(bpy.context.scene.objects):
        obj.animation_data_clear()
        obj.select_set(obj == armature)
        if obj != armature:
            bpy.data.objects.remove(obj, do_unlink=True)
    for action in list(bpy.data.actions):
        bpy.data.actions.remove(action)
    bpy.context.view_layer.objects.active = armature
    bpy.ops.export_scene.gltf(
        filepath=str(output_path),
        export_format="GLB",
        use_selection=True,
        export_animations=False,
    )
    print(
        "GHOSTLINE_RIG_ASSET_COMPLETE "
        + json.dumps(
            {
                "input": str(input_path),
                "output": str(output_path),
                "bones": len(armature.data.bones),
                "actions": len(bpy.data.actions),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
