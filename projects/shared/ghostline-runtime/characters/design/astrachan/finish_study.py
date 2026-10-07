"""Finish and export the first reviewable custom-authoring candidate."""
import bpy
import math
import json
from pathlib import Path
from mathutils import Vector
from mathutils.bvhtree import BVHTree

ROOT=next(parent for parent in Path(__file__).resolve().parents if (parent / "AGENTS.md").is_file())
OUT=ROOT/'generated/astrachan'
col=bpy.data.collections['Astrachan custom study']
cloth=bpy.data.materials['Astra charcoal cloth']
knit=bpy.data.materials['Astra rib knit']
gold=bpy.data.materials['Astra antique gold']

def mesh(name,v,f,mat):
    old=bpy.data.objects.get(name)
    if old:bpy.data.objects.remove(old,do_unlink=True)
    d=bpy.data.meshes.new(name);d.from_pydata(v,[],f);d.update()
    o=bpy.data.objects.new(name,d);col.objects.link(o);d.materials.append(mat)
    for p in d.polygons:p.use_smooth=True
    return o

# Curved opening and soft vertical folds in the open jacket body.
v=[];f=[];ns=80;nr=28
for j in range(nr+1):
    t=j/nr
    rx=.25-.055*t
    ry=.178-.032*t
    for i in range(ns+1):
        a=.48+(2*math.pi-.96)*i/ns
        z=.875+(1.44-.11*(math.cos(a)+1)/2-.875)*t
        fold=(.005*math.sin(a*13+t*5)+.002*math.sin(a*25-t*7))*math.sin(math.pi*t)
        v.append(((rx+fold)*math.sin(a),-.06+(ry+fold)*math.cos(a),z))
        if j and i:
            k=j*(ns+1)+i;f.append((k-ns-2,k-ns-1,k,k-1))
o=mesh('Open jacket body',v,f,cloth)
s=o.modifiers.new('Fabric thickness','SOLIDIFY');s.thickness=.004
b=o.modifiers.new('Soft garment surface','SUBSURF');b.levels=1

for sign in [-1,1]:
    center=Vector((sign*.43,.165,1.143))
    tangent=Vector((sign*.04,.075,-.057)).normalized()
    u=tangent.cross(Vector((0,1,0))).normalized();w=tangent.cross(u).normalized()
    v=[];f=[];n=48
    for j in range(5):
        c=center+tangent*(-.026+j*.013)
        for i in range(n):
            a=2*math.pi*i/n;r=.053+.0012*math.cos(a*24)
            v.append(c+r*(math.cos(a)*u+math.sin(a)*w))
            if j:
                k=j*n+i;f.append((k-n,(j-1)*n+(i+1)%n,j*n+(i+1)%n,k))
    o=mesh('Ribbed jacket cuff '+str(sign),v,f,knit)
    s=o.modifiers.new('Cuff thickness','SOLIDIFY');s.thickness=.005

# Suppress the excessive silver shine in the first hair preview.
p=bpy.data.materials['Astra long hair preview'].node_tree.nodes.get('Principled BSDF')
p.inputs['Roughness'].default_value=.58
p.inputs['Specular IOR Level'].default_value=.16

def line(name,points,width,mat):
    old=bpy.data.objects.get(name)
    if old:bpy.data.objects.remove(old,do_unlink=True)
    d=bpy.data.curves.new(name,'CURVE');d.dimensions='3D';d.bevel_depth=width;d.bevel_resolution=2
    sp=d.splines.new('BEZIER');sp.bezier_points.add(len(points)-1)
    for p,co in zip(sp.bezier_points,points):p.co=co;p.handle_left_type='AUTO';p.handle_right_type='AUTO'
    ob=bpy.data.objects.new(name,d);col.objects.link(ob);d.materials.append(mat)
    return ob

dark=bpy.data.materials['Astra hair cap']
for sign in [-1,1]:
    line('Eyebrow study '+str(sign),[(sign*.014,.051,1.712),(sign*.028,.050,1.715),(sign*.043,.041,1.710)],.0013,dark)
    line('Lash study '+str(sign),[(sign*.017,.060,1.691),(sign*.030,.067,1.697),(sign*.043,.054,1.692)],.0007,dark)
    line('Jacket zipper '+str(sign),[(sign*.25*math.sin(.48),.101,.879),(sign*.226*math.sin(.48),.092,1.14),(sign*.195*math.sin(.48),.069,1.335)],.0015,gold)

# Apply the authoritative boot component mask (13 = visible chunks 0, 2, 3)
# and include the independent laces component retained in the item database.
for ob in bpy.context.scene.objects:
    if ob.get('astra_role')=='boot_donor' and 'submesh_01_' in ob.name:
        ob.hide_render=True
if not any(ob.get('astra_role')=='boot_laces' for ob in bpy.context.scene.objects):
    before=set(bpy.data.objects)
    bpy.ops.import_scene.gltf(filepath=str(OUT/'donors/s1_066_pwa_boot__bovver_laces_01.glb'))
    for ob in set(bpy.data.objects)-before:
        ob['astra_role']='boot_laces'
        if ob.type=='MESH':
            ob.data.materials.clear()
            ob.data.materials.append(bpy.data.materials['Astra boot leather'])

# Fit the star pins to the evaluated hair surface instead of leaving them on a
# flat image-reference plane. Alpha holes are not considered by this fit pass.
dep=bpy.context.evaluated_depsgraph_get()
hairtrees=[]
for ob in bpy.context.scene.objects:
    if ob.get('astra_role')=='weighted_hair' and ob.type=='MESH' and not ob.name.startswith('Icosphere'):
        ev=ob.evaluated_get(dep);me=ev.to_mesh()
        hairtrees.append(BVHTree.FromPolygons([ob.matrix_world@v.co for v in me.vertices],[list(p.vertices) for p in me.polygons]))
        ev.to_mesh_clear()
for index,ob in enumerate(sorted((o for o in col.objects if o.name.startswith('Hair star')),key=lambda o:o.name)):
    x=-.048-index*.008;z=1.787-index*.027
    hits=[]
    for tree in hairtrees:
        pnt,normal,face,dist=tree.ray_cast(Vector((x,1,z)),Vector((0,-1,0)))
        if pnt is not None:hits.append(pnt)
    if hits:
        target=max(hits,key=lambda p:p.y)+Vector((0,.0025,0))
        center=sum((ob.matrix_world@v.co for v in ob.data.vertices),Vector())/len(ob.data.vertices)
        delta=target-center
        ob.location+=delta

# All source and game reference images are packed into the editable .blend.
for im in bpy.data.images:
    if im.source=='FILE' and im.has_data:
        try:im.pack()
        except RuntimeError:pass

scene=bpy.context.scene
scene['astrachan_stage']='First custom modelling candidate: not game-ready'
scene['astrachan_remaining']='Hair rig/dyng matching, clothing weights and UVs, final textures, head likeness, platform boots, in-game deformation'
scene.render.resolution_x=1000;scene.render.resolution_y=1250
cam=scene.camera
for name,pos in [('front',(0,5,1.35)),('back',(0,-5,1.35)),('three-quarter',(2.2,5,1.75))]:
    cam.location=pos;cam.rotation_euler=(Vector((0,0,.96))-cam.location).to_track_quat('-Z','Y').to_euler()
    scene.render.filepath=str(OUT/('candidate-'+name+'.png'))
    bpy.ops.render.render(write_still=True)
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'astrachan-custom-candidate.blend'))
report={'stage':'first custom modelling candidate','blender':bpy.app.version_string,
        'io_suite':'2.0.0','runtime_validated':False,'hair_physics_updated':False,
        'custom_clothing_weighted':False,'views':['candidate-front.png','candidate-back.png','candidate-three-quarter.png'],
        'blend':'astrachan-custom-candidate.blend',
        'visible_meshes':sum(o.type=='MESH' and not o.hide_render for o in scene.objects)}
(OUT/'candidate-report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
