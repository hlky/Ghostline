-- Real CET entrypoint and engine, with a minimal read-only game and file transport.
package.path=arg[1]..'/?.lua;'..package.path
local callbacks,hotkeys,files,values={},{},{},{}
local now=1000
os.time=function() return now end
local seq=0
json={encode=function(value) seq=seq+1;local key='json'..seq;values[key]=value;return key end,
      decode=function(raw) return values[raw] end}
local open=io.open
io.open=function(path,mode)
    if not path:match('^runtime/') then return open(path,mode) end
    if mode=='r' then
        if not files[path] then return nil end
        return {read=function() return files[path] end,close=function() end}
    end
    return {write=function(_,raw) files[path]=raw end,close=function() end}
end
os.remove=function(path) files[path]=nil;return true end
os.rename=function(a,b) files[b]=files[a];files[a]=nil;return true end
local flight,paused,mounted,attached=false,false,false,true
local player={IsAttached=function() return attached end,
    GetWorldPosition=function() return {x=1,y=2,z=3} end,
    GetMountedVehicle=function() return mounted and {} or nil end,
    IsInCombat=function() return false end}
Game={GetPlayer=function() return player end,
    GetSystemRequestsHandler=function() return {IsGamePaused=function() return paused end} end,
    GetCameraSystem=function() return {GetActiveCameraForward=function() return {x=0,y=1,z=0} end,
        GetActiveCameraFOV=function() return 80 end} end,
    GetTargetingSystem=function() return {GetCrosshairData=function() return {x=1,y=2,z=4.7} end} end}
GetMod=function(name) assert(name=='freefly');return {runtimeData={active=flight}} end
Observe=function() end
registerForEvent=function(name,callback) callbacks[name]=callback end
registerHotkey=function(name,_,callback) hotkeys[name]=callback end
local runtime=dofile(arg[1]..'/init.lua')
callbacks.onInit()
assert(runtime.status().ready,'Gameplay must work without FreeFly')
assert(runtime.status().mode=='on_foot')
local function put(name,value) files['runtime/'..name..'.json']=json.encode(value) end
local function tick() callbacks.onUpdate(.1) end
local function command(kind,id)
    put('command',{id=id,kind=kind,boot=runtime.status().boot,session='session',expires=now+5,arguments={}})
    tick();return json.decode(files['runtime/response.json'])
end
put('lease',{session='session',timestamp=now})
assert(command('begin','one').ok)
assert(runtime.status().session=='session')
mounted=true;tick();assert(runtime.status().mode=='vehicle' and runtime.status().session=='session')
flight=true;tick();assert(not runtime.status().ready and not runtime.status().session)
assert(not command('begin','two').ok,'Flight must block begin')
flight=false;paused=true;tick();assert(not runtime.status().ready)
paused=false;assert(command('begin','three').ok)
callbacks.onOverlayOpen();assert(not runtime.status().session and not runtime.status().ready)
callbacks.onOverlayClose();assert(command('begin','four').ok)
now=now+3;tick();assert(not runtime.status().session,'Expired lease must stop ownership')
put('lease',{session='session',timestamp=now})
assert(command('begin','five').ok)
hotkeys.cyberpunk_mcp_stop();assert(not runtime.status().session)
assert(command('begin','six').ok)
put('stop',{id='stop',session='wrong'});tick();assert(runtime.status().session=='session')
put('stop',{id='stop2',session='session'});tick();assert(not runtime.status().session)
put('command',{id='stale',kind='begin',boot='wrong',session='session',expires=now+5});tick()
assert(not json.decode(files['runtime/response.json']).ok)
assert(command('begin','seven').ok)
assert(command('end','eight').ok and not runtime.status().session)
attached=false;tick();assert(not runtime.status().ready)
print('cyberpunk_mcp runtime checks passed')
