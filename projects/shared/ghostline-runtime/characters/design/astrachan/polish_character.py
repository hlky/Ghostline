"""Astrachan modelling pass: fitted donors, hair cards, hardware and materials.

Run in the saved donor-fit scene. This is actual Blender geometry and shading;
rendered images are not retouched. Keep the CC-BY donor notices with derivatives.
"""
import bpy
import bmesh
import math
import random
from pathlib import Path
from mathutils import Vector
from mathutils.bvhtree import BVHTree

ROOT=next(parent for parent in Path(__file__).resolve().parents if (parent / "AGENTS.md").is_file())
OUT=ROOT/'generated/astrachan'
random.seed(37)
prior=bpy.data.collections.get('Astra detailed authoring')
if prior:
    for ob in list(prior.objects):bpy.data.objects.remove(ob,do_unlink=True)
    bpy.data.collections.remove(prior)
COL=bpy.data.collections.new('Astra detailed authoring');bpy.context.scene.collection.children.link(COL)


def mat(name,color,rough=.6,metal=0):
    m=bpy.data.materials.get(name) or bpy.data.materials.new(name);m.use_nodes=True
    p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(*color,1)
    p.inputs['Roughness'].default_value=rough;p.inputs['Metallic'].default_value=metal
    m.diffuse_color=(*color,1)
    return m


coatmat=mat('Astra black twill',(.0045,.0053,.008),.77)
skirtmat=mat('Astra skirt wool',(.006,.0065,.010),.82)
knit=mat('Astra fitted rib knit',(.003,.0035,.005),.76)
leather=mat('Astra strap leather',(.006,.006,.008),.49)
gold=mat('Astra brushed brass',(.40,.245,.10),.32,.78)
thread=mat('Astra pale gold embroidery',(.32,.245,.15),.59,.2)
lining=mat('Astra navy lining',(.008,.01,.022),.6)


def weave(m,scale=650,strength=.08):
    n=m.node_tree.nodes;l=m.node_tree.links;p=n.get('Principled BSDF')
    if n.get('Astra textile grain'):return
    tex=n.new('ShaderNodeTexNoise');tex.name='Astra textile grain';tex.inputs['Scale'].default_value=scale
    bump=n.new('ShaderNodeBump');bump.inputs['Strength'].default_value=strength;bump.inputs['Distance'].default_value=.0005
    l.new(tex.outputs['Fac'],bump.inputs['Height']);l.new(bump.outputs['Normal'],p.inputs['Normal'])


weave(skirtmat);weave(leather,220,.05)
nodes=coatmat.node_tree.nodes;links=coatmat.node_tree.links
if not nodes.get('Donor cloth normal'):
    tex=nodes.new('ShaderNodeTexImage');tex.name='Donor cloth normal'
    tex.image=bpy.data.images.load(str(OUT/'external/shirts02/clothes/elvs_hooded_sweat_jacket1/normalshoodie.png'),check_existing=True)
    tex.image.colorspace_settings.name='Non-Color'
    norm=nodes.new('ShaderNodeNormalMap');norm.inputs['Strength'].default_value=.6
    links.new(tex.outputs['Color'],norm.inputs['Color']);links.new(norm.outputs['Normal'],nodes.get('Principled BSDF').inputs['Normal'])
n=knit.node_tree.nodes;l=knit.node_tree.links
if not n.get('Vertical ribs'):
    wave=n.new('ShaderNodeTexWave');wave.name='Vertical ribs';wave.wave_type='BANDS';wave.bands_direction='X';wave.inputs['Scale'].default_value=100
    bump=n.new('ShaderNodeBump');bump.inputs['Strength'].default_value=.32;bump.inputs['Distance'].default_value=.0007
    l.new(wave.outputs['Color'],bump.inputs['Height']);l.new(bump.outputs['Normal'],n.get('Principled BSDF').inputs['Normal'])


def mesh(name,verts,faces,material,uv=None):
    me=bpy.data.meshes.new(name);me.from_pydata(verts,[],faces);me.update()
    ob=bpy.data.objects.new(name,me);COL.objects.link(ob);me.materials.append(material)
    for p in me.polygons:p.use_smooth=True
    if uv:
        layer=me.uv_layers.new()
        for loop in me.loops:layer.data[loop.index].uv=uv[loop.vertex_index]
    return ob


def line(name,points,radius,material,bezier=True):
    d=bpy.data.curves.new(name,'CURVE');d.dimensions='3D';d.bevel_depth=radius;d.bevel_resolution=3
    sp=d.splines.new('BEZIER' if bezier else 'POLY')
    if bezier:
        sp.bezier_points.add(len(points)-1)
        for p,co in zip(sp.bezier_points,points):p.co=co;p.handle_left_type='AUTO';p.handle_right_type='AUTO'
    else:
        sp.points.add(len(points)-1)
        for p,co in zip(sp.points,points):p.co=(*co,1)
    ob=bpy.data.objects.new(name,d);COL.objects.link(ob);d.materials.append(material)
    return ob


def patch(name,points,width,material,thickness=.002):
    vv=[];ff=[]
    for j,p in enumerate(points):
        p=Vector(p);a=Vector(points[min(j+1,len(points)-1)])-Vector(points[max(j-1,0)])
        side=a.cross(Vector((0,1,0))).normalized()*width/2
        vv.extend([p-side,p+side])
        if j:ff.append((2*j-2,2*j-1,2*j+1,2*j))
    ob=mesh(name,vv,ff,material)
    so=ob.modifiers.new('Leather thickness','SOLIDIFY');so.thickness=thickness
    be=ob.modifiers.new('Rounded strap edge','BEVEL');be.width=.0007;be.segments=2
    return ob


def buckle(name,x,y,z,w=.022,h=.025):
    # Rounded frame, central bar and tongue. Y faces the front of the character.
    r=.003
    pts=[]
    for cx,cz,offset in [(x+w/2-r,z+h/2-r,0),(x-w/2+r,z+h/2-r,90),(x-w/2+r,z-h/2+r,180),(x+w/2-r,z-h/2+r,270)]:
        for i in range(5):
            a=math.radians(offset+i*90/4);pts.append((cx+r*math.cos(a),y,cz+r*math.sin(a)))
    pts.append(pts[0]);line(name+' frame',pts,.0015,gold,False)
    line(name+' bar',[(x-w/2,y,z),(x+w/2,y,z)],.0012,gold,False)
    line(name+' tongue',[(x,y+.001,z),(x,y+.002,z+h*.4)],.0009,gold,False)


def star(name,center,size,material=gold,back=False):
    x,y,z=center;vv=[(x,y+(-.001 if back else .001),z)]
    for i in range(10):
        a=i*math.pi/5;r=size if i%2==0 else size*.39
        vv.append((x+math.sin(a)*r,y,z+math.cos(a)*r))
    ob=mesh(name,vv,[(0,i+1,(i+1)%10+1) for i in range(10)],material)
    so=ob.modifiers.new('Star thickness','SOLIDIFY');so.thickness=.001
    be=ob.modifiers.new('Polished edge','BEVEL');be.width=.0005;be.segments=2
    return ob

# Better proportioned, slightly oversized jacket, preserving the donor folds.
jacket=bpy.data.objects['Astra tailored jacket donor']
jacket.data.materials.clear();jacket.data.materials.append(coatmat)
if not jacket.get('astra_loose_fit'):
    for v in jacket.data.vertices:
        x,y,z=v.co
        body=max(0,min(1,(.26-abs(x))/.085))
        v.co.x*=1+.12*body
        v.co.y=-.045+(y+.045)*(1+.075*body)
        if abs(x)>.19:
            sleeve=max(0,min(1,(abs(x)-.19)/.065))*max(0,min(1,(.46-abs(x))/.07))
            v.co+=v.normal*.012*sleeve
    jacket['astra_loose_fit']=True
skirt=bpy.data.objects['Astra pleated skirt donor'];skirt.data.materials.clear();skirt.data.materials.append(skirtmat)

# Replace the segmented top studies with one welded body-fitted mesh.
verts=[];faces=[]
for name in ['submesh_00_LOD_1','submesh_01_LOD_1','submesh_02_LOD_1','submesh_03_LOD_1']:
    ob=bpy.data.objects[name];offset=len(verts)
    verts.extend([ob.matrix_world@v.co for v in ob.data.vertices])
    faces.extend([tuple(offset+i for i in p.vertices) for p in ob.data.polygons])
top=mesh('Astra sleeveless zip knit',verts,faces,knit)
bm=bmesh.new();bm.from_mesh(top.data)
bmesh.ops.bisect_plane(bm,geom=list(bm.verts)+list(bm.edges)+list(bm.faces),dist=.00001,plane_co=(0,0,1.091),plane_no=(0,0,1),clear_inner=True)
bmesh.ops.remove_doubles(bm,verts=list(bm.verts),dist=.00008)
bmesh.ops.recalc_face_normals(bm,faces=list(bm.faces));bm.to_mesh(top.data);bm.free()
for v in top.data.vertices:v.co+=v.normal*.005
solid=top.modifiers.new('Knit thickness','SOLIDIFY');solid.thickness=.0015
for ob in bpy.data.collections['Astrachan custom study'].objects:
    if ob.name.startswith(('Top fit donor','Top lower','Top zipper','Front shoulder','Collar pendant','Eyebrow study','Lash study','Waist belt','Thigh harness')):ob.hide_render=True
    if ob.name.startswith('Top high collar'):ob.data.materials.clear();ob.data.materials.append(knit)

# Face sculpt study: softer jaw, smaller nose, slightly larger eye openings.
def face_warp(v):
    v=Vector(v);x,y,z=v
    front=max(0,min(1,(y+.012)/.05))
    cx=.0295 if x>0 else -.0295
    eye=math.exp(-((x-cx)/.024)**4-((z-1.689)/.025)**4)*front
    v.x+=(x-cx)*.18*eye;v.z+=(z-1.689)*.16*eye
    lower=math.exp(-((z-1.606)/.045)**2)
    v.x*=1-.085*lower
    nose=math.exp(-(x/.020)**2-((z-1.656)/.028)**2)*front
    v.y-=.004*nose
    chin=math.exp(-((z-1.575)/.025)**2)*front;v.z+=.004*chin
    return v

for ob in bpy.context.scene.objects:
    if ob.type=='MESH' and (ob.name=='submesh_00_LOD_1.001' or ob.get('astra_role')=='eyes') and not ob.name.startswith('Icosphere'):
        if not ob.get('astra_soft_face'):
            inv=ob.matrix_world.inverted()
            for v in ob.data.vertices:v.co=inv@face_warp(ob.matrix_world@v.co)
            ob['astra_soft_face']=True

# Match exposed body to the textured face under the same studio light.
skin=bpy.data.materials['Fit mannequin'].node_tree.nodes.get('Principled BSDF')
skin.inputs['Base Color'].default_value=(.31,.185,.135,1);skin.inputs['Subsurface Weight'].default_value=.05

# Dedicated swept fringe. Each ribbon has real strand UVs from the game atlas.
hm=bpy.data.materials['Astra long hair preview']
for ob in bpy.context.scene.objects:
    if ob.get('astra_role')=='weighted_hair' and ob.type=='MESH':
        if 'submesh_01_' in ob.name:ob.hide_render=True
        elif 'submesh_00_' in ob.name and not ob.get('astra_coat_clearance_v3'):
            for v in ob.data.vertices:
                x,y,z=v.co;t=max(0,min(1,(1.62-z)/.4))
                if y>0:v.co.y+=.072*t
                else:v.co.y-=.025*t
                v.co.x+=.013*math.sin(8*t+x*22)*t
            ob['astra_coat_clearance_v3']=True


def hair_ribbon(name,controls,width,slot=.03):
    c=[Vector(p) for p in controls];vv=[];ff=[];uv=[];count=22;across=4
    for j in range(count+1):
        t=j/count;p=(1-t)**3*c[0]+3*t*(1-t)**2*c[1]+3*t*t*(1-t)*c[2]+t**3*c[3]
        tangent=(3*(1-t)**2*(c[1]-c[0])+6*t*(1-t)*(c[2]-c[1])+3*t*t*(c[3]-c[2])).normalized()
        side=tangent.cross(Vector((0,1,0))).normalized()
        w=width*(.5+.5*math.sin(math.pi*min(t/.4,1)/2))*(1-.78*t**3)
        for k in range(across+1):
            s=-1+2*k/across;vv.append(p+side*w*s+Vector((0,.002*(1-s*s),0)));uv.append((slot+.16*k/across,.93-.62*t))
            if j and k:
                q=j*(across+1)+k;ff.append((q-across-2,q-across-1,q,q-1))
    ob=mesh(name,vv,ff,hm,uv);ob['stage']='Custom strand cards; requires final scalp/dangle binding'
    return ob

for i in range(10):
    startx=-.061+i*.009
    endx=-.079+i*.015
    endz=1.696+(.014 if i<3 else 0)-(.012 if 5<=i<=7 else 0)+.004*math.sin(i*2)
    hair_ribbon('Swept fringe %02d'%i,[(startx,.039,1.801),(-.01+i*.009,.075,1.788),(endx+.02,.088,1.735),(endx,.083,endz)],.013)
for side in [-1,1]:
    for i in range(4):
        hair_ribbon('Face framing wisp %s %s'%(side,i),[(side*.065,.006,1.784),(side*.09,.09,1.718),(side*(.104+i*.005),.105,1.64),(side*(.09+i*.009),.09,1.51-i*.035)],.006)

# Fine eyebrows and eyeliner fitted to the face, with a soft wing at the outside.
ink=mat('Astra soft charcoal brows',(.015,.01,.016),.75)
for side in [-1,1]:
    pts=[(side*.014,.053,1.713),(side*.029,.054,1.718),(side*.046,.045,1.712)]
    line('Sculpted brow '+str(side),pts,.0015,ink)
    line('Upper lash '+str(side),[(side*.016,.06,1.691),(side*.030,.068,1.699),(side*.046,.054,1.693),(side*.051,.047,1.697)],.0008,ink)

# Jacket pockets, straps and properly shaped hardware.
for side in [-1,1]:
    x=side*.176
    pocket=mesh('Cargo pocket '+str(side),[(x-.035,.106,1.095),(x+.035,.106,1.095),(x+.032,.135,.996),(x-.032,.135,.996)],[(0,1,2,3)],coatmat)
    s=pocket.modifiers.new('Pocket depth','SOLIDIFY');s.thickness=.007
    b=pocket.modifiers.new('Pocket eased corners','BEVEL');b.width=.007;b.segments=3
    line('Pocket stitch '+str(side),[(x-.030,.117,1.087),(x-.028,.145,1.005),(x+.028,.145,1.005),(x+.030,.117,1.087)],.00065,thread,False)
    patch('Pocket flap '+str(side),[(x,.121,1.112),(x,.131,1.08)],.075,coatmat,.003)
    patch('Utility strap '+str(side),[(side*.20,.103,1.22),(side*.22,.119,1.11),(side*.22,.145,.984),(side*.216,.14,.844)],.012,leather)
    buckle('Side utility buckle '+str(side),side*.218,.144,1.126,.025,.025)
    star('Hanging strap emblem '+str(side),(side*.216,.145,.865),.007)
    patch('Shoulder harness '+str(side),[(side*.095,.06,1.489),(side*.103,.112,1.40),(side*.098,.14,1.29)],.014,leather)
    buckle('Shoulder buckle '+str(side),side*.103,.129,1.423,.022,.030)

line('Knit zipper',[(0,.012,1.531),(0,.083,1.414),(0,.064,1.28),(0,.051,1.10)],.00115,gold)
star('Zipper star pull',(0,.038,1.489),.011)

# Flat waist belt, suspended skirt straps, thigh ring and tag.
v=[];f=[]
for j,z in enumerate([1.112,1.083]):
    for i in range(81):
        a=i*2*math.pi/80;v.append((.172*math.sin(a),-.038+.122*math.cos(a),z))
        if j and i:q=j*81+i;f.append((q-82,q-81,q,q-1))
mesh('Waist utility belt',v,f,leather)
buckle('Waist buckle',.017,.093,1.098,.030,.023)
for side in [-1,1]:
    patch('Skirt suspension '+str(side),[(side*.119,.098,1.09),(side*.144,.143,.963),(side*.15,.14,.90)],.01,leather)
    buckle('Skirt strap buckle '+str(side),side*.14,.153,.977,.020,.025)

x=.12;y=.037;z=.865
points=[(x+.049*math.cos(i*2*math.pi/64),y+.064*math.sin(i*2*math.pi/64),z+.005*math.cos(i*2*math.pi/64)) for i in range(65)]
line('Thigh garter foundation',points,.007,leather,False)
ring=[(.152+.016*math.cos(i*2*math.pi/48),.111,.857+.016*math.sin(i*2*math.pi/48)) for i in range(49)]
line('Thigh brass ring',ring,.002,gold,False)
patch('Thigh hanging tag',[(.151,.114,.837),(.15,.118,.784)],.019,leather)
star('Tag celestial emblem',(.15,.121,.804),.006)

# Constellations follow the actual jacket surface using a BVH projection.
dep=bpy.context.evaluated_depsgraph_get();evalob=jacket.evaluated_get(dep);me=evalob.to_mesh()
bvh=BVHTree.FromPolygons([jacket.matrix_world@v.co for v in me.vertices],[list(p.vertices) for p in me.polygons]);evalob.to_mesh_clear()
def on_coat(x,z,back=False):
    p,n,index,dist=bvh.ray_cast(Vector((x,-1 if back else 1,z)),Vector((0,1 if back else -1,0)))
    return p+Vector((0,-.002 if back else .002,0)) if p is not None else None
for side in [-1,1]:
    seq=[(side*.255,1.353),(side*.283,1.323),(side*.318,1.344),(side*.340,1.301),(side*.364,1.282)]
    pts=[on_coat(x,z) for x,z in seq];pts=[p for p in pts if p is not None]
    if len(pts)>1:line('Sleeve constellation '+str(side),pts,.00065,thread,False)
    for i,p in enumerate(pts):star('Sleeve stitched star %s %s'%(side,i),p,.0045,thread)
seq=[(-.097,1.10),(-.055,1.077),(0,1.104),(.054,1.077),(.095,1.10)]
pts=[on_coat(x,z,True) for x,z in seq];pts=[p for p in pts if p is not None]
if len(pts)>1:line('Back star arc',pts,.0007,thread,False)
for i,p in enumerate(pts):star('Back embroidered star '+str(i),p,.008 if i==2 else .004,thread,True)

# Save a real geometry/material candidate and render useful inspection views.
scene=bpy.context.scene;scene.cycles.samples=48
scene.render.resolution_x=1100;scene.render.resolution_y=1400
cam=scene.camera
for view,pos,look,scale in [('front',(0,5,1.45),(0,0,.97),2.0),('three-quarter',(2.1,5,1.8),(0,0,.98),2.0),('portrait',(.48,3,1.72),(0,.02,1.57),.61),('back',(0,-5,1.4),(0,0,.98),2.0)]:
    cam.location=pos;cam.rotation_euler=(Vector(look)-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.ortho_scale=scale
    scene.render.filepath=str(OUT/('polished-'+view+'.png'));bpy.ops.render.render(write_still=True)
for image in bpy.data.images:
    if image.source=='FILE' and image.has_data:
        try:image.pack()
        except RuntimeError:pass
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'astrachan-detailed-authoring.blend'))
print('Detailed authoring pass saved')
