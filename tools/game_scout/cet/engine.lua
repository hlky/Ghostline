-- Standalone scouting primitives. FreeFly owns flight and its protections.
local Engine = {}
Engine.__index = Engine
local atan2 = math.atan2 or math.atan
local function vec(p) return Vector4.new(p.x,p.y,p.z,1) end
local function xyz(p) return {x=p.x,y=p.y,z=p.z} end
local function finite(v) return type(v)=='number' and v==v and math.abs(v)<math.huge end
local hudSettings={
    {'/interface/hud',{'minimap','healthbar','stamina_oxygen','npc_healthbar','ammo_counter','input_hints',
        'action_buttons','activity_log','crosshairs','quest_tracker','johnny_hud','object_markers','npc_names',
        'wanted_level','npc_nameplates','crouch_indicator','vehicle_hud','hud_markers'}},
    {'/accessibility/subtitles',{'Cinematic','Radio','CinematicForceKiroshiTexts','Overheads','OverheadsForceKiroshiTexts'}},
    {'/gameplay/muteholocalls',{'ncpd_dispatcher','fixer_briefs_and_debriefs'},true},
}
local function dist(a,b) return math.sqrt((a.x-b.x)^2+(a.y-b.y)^2+(a.z-b.z)^2) end
local function validate(p)
    for _,key in ipairs({'x','y','z','yaw','pitch'}) do
        if not finite(p[key]) then error('invalid pose '..key) end
    end
    if math.abs(p.pitch)>85 then error('pitch outside -85..85') end
end

function Engine.new()
    return setmetatable({loaders={},hud={},hidden={},overlay=false,frame=0,stable=0},Engine)
end

function Engine:loading()
    local player=Game.GetPlayer()
    if not player or not player:IsAttached() then return true,{'player_detached'} end
    local sources={}
    for key,controller in pairs(self.loaders) do
        local ok,visible=pcall(function() local root=controller:GetRootWidget(); return root and root:IsVisible() end)
        if ok and visible then sources[#sources+1]=key end
        if not ok then self.loaders[key]=nil end
    end
    pcall(function()
        local defs=Game.GetAllBlackboardDefs().FastTRavelSystem
        local board=Game.GetBlackboardSystem():Get(defs)
        if board:GetBool(defs.FastTravelLoadingScreenStarted) and not board:GetBool(defs.FastTravelLoadingScreenFinished) then sources[#sources+1]='fast_travel' end
    end)
    return #sources>0,sources
end

function Engine:flight()
    local ok,mod=pcall(function() return GetMod('freefly') end)
    return ok and mod and mod.runtimeData and mod.runtimeData.active==true and mod.runtimeData.inGame==true and mod.runtimeData.inMenu~=true
end

function Engine:camera()
    local player=Game.GetPlayer()
    local system=Game.GetCameraSystem()
    local forward,right,up=system:GetActiveCameraForward(),system:GetActiveCameraRight(),system:GetActiveCameraUp()
    local position=Game.GetTargetingSystem():GetCrosshairData(player)
    local camera={x=position.x,y=position.y,z=position.z,
        yaw=math.deg(atan2(-forward.x,forward.y))%360,
        pitch=math.deg(atan2(forward.z,math.sqrt(forward.x^2+forward.y^2))),
        roll=math.deg(atan2(right.z,up.z)),fov=system:GetActiveCameraFOV()}
    validate(camera)
    return camera
end

function Engine:status()
    local loading,sources=self:loading()
    local status={loading=loading,loading_sources=sources,freefly_active=self:flight() or false,
        overlay_open=self.overlay,frame=self.frame,ready=self.saved~=nil and self.stable>=0.5 and not self.motion and not loading and not self.overlay,
        controlling=self.saved~=nil,operation=self.motion and 'moving' or 'idle',hud_hidden=self.hideHUD==true}
    pcall(function() status.paused=Game.GetSystemRequestsHandler():IsGamePaused() end)
    pcall(function()
        status.camera=self:camera()
        status.player=xyz(Game.GetPlayer():GetWorldPosition())
        status.aspect=Game.GetCameraSystem():GetAspectRatio()
        status.in_combat=Game.GetPlayer():IsInCombat()
        status.protected=Game.GetGodModeSystem():HasGodMode(Game.GetPlayer():GetEntityID(),gameGodModeType.Invulnerable)
        status.ai_invisible=Game.GetPlayer():IsInvisible()
    end)
    return status
end

function Engine:hide()
    if not self.saved or not self.hideHUD then return end
    for key,controller in pairs(self.hud) do
        pcall(function()
            local root=controller:GetRootWidget()
            if not self.hidden[key] then self.hidden[key]={root=root,visible=root:IsVisible()} end
            root:SetVisible(false)
        end)
    end
end

function Engine:disableSettings()
    self.settings={}
    local system=Game.GetSettingsSystem()
    if not system then error('Settings system unavailable') end
    for _,group in ipairs(hudSettings) do
        for _,name in ipairs(group[2]) do
            if system:HasVar(group[1],name) then
                local setting=system:GetVar(group[1],name)
                local value=setting:GetValue()
                if type(value)~='boolean' then error('HUD setting is not boolean: '..name) end
                self.settings[#self.settings+1]={setting=setting,value=value}
                setting:SetValue(group[3]==true)
            end
        end
    end
end

function Engine:demoEnvironment()
    Game.GetTimeSystem():SetGameTimeByHMS(12,0,0)
    Game.GetWeatherSystem():SetWeather('24h_weather_sunny',0.0,10)
    return {time='12:00',weather='24h_weather_sunny'}
end

function Engine:begin(hideHUD)
    if self:loading() then error('Wait for gameplay to load') end
    if not self:flight() then error('Activate FreeFly before scouting') end
    if self.overlay then error('Close the CET overlay') end
    local paused=false
    pcall(function() paused=Game.GetSystemRequestsHandler():IsGamePaused() end)
    if paused then error('Unpause the game before scouting') end
    local player=Game.GetPlayer()
    if player:GetMountedVehicle() then error('Exit the vehicle before scouting') end
    if self.saved then return self:status() end
    local component=player:GetFPPCameraComponent()
    self.saved={component=component,pitchMin=component.pitchMin,pitchMax=component.pitchMax,
        orientation=component:GetLocalOrientation()}
    self.target=self:camera()
    self.hideHUD=hideHUD
    if hideHUD then
        local ok,err=pcall(function() self:disableSettings() end)
        if not ok then self:release(); error(err) end
    end
    self:hide()
    self.stable=0
    return self:status()
end

function Engine:release()
    local warnings={}
    self.motion=nil; self.target=nil; self.hideHUD=false; self.stable=0
    if self.saved then
        local saved=self.saved
        local ok,err=pcall(function()
            saved.component.pitchMin=saved.pitchMin; saved.component.pitchMax=saved.pitchMax
            saved.component:ResetPitch(); saved.component:SetLocalOrientation(saved.orientation)
        end)
        if not ok then warnings[#warnings+1]=tostring(err) end
    end
    for _,saved in pairs(self.hidden) do
        local ok,err=pcall(function() saved.root:SetVisible(saved.visible) end)
        if not ok then warnings[#warnings+1]=tostring(err) end
    end
    for _,saved in ipairs(self.settings or {}) do
        local ok,err=pcall(function() saved.setting:SetValue(saved.value) end)
        if not ok then warnings[#warnings+1]=tostring(err) end
    end
    self.settings=nil
    self.saved=nil; self.hidden={}
    return {released=true,cleanup_warnings=warnings}
end

function Engine:trace(origin,destination)
    local nearest=nil
    for _,group in ipairs({'Static','Vehicle','Dynamic'}) do
        local hit,trace=Game.GetSpatialQueriesSystem():SyncRaycastByCollisionGroup(vec(origin),vec(destination),group,false,false)
        if hit then
            local position=xyz(trace.position)
            local length=dist(origin,position)
            if not nearest or length<nearest.distance then nearest={hit=true,position=position,distance=length,collision_group=group,trace=trace} end
        end
    end
    return nearest or {hit=false}
end

function Engine:clearPath(origin,destination)
    if dist(origin,destination)<0.01 then return true end
    for _,offset in ipairs({{0,0,0},{0.25,0,0},{-0.25,0,0},{0,0.25,0},{0,-0.25,0}}) do
        local a={x=origin.x+offset[1],y=origin.y+offset[2],z=origin.z+offset[3]}
        local b={x=destination.x+offset[1],y=destination.y+offset[2],z=destination.z+offset[3]}
        if self:trace(a,b).hit then return false end
    end
    return true
end

function Engine:pose(arguments)
    if not self.saved then error('No scouting session') end
    validate(arguments.pose)
    if not finite(arguments.duration) or arguments.duration<0.1 or arguments.duration>10 then error('invalid duration') end
    local current=self:camera()
    if dist(current,arguments.pose)>50 and not arguments.teleport then error('Long travel requires teleport') end
    if arguments.collision and not arguments.teleport and not self:clearPath(current,arguments.pose) then error('blocked_path: collision along movement') end
    self.motion={origin=current,target=arguments.pose,elapsed=0,duration=arguments.teleport and 0.01 or arguments.duration,
        collision=arguments.collision and not arguments.teleport,settle=0,loading=0}
    self.stable=0
end

function Engine:align(pose)
    local player=Game.GetPlayer()
    local camera=player:GetFPPCameraComponent()
    camera.pitchMin=pose.pitch; camera.pitchMax=pose.pitch
    local actual=self:camera()
    local root=player:GetWorldPosition()
    local errorYaw=(pose.yaw-actual.yaw+180)%360-180
    local body=player:GetWorldForward()
    local bodyYaw=math.deg(atan2(-body.x,body.y))
    Game.GetTeleportationFacility():Teleport(player,Vector4.new(
        root.x+pose.x-actual.x,root.y+pose.y-actual.y,root.z+pose.z-actual.z,1),EulerAngles.new(0,0,bodyYaw+errorYaw))
end

function Engine:update(delta)
    self.frame=self.frame+1
    if not self.saved then return false end
    local loading=self:loading()
    local paused=false
    pcall(function() paused=Game.GetSystemRequestsHandler():IsGamePaused() end)
    if loading or self.overlay or paused then
        self.stable=0
        if self.motion then
            self.motion.loading=self.motion.loading+delta
            if self.motion.loading>30 then error('loading_timeout') end
        end
        return false
    end
    if not self:flight() then error('FreeFly was disabled or gameplay detached') end
    self:hide()
    local motion=self.motion
    if motion then
        motion.elapsed=motion.elapsed+math.max(0,delta)
        local t=math.min(1,motion.elapsed/motion.duration)
        local a,b=motion.origin,motion.target
        local pose={x=a.x+(b.x-a.x)*t,y=a.y+(b.y-a.y)*t,z=a.z+(b.z-a.z)*t,
            yaw=(a.yaw+((b.yaw-a.yaw+180)%360-180)*t)%360,pitch=a.pitch+(b.pitch-a.pitch)*t}
        if motion.collision and not self:clearPath(self:camera(),pose) then error('blocked_path: obstacle appeared during movement') end
        self.target=pose
    end
    if self.target then self:align(self.target) end
    local actual=self:camera()
    local good=self.target and dist(actual,self.target)<0.1 and math.abs((actual.yaw-self.target.yaw+180)%360-180)<1 and math.abs(actual.pitch-self.target.pitch)<1
    self.stable=good and (self.stable+delta) or 0
    if motion and motion.elapsed>=motion.duration then
        motion.settle=motion.settle+delta
        if self.stable>=0.5 then self.motion=nil; return true end
        if motion.settle>5 then error('camera_settle_timeout') end
    end
    return false
end

function Engine:screenRay(u,v)
    if not finite(u) or not finite(v) or u<0 or u>1 or v<0 or v>1 then error('invalid screen point') end
    local origin=self:camera()
    local camera=Game.GetCameraSystem()
    local f,r,up=camera:GetActiveCameraForward(),camera:GetActiveCameraRight(),camera:GetActiveCameraUp()
    local function project(dx,dy,dz)
        return camera:ProjectPoint(Vector4.new(origin.x+10*(f.x+dx*r.x+dy*up.x),origin.y+10*(f.y+dx*r.y+dy*up.y),origin.z+10*(f.z+dx*r.z+dy*up.z)+dz,1))
    end
    -- Calibrate with the native projection: no assumed horizontal/vertical FOV.
    local c,pr,pu=project(0,0,0),project(1,0,0),project(0,1,0)
    if not finite(c.x) or not finite(c.y) or math.abs(pr.x-c.x)<0.00001 or math.abs(pu.y-c.y)<0.00001 then error('camera projection unavailable') end
    local sx=math.abs(c.x)>1 and math.abs(c.x)*2 or (math.abs(c.x-0.5)<0.1 and 1 or 2)
    local sy=math.abs(c.y)>1 and math.abs(c.y)*2 or (math.abs(c.y-0.5)<0.1 and 1 or 2)
    local rx=(u-0.5)*sx/(math.abs(pr.x-c.x))
    local uy=(0.5-v)*sy/(math.abs(pu.y-c.y))
    local d={x=f.x+rx*r.x+uy*up.x,y=f.y+rx*r.y+uy*up.y,z=f.z+rx*r.z+uy*up.z}
    local length=math.sqrt(d.x^2+d.y^2+d.z^2)
    return origin,{x=d.x/length,y=d.y/length,z=d.z/length}
end

function Engine:inspect(arguments)
    if not finite(arguments.range_m) or arguments.range_m<=0 or arguments.range_m>500 then error('invalid ray range') end
    local origin,direction=self:screenRay(arguments.u,arguments.v)
    if arguments.camera then
        local requested=arguments.camera
        if dist(origin,requested)>0.05 or math.abs((origin.yaw-requested.yaw+180)%360-180)>0.5 or math.abs(origin.pitch-requested.pitch)>0.5 or math.abs(origin.fov-requested.fov)>0.1 then
            error('Camera changed since the image; observe again')
        end
    end
    local destination={x=origin.x+direction.x*arguments.range_m,y=origin.y+direction.y*arguments.range_m,z=origin.z+direction.z*arguments.range_m}
    local hit=self:trace(origin,destination)
    if hit.trace then
        pcall(function()
            local resolved=Game.GetWorldInspector():GetPhysicsTraceObject(hit.trace)
            if resolved.resolved then
                hit.entity={hash=tostring(resolved.hash),proxy_id=tostring(resolved.proxyID)}
                pcall(function() hit.entity.id=tostring(resolved.entity:GetEntityID().hash) end)
                pcall(function() hit.entity.template=tostring(RedHotTools.GetEntityTemplatePath(resolved.entity)) end)
            end
        end)
    end
    hit.trace=nil; hit.origin=xyz(origin); hit.direction=direction; hit.projection='native_camera_calibration'
    return hit
end

function Engine:observers()
    for _,class in ipairs({'LoadingScreenLogicController','DefaultLoadingScreenLogicController','InitialLoadingScreenLogicController','LoadingScreenProgressBarController'}) do
        local key=class
        for _,event in ipairs({'OnInitialize','SetLoadProgress','SetProgress'}) do
            pcall(function() Observe(key,event,function(controller) self.loaders[key]=controller end) end)
        end
        pcall(function() Observe(key,'OnUninitialize',function() self.loaders[key]=nil end) end)
    end
    local classes={'ZoneAlertNotificationQueue','ZoneAlertNotification','JournalNotificationQueue','JournalNotification',
        'NewLocationNotification','NewAreaGameController','CustomQuestNotificationGameController','StealthZonesGameController',
        'interactionWidgetGameController','dialogWidgetGameController','InteractionsHubGameController','LootingGameController',
        'NewHudPhoneGameController','PhoneMessagePopupGameController','HudPhoneMessageController','MessengerNotification'}
    for _,class in ipairs(classes) do
        local key=class
        for _,event in ipairs({'OnInitialize','OnPlayerAttach','SetNotificationData','OnUpdateInteraction','UpdateVisibility','ResolveRootVisibility','Setup','OnNotificationsQueueChanged'}) do
            pcall(function() Observe(key,event,function(controller) self.hud[key]=controller; self:hide() end) end)
        end
        pcall(function() Observe(key,'OnUninitialize',function() self.hud[key]=nil; self.hidden[key]=nil end) end)
    end
end

return Engine
