"""Render the existing workspot scene with faster lossless intermediate PNGs."""
import bpy
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import workspot_preview_blender as renderer

configure_original = renderer._configure_scene


def configure(*args):
    configure_original(*args)
    bpy.context.scene.render.image_settings.compression = 0


renderer._configure_scene = configure
if __name__ == "__main__":
    renderer.main()
