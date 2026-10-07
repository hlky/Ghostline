"""Correct component-specific eye materials and hair/jacket intersections."""
import bpy
import json
from pathlib import Path
from mathutils import Vector
from mathutils.bvhtree import BVHTree

ROOT=next(parent for parent in Path(__file__).resolve().parents if (parent / "AGENTS.md").is_file());OUT=ROOT/'generated/astrachan';repo=OUT/'materials'
data=json.loads((OUT/'donors/eyes.Material.json').read_text())
source=next(m['Data'] for m in data['Materials'] if m['Name']=='gradient_blue')
profile=repo/Path(source['IrisColorGradient'].replace('\\','/')+'.json')
# Native JSON elides RED defaults; the Blender material helper expects RGB keys.
d=json.loads(profile.read_text())
for entry in d['Data']['RootChunk']['gradientEntries']:
    color=entry.setdefault('color',{'$type':'Color'})
    for channel in ['Red','Green','Blue','Alpha']:color.setdefault(channel,0)
profile.write_text(json.dumps(d,indent=2)+'\n')

eye=bpy.data.materials.get('Astra native blue iris') or bpy.data.materials.new('Astra native blue iris');eye.use_nodes=True
from i_scene_cp77_gltf.material_types.eyegradient import EyeGradient
EyeGradient(str(repo)+'/', 'png', str(OUT)+'/').create(source,eye)
p=eye.node_tree.nodes.get('Principled BSDF');p.inputs['Transmission Weight'].default_value=.07;p.inputs['Subsurface Weight'].default_value=.12

lash=bpy.data.materials.get('Astra native dark lashes') or bpy.data.materials.new('Astra native dark lashes');lash.use_nodes=True
p=lash.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(.003,.002,.004,1);p.inputs['Roughness'].default_value=.65
tex=lash.node_tree.nodes.new('ShaderNodeTexImage')
tex.image=bpy.data.images.load(str(repo/'base/characters/common/hair/textures/hb1_brow_beard_lashes/hb1_01__lash_single_d.png'),check_existing=True)
tex.image.colorspace_settings.name='Non-Color';lash.node_tree.links.new(tex.outputs['Color'],p.inputs['Alpha']);lash.surface_render_method='DITHERED'

wet=bpy.data.materials.get('Astra eye tear film') or bpy.data.materials.new('Astra eye tear film');wet.use_nodes=True
p=wet.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(.10,.035,.027,1);p.inputs['Roughness'].default_value=.24;p.inputs['Alpha'].default_value=.12;wet.surface_render_method='DITHERED'
for ob in bpy.context.scene.objects:
    if ob.get('astra_role')=='eyes' and ob.type=='MESH' and not ob.name.startswith('Icosphere'):
        ob.data.materials.clear()
        ob.data.materials.append(lash if 'submesh_00_' in ob.name else eye if 'submesh_01_' in ob.name else wet)

# Project hair to the evaluated garment, including smoothing/lining modifiers.
coat=bpy.data.objects['Astra tailored jacket donor'];dep=bpy.context.evaluated_depsgraph_get()
ev=coat.evaluated_get(dep);me=ev.to_mesh()
bvh=BVHTree.FromPolygons([coat.matrix_world@v.co for v in me.vertices],[list(p.vertices) for p in me.polygons]);ev.to_mesh_clear()
fixed=0
for ob in bpy.context.scene.objects:
    if ob.get('astra_role')=='weighted_hair' and 'submesh_00_' in ob.name:
        for v in ob.data.vertices:
            x,y,z=v.co
            if z>1.52:continue
            front=y>-.025
            hit=bvh.ray_cast(Vector((x,1 if front else -1,z)),Vector((0,-1 if front else 1,0)))[0]
            if hit is not None:
                target=hit.y+(.022 if front else -.022)
                if (front and y<target) or (not front and y>target):v.co.y=target;fixed+=1
        ob.data.update()

scene=bpy.context.scene;scene.cycles.samples=24;scene.render.resolution_x=1000;scene.render.resolution_y=1250
cam=scene.camera
for name,pos,look,scale in [('portrait',(.3,3,1.72),(0,.02,1.58),.55),('front',(0,5,1.45),(0,0,.98),2)]:
    cam.location=pos;cam.rotation_euler=(Vector(look)-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.ortho_scale=scale
    scene.render.filepath=str(OUT/('corrected-'+name+'.png'));bpy.ops.render.render(write_still=True)
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'astrachan-corrected-materials.blend'))
print('Corrected',fixed,'hair vertices and all three eye component materials')
