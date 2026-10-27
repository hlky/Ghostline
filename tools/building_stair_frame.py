"""Orthogonal stair coordinates shared by geometry, cuts, navigation and probes."""


def point(stair, u, v, z):
    if stair.get('axis', 'y') == 'x':
        return [stair['x']+v, stair['y']-u, z]
    return [stair['x']+u, stair['y']+v, z]


def rectangle(stair, bounds):
    a,b,c,d=bounds
    vertices=[point(stair,u,v,0) for u,v in ((a,b),(a,d),(c,b),(c,d))]
    return [min(p[0] for p in vertices),min(p[1] for p in vertices),max(p[0] for p in vertices),max(p[1] for p in vertices)]


def shaft(stair, guards=False):
    pad=.12 if guards and stair.get('railings',True) else 0
    left=-pad if stair.get('wall_side') != 'left' else 0
    right=stair['width']+(pad if stair.get('wall_side') != 'right' else 0)
    start= -stair['landing']-pad if stair.get('type')=='return' else (-pad if not stair.get('reverse') else 0)
    end=stair['run']+(pad if stair.get('reverse') else 0)
    return rectangle(stair,[left,start,right,end])
