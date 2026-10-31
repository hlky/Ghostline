-- Camera survey primitives. No inputs, HUD state, or FreeFly ownership changes.
local Survey = { loadingControllers = {}, revision = 2 }
local atan2 = math.atan2 or math.atan

local function vector(x, y, z) return Vector4.new(x, y, z, 1) end
local function finite(value) return type(value) == 'number' and value == value and math.abs(value) < math.huge end
local function distance(a, b)
    return math.sqrt((a.x-b.x)^2 + (a.y-b.y)^2 + (a.z-b.z)^2)
end
local function direction(yaw, pitch)
    local y, p = math.rad(yaw), math.rad(pitch)
    return { x=-math.sin(y)*math.cos(p), y=math.cos(y)*math.cos(p), z=math.sin(p) }
end

function Survey.readPose(player)
    local position = player:GetWorldPosition()
    local cameraSystem = Game.GetCameraSystem()
    local forward = cameraSystem:GetActiveCameraForward()
    local right, up = cameraSystem:GetActiveCameraRight(), cameraSystem:GetActiveCameraUp()
    -- This API is also used by the installed RedHotTools world inspector.
    local cameraPosition = Game.GetTargetingSystem():GetCrosshairData(player)
    if not cameraPosition or not finite(cameraPosition.x) or not finite(forward.z) then
        error('active camera pose is unavailable')
    end
    local yaw = math.deg(atan2(-forward.x, forward.y)) % 360
    local pitch = math.deg(atan2(forward.z, math.sqrt(forward.x^2+forward.y^2)))
    local roll = math.deg(atan2(right.z, up.z))
    return {
        x=position.x, y=position.y, z=position.z, yaw=yaw, pitch=pitch, roll=roll,
        forward={x=forward.x,y=forward.y,z=forward.z},
        position_frame='player_root', orientation_frame='active_camera', camera_verified=true,
        camera_pose={x=cameraPosition.x,y=cameraPosition.y,z=cameraPosition.z,yaw=yaw,pitch=pitch,roll=roll},
    }
end

function Survey.holdCamera(state)
    local command = state.command
    if not command or not command.survey or not state.active then return true end
    local ok, message = pcall(function()
        local player = Game.GetPlayer()
        local camera = player:GetFPPCameraComponent()
        if not state.snapshot.surveyCamera then
            state.snapshot.surveyCamera = { component=camera, orientation=camera:GetLocalOrientation(),
                pitchMin=camera.pitchMin, pitchMax=camera.pitchMax }
        end
        local pose = command.effective_pose or command.pose
        -- The installed entSpawner editor uses these native FPP pitch limits
        -- for absolute pitch control. Never tilt the player capsule for a photo.
        camera.pitchMin=pose.pitch or 0
        camera.pitchMax=pose.pitch or 0
        local actual=Survey.readPose(player)
        local errorYaw=(pose.yaw-actual.yaw+180)%360-180
        local body = player:GetWorldForward()
        local bodyYaw = math.deg(atan2(-body.x, body.y))
        if math.abs(errorYaw)>0.05 then
            local position=player:GetWorldPosition()
            Game.GetTeleportationFacility():Teleport(player,vector(position.x,position.y,position.z),EulerAngles.new(0,0,bodyYaw+errorYaw))
        end
    end)
    return ok, message
end

function Survey.restoreCamera(state)
    local saved = state.snapshot and state.snapshot.surveyCamera
    if not saved then return true end
    local ok = pcall(function()
        saved.component.pitchMin=saved.pitchMin
        saved.component.pitchMax=saved.pitchMax
        saved.component:ResetPitch()
        saved.component:SetLocalOrientation(saved.orientation)
    end)
    if ok then state.snapshot.surveyCamera = nil end
    return ok
end

function Survey.installLoadingObservers()
    for _, name in ipairs({'LoadingScreenLogicController','DefaultLoadingScreenLogicController','InitialLoadingScreenLogicController'}) do
        local key = name
        pcall(function() Observe(key, 'OnInitialize', function(controller) Survey.loadingControllers[key]=controller end) end)
        pcall(function() Observe(key, 'SetLoadProgress', function(controller) Survey.loadingControllers[key]=controller end) end)
        pcall(function() Observe(key, 'OnUninitialize', function() Survey.loadingControllers[key]=nil end) end)
    end
end

function Survey.loadingState()
    local sources = {}
    pcall(function()
        local player = Game.GetPlayer()
        if not player or not player:IsAttached() then table.insert(sources,'player_detached') end
    end)
    for key, controller in pairs(Survey.loadingControllers) do
        local ok, visible = pcall(function()
            local root = controller:GetRootWidget()
            return root ~= nil and root:IsVisible()
        end)
        if ok and visible then table.insert(sources,key) end
        if not ok then Survey.loadingControllers[key]=nil end
    end
    pcall(function()
        local definition = Game.GetAllBlackboardDefs().FastTRavelSystem
        if not definition then return end
        local board = Game.GetBlackboardSystem():Get(definition)
        if board:GetBool(definition.FastTravelLoadingScreenStarted)
            and not board:GetBool(definition.FastTravelLoadingScreenFinished) then
            table.insert(sources,'fast_travel_blackboard')
        end
    end)
    return #sources > 0, sources
end

local function trace(start, destination, groups)
    local ok, blocked = pcall(function()
        local system = Game.GetSpatialQueriesSystem()
        for _, group in ipairs(groups or {'Static','Vehicle','Dynamic'}) do
            local hit = system:SyncRaycastByCollisionGroup(start, destination, group, false, false)
            if hit then return true end
        end
        return false
    end)
    return ok, blocked
end

function Survey.pathClear(start, destination)
    -- Parallel probes provide a small camera-clearance margin along the move.
    for _, delta in ipairs({{0,0,0},{0.25,0,0},{-0.25,0,0},{0,0.25,0},{0,-0.25,0}}) do
        local ok, hit = trace(vector(start.x+delta[1],start.y+delta[2],start.z+delta[3]),
            vector(destination.x+delta[1],destination.y+delta[2],destination.z+delta[3]), {'Static','Vehicle'})
        if not ok or hit then return false end
    end
    return true
end

function Survey.startMovement(state)
    local command, player = state.command, Game.GetPlayer()
    local pose = command.effective_pose or command.pose
    local current = player:GetWorldPosition()
    local travel = distance(current,pose)
    state.surveyMotion = nil
    if travel < 0.03 then return 'stationary' end
    local options = command.survey
    if travel <= options.local_move_maximum_m then
        local actual = Survey.readPose(player)
        local origin = actual.camera_pose
        local target = {x=origin.x+pose.x-current.x,y=origin.y+pose.y-current.y,z=origin.z+pose.z-current.z}
        if Survey.pathClear(origin,target) then
            state.surveyMotion={origin={x=current.x,y=current.y,z=current.z},target=pose,elapsed=0,
                duration=travel/options.local_move_speed_mps}
            return 'local_flight'
        end
    end
    Game.GetTeleportationFacility():Teleport(player,vector(pose.x,pose.y,pose.z),EulerAngles.new(0,0,pose.yaw))
    return 'teleport'
end

function Survey.advanceMovement(state, delta)
    local motion = state.surveyMotion
    if not motion then return true end
    motion.elapsed = motion.elapsed + math.max(0,delta)
    local t = math.min(1,motion.elapsed/motion.duration)
    local a,b = motion.origin,motion.target
    Game.GetTeleportationFacility():Teleport(Game.GetPlayer(),vector(a.x+(b.x-a.x)*t,a.y+(b.y-a.y)*t,a.z+(b.z-a.z)*t),EulerAngles.new(0,0,b.yaw))
    if t >= 1 then state.surveyMotion=nil; return true end
    return false
end

function Survey.probe(pose, origin, range)
    local hits, available, columns = 0,true,{0,0,0}
    for column,yaw in ipairs({-22,0,22}) do
        for _, pitch in ipairs({-12,0,12}) do
            local d = direction(pose.yaw+yaw,pose.pitch+pitch)
            local ok, hit = trace(vector(origin.x,origin.y,origin.z),
                vector(origin.x+d.x*range,origin.y+d.y*range,origin.z+d.z*range))
            available = available and ok
            if hit then hits=hits+1; columns[column]=columns[column]+1 end
        end
    end
    return {available=available,near_hits=hits,blocked=available and (hits>=5 or columns[1]==3 or columns[2]==3 or columns[3]==3)}
end

function Survey.recoverObstruction(state)
    local command = state.command
    if not command.survey or not command.survey.obstruction_enabled then return false end
    if state.surveyObstructionChecked then return false end
    state.surveyObstructionChecked=true
    local actual = Survey.readPose(Game.GetPlayer())
    local range = command.survey.near_obstruction_m
    local evidence = Survey.probe(actual,actual.camera_pose,range)
    evidence.recoveries=state.surveyRecoveries or 0
    state.surveyObstruction=evidence
    if not evidence.blocked or evidence.recoveries>=command.survey.maximum_recoveries then return false end
    local current = command.effective_pose
    local best,bestHits = nil,evidence.near_hits
    for _, candidate in ipairs(command.recovery_candidates or {}) do
        local origin = {x=actual.camera_pose.x+candidate.x-current.x,
            y=actual.camera_pose.y+candidate.y-current.y,z=actual.camera_pose.z+candidate.z-current.z}
        if Survey.pathClear(actual.camera_pose,origin) then
            local trial = Survey.probe(actual,origin,range)
            if trial.available and trial.near_hits < bestHits then best,bestHits=candidate,trial.near_hits end
        end
    end
    if not best then evidence.recovery_exhausted=true; return false end
    command.effective_pose=best
    state.surveyRecoveries=evidence.recoveries+1
    state.surveyObstructionChecked=false
    return true
end

return Survey
