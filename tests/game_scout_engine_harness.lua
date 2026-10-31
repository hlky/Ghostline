local yaw=0
local root={x=0,y=0,z=0}
local component={pitchMin=-85,pitchMax=85,GetLocalOrientation=function() return 'original' end,
    ResetPitch=function() end,SetLocalOrientation=function(_,value) assert(value=='original') end}
Vector4={new=function(x,y,z,w) return {x=x,y=y,z=z,w=w} end}
EulerAngles={new=function(roll,pitch,y) return {roll=roll,pitch=pitch,yaw=y} end}
local function vectors()
    local y=math.rad(yaw)
    local p=math.rad(component.pitchMin==component.pitchMax and component.pitchMin or 0)
    return {x=-math.sin(y)*math.cos(p),y=math.cos(y)*math.cos(p),z=math.sin(p)},
        {x=math.cos(y),y=math.sin(y),z=0},
        {x=math.sin(y)*math.sin(p),y=-math.cos(y)*math.sin(p),z=math.cos(p)}
end
local player={GetWorldPosition=function() return root end,GetFPPCameraComponent=function() return component end,
    IsAttached=function() return true end,GetMountedVehicle=function() return nil end,
    GetWorldForward=function() return {x=-math.sin(math.rad(yaw)),y=math.cos(math.rad(yaw)),z=0} end}
local function position() return {x=root.x,y=root.y,z=root.z+1.7} end
local camera={GetActiveCameraForward=function() local f=vectors(); return f end,
    GetActiveCameraRight=function() local _,r=vectors(); return r end,
    GetActiveCameraUp=function() local _,_,u=vectors(); return u end,
    GetActiveCameraFOV=function() return 80 end,GetAspectRatio=function() return 16/9 end,
    ProjectPoint=function(_,p)
        local o=position();local f,r,u=vectors();local d={x=p.x-o.x,y=p.y-o.y,z=p.z-o.z}
        local function dot(a,b) return a.x*b.x+a.y*b.y+a.z*b.z end
        return {x=dot(d,r)/dot(d,f),y=dot(d,u)/dot(d,f)}
    end}
local blocked=false
local flight=true
local values={minimap=true,ncpd_dispatcher=false}
local settings={HasVar=function(_,_,name) return values[name]~=nil end,
    GetVar=function(_,_,name) return {GetValue=function() return values[name] end,
        SetValue=function(_,value) values[name]=value end} end}
local time,weather
GetMod=function() return {runtimeData={active=flight,inGame=true}} end
Game={GetPlayer=function() return player end,GetCameraSystem=function() return camera end,
    GetTargetingSystem=function() return {GetCrosshairData=function() return position() end} end,
    GetTeleportationFacility=function() return {Teleport=function(_,_,p,a) root={x=p.x,y=p.y,z=p.z};yaw=a.yaw end} end,
    GetSpatialQueriesSystem=function() return {SyncRaycastByCollisionGroup=function(_,a,b) return blocked,{position=b} end} end,
    GetSettingsSystem=function() return settings end,
    GetTimeSystem=function() return {SetGameTimeByHMS=function(_,h,m,s) time={h,m,s} end} end,
    GetWeatherSystem=function() return {SetWeather=function(_,name) weather=name end} end}
local Engine=dofile(arg[1])
local e=Engine.new()
e:begin(true)
assert(values.minimap==false and values.ncpd_dispatcher==true,'HUD and call settings are suppressed')
e:demoEnvironment()
assert(time[1]==12 and time[2]==0 and weather=='24h_weather_sunny','demo environment uses midday and sunny weather')
assert(e:release().released)
assert(values.minimap==true and values.ncpd_dispatcher==false,'original settings are restored')
e:begin(false)
e:pose({pose={x=10,y=5,z=8,yaw=90,pitch=-20},duration=1,collision=true})
for _=1,20 do e:update(0.1) end
local actual=e:camera()
assert(math.abs(actual.x-10)<0.001 and math.abs(actual.z-8)<0.001,'camera origin must be exact, not player root')
assert(math.abs(root.z-6.3)<0.001)
assert(math.abs(actual.pitch+20)<0.001 and math.abs(actual.yaw-90)<0.001)
assert(not e.motion)
local origin,d=e:screenRay(0.5,0.5)
local f=camera:GetActiveCameraForward()
assert(math.abs(d.x-f.x)<0.001 and math.abs(d.z-f.z)<0.001)
local _,right=e:screenRay(1,0.5)
assert(right.y>0,'screen right follows active camera right')
local loader={GetRootWidget=function() return {IsVisible=function() return true end} end}
e.loaders.test=loader
local before=root.x
e:pose({pose={x=12,y=5,z=8,yaw=90,pitch=-20},duration=1,collision=true})
e:update(1)
assert(root.x==before,'loading must pause movement')
e.loaders={}
blocked=true
local ok,err=pcall(function() e:pose({pose={x=14,y=5,z=8,yaw=90,pitch=-20},duration=1,collision=true}) end)
assert(not ok and tostring(err):find('blocked_path'))
blocked=false
local result=e:release()
assert(result.released and component.pitchMin==-85 and component.pitchMax==85,'restore original pitch limits')
assert(not e.target and not e.motion)
flight=false
assert(not pcall(function() e:begin(false) end),'flight is required')
print('Game Scout engine harness passed')

-- Exercise the actual CET command loop without native IO or JSON dependencies.
flight=true
local files,objects,callbacks={},{},{}
local counter=0
local clock=1000
json={encode=function(value) counter=counter+1; local key='json_'..counter;objects[key]=value;return key end,
    decode=function(value) assert(objects[value]); return objects[value] end}
local originalIO,originalTime,originalRemove,originalRename=io.open,os.time,os.remove,os.rename
io.open=function(path,mode)
    if mode=='r' then
        if not files[path] then return nil end
        return {read=function() return files[path] end,close=function() end}
    end
    return {write=function(_,raw) files[path]=raw end,close=function() end}
end
os.time=function() return clock end
os.remove=function(path) files[path]=nil;return true end
os.rename=function(a,b) files[b]=files[a];files[a]=nil;return true end
Observe=function() end
registerForEvent=function(name,callback) callbacks[name]=callback end
registerHotkey=function() end
package.preload.engine=function() return Engine end
local entry=arg[1]:gsub('engine%.lua$','init.lua')
dofile(entry)
callbacks.onInit()
local function read(name) return json.decode(files['runtime/'..name..'.json']) end
local function write(name,value) files['runtime/'..name..'.json']=json.encode(value) end
local boot=read('state').boot
local function command(id,kind,arguments)
    write('command',{id=id,kind=kind,boot=boot,session='test',expires=clock+40,arguments=arguments or {}})
end
write('lease',{session='test',timestamp=clock})
command('a','begin',{hide_hud=false})
callbacks.onUpdate(0.2)
assert(read('response').ok and read('state').session=='test')
command('b','pose',{pose={x=20,y=5,z=8,yaw=90,pitch=-20},duration=2,collision=false})
callbacks.onUpdate(0.2)
assert(read('state').operation=='moving')
write('stop',{session='test',id='stop-1'})
callbacks.onUpdate(0.2)
assert(not read('state').session and not read('response').ok,'out-of-band stop interrupts pending motion')
assert(component.pitchMin==-85 and component.pitchMax==85)
write('lease',{session='test',timestamp=clock})
command('c','begin',{hide_hud=false})
callbacks.onUpdate(0.2)
clock=clock+10
callbacks.onUpdate(0.2)
assert(not read('state').session,'watchdog must release abandoned camera control')
io.open,os.time,os.remove,os.rename=originalIO,originalTime,originalRemove,originalRename
print('Game Scout command, stop and watchdog harness passed')
