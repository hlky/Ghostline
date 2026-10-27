import test from 'node:test';
import assert from 'node:assert/strict';
import {drawWall,setWallMode} from '../tools/building_ui/wall-controls.js';

test('opening a device bay removes incompatible device authoring',()=>{
  const id='0:x:0:0',layout={openings:{[id]:'door_manual'},door_devices:{[id]:{preset:'hinged_h'}},door_states:{[id]:'LOCKED'},navigation:{door_connections:{[id]:{}}}};
  setWallMode(layout,'edge:'+id,'open');
  assert.equal(layout.openings[id],'passage');
  assert.deepEqual(layout.door_devices,{});
  assert.deepEqual(layout.door_states,{});
  assert.deepEqual(layout.navigation.door_connections,{});
});

test('custom walls can open and restore a doorway at the correct storey',()=>{
  const layout={kit:'rancho-3m'};
  const key=drawWall(layout,{x:0,y:0},{x:3,y:0},1,3.5,4.4);
  assert.equal(layout.shell_liners[0].start[2],4.4);
  setWallMode(layout,key,'open');
  assert.equal(layout.shell_liners[0].disabled,true);
  setWallMode(layout,key,'doorway');
  assert.equal(layout.shell_liners[0].disabled,false);
  assert.deepEqual(layout.shell_liners[0].openings,[{center:1.5,width:1.5,height:2.5}]);
});

test('opening a shell wall removes only its own door device',()=>{
  const layout={kit:'rancho-3m',shell_rooms:[{id:'room',position:[0,0,0],width:3,depth:3,height:3.5}],shell_doors:[{id:'near',gate:[1,-.04,2,.04]},{id:'other',gate:[1,2.96,2,3.04]}],door_states:{near:'LOCKED',other:'CLOSED'}};
  setWallMode(layout,'shell:room:south','open');
  assert.equal(layout.shell_rooms[0].walls.south,false);
  assert.deepEqual(layout.shell_doors.map(d=>d.id),['other']);
  assert.deepEqual(layout.door_states,{other:'CLOSED'});
});

test('invalid short doorway leaves the wall intact',()=>{
  const layout={kit:'rancho-3m'};
  const key=drawWall(layout,{x:0,y:0},{x:1,y:0},0,3.5);
  const before=structuredClone(layout);
  assert.throws(()=>setWallMode(layout,key,'doorway'),/at least 1.8/);
  assert.deepEqual(layout,before);
});
