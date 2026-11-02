"""Vehicle rig/slot assembly for the existing item renderer."""
from __future__ import annotations
import json
from pathlib import Path
import re
import hashlib
import shutil
from contextlib import redirect_stdout
import io
import sys
import bpy
from mathutils import Matrix, Quaternion, Vector
from item_render_blender import enable_material_cache, import_cp77, repair_multilayer_masks
from vehicle_studio import resolve_slot, selected_chunk_materials, glb_metadata

def vehicle_material_compatibility():
    from i_scene_cp77_gltf.main.material_registry import MaterialRule, REGISTRY
    REGISTRY.register([r'base\vehicles\common\materials\vehicle_modding_destruction.mt'],
                      REGISTRY.resolve(r'base\materials\vehicle_destr_blendshape.mt'))
    REGISTRY.register([r'base\fx\shaders\device_diode.mt', r'base\materials\metal_base_ui.mt'],
                      REGISTRY.resolve(r'engine\materials\metal_base.remt'))

    class CrystalGlazing:
        def create(self, data, material):
            nodes, links = material.node_tree.nodes, material.node_tree.links
            nodes.clear()
            shader = nodes.new('ShaderNodeBsdfPrincipled')
            shader.inputs['Base Color'].default_value = (.015, .025, .035, 1)
            shader.inputs['Roughness'].default_value = .12
            shader.inputs['Metallic'].default_value = .35
            shader.inputs['Transmission Weight'].default_value = .1
            output = nodes.new('ShaderNodeOutputMaterial')
            links.new(shader.outputs['BSDF'], output.inputs['Surface'])

    class CrystalOverlay:
        def create(self, data, material):
            nodes, links = material.node_tree.nodes, material.node_tree.links
            nodes.clear()
            shader = nodes.new('ShaderNodeBsdfTransparent')
            output = nodes.new('ShaderNodeOutputMaterial')
            links.new(shader.outputs['BSDF'], output.inputs['Surface'])

    REGISTRY.register([r'base\fx\_shaders\crystal_dome.mt'],
                      MaterialRule(factory=lambda builder, raw: CrystalGlazing()))
    REGISTRY.register([r'base\fx\_shaders\crystal_dome_opaque.mt'],
                      MaterialRule(factory=lambda builder, raw: CrystalOverlay()))

def transform(data):
    position = data.get('Translation', data.get('Position', {}))
    rotation = data.get('Rotation', data.get('Orientation', {}))
    scale = data.get('Scale', {})
    coordinates = []
    for axis in 'XYZ':
        coordinate = position.get(axis, position.get(axis.lower(), 0))
        coordinates.append(coordinate.get('Bits', 0) / 131072 if isinstance(coordinate, dict) else coordinate)
    return Matrix.LocRotScale(Vector(coordinates), Quaternion((rotation.get('r', 1),
        rotation.get('i', 0), rotation.get('j', 0), rotation.get('k', 0))),
        Vector([scale.get(axis, 1) for axis in 'XYZ']))

def import_full_vehicle(job):
    components = job['components']
    by_name = {c['name']['$value']: c for c in components if 'name' in c}
    handles = {c['parentTransform']['HandleId']: c['parentTransform']['Data'] for c in components
               if c.get('parentTransform', {}).get('Data')}
    rigs = {}
    for name, path in job['rigs'].items():
        root = json.loads(Path(path).read_text(encoding='utf-8'))['Data']['RootChunk']
        matrices = {}

        def bone(index):
            if index not in matrices:
                parent = root['boneParentIndexes'][index]
                matrices[index] = (bone(parent) if parent >= 0 else Matrix.Identity(4)) @ transform(root['boneTransforms'][index])
            return matrices[index]
        rigs[name] = {n['$value']: bone(i) for i, n in enumerate(root['boneNames'])}
    resolved = {}

    def component_matrix(name, visiting=()):
        if name in resolved:
            return resolved[name]
        if name in visiting:
            raise RuntimeError(f'Cyclic vehicle component binding: {name}')
        comp = by_name.get(name)
        if comp is None:
            raise RuntimeError(f'Missing bound vehicle component: {name}')
        binding = comp.get('parentTransform', {})
        binding = binding.get('Data', handles.get(binding.get('HandleRefId'), {}))
        parent, slot = binding.get('bindName', {}).get('$value'), binding.get('slotName', {}).get('$value')
        matrix = Matrix.Identity(4)
        if parent:
            matrix = component_matrix(parent, (*visiting, name))
            if slot and parent in rigs:
                matrix = matrix @ rigs[parent][slot]
            elif slot and by_name[parent].get('slots'):
                definition = resolve_slot(by_name[parent], slot)
                rig_binding = by_name[parent].get('parentTransform', {})
                rig_binding = rig_binding.get('Data', handles.get(rig_binding.get('HandleRefId'), {}))
                rig_name = rig_binding.get('bindName', {}).get('$value')
                bone_name = definition.get('boneName', {}).get('$value')
                if bone_name:
                    matrix = matrix @ rigs[rig_name][bone_name]
                matrix = matrix @ transform({'Translation': definition.get('relativePosition', {}),
                    'Rotation': definition.get('relativeRotation', {})})
        matrix = matrix @ transform(comp.get('localTransform', {}))
        resolved[name] = matrix
        return matrix

    diagnostics = []
    enable_material_cache()
    vehicle_material_compatibility()
    for comp in components:
        if not comp.get('resolved_glb'):
            continue
        before = set(bpy.data.objects)
        glb = Path(comp['resolved_glb'])
        if comp.get('native_pbr'):
            bpy.ops.import_scene.gltf(filepath=str(glb))
        else:
            source_sidecar = glb.with_suffix('.Material.json')
            payload = json.loads(source_sidecar.read_text(encoding='utf-8'))
            selected_materials, selected_key = selected_chunk_materials(payload, glb_metadata(glb),
                comp.get('meshAppearance', {}).get('$value'), comp.get('chunkMask', 2**64 - 1))
            from i_scene_cp77_gltf.main.material_registry import REGISTRY
            unsupported = [m['MaterialTemplate'] for m in selected_materials if REGISTRY.resolve(m['MaterialTemplate']) is None]
            if unsupported:
                raise RuntimeError(f'Unsupported authored shader on {comp["name"]["$value"]}: {unsupported}')
            original_repo = payload['MaterialRepo']
            payload['MaterialRepo'] = str(Path(original_repo.removeprefix('\\\\?\\')).resolve())
            changed = payload['MaterialRepo'] != original_repo
            for material in payload['Materials']:
                data = material['Data']
                if 'MultilayerMask' in data and 'GlobalNormal' not in data and 'BakedNormal' not in data:
                    data['BakedNormal'] = r'engine\textures\small_flat_normal.xbm'
                    changed = True
            if changed:
                source_sidecar.write_text(json.dumps(payload), encoding='utf-8')
            class ImportLog(io.StringIO):
                def write(self, text):
                    sys.__stdout__.write(text)
                    return super().write(text)
            import_log = ImportLog()
            with redirect_stdout(import_log):
                import_cp77(glb, comp.get('meshAppearance', {}).get('$value', 'Default'))
            if 'Material Setup Failed on:' in import_log.getvalue() or 'invalid .mlsetup.json' in import_log.getvalue():
                raise RuntimeError(f'Authored material import failed on {comp["name"]["$value"]}')
            sidecar = json.loads(glb.with_suffix('.Material.json').read_text(encoding='utf-8'))
            for mat in sidecar['Materials']:
                repair_multilayer_masks(glb, mat['Name'], Path(job['output']) / '_materials' / comp['name']['$value'])
        imported = set(bpy.data.objects) - before
        name = comp['name']['$value']
        mask = int(comp.get('chunkMask', 2**64 - 1))
        matrix = component_matrix(name)
        visual_scale = comp.get('visualScale', {})
        matrix = matrix @ Matrix.Diagonal(Vector([visual_scale.get(axis, 1) for axis in 'XYZ'] + [1]))
        vertices = 0
        for obj in imported:
            if obj.type == 'MESH':
                for polygon in obj.data.polygons:
                    polygon.use_smooth = True
                match = re.search(r'submesh_(\d+)', obj.name)
                if match and not (mask & (1 << int(match.group(1)))):
                    obj.hide_render = True
                    obj.hide_viewport = True
                else:
                    vertices += len(obj.data.vertices)
            if obj.parent not in imported:
                obj.matrix_world = matrix @ obj.matrix_world
        diagnostics.append({'component': name, 'vertices': vertices, 'matrix': [list(v) for v in matrix],
                            'mesh_appearance': comp.get('meshAppearance', {}).get('$value'),
                            'selected_materials': [m['Name'] for m in selected_materials] if not comp.get('native_pbr') else [],
                            'shader_approximations': comp.get('shader_approximations', [])})
    bpy.context.view_layer.update()
    # Short texture paths keep Blender's loader on the same inputs that WolvenKit exported.
    staging = Path(job['output']) / '_textures'
    for texture in bpy.data.images:
        if texture.source != 'FILE' or not texture.filepath:
            continue
        path = Path(bpy.path.abspath(texture.filepath)).resolve()
        if path.is_file() and (len(str(path)) > 230 or not texture.has_data):
            staging.mkdir(parents=True, exist_ok=True)
            destination = staging / (hashlib.sha256(str(path).encode()).hexdigest()[:24] + path.suffix)
            if not destination.exists():
                shutil.copyfile(path, destination)
            texture.filepath = str(destination)
            texture.reload()
    # Existing item studio views look toward -Y; RED vehicles point toward +Y.
    rotation = Matrix.Rotation(3.141592653589793, 4, 'Z')
    for obj in bpy.context.scene.objects:
        if obj.parent is None:
            obj.matrix_world = rotation @ obj.matrix_world
    bpy.context.view_layer.update()
    return diagnostics
