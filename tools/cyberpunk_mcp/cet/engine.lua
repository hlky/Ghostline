-- Read-only telemetry. Never enables flight, teleports, hides HUD or alters player state.
local Engine={}; Engine.__index=Engine
local function xyz(v) return {x=v.x,y=v.y,z=v.z} end
function Engine.new()
    return setmetatable({frame=0,overlay=false,inMenu=false,loaders={}},Engine)
end
function Engine:status()
    local s={protocol=1,product='cyberpunk_mcp',timestamp=os.time(),frame=self.frame,
        overlay_open=self.overlay,loading=true,paused=true,freefly_active=false,ready=false}
    local ok,err=pcall(function()
        local player=Game.GetPlayer()
        if not player or not player:IsAttached() then return end
        s.loading=false
        for _,controller in pairs(self.loaders) do
            local visible,shown=pcall(function() return controller:GetRootWidget():IsVisible() end)
            if visible and shown then s.loading=true end
        end
        pcall(function()
            local defs=Game.GetAllBlackboardDefs().FastTRavelSystem
            local board=Game.GetBlackboardSystem():Get(defs)
            if board:GetBool(defs.FastTravelLoadingScreenStarted) and not board:GetBool(defs.FastTravelLoadingScreenFinished) then s.loading=true end
        end)
        s.paused=Game.GetSystemRequestsHandler():IsGamePaused()
        local freefly=GetMod('freefly')
        s.freefly_active=freefly and freefly.runtimeData and freefly.runtimeData.active==true or false
        s.in_menu=self.inMenu or (freefly and freefly.runtimeData and freefly.runtimeData.inMenu==true) or false
        s.player=xyz(player:GetWorldPosition())
        s.mounted=player:GetMountedVehicle()~=nil
        s.mode=s.mounted and 'vehicle' or 'on_foot'
        pcall(function() s.in_combat=player:IsInCombat() end)
        local camera=Game.GetCameraSystem()
        local f=camera:GetActiveCameraForward()
        local position=Game.GetTargetingSystem():GetCrosshairData(player)
        local atan2=math.atan2 or math.atan
        s.camera={x=position.x,y=position.y,z=position.z,
            yaw=math.deg(atan2(-f.x,f.y))%360,pitch=math.deg(atan2(f.z,math.sqrt(f.x*f.x+f.y*f.y))),
            fov=camera:GetActiveCameraFOV()}
        s.ready=not s.loading and not s.paused and not s.in_menu and not s.overlay_open and not s.freefly_active
    end)
    if not ok then s.ready=false; s.telemetry_error=tostring(err) end
    return s
end
function Engine:begin()
    local s=self:status()
    if not s.ready then error('Gameplay not ready: close CET/menus, load a save, unpause and disable FreeFly') end
    return s
end
function Engine:observers()
    pcall(function() Observe('RadialWheelController','OnIsInMenuChanged',function(_,isInMenu) self.inMenu=isInMenu==true end) end)
    for _,name in ipairs({'LoadingScreenLogicController','DefaultLoadingScreenLogicController','InitialLoadingScreenLogicController','LoadingScreenProgressBarController'}) do
        local class=name
        for _,event in ipairs({'OnInitialize','SetLoadProgress','SetProgress'}) do
            pcall(function() Observe(class,event,function(controller) self.loaders[class]=controller end) end)
        end
        pcall(function() Observe(class,'OnUninitialize',function() self.loaders[class]=nil end) end)
    end
end
return Engine
