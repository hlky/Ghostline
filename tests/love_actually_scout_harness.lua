-- CET API and filesystem contract only; not an in-game UI simulation.
local fixture = dofile(arg[1])
local function copy(value)
  if type(value) ~= 'table' then return value end
  local result = {}; for k,v in pairs(value) do result[k] = copy(v) end; return result
end
local files, encoded, serial = {['targets.json']='targets'}, {targets=fixture}, 0
local failWrite, failPublish, noPlayer = false, false, false
local position, forward = {x=10,y=20,z=30}, {x=0,y=1}
local path = 'love-actually-locations.json'
local function setup()
  local events, hotkey, pending, text = {}, nil, nil, {}
  local env = setmetatable({}, {__index=_G})
  env.math = setmetatable({atan2=function(y,x) return math.atan(y,x) end}, {__index=math})
  env.json = {
    encode=function(value) serial=serial+1; local key='json'..serial; encoded[key]=copy(value); return key end,
    decode=function(raw) assert(encoded[raw], 'bad json'); return copy(encoded[raw]) end,
  }
  env.io = {open=function(name, mode)
    if mode == 'w' then
      if failWrite then return nil end
      return {write=function(_, raw) files[name]=raw; return true end, close=function() return true end}
    end
    if files[name] then return {read=function() return files[name] end, close=function() return true end} end
  end}
  env.os = {
    remove=function(name) files[name]=nil; return true end,
    rename=function(from,to)
      if failPublish and from == path..'.tmp' and to == path then return nil end
      if not files[from] then return nil end
      files[to], files[from] = files[from], nil; return true
    end,
  }
  env.Game = {GetPlayer=function()
    if noPlayer then return nil end
    return {GetWorldPosition=function() return position end, GetWorldForward=function() return forward end}
  end}
  env.ImGui = {
    Begin=function() return true end, End=function() end, SameLine=function() end,
    Text=function(value) text[#text+1]=value end,
    TextWrapped=function(value) text[#text+1]=value end,
    Button=function(label) if pending == label then pending=nil; return true end; return false end,
  }
  env.registerForEvent = function(name, fn) events[name]=fn end
  env.registerHotkey = function(_,_,fn) hotkey=fn end
  assert(loadfile('projects/ghostline/quests/gq004/implementation/cet/init.lua','t',env))()
  events.onInit(); events.onOverlayOpen()
  return {
    record=function() hotkey() end,
    click=function(label) pending=label; events.onDraw(); assert(not pending, 'missing button: '..label) end,
    draw=function() text={}; events.onDraw(); return table.concat(text,'\n') end,
  }
end
local function log() return encoded[files[path]] end
local function count()
  local n=0; for _ in pairs(log().captures) do n=n+1 end; return n
end
local ui = setup()
noPlayer=true; ui.record(); assert(not files[path]); noPlayer=false
ui.click('Record meeting group here (8)'); assert(count()==8)
assert(log().captures.origin.z==30 and log().captures.origin.yaw==0)
position={x=100,y=200,z=10}; ui.click('Record operation centres here (3)'); assert(count()==11)
forward={x=1,y=0}; ui.record(); assert(count()==12)
assert(math.abs(log().captures['#gq004_ap_relay'].z-11.2)<0.0001)
assert(log().captures['#gq004_ap_relay'].yaw==-90)
local before=files[path]
failWrite=true; ui.record(); assert(files[path]==before and count()==12)
assert(ui.draw():find('Saved 12/16',1,true)); failWrite=false
ui.record(); assert(count()==13)
ui.record(); ui.record(); ui.record(); assert(count()==16)
assert(ui.draw():find('Complete.',1,true))
ui=setup(); assert(ui.draw():find('Saved 16/16',1,true))
before=files[path]; failPublish=true
ui.click('Record meeting group here (8)'); assert(files[path]==before)
failPublish=false
for _, example in ipairs({{x=0,y=1,yaw=0},{x=1,y=0,yaw=-90},{x=0,y=-1,yaw=-180},{x=-1,y=0,yaw=90}}) do
  forward=example; ui.click('Record meeting group here (8)')
  assert(math.abs((log().captures.origin.yaw-example.yaw+180)%360-180)<0.0001)
end
files[path]='invalid json'; ui=setup(); before=files[path]; ui.record()
assert(files[path]==before and ui.draw():find('STOP:',1,true))
print('Scout harness passed: grouped capture, mounting height, yaw, resume, failure rollback, complete count and corrupt-log protection.')
