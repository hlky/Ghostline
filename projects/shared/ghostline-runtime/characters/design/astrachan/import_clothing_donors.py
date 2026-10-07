"""Import attributed MakeHuman clothing as a fit/quality comparison.

Assets are downloaded from the official MakeHuman Community asset packs.
Geometry is CC-BY; retain the original mhclo attribution with any derivative.
"""
import bpy
import bmesh
from pathlib import Path
from mathutils import Vector

ROOT=next(parent for parent in Path(__file__).resolve().parents if (parent / "AGENTS.md").is_file())
OUT=ROOT/'generated/astrachan'


def obj_import(path,name,scale=(.1,.1,.1),offset=(0,-.045,1.02)):
    vertices=[];uvs=[];faces=[];faceuv=[]
    for line in path.read_text().splitlines():
        a=line.split()
        if not a:continue
        if a[0]=='v':
            x,y,z=map(float,a[1:4]);vertices.append((x*scale[0]+offset[0],z*scale[1]+offset[1],y*scale[2]+offset[2]))
        elif a[0]=='vt':uvs.append(tuple(map(float,a[1:3])))
        elif a[0]=='f':
            pairs=[p.split('/') for p in a[1:]][::-1]
            faces.append([int(p[0])-1 for p in pairs]);faceuv.append([int(p[1])-1 if len(p)>1 and p[1] else 0 for p in pairs])
    old=bpy.data.objects.get(name)
    if old:bpy.data.objects.remove(old,do_unlink=True)
    me=bpy.data.meshes.new(name);me.from_pydata(vertices,[],faces);me.update()
    if uvs:
        layer=me.uv_layers.new(name='UVMap')
        for polygon,inds in zip(me.polygons,faceuv):
            for loop,idx in zip(polygon.loop_indices,inds):layer.data[loop].uv=uvs[idx]
    ob=bpy.data.objects.new(name,me);bpy.context.scene.collection.objects.link(ob)
    for p in me.polygons:p.use_smooth=True
    ob['source_asset']=str(path.relative_to(ROOT));ob['license']='CC-BY';ob['stage']='Fitted donor; weights pending'
    return ob

hoodie=obj_import(OUT/'external/shirts02/clothes/elvs_hooded_sweat_jacket1/ladieshoodiedown1.obj','Astra tailored jacket donor')
hoodie['author']='Elvaerwyn'
hoodie.data.materials.append(bpy.data.materials['Astra charcoal cloth'])

# Turn the closed sweat-jacket into an open garment, then lower its neckline.
# Preserve a pristine downloaded OBJ for future topology/fit changes.
bm=bmesh.new();bm.from_mesh(hoodie.data)
cut=[]
for face in bm.faces:
    c=face.calc_center_median()
    xs=[v.co.x for v in face.verts]
    if c.y>-.01 and min(xs)<=.003 and max(xs)>=-.003:cut.append(face)
bmesh.ops.delete(bm,geom=cut,context='FACES')
for v in bm.verts:
    x,y,z=v.co
    front=max(0,min(1,(y+.045)/.12))
    waist=max(0,min(1,(.22-abs(x))/.13))
    v.co.x+=(-1 if x<0 else 1)*.063*front*waist
    if z>1.32:v.co.z=1.32+(z-1.32)*.58
    if z<1.10:v.co.z=1.10+(z-1.10)*1.40
    # Loose female fit through the chest and hips.
    v.co.x*=1.035
    v.co.y=-.045+(v.co.y+.045)*1.1
bmesh.ops.recalc_face_normals(bm,faces=bm.faces);bm.to_mesh(hoodie.data);bm.free()
sub=hoodie.modifiers.new('Tailored surface','SUBSURF');sub.levels=1
sol=hoodie.modifiers.new('Fabric lining','SOLIDIFY');sol.thickness=.0025

skirt=obj_import(OUT/'external/skirts02/clothes/elvs_pleated_plaid_mini_skirt/pleated_skirtelv1.obj','Astra pleated skirt donor',scale=(.105,.10,.070),offset=(0,-.035,1.003))
skirt['author']='Elvaerwyn';skirt.data.materials.append(bpy.data.materials['Astra charcoal cloth'])
sub=skirt.modifiers.new('Pleat finish','SUBSURF');sub.levels=1
sol=skirt.modifiers.new('Skirt fabric','SOLIDIFY');sol.thickness=.0015

for ob in bpy.data.collections['Astrachan custom study'].objects:
    if ob.name.startswith(('Open jacket','Jacket dropped','Ribbed jacket','Jacket zipper','Pocket','Jacket back','Embroidery','Pleated skirt','Hanging strap','Strap star','Front shoulder strap')):
        ob.hide_render=True

# Use the native basehead albedo/normal instead of the blank mannequin material.
head=bpy.data.objects.get('submesh_00_LOD_1.001')
if head:
    mat=bpy.data.materials.get('Astra skin preview') or bpy.data.materials.new('Astra skin preview');mat.use_nodes=True
    n=mat.node_tree.nodes;l=mat.node_tree.links;p=n.get('Principled BSDF')
    tex=n.new('ShaderNodeTexImage');tex.image=bpy.data.images.load(str(OUT/'materials/base/characters/head/player_base_heads/player_female_average/h0_000_pwa_c__basehead/textures/h0_000_pwa_c__basehead_d01.png'),check_existing=True)
    l.new(tex.outputs['Color'],p.inputs['Base Color']);p.inputs['Roughness'].default_value=.6
    p.inputs['Subsurface Weight'].default_value=.07
    head.data.materials.clear();head.data.materials.append(mat)

scene=bpy.context.scene;scene.cycles.samples=32
cam=scene.camera;cam.location=(2,5,1.75);cam.rotation_euler=(Vector((0,0,.96))-cam.location).to_track_quat('-Z','Y').to_euler()
scene.render.filepath=str(OUT/'donor-fit-comparison.png');bpy.ops.render.render(write_still=True)
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'astrachan-donor-fit.blend'))
print('Imported and fitted attributed jacket and pleated skirt donors')
