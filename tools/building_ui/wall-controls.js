// Authoring operations shared by wall selection and the opening tools.
export function clearDoor(layout, id) {
  delete layout.door_devices?.[id];
  delete layout.door_states?.[id];
  delete layout.navigation?.door_connections?.[id];
  delete layout.windows?.[id];
}

export function wallSpan(layout, key) {
  if (key.startsWith('liner:')) {
    const wall = layout.shell_liners?.[Number(key.slice(6))];
    return wall ? {start:wall.start, end:wall.end, height:wall.height, level:wall.level || 0, disabled:!!wall.disabled} : null;
  }
  if (key.startsWith('shell:')) {
    const [,id,side] = key.split(':');
    const room = layout.shell_rooms?.find(r=>r.id===id);
    if (!room) return null;
    const [x,y,z]=room.position, w=room.width,d=room.depth;
    const sides={south:[[x,y,z],[x+w,y,z]],east:[[x+w,y,z],[x+w,y+d,z]],north:[[x+w,y+d,z],[x,y+d,z]],west:[[x,y+d,z],[x,y,z]]};
    return {start:sides[side][0],end:sides[side][1],height:room.height+.1,level:room.level||0,disabled:room.walls?.[side]===false};
  }
  return null;
}

export function setWallMode(layout, key, mode) {
  if (key.startsWith('edge:')) {
    const id=key.slice(5);
    if (mode==='solid') delete layout.openings[id];
    else layout.openings[id]=mode==='open'?'passage':'doorway';
    clearDoor(layout,id);
    return;
  }
  const span=wallSpan(layout,key);
  if (!span) throw new Error('Select a wall first');
  const length=Math.hypot(span.end[0]-span.start[0],span.end[1]-span.start[1]);
  if (mode==='doorway' && length<1.8) throw new Error('A doorway needs a wall at least 1.8 m long');
  const openings=mode==='doorway'?[{center:length/2,width:1.5,height:Math.min(2.5,span.height)}]:[];
  if (key.startsWith('liner:')) {
    Object.assign(layout.shell_liners[Number(key.slice(6))],{disabled:mode==='open',openings});
  } else {
    const [,id,side]=key.split(':');
    const room=layout.shell_rooms.find(r=>r.id===id);
    room.walls ||= {};
    room.walls[side]=mode==='open'?false:{openings};
  }
  // An empty aperture must also remove a device attached to this wall.
  layout.shell_doors=(layout.shell_doors||[]).filter(door=>{
    if ((door.level||0)!==span.level) return true;
    const [a,b,c,d]=door.gate;
    const x=(a+c)/2,y=(b+d)/2;
    const dx=span.end[0]-span.start[0],dy=span.end[1]-span.start[1];
    const u=((x-span.start[0])*dx+(y-span.start[1])*dy)/(length*length);
    const distance=Math.abs((x-span.start[0])*dy-(y-span.start[1])*dx)/length;
    const matches=u>=0 && u<=1 && distance<.3;
    if(matches) clearDoor(layout,door.id);
    return !matches;
  });
}

export function drawWall(layout,start,end,level,height,storey=4) {
  if(layout.kit!=='rancho-3m') throw new Error('Independent partitions currently use the Rancho kit');
  if(start.x!==end.x && start.y!==end.y) throw new Error('Draw a horizontal or vertical wall');
  if(Math.hypot(end.x-start.x,end.y-start.y)<.1) throw new Error('Choose two different wall endpoints');
  layout.shell_liners ||= [];
  layout.shell_liners.push({start:[start.x,start.y,level*storey],end:[end.x,end.y,level*storey],level,height,double_sided:true,openings:[]});
  return 'liner:'+(layout.shell_liners.length-1);
}
