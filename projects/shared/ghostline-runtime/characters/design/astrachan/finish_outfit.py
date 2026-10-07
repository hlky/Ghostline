"""Stocking shells, platform boot construction and final material corrections."""
import bpy
import math
from pathlib import Path
from mathutils import Vector

ROOT=next(parent for parent in Path(__file__).resolve().parents if (parent / "AGENTS.md").is_file());OUT=ROOT/'generated/astrachan'
old=bpy.data.collections.get('Astra outfit finishing')
if old:
    for ob in list(old.objects):bpy.data.objects.remove(ob,do_unlink=True)
    bpy.data.collections.remove(old)
col=bpy.data.collections.new('Astra outfit finishing');bpy.context.scene.collection.children.link(col)

def mat(name,color,rough=.5,metal=0):
    m=bpy.data.materials.get(name) or bpy.data.materials.new(name);m.use_nodes=True
    p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(*color,1);p.inputs['Roughness'].default_value=rough;p.inputs['Metallic'].default_value=metal
    return m

rubber=mat('Astra platform rubber',(.003,.0035,.005),.79)
leather=bpy.data.materials['Astra strap leather'];gold=bpy.data.materials['Astra brushed brass'];knit=bpy.data.materials['Astra fitted rib knit']
stocking=mat('Astra sheer stocking shell',(.009,.008,.012),.54)
p=stocking.node_tree.nodes.get('Principled BSDF');p.inputs['Alpha'].default_value=.78;stocking.surface_render_method='DITHERED'
p.inputs['Sheen Weight'].default_value=.18

def mesh(name,v,f,m):
    d=bpy.data.meshes.new(name);d.from_pydata(v,[],f);d.update();o=bpy.data.objects.new(name,d);col.objects.link(o);d.materials.append(m)
    for p in d.polygons:p.use_smooth=True
    return o

def line(name,pts,r,m):
    d=bpy.data.curves.new(name,'CURVE');d.dimensions='3D';d.bevel_depth=r;d.bevel_resolution=3
    s=d.splines.new('POLY');s.points.add(len(pts)-1)
    for p,v in zip(s.points,pts):p.co=(*v,1)
    o=bpy.data.objects.new(name,d);col.objects.link(o);d.materials.append(m);return o

# Actual translucent stocking geometry over the original weighted body meshes.
for name in ['submesh_04_LOD_1','submesh_05_LOD_1','submesh_06_LOD_1']:
    src=bpy.data.objects[name];src.data.materials.clear();src.data.materials.append(bpy.data.materials['Fit mannequin'])
    o=src.copy();o.data=src.data.copy();o.name='Astra stockings '+name;col.objects.link(o)
    o.data.materials.clear();o.data.materials.append(stocking)
    for v in o.data.vertices:v.co+=v.normal*.0008
    o['stage']='Body-fitted stocking shell; donor skin weights retained'
bpy.data.objects['submesh_07_LOD_1'].hide_render=True

# Fit the high collar to the neck instead of leaving a wide cylindrical rim.
for o in bpy.context.scene.objects:
    if o.name.startswith('Top high collar'):o.hide_render=True
v=[];f=[]
for j,(z,rx,ry,cy) in enumerate([(1.496,.054,.049,-.052),(1.52,.050,.045,-.052),(1.544,.046,.042,-.052)]):
    for i in range(65):
        a=i*2*math.pi/64;v.append((rx*math.sin(a),cy+ry*math.cos(a),z))
        if j and i:k=j*65+i;f.append((k-66,k-65,k,k-1))
o=mesh('Astra fitted high collar',v,f,knit);s=o.modifiers.new('Rib knit thickness','SOLIDIFY');s.thickness=.002

# Platform soles follow a shoe-shaped outline, including the narrowed heel.
outline=[(-.041,-.162),(.041,-.162),(.053,-.136),(.055,-.074),(.066,-.008),(.068,.060),(.057,.107),(.025,.133),(-.025,.133),(-.057,.107),(-.068,.060),(-.066,-.008),(-.055,-.074),(-.053,-.136)]
for sign in [-1,1]:
    cx=sign*.152;v=[];f=[];count=len(outline)
    for j,(z,factor) in enumerate([(.005,.96),(.014,1),(.039,1),(.052,.98)]):
        for i,(x,y) in enumerate(outline):
            v.append((cx+x*factor,y*factor,z))
            if j:k=j*count+i;f.append((k-count,(j-1)*count+(i+1)%count,j*count+(i+1)%count,k))
    f.extend([tuple(reversed(range(count))),tuple(range(3*count,4*count))])
    o=mesh('Platform sole '+str(sign),v,f,rubber)
    be=o.modifiers.new('Rounded outsole edge','BEVEL');be.width=.009;be.segments=3
    # Tread lugs are separate editable geometry with broad contact surfaces.
    for i in range(8):
        y=-.14+i*.032;w=.047 if i<3 else .058
        bpy.ops.mesh.primitive_cube_add(size=1,location=(cx,y,.006))
        ob=bpy.context.object;ob.name='Boot tread %s %s'%(sign,i);ob.scale=(w*2,.022,.012)
        bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
        for c in list(ob.users_collection):c.objects.unlink(ob)
        col.objects.link(ob);ob.data.materials.append(rubber)
        be=ob.modifiers.new('Tread bevel','BEVEL');be.width=.003;be.segments=2
    # Top ankle band and side buckle.
    v=[];f=[]
    for j,z in enumerate([.229,.251]):
        for i in range(65):
            a=i*2*math.pi/64;v.append((cx+.061*math.sin(a),-.070+.067*math.cos(a),z))
            if j and i:k=j*65+i;f.append((k-66,k-65,k,k-1))
    ob=mesh('Boot ankle belt '+str(sign),v,f,leather);so=ob.modifiers.new('Band leather','SOLIDIFY');so.thickness=.002
    x=cx+sign*.041;y=-.012;z=.24
    line('Boot brass buckle '+str(sign),[(x-.012,y,z-.011),(x+.012,y,z-.011),(x+.012,y,z+.011),(x-.012,y,z+.011),(x-.012,y,z-.011)],.0014,gold)
    line('Boot buckle tongue '+str(sign),[(x,y,z-.01),(x,y+.001,z+.009)],.0009,gold)

# Recolour only the iris using the native mask, retaining the albedo sclera and
# its pupil/vein detail. No screen-space eye texture is used.
m=bpy.data.materials['Astra native blue iris'];n=m.node_tree.nodes;l=m.node_tree.links;p=n.get('Principled BSDF')
albedo=next(node for node in n if node.type=='TEX_IMAGE' and node.image and 'he_000_base_d02' in node.image.name)
mask=next(node for node in n if node.type=='TEX_IMAGE' and node.image and node.image.name.startswith('eye_mask'))
r=n.new('ShaderNodeValToRGB');r.color_ramp.elements[0].color=(.002,.008,.021,1);r.color_ramp.elements[1].color=(.12,.31,.46,1)
r.color_ramp.elements.new(.35).color=(.021,.083,.18,1)
l.new(mask.outputs['Color'],r.inputs[0])
fac=n.new('ShaderNodeMath');fac.operation='GREATER_THAN';fac.inputs[1].default_value=.006;l.new(mask.outputs['Color'],fac.inputs[0])
mix=n.new('ShaderNodeMixRGB');l.new(fac.outputs[0],mix.inputs[0]);l.new(albedo.outputs['Color'],mix.inputs[1]);l.new(r.outputs[0],mix.inputs[2]);l.new(mix.outputs[0],p.inputs['Base Color'])
p.inputs['Specular IOR Level'].default_value=.32;p.inputs['Coat Weight'].default_value=.25;p.inputs['Transmission Weight'].default_value=0

coat=bpy.data.materials['Astra black twill'];coat.node_tree.nodes.get('Principled BSDF').inputs['Specular IOR Level'].default_value=.25
for node in coat.node_tree.nodes:
    if node.type=='NORMAL_MAP':node.inputs['Strength'].default_value=.35

scene=bpy.context.scene;scene.cycles.samples=24;cam=scene.camera
for name,pos,look,scale in [('front',(0,5,1.45),(0,0,.98),2),('portrait',(.3,3,1.72),(0,.02,1.58),.55)]:
    cam.location=pos;cam.rotation_euler=(Vector(look)-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.ortho_scale=scale
    scene.render.filepath=str(OUT/('outfit-'+name+'.png'));bpy.ops.render.render(write_still=True)
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'astrachan-outfit-authoring.blend'))
print('Stockings, platforms and blue iris shader saved')
