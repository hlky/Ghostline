"""Two parallel flights with a shared half-storey turning landing."""
from __future__ import annotations

import math


def bounds(stair):
    return [stair['x'], stair['y']-stair['landing'],
            stair['x']+stair['width'], stair['y']+stair['run']]


def probes(stair, storey):
    x, y, w, run, fw = (stair[k] for k in ('x', 'y', 'width', 'run', 'flight_width'))
    z = stair['level'] * storey
    return [x+fw/2, y+run+.7, z], [x+w-fw/2, y+run+.7, z+storey]


def shared_side(scene, stair, side):
    """Find an enclosed stair on the next storey across a narrow partition."""
    if stair.get('axis', 'y') != 'y' or not stair.get('enclosed'):
        return None
    edge = stair['x'] if side == 0 else stair['x']+stair['width']
    for other in scene['stairs']:
        if (other['id']==stair['id'] or other.get('type')!='return'
                or other.get('axis','y')!='y' or not other.get('enclosed')
                or not other.get('railings',True)
                or abs(other['level']-stair['level'])!=1
                or stair.get('wall_side')==('left' if side==0 else 'right')
                or other.get('wall_side')==('right' if side==0 else 'left')):
            continue
        opposite = other['x']+other['width'] if side==0 else other['x']
        gap = edge-opposite if side==0 else opposite-edge
        low=max(stair['y']-stair['landing'],other['y']-other['landing'])
        high=min(stair['y']+stair['run'],other['y']+other['run'])
        if .12 <= gap <= .24 and high-low > .5:
            return other, gap, low, high
    return None


def add_geometry(scene, stair, box):
    x, y, w, run, landing, fw = (stair[k] for k in ('x', 'y', 'width', 'run', 'landing', 'flight_width'))
    level = stair['level']
    rise = scene['kit']['storey_height']
    base, half, upper = level*rise, rise/2, (level+1)*rise
    count = math.ceil(half/.2)
    tread, riser = run/count, half/count
    for side in (0, 1):
        sx = x if side == 0 else x+w-fw
        for i in range(count):
            top = base + ((count-i)*riser if side == 0 else half+(i+1)*riser)
            box(f"stair:{stair['id']}:{side}:{i}", [sx+fw/2, y+(i+.5)*tread, (base+top)/2],
                [fw,tread,top-base], level, 'stair', 'stair')
            if stair.get('railings', True) and not stair.get('enclosed'):
                guard_top = min(top+1.05, upper-.2)
                gx = x-.06 if side == 0 else x+w+.06
                box(f"guard:{stair['id']}:slope:{side}:{i}", [gx,y+(i+.5)*tread,(base+guard_top)/2],
                    [.12,tread,guard_top-base], level, 'guard', 'guard')
    box(f"stair:{stair['id']}:turn", [x+w/2,y-landing/2,base+half/2],
        [w,landing,half],level,'stair','stair')
    # The central partition has one continuous volume; its upper guard meets
    # the slab underside without a second coplanar facing.
    if stair.get('enclosed'):
        split=upper-.2
        for suffix,low,high,floor in (('lower',base,split,level),('upper',split,upper+1.05,level+1)):
            box(f"guard:{stair['id']}:centre:{suffix}",[x+w/2,y+run/2,(low+high)/2],
                [w-2*fw,run,high-low],floor,'guard','guard')
    else:
        box(f"guard:{stair['id']}:centre",[x+w/2,y+run/2,(base+upper+1.05)/2],
            [w-2*fw,run,upper+1.05-base],level,'guard','guard')
    if stair.get('railings', True):
        bottom, top = upper-.2, upper+1.05
        joins = [shared_side(scene,stair,side) for side in (0,1)]
        left_return = (joins[0][1] if joins[0] else .12) if stair.get('wall_side') != 'left' else 0
        right_return = (joins[1][1] if joins[1] else .12) if stair.get('wall_side') != 'right' else 0
        if stair.get('enclosed'):
            if stair.get('wall_side') != 'left':
                box(f"guard:{stair['id']}:enclosure:left",[x-left_return/2,y+(run-landing)/2,(base+bottom)/2],
                    [left_return,run+landing,bottom-base],level,'guard','guard')
            if stair.get('wall_side') != 'right':
                box(f"guard:{stair['id']}:enclosure:right",[x+w+right_return/2,y+(run-landing)/2,(base+bottom)/2],
                    [right_return,run+landing,bottom-base],level,'guard','guard')
            box(f"guard:{stair['id']}:enclosure:front",[x+(fw+w+right_return)/2,y+run+.06,(base+bottom)/2],
                [w-fw+right_return,.12,bottom-base],level,'guard','guard')
        for side, gx, thickness in ((0,x-left_return/2,left_return),(1,x+w+right_return/2,right_return)):
            if stair.get('wall_side') == ('left' if side == 0 else 'right'):
                continue
            spans=[(y-landing,y+run,bottom,top,'')]
            join=joins[side]
            if join and join[0]['level']==level+1:
                # The taller neighbour owns the shared partition above the
                # floor. Retain only the guard's slab band and exposed tail.
                _,_,low,high=join
                spans=[(low,high,bottom,upper,'')]
                if low>y-landing: spans.append((y-landing,low,bottom,top,':rear'))
                if high<y+run: spans.append((high,y+run,bottom,top,':front'))
            for low,high,zlow,zhigh,suffix in spans:
                box(f"guard:{stair['id']}:upper:{side}{suffix}",[gx,(low+high)/2,(zlow+zhigh)/2],
                    [thickness,high-low,zhigh-zlow],level+1,'guard','guard')
        # A room-provided rear wall encloses both the turning landing and the
        # floor above. Do not put a second concrete wall in front of it.
        if not stair.get('wall_back'):
            box(f"guard:{stair['id']}:back",[x+(w+right_return-left_return)/2,y-landing-.06,(base+top)/2],
                [w+left_return+right_return,.12,top-base],level,'guard','guard')
        # Return the landing guard across the centre partition as well as the
        # low flight. Ending at fw left the partition touching only one corner
        # of this guard, exposing a detached-looking narrow end panel.
        front_width = w-fw
        # The return owns the outer corner square as well as the inner span;
        # stopping at x merely touched the side guard at one vertical edge.
        box(f"guard:{stair['id']}:front",[x+(front_width-left_return)/2,y+run+.06,(bottom+top)/2],
            [front_width+left_return,.12,top-bottom],level+1,'guard','guard')


def flight_edges(stair, radius, wall_clearance=0):
    """Match floor portals to the usable width beside a room-provided wall."""
    x, w, fw = (stair[k] for k in ('x', 'width', 'flight_width'))
    return (x+radius+(wall_clearance if stair.get('wall_side') == 'left' else 0),
            x+fw-radius, x+w-fw+radius,
            x+w-radius-(wall_clearance if stair.get('wall_side') == 'right' else 0))


def navigation(stair, storey, radius, wall_clearance=0):
    from shapely.geometry import box
    from shapely import constrained_delaunay_triangles
    from building_navigation import _constrain
    x,y,w,run,landing,fw=(stair[k] for k in ('x','y','width','run','landing','flight_width'))
    z=stair['level']*storey
    a,b,c,d=flight_edges(stair,radius,wall_clearance)
    triangles=[]
    for left,right,near,far in ((a,b,z+storey/2,z),(c,d,z+storey/2,z+storey)):
        p,q=[left,y,near],[right,y,near]
        r,s=[right,y+run,far],[left,y+run,far]
        triangles.extend([[p,q,r],[p,r,s]])
    turn=box(x+radius,y-landing+radius,x+w-radius,y)
    for tri in constrained_delaunay_triangles(_constrain(turn,[(v,y) for v in (a,b,c,d)])).geoms:
        if tri.area>1e-8:
            triangles.append([[px,py,z+storey/2] for px,py in list(tri.exterior.coords)[:3]])
    return triangles
