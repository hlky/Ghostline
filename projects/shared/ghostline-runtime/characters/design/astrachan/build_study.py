"""Editable Astrachan silhouette study. Run inside the prepared Blender MCP scene.

This produces modelling guides, not game-ready meshes or final hair cards.
"""
import bpy, math, random
from mathutils import Vector
from pathlib import Path
OUT=Path('H:/projects/Ghostline/generated/astrachan')
random.seed(21)
old=bpy.data.collections.get('Astrachan custom study')
if old:
    for o in list(old.objects): bpy.data.objects.remove(o,do_unlink=True)
    bpy.data.collections.remove(old)
col=bpy.data.collections.new('Astrachan custom study');bpy.context.scene.collection.children.link(col)
def material(name,color,metal=0):
    m=bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.diffuse_color=(*color,1);m.use_nodes=True
    p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(*color,1);p.inputs['Metallic'].default_value=metal;p.inputs['Roughness'].default_value=.55
    return m
cloth=material('Astra charcoal cloth',(.026,.029,.04));rib=material('Astra rib knit',(.014,.017,.024));hair=material('Astra midnight hair',(.018,.019,.033));navy=material('Astra navy ends',(.04,.047,.085));gold=material('Astra antique gold',(.56,.34,.14),.7);skin=material('Fit mannequin',(.43,.40,.38));stock=material('Astra stocking study',(.075,.061,.065));leather=material('Astra boot leather',(.022,.024,.03))
def link(o,mat):
    for c in list(o.users_collection):c.objects.unlink(o)
    col.objects.link(o)
    if mat:o.data.materials.append(mat)
    o['stage']='silhouette study; requires retopology, UVs, rigging and game validation'
    return o

def mesh(name,v,f,mat,smooth=True):
    d=bpy.data.meshes.new(name);d.from_pydata(v,[],f);d.update();o=bpy.data.objects.new(name,d);col.objects.link(o);d.materials.append(mat)
    for p in d.polygons:p.use_smooth=smooth
    o['stage']='silhouette study'
    return o

def shell(name,rings,mat,start=0,end=2*math.pi,steps=64,pleats=0):
    v=[];f=[]
    for z,rx,ry,cy in rings:
        for i in range(steps+1):
            a=start+(end-start)*i/steps
            fold=1+pleats*math.cos(a*16)
            v.append((rx*math.sin(a)*fold,cy+ry*math.cos(a)*fold,z))
    for j in range(len(rings)-1):
        for i in range(steps):
            k=j*(steps+1)+i;f.append((k,k+1,k+steps+2,k+steps+1))
    o=mesh(name,v,f,mat);s=o.modifiers.new('Fabric thickness','SOLIDIFY');s.thickness=.003
    return o

def curve(name,points,width,mat):
    d=bpy.data.curves.new(name,'CURVE');d.dimensions='3D';d.bevel_depth=width;d.bevel_resolution=3
    s=d.splines.new('BEZIER');s.bezier_points.add(len(points)-1)
    for b,p in zip(s.bezier_points,points):b.co=p;b.handle_left_type='AUTO';b.handle_right_type='AUTO'
    o=bpy.data.objects.new(name,d);col.objects.link(o);d.materials.append(mat);return o

def sleeve(sign):
    centers=[(sign*.18,-.04,1.415),(sign*.245,-.037,1.36),(sign*.33,-.023,1.285),(sign*.39,.09,1.20),(sign*.43,.165,1.143)]
    radii=[.093,.11,.112,.092,.060];v=[];f=[];n=24
    for j,p in enumerate(centers):
        tangent=Vector(centers[min(j+1,4)])-Vector(centers[max(j-1,0)]);tangent.normalize();u=tangent.cross(Vector((0,1,0))).normalized();w=tangent.cross(u).normalized()
        for i in range(n):
            a=2*math.pi*i/n;r=radii[j]*(1+.04*math.cos(a*6));v.append(Vector(p)+r*(math.cos(a)*u+math.sin(a)*w))
    for j in range(4):
        for i in range(n):k=j*n+i;f.append((k,j*n+(i+1)%n,(j+1)*n+(i+1)%n,k+n))
    o=mesh('Jacket dropped sleeve '+str(sign),v,f,cloth);m=o.modifiers.new('Sleeve smoothing','SUBSURF');m.levels=2
    s=o.modifiers.new('Sleeve thickness','SOLIDIFY');s.thickness=.004

def star(name,x,y,z,r=.012):
    v=[(x,y,z)]
    for i in range(10):
        a=i*math.pi/5;rr=r if i%2==0 else r*.43;v.append((x+math.sin(a)*rr,y,z+math.cos(a)*rr))
    o=mesh(name,v,[(0,i+1,(i+1)%10+1) for i in range(10)],gold,False);s=o.modifiers.new('Metal thickness','SOLIDIFY');s.thickness=.002
    b=o.modifiers.new('Soft edges','BEVEL');b.width=.0008;b.segments=2

# Cover the body using editable garment volumes and a copied fitted upper torso.
for o in list(bpy.context.scene.objects):
    if o.name.startswith('submesh') and o.type=='MESH':
        o.data.materials.clear();o.data.materials.append(skin)
        if o.name in ['submesh_04_LOD_1','submesh_05_LOD_1','submesh_06_LOD_1']:o.data.materials.clear();o.data.materials.append(stock)
for name in ['submesh_00_LOD_1','submesh_01_LOD_1','submesh_02_LOD_1']:
    src=bpy.data.objects.get(name)
    o=src.copy();o.data=src.data.copy();col.objects.link(o);o.name='Top fit donor '+name;o.data.materials.clear();o.data.materials.append(rib)
    m=o.modifiers.new('Garment ease','DISPLACE');m.strength=.006;m.mid_level=0
shell('Top high collar',[(1.49,.059,.054,-.055),(1.54,.057,.052,-.055)],rib)
shell('Pleated skirt',[(1.09,.163,.12,-.055),(1.035,.18,.127,-.05),(.88,.224,.155,-.04)],cloth,pleats=.045)
shell('Waist belt',[(1.075,.17,.125,-.05),(1.104,.167,.125,-.05)],leather)
shell('Open jacket body',[(.87,.25,.178,-.065),(.94,.258,.183,-.065),(1.18,.223,.174,-.065),(1.34,.21,.17,-.055),(1.41,.195,.146,-.055)],cloth,start=.48,end=2*math.pi-.48)
for sign in [-1,1]:
    sleeve(sign)
    curve('Jacket zipper '+str(sign),[(sign*.25*math.sin(.48),.094,.87),(sign*.223*math.sin(.48),.09,1.18),(sign*.195*math.sin(.48),.075,1.41)],.002,gold)
    curve('Hanging strap '+str(sign),[(sign*.2,.075,1.11),(sign*.225,.10,.95),(sign*.215,.11,.80)],.009,leather)
    star('Strap star '+str(sign),sign*.215,.122,.825,.01)
curve('Top zipper',[(0,.011,1.53),(0,.089,1.4),(0,.04,1.22),(0,.043,1.10)],.0018,gold)
star('Collar pendant',0,.033,1.48,.015)
# Continuous scalp dome and layered tapered ribbon guides.
v=[];f=[]
for j in range(13):
    p=.02+1.55*j/12
    for i in range(49):
        a=i*2*math.pi/48;v.append((.099*math.sin(p)*math.sin(a),-.03+.118*math.sin(p)*math.cos(a),1.69+.12*math.cos(p)))
for j in range(12):
    for i in range(48):k=j*49+i;f.append((k,k+1,k+50,k+49))
mesh('Hair scalp volume',v,f,hair)
for j in range(38):
    a=.65+j*(2*math.pi-1.3)/37
    length=.47+random.random()*.17;v=[];f=[]
    for k in range(17):
        t=k/16;z=1.77-length*t
        x=math.sin(a)*(.055+.08*min(t*4,1))+.016*math.sin(t*9+j)*t
        y=-.03+math.cos(a)*(.065+.105*min(t*4,1))
        width=(.016+random.random()*.002)*(math.sin(math.pi*min(t/.18,1)/2) if t<.18 else (1-t)**.4)+.001
        for side in [-1,0,1]:v.append((x+side*width,y-(1-abs(side))*.005,z))
    for k in range(16):
        for q in range(2):n=k*3+q;f.append((n,n+1,n+4,n+3))
    o=mesh('Hair layer %02d'%j,v,f,navy if j%6==0 else hair);s=o.modifiers.new('Strand volume','SOLIDIFY');s.thickness=.0015
for j in range(9):
    x=-.076+j*.018
    curve('Fringe guide %02d'%j,[(x*.5,.035,1.794),(x,.083,1.75),(x-.018,.091,1.68+abs(x)*.45)],.009,hair)
for j in range(5):star('Hair star %02d'%j,-.065-j*.007,.077-j*.012,1.77-j*.025,.010)
for sign in [-1,1]:
    curve('Earring chain '+str(sign),[(sign*.09,-.002,1.65),(sign*.094,.007,1.60)],.001,gold);star('Earring star '+str(sign),sign*.094,.012,1.598,.012)
# Blockout boots use editable rounded volumes; no claim of finished shoe geometry.
for sign in [-1,1]:
    for name,loc,scale,mat in [('platform',(sign*.15,-.016,.054),(.072,.137,.033),rib),('boot toe',(sign*.15,.012,.106),(.069,.128,.052),leather),('boot shaft',(sign*.15,-.075,.18),(.063,.062,.115),leather)]:
        bpy.ops.mesh.primitive_cube_add(size=2,location=loc);o=link(bpy.context.object,mat);o.name=name+' '+str(sign);o.scale=scale;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);b=o.modifiers.new('Rounded leather form','BEVEL');b.width=.025;b.segments=4
    for z in [.15,.175,.20,.225,.25]:curve('Boot lace',[(sign*.15-.028,-.003,z),(sign*.15+.028,.001,z+.016)],.002,gold)
# Store the reference as a packed image empty, outside the rendered study.
if not bpy.data.objects.get('Astra reference sheet'):
    ref=bpy.data.objects.new('Astra reference sheet',None);bpy.context.scene.collection.objects.link(ref);ref.empty_display_type='IMAGE';ref.data=bpy.data.images.load('C:/Users/user/Desktop/astrachan.png',check_existing=True);ref.data.pack();ref.empty_display_size=2;ref.location=(-2,0,1);ref.hide_render=True
s=bpy.context.scene;s.render.engine='BLENDER_WORKBENCH';s.display.shading.color_type='MATERIAL';s.display.shading.light='STUDIO';s.display.shading.show_shadows=True;s.display.shading.show_cavity=True;s.display.shading.background_type='WORLD';s.world.color=(.12,.12,.12)
s.render.resolution_x=900;s.render.resolution_y=1100;s.render.resolution_percentage=100
cam=s.camera;cam.data.type='ORTHO';cam.data.ortho_scale=2.02
for view,pos in [('front',(0,5,1.5)),('back',(0,-5,1.5)),('three-quarter',(2.8,5,1.9))]:
    cam.location=pos;cam.rotation_euler=(Vector((0,0,.94))-cam.location).to_track_quat('-Z','Y').to_euler();s.render.filepath=str(OUT/('study-'+view+'.png'));bpy.ops.render.render(write_still=True)
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'astrachan-custom-study.blend'))
print('Saved editable custom study',len(col.objects),'objects')
