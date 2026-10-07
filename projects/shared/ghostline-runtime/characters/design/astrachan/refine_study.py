"""Refine the saved Astrachan study using weighted game geometry.

Run through Blender MCP after build_study.py. Generated output remains a visual
authoring candidate; RED materials and dangle simulation are not validated here.
"""
import bpy
import math
from pathlib import Path
from mathutils import Vector

ROOT = next(parent for parent in Path(__file__).resolve().parents if (parent / "AGENTS.md").is_file())
OUT = ROOT / 'generated/astrachan'
MATS = OUT / 'materials/base/characters/common/hair/textures'
study = bpy.data.collections['Astrachan custom study']


def material(name, color, roughness=.65, metal=0):
    m = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes = True
    m.diffuse_color = (*color, 1)
    p = m.node_tree.nodes.get('Principled BSDF')
    p.inputs['Base Color'].default_value = (*color, 1)
    p.inputs['Metallic'].default_value = metal
    p.inputs['Roughness'].default_value = roughness
    return m


cloth = material('Astra charcoal cloth', (.021, .024, .033), .86)
knit = material('Astra rib knit', (.014, .015, .023), .82)
gold = material('Astra antique gold', (.48, .285, .09), .35, .72)
leather = material('Astra boot leather', (.009, .011, .017), .42)
skin = material('Fit mannequin', (.46, .32, .255), .72)
for o in list(bpy.context.scene.objects):
    if o.name.startswith(('Hair layer', 'Hair scalp', 'Fringe guide',
                          'Astra hair donor', 'boot toe', 'boot shaft',
                          'platform', 'Boot lace')) or o.name.startswith('Icosphere'):
        o.hide_render = True
        if o.name in bpy.context.view_layer.objects:
            o.hide_set(True)


def import_glb(path, role):
    present = [o for o in bpy.context.scene.objects if o.get('astra_role') == role]
    if present:
        return present
    before = set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=str(path))
    objs = list(set(bpy.data.objects) - before)
    for o in objs:
        o['astra_role'] = role
        if o.name.startswith('Icosphere'):
            o.hide_render = True
            if o.name in bpy.context.view_layer.objects:
                o.hide_set(True)
    return objs


weighted = import_glb(
    ROOT / 'converted/characters/goth_baddie/full-preview/raw/ep1/characters/common/hair/hh_225_wa__long_bangs/hh_225_wa__long_bangs.glb',
    'weighted_hair')
bodypath = ROOT / 'converted/characters/goth_baddie/full-preview/raw/mod/ghostline/characters/honey/body'
for side in ['l', 'r']:
    for o in import_glb(bodypath / ('a0_000_pwa_base_hq__' + side + '.glb'), 'arm_' + side):
        if o.type == 'MESH' and not o.name.startswith('Icosphere'):
            o.data.materials.clear()
            o.data.materials.append(skin)

# Preview shader uses the original strand alpha and gradient maps, with a
# dedicated muted blue-black palette. These nodes do not replace RED materials.
hm = material('Astra long hair preview', (.008, .009, .018), .43)
nodes = hm.node_tree.nodes
links = hm.node_tree.links
p = nodes.get('Principled BSDF')
alpha = nodes.get('Astra strand alpha') or nodes.new('ShaderNodeTexImage')
alpha.name = 'Astra strand alpha'
alpha.image = bpy.data.images.load(str(MATS / 'hh_long01_alpha01_r.png'), check_existing=True)
alpha.image.colorspace_settings.name = 'Non-Color'
links.new(alpha.outputs['Color'], p.inputs['Alpha'])
hm.surface_render_method = 'DITHERED'
geo = nodes.new('ShaderNodeNewGeometry')
separate = nodes.new('ShaderNodeSeparateXYZ')
links.new(geo.outputs['Position'], separate.inputs[0])
mapping = nodes.new('ShaderNodeMapRange')
mapping.inputs['From Min'].default_value = 1.05
mapping.inputs['From Max'].default_value = 1.8
links.new(separate.outputs['Z'], mapping.inputs['Value'])
ramp = nodes.new('ShaderNodeValToRGB')
ramp.color_ramp.elements[0].color = (.027, .035, .075, 1)
ramp.color_ramp.elements[1].color = (.006, .007, .013, 1)
links.new(mapping.outputs[0], ramp.inputs[0])
links.new(ramp.outputs['Color'], p.inputs['Base Color'])


def elongate(v):
    """Smooth shoulder-length to waist-length change; scalp stays fixed."""
    x, y, z = v
    t = max(0, min(1, (1.73 - z) / .25))
    z -= .38 * (t * t * (3 - 2 * t))
    x *= 1 + .52 * t
    # Keep hair outside the jacket envelope; extending Z alone buries the tips.
    target_y = .153 if y > -.026 else -.275
    y = y * (1-t) + target_y * t
    x += .012 * math.sin(t * 7 + x * 35) * t
    return Vector((x, y, z))


for o in weighted:
    if o.type != 'MESH' or o.name.startswith('Icosphere'):
        continue
    is_fringe = 'submesh_01_' in o.name
    is_cap = 'submesh_02_' in o.name
    if not o.get('astra_elongated'):
        inv = o.matrix_world.inverted()
        for v in o.data.vertices:
            world = o.matrix_world @ v.co
            if not is_cap and not is_fringe:
                world = elongate(world)
            elif is_fringe:
                # Give the blunt stock fringe a small side sweep, keeping eyes clear.
                t = max(0, min(1, (1.79 - world.z) / .09))
                world.x += .026 * t
                world.z += .006 * t + .012 * t * world.x / .07
            v.co = inv @ world
        o['astra_elongated'] = True
    o.data.materials.clear()
    o.data.materials.append(material('Astra hair cap', (.006, .007, .013), .65) if is_cap else hm)
    o['stage'] = 'Custom geometry candidate; rest rig and dyng need matching edits'

# Lower the sleeve opening into the intended dropped-shoulder position.
for o in study.objects:
    if o.name.startswith('Jacket dropped sleeve') and not o.get('astra_lowered'):
        for v in o.data.vertices:
            t = max(0, min(1, (v.co.z - 1.26) / .21))
            v.co.z -= .077 * t
        o['astra_lowered'] = True

# Make the fitted top continuous: a small matching waist panel hides the donor
# body's material boundaries while retaining the upper donor's fitted shape.
def mesh_object(name, verts, faces, mat):
    old = bpy.data.objects.get(name)
    if old:
        bpy.data.objects.remove(old, do_unlink=True)
    me = bpy.data.meshes.new(name)
    me.from_pydata(verts, [], faces)
    me.update()
    o = bpy.data.objects.new(name, me)
    study.objects.link(o)
    me.materials.append(mat)
    for poly in me.polygons:
        poly.use_smooth = True
    return o


verts, faces = [], []
for j, (z, rx, ry, cy) in enumerate([(1.09,.167,.119,-.053),(1.16,.148,.104,-.044),(1.23,.139,.097,-.041)]):
    for i in range(65):
        a = i * 2 * math.pi / 64
        verts.append((rx*math.sin(a),cy+ry*math.cos(a),z))
        if j and i:
            k=j*65+i
            faces.append((k-66,k-65,k,k-1))
mesh_object('Top lower fitted panel', verts, faces, knit)

def line(name, points, radius, mat):
    old = bpy.data.objects.get(name)
    if old:
        bpy.data.objects.remove(old, do_unlink=True)
    d=bpy.data.curves.new(name,'CURVE');d.dimensions='3D';d.bevel_depth=radius;d.bevel_resolution=2
    s=d.splines.new('POLY');s.points.add(len(points)-1)
    for pt,co in zip(s.points,points):pt.co=(*co,1)
    o=bpy.data.objects.new(name,d);study.objects.link(o);d.materials.append(mat)
    return o


# Garment construction detail: hem, pockets, straps and simple back embroidery.
for side in [-1,1]:
    x=side*.192
    line('Pocket welt '+str(side),[(x-.029,.056,1.15),(x+.029,.056,1.15)],.005,leather)
    line('Pocket border '+str(side),[(x-.035,.071,1.14),(x-.034,.089,1.05),(x+.033,.088,1.05),(x+.034,.071,1.14)],.0013,gold)
    line('Front shoulder strap '+str(side),[(side*.095,.033,1.49),(side*.12,.076,1.37),(side*.12,.05,1.13)],.004,leather)
    line('Thigh harness '+str(side),[(side*.12-.042,.022,.876),(side*.12,.05,.871),(side*.12+.042,.022,.876)],.008,leather)

back=[(-.105,-.234,1.15),(-.065,-.249,1.12),(-.027,-.251,1.17),(.012,-.25,1.135),(.06,-.245,1.18),(.11,-.229,1.15)]
line('Jacket back constellation',back,.0013,gold)
for i,pnt in enumerate(back):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=12,ring_count=8,radius=.004,location=pnt)
    o=bpy.context.object;o.name='Embroidery star '+str(i);o.data.materials.append(gold)
    for c in list(o.users_collection):c.objects.unlink(o)
    study.objects.link(o)

# Use the detailed stock boot geometry as the editable foundation.
bootpath=ROOT/'converted/item-database/asset-cache/0b8164ac01d1385d7aa7701f64dc30a691dad101/raw/base/characters/garment/player_equipment/feet/s1_066_boot__bovver/s1_066_pwa_boot__bovver.glb'
for o in import_glb(bootpath,'boot_donor'):
    if o.type=='MESH' and not o.name.startswith('Icosphere'):
        o.data.materials.clear();o.data.materials.append(leather)
        o['stage']='Stock boot donor; platform and buckle customization pending'

# Neutral studio lighting makes silhouette and surface problems inspectable.
scene=bpy.context.scene
scene.render.engine='CYCLES'
scene.cycles.samples=32
scene.cycles.use_denoising=True
scene.world.use_nodes=True
scene.world.node_tree.nodes['Background'].inputs[0].default_value=(.23,.26,.33,1)
scene.world.node_tree.nodes['Background'].inputs[1].default_value=.3
for name,location,power,size,color in [
    ('Astra key',(2.5,3.8,4),650,3,(1,.90,.80)),
    ('Astra fill',(-3,2,2.4),450,3,(.69,.80,1)),
    ('Astra rim',(0,-3,3.2),750,2,(.7,.79,1))]:
    o=bpy.data.objects.get(name)
    if o is None:
        d=bpy.data.lights.new(name,'AREA');o=bpy.data.objects.new(name,d);scene.collection.objects.link(o)
    o.location=location;o.rotation_euler=(Vector((0,0,1))-o.location).to_track_quat('-Z','Y').to_euler()
    o.data.energy=power;o.data.shape='DISK';o.data.size=size;o.data.color=color
scene.view_settings.view_transform='AgX'
scene.render.resolution_x=900;scene.render.resolution_y=1100;scene.render.resolution_percentage=100
cam=scene.camera;cam.data.ortho_scale=2.02
for view,pos in [('front',(0,5,1.35)),('back',(0,-5,1.35)),('three-quarter',(2.3,5,1.75))]:
    cam.location=pos;cam.rotation_euler=(Vector((0,0,.96))-cam.location).to_track_quat('-Z','Y').to_euler()
    scene.render.filepath=str(OUT/('refined-'+view+'.png'))
    bpy.ops.render.render(write_still=True)
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'astrachan-refined-study.blend'))
print('Saved refined study with weighted hair donor and real arms/boots')
