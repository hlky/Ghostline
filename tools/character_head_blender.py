"""Blender-side runner for the NPV template's embedded head scripts."""

from __future__ import annotations

import argparse
import ast
import json
import sys
from pathlib import Path

import bpy  # type: ignore[import-not-found]


SCRIPT_NAMES = ("00_import_files.py", "01_apply_shapekeys.py", "02_export_files.py")
SHAPE_NAMES = ("eyes", "nose", "mouth", "jaw", "ears")


class HeadScriptTransformer(ast.NodeTransformer):
    def __init__(self, shapes: dict[str, int]) -> None:
        self.shapes = shapes

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.AST:
        if node.name == "showPopup":
            return ast.FunctionDef(
                name="showPopup",
                args=node.args,
                body=[ast.Pass()],
                decorator_list=[],
                returns=None,
                type_comment=None,
            )
        return self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign) -> ast.AST:
        if any(isinstance(target, ast.Name) and target.id == "meshVariants" for target in node.targets):
            return ast.Assign(
                targets=node.targets,
                value=ast.Dict(
                    keys=[ast.Constant(name) for name in SHAPE_NAMES],
                    values=[ast.Constant(str(self.shapes[name])) for name in SHAPE_NAMES],
                ),
            )
        return self.generic_visit(node)


def parse_args() -> argparse.Namespace:
    arguments = sys.argv[sys.argv.index("--") + 1 :] if "--" in sys.argv else []
    parser = argparse.ArgumentParser()
    parser.add_argument("--shapes", type=Path, required=True)
    return parser.parse_args(arguments)


def execute_text(name: str, shapes: dict[str, int]) -> None:
    text = bpy.data.texts.get(name)
    if text is None:
        raise RuntimeError(f"Blend template is missing embedded script {name}")
    tree = ast.parse(text.as_string(), filename=name)
    tree = HeadScriptTransformer(shapes).visit(tree)
    ast.fix_missing_locations(tree)
    namespace = {"__name__": "__main__", "__file__": name}
    exec(compile(tree, name, "exec"), namespace, namespace)


def main() -> None:
    args = parse_args()
    shapes = json.loads(args.shapes.read_text(encoding="utf-8"))
    if set(shapes) != set(SHAPE_NAMES):
        raise RuntimeError(f"Expected shapes: {', '.join(SHAPE_NAMES)}")
    for name in SCRIPT_NAMES:
        print(f"GHOSTLINE_HEAD_SCRIPT {name}")
        execute_text(name, shapes)
    print("GHOSTLINE_HEAD_COMPLETE")


if __name__ == "__main__":
    main()
