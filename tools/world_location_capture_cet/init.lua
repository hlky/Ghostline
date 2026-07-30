-- Night City world-location capture runtime.
-- All communication is scoped to this CET mod's runtime directory.

local config = nil
local state = {
    active = false,
    snapshot = nil,
    command = nil,
    lastCommandId = nil,
    stage = 'idle',
    loadingScreen = false,
    menuOpen = false,
    overlayOpen = false,
    phonePresentationActive = false,
    notificationSuppressionActive = false,
    frame = 0,
    elapsed = 0.0,
    heartbeatElapsed = 0.0,
    readyEvidence = nil,
    preflightEvidence = nil,
    lastReadiness = nil,
    hiddenControllers = {},
    popupControllers = {},
    hiddenWeapon = nil,
}

local function log(level, message)
    local prefix = '[world_location_capture] '
    if spdlog and spdlog[level] then
        spdlog[level](prefix .. tostring(message))
    else
        print(prefix .. tostring(message))
    end
end

local function readJson(path)
    local file = io.open(path, 'r')
    if not file then return nil, nil end
    local contents = file:read('*a')
    file:close()
    local ok, value = pcall(function() return json.decode(contents) end)
    if not ok or type(value) ~= 'table' then
        return nil, 'malformed JSON in ' .. path
    end
    return value, nil
end

local function writeJsonAtomic(path, value)
    local temporary = path .. '.tmp'
    os.remove(temporary)
    local ok, payload = pcall(function() return json.encode(value) end)
    if not ok then return false, tostring(payload) end
    local file = io.open(temporary, 'w')
    if not file then return false, 'cannot open ' .. temporary end
    file:write(payload)
    file:flush()
    file:close()
    -- Command-specific event destinations are absent before their only write.
    -- Heartbeats may replace their previous value.
    os.remove(path)
    local renamed, renameError = os.rename(temporary, path)
    if not renamed then
        os.remove(temporary)
        return false, tostring(renameError)
    end
    return true, nil
end

local function runtimePath(name)
    return config.runtime_directory .. '/' .. name
end

local function now()
    return os.date('!%Y-%m-%dT%H:%M:%SZ')
end

local function copyTable(source)
    local target = {}
    if type(source) ~= 'table' then return target end
    for key, value in pairs(source) do
        if type(value) == 'table' then
            target[key] = copyTable(value)
        else
            target[key] = value
        end
    end
    return target
end

local function merge(target, values)
    for key, value in pairs(values or {}) do target[key] = value end
    return target
end

local function writeEvent(eventName, values)
    if not state.command then return end
    local event = {
        schema_version = 1,
        session_id = state.command.session_id,
        command_id = state.command.command_id,
        location_id = state.command.location_id,
        event = eventName,
        timestamp = now(),
    }
    merge(event, values)
    local ok, err = writeJsonAtomic(runtimePath('event-' .. eventName .. '.json'), event)
    if not ok then log('error', err) end
end

local function failCommand(code, detail)
    writeEvent('error', { error_code = code, error_detail = tostring(detail) })
    state.stage = 'error'
end

local function configuredSetting(settingsSystem, descriptor)
    local path = type(descriptor) == 'table' and descriptor.path or nil
    local name = type(descriptor) == 'table' and descriptor.name or nil
    if type(path) ~= 'string' or path == '' or type(name) ~= 'string' or name == '' then
        return nil, 'invalid empty settings path or name in capture config'
    end
    local hasOk, exists = pcall(function() return settingsSystem:HasVar(path, name) end)
    if not hasOk then return nil, 'settings HasVar failed for ' .. path .. '/' .. name end
    if not exists then return nil, 'capture setting does not exist: ' .. path .. '/' .. name end
    local getOk, setting = pcall(function() return settingsSystem:GetVar(path, name) end)
    if not getOk or not setting then
        return nil, 'settings GetVar failed for ' .. path .. '/' .. name
    end
    return setting, nil
end

local function snapshotAndDisableSettings()
    local prepared = {}
    local settingsSystem = Game.GetSettingsSystem()
    if not settingsSystem then return nil, 'settings system unavailable' end
    for _, descriptor in ipairs(config.settings_vars or {}) do
        local setting, settingError = configuredSetting(settingsSystem, descriptor)
        if not setting then return nil, settingError end
        local valueOk, value = pcall(function() return setting:GetValue() end)
        if not valueOk or type(value) ~= 'boolean' then
            return nil, 'capture setting is not boolean: ' .. descriptor.path .. '/' .. descriptor.name
        end
        table.insert(prepared, {
            path = descriptor.path,
            name = descriptor.name,
            value = value,
            captureValue = descriptor.capture_value == nil and false or descriptor.capture_value == true,
            setting = setting,
        })
    end
    if #prepared == 0 then return nil, 'no HUD/subtitle settings were found' end

    local snapshot = {}
    for index, item in ipairs(prepared) do
        local setOk = pcall(function() item.setting:SetValue(item.captureValue) end)
        if not setOk then
            for restoreIndex = 1, index - 1 do
                local prior = prepared[restoreIndex]
                pcall(function() prior.setting:SetValue(prior.value) end)
            end
            return nil, 'failed to suppress ' .. item.path .. '/' .. item.name
        end
        table.insert(snapshot, {
            path = item.path,
            name = item.name,
            value = item.value,
            captureValue = item.captureValue,
        })
    end
    return snapshot, nil
end

local function settingsAreSuppressed()
    if not state.snapshot or not state.snapshot.settings then return false end
    local settingsSystem = Game.GetSettingsSystem()
    if not settingsSystem then return false end
    for _, saved in ipairs(state.snapshot.settings) do
        local setting = configuredSetting(settingsSystem, saved)
        if not setting then return false end
        local ok, value = pcall(function() return setting:GetValue() end)
        if not ok or value ~= saved.captureValue then return false end
    end
    return true
end

local function restoreSettings()
    if not state.snapshot or not state.snapshot.settings then return true end
    local settingsSystem = Game.GetSettingsSystem()
    if not settingsSystem then return false end
    local restored = true
    for _, saved in ipairs(state.snapshot.settings) do
        local ok, matches = pcall(function()
            local setting = configuredSetting(settingsSystem, saved)
            if not setting then return false end
            setting:SetValue(saved.value)
            return setting:GetValue() == saved.value
        end)
        if not ok or not matches then restored = false end
    end
    return restored
end

local function restoreControllers()
    local restored = true
    for _, saved in pairs(state.hiddenControllers) do
        local ok, matches = pcall(function()
            saved.widget:SetVisible(saved.visible)
            return saved.widget:IsVisible() == saved.visible
        end)
        if not ok or not matches then restored = false end
    end
    state.hiddenControllers = {}
    return restored
end

local function statusEffectExists(effectName)
    local ok, record = pcall(function() return TweakDB:GetRecord(effectName) end)
    return ok and record ~= nil
end

local function hasStatusEffect(player, effectName)
    local ok, value = pcall(function()
        return Game.GetStatusEffectSystem():HasStatusEffect(
            player:GetEntityID(), TweakDBID.new(effectName)
        )
    end)
    return ok and value == true
end

local function applyCaptureEffects(player)
    local snapshot = {}
    local effects = { 'BaseStatusEffect.Invulnerable' }
    for _, name in ipairs(config.restrictions or {}) do table.insert(effects, name) end
    local system = Game.GetStatusEffectSystem()
    if not system then return nil, 'status effect system unavailable' end
    for _, effectName in ipairs(effects) do
        if not statusEffectExists(effectName) then
            return nil, 'required status effect is missing: ' .. effectName
        end
        table.insert(snapshot, {
            name = effectName,
            alreadyApplied = hasStatusEffect(player, effectName),
        })
    end
    for index, effect in ipairs(snapshot) do
        if not effect.alreadyApplied then
            local ok = pcall(function()
                system:ApplyStatusEffect(player:GetEntityID(), TweakDBID.new(effect.name))
            end)
            if not ok or not hasStatusEffect(player, effect.name) then
                for restoreIndex = 1, index - 1 do
                    local prior = snapshot[restoreIndex]
                    if not prior.alreadyApplied then
                        pcall(function()
                            system:RemoveStatusEffect(
                                player:GetEntityID(), TweakDBID.new(prior.name)
                            )
                        end)
                    end
                end
                return nil, 'failed to apply ' .. effect.name
            end
        end
    end
    return snapshot, nil
end

local function effectsAreApplied(player)
    if not state.snapshot or not state.snapshot.effects then return false end
    for _, effect in ipairs(state.snapshot.effects) do
        if not hasStatusEffect(player, effect.name) then return false end
    end
    return true
end

local function restoreEffects(player)
    if not state.snapshot or not state.snapshot.effects then return true end
    if not player then return false end
    local system = Game.GetStatusEffectSystem()
    if not system then return false end
    local restored = true
    for _, effect in ipairs(state.snapshot.effects) do
        if not effect.alreadyApplied then
            local removed = pcall(function()
                system:RemoveStatusEffect(player:GetEntityID(), TweakDBID.new(effect.name))
            end)
            if not removed then restored = false end
        end
        if hasStatusEffect(player, effect.name) ~= effect.alreadyApplied then restored = false end
    end
    return restored
end

local function snapshotPrevention()
    local ok, prevention = pcall(function()
        return Game.GetScriptableSystemsContainer():Get('PreventionSystem')
    end)
    if not ok or not prevention then return nil end
    local snapshot = { system = prevention }
    pcall(function() snapshot.enabled = prevention:IsSystemEnabled() end)
    pcall(function() snapshot.heat = prevention:GetHeatStageAsInt() end)
    pcall(function()
        if snapshot.heat and snapshot.heat ~= 0 then
            prevention:ChangeHeatStage(EPreventionHeatStage.Heat_0, 'world_location_capture')
        end
        if snapshot.enabled then prevention:TogglePreventionSystem(false) end
    end)
    return snapshot
end

local function restorePrevention()
    local saved = state.snapshot and state.snapshot.prevention or nil
    if not saved or not saved.system then return true end
    local ok, matches = pcall(function()
        if saved.enabled and not saved.system:IsSystemEnabled() then
            saved.system:TogglePreventionSystem(true)
        elseif saved.enabled == false and saved.system:IsSystemEnabled() then
            saved.system:TogglePreventionSystem(false)
        end
        if saved.heat and saved.heat > 0 then
            local value = EPreventionHeatStage['Heat_' .. tostring(saved.heat)]
            if value then saved.system:ChangeHeatStage(value, 'world_location_capture_restore') end
        end
        local enabledMatches = saved.enabled == nil or saved.system:IsSystemEnabled() == saved.enabled
        local heatMatches = saved.heat == nil or saved.system:GetHeatStageAsInt() == saved.heat
        return enabledMatches and heatMatches
    end)
    return ok and matches == true
end

local function setProfile(profile)
    local player = Game.GetPlayer()
    if not player then return false, 'player unavailable' end
    if not state.snapshot.time then
        local timeSystem = Game.GetTimeSystem()
        local gameTime = timeSystem and timeSystem:GetGameTime() or nil
        if gameTime then
            local ok = pcall(function()
                state.snapshot.time = {
                    hours = gameTime:Hours(), minutes = gameTime:Minutes(), seconds = gameTime:Seconds()
                }
            end)
            if not ok then state.snapshot.time = nil end
        end
    end
    if profile.time then
        local hours, minutes = tostring(profile.time):match('^(%d%d?):(%d%d)$')
        if not hours then return false, 'profile time must be HH:MM' end
        Game.GetTimeSystem():SetGameTimeByHMS(tonumber(hours), tonumber(minutes), 0)
    end
    local camera = player:GetFPPCameraComponent()
    if not camera then return false, 'first-person camera unavailable' end
    if state.snapshot.fov == nil then
        local ok, fov = pcall(function() return camera:GetFOV() end)
        if ok then state.snapshot.fov = fov end
    end
    if state.snapshot.zoom == nil then
        local ok, zoom = pcall(function() return camera:GetZoom() end)
        if ok then state.snapshot.zoom = zoom end
    end
    if profile.fov then
        if state.snapshot.zoom ~= nil then camera:SetZoom(0.0) end
        camera:SetFOV(tonumber(profile.fov))
    end
    if profile.weather then
        local weatherName = (config.weather_names or {})[profile.weather]
        if not weatherName then return false, 'unknown weather profile: ' .. tostring(profile.weather) end
        local ok = pcall(function()
            Game.GetWeatherSystem():SetWeather(weatherName, 0.0, 10)
        end)
        if not ok then return false, 'weather system SetWeather failed' end
        state.snapshot.weatherOverrideApplied = true
    end
    return true, nil
end

local function hideController(controller)
    if not state.active or not controller then return end
    pcall(function()
        local widget = controller:GetRootWidget()
        if widget then
            local key = tostring(controller)
            if not state.hiddenControllers[key] then
                local visible = widget:IsVisible()
                state.hiddenControllers[key] = { widget = widget, visible = visible }
            end
            widget:SetVisible(false)
        end
    end)
end

local function rememberPopupController(controller)
    if controller then state.popupControllers[tostring(controller)] = controller end
end

local function forgetPopupController(controller)
    if controller then state.popupControllers[tostring(controller)] = nil end
end

local function suppressPopupController(controller)
    rememberPopupController(controller)
    pcall(function() controller:Dismiss() end)
    hideController(controller)
end

local function setPhoneMessageNotificationsHidden(hidden)
    local ok, matches = pcall(function()
        local definitions = Game.GetAllBlackboardDefs()
        local board = Game.GetBlackboardSystem():Get(definitions.UI_ComDevice)
        if state.snapshot and state.snapshot.contactsActive == nil then
            state.snapshot.contactsActive = board:GetBool(definitions.UI_ComDevice.ContactsActive)
        end
        local value = hidden
        if not hidden and state.snapshot and state.snapshot.contactsActive ~= nil then
            value = state.snapshot.contactsActive
        end
        board:SetBool(definitions.UI_ComDevice.ContactsActive, value, true)
        return board:GetBool(definitions.UI_ComDevice.ContactsActive) == value
    end)
    return ok and matches == true
end

local function dismissNotifications()
    local ok = pcall(function()
        local definitions = Game.GetAllBlackboardDefs()
        local board = Game.GetBlackboardSystem():Get(definitions.UI_Notifications)
        local message = SimpleScreenMessage.new()
        message.message = ''
        message.duration = 0.0
        message.isShown = false
        board:SetVariant(definitions.UI_Notifications.OnscreenMessage, ToVariant(message), true)
        board:SetVariant(definitions.UI_Notifications.WarningMessage, ToVariant(message), true)
    end)
    for _, controller in pairs(state.popupControllers) do
        suppressPopupController(controller)
    end
    state.notificationSuppressionActive = ok and setPhoneMessageNotificationsHidden(true)
end

local function equipmentData(player)
    local ok, data = pcall(function()
        return Game.GetScriptableSystemsContainer():Get('EquipmentSystem'):GetPlayerData(player)
    end)
    if not ok then return nil end
    return data
end

local function hideCurrentWeapon(player)
    local ok, weapon = pcall(function()
        return Game.GetTransactionSystem():GetItemInSlot(
            player, TweakDBID.new('AttachmentSlots.WeaponRight')
        )
    end)
    if not ok then return false end
    if not weapon then return true end
    local data = equipmentData(player)
    if not data then return false end
    if not state.hiddenWeapon then
        local idKnown, itemID = pcall(function() return weapon:GetItemID() end)
        if not idKnown then return false end
        state.hiddenWeapon = { equipment = data, itemID = itemID }
    end
    pcall(function()
        data:CreateUnequipWeaponManipulationRequest()
    end)
    return false
end

local function restoreWeapon()
    if not state.hiddenWeapon then return true end
    local saved = state.hiddenWeapon
    state.hiddenWeapon = nil
    return pcall(function()
        saved.equipment:EquipItem(saved.itemID, false, true)
    end)
end

local function restoreCaptureMode(reason)
    if not state.active and not state.snapshot then return true end
    local player = Game.GetPlayer()
    local effectsRestored = restoreEffects(player)
    local weaponRestored = restoreWeapon()
    local controllersRestored = restoreControllers()
    local phoneNotificationsRestored = setPhoneMessageNotificationsHidden(false)
    local verification = {
        weapon = weaponRestored,
        controllers = controllersRestored,
        phone_notifications = phoneNotificationsRestored,
        effects = effectsRestored,
        settings = restoreSettings(),
        prevention = restorePrevention(),
        camera = true,
        time = true,
        weather = true,
    }
    if state.snapshot then
        if state.snapshot.fov and player then
            local ok, matches = pcall(function()
                local camera = player:GetFPPCameraComponent()
                if state.snapshot.zoom ~= nil then camera:SetZoom(state.snapshot.zoom) end
                camera:SetFOV(state.snapshot.fov)
                local fovMatches = math.abs(camera:GetFOV() - state.snapshot.fov) <= 0.05
                local zoomMatches = state.snapshot.zoom == nil
                    or math.abs(camera:GetZoom() - state.snapshot.zoom) <= 0.001
                return fovMatches and zoomMatches
            end)
            verification.camera = ok and matches == true
        end
        if state.snapshot.time then
            local ok, matches = pcall(function()
                Game.GetTimeSystem():SetGameTimeByHMS(
                    state.snapshot.time.hours, state.snapshot.time.minutes, state.snapshot.time.seconds
                )
                local restoredTime = Game.GetTimeSystem():GetGameTime()
                return restoredTime:Hours() == state.snapshot.time.hours
                    and restoredTime:Minutes() == state.snapshot.time.minutes
            end)
            verification.time = ok and matches == true
        end
        if state.snapshot.weatherOverrideApplied then
            verification.weather = pcall(function() Game.GetWeatherSystem():ResetWeather(true) end)
        end
    end
    state.active = false
    state.snapshot = nil
    state.phonePresentationActive = false
    state.notificationSuppressionActive = false
    log('info', 'capture mode restored: ' .. tostring(reason))
    local restored = true
    for _, value in pairs(verification) do
        if value ~= true then restored = false end
    end
    return restored, verification
end

local function enterCaptureMode(profile)
    if state.active then return setProfile(profile) end
    local player = Game.GetPlayer()
    if not player or not player:IsAttached() then return false, 'player is not attached' end
    state.snapshot = {}
    local settings, settingsError = snapshotAndDisableSettings()
    if not settings then
        state.snapshot = nil
        return false, settingsError
    end
    state.snapshot.settings = settings
    local effects, effectsError = applyCaptureEffects(player)
    state.snapshot.effects = effects
    state.snapshot.prevention = snapshotPrevention()
    state.active = true
    dismissNotifications()
    local ok, profileError = setProfile(profile)
    if not ok then
        restoreCaptureMode('profile setup failed')
        return false, profileError
    end
    return true, nil
end

local function getMenuOpen()
    local ok, value = pcall(function()
        local definitions = Game.GetAllBlackboardDefs()
        local board = Game.GetBlackboardSystem():Get(definitions.UI_System)
        return board:GetBool(definitions.UI_System.IsInMenu)
    end)
    return ok and value == true
end

local function getPaused()
    local ok, value = pcall(function()
        return Game.GetSystemRequestsHandler():IsGamePaused()
    end)
    return ok and value == true
end

local function getActualPose(player)
    local position = player:GetWorldPosition()
    local forward = player:GetWorldForward()
    local yaw = math.deg(math.atan2(-forward.x, forward.y))
    if yaw < 0 then yaw = yaw + 360.0 end
    return {
        x = position.x, y = position.y, z = position.z,
        yaw = yaw, pitch = 0.0, roll = 0.0,
        forward = { x = forward.x, y = forward.y, z = forward.z },
    }
end

local function angleDelta(left, right)
    local delta = math.abs((left - right + 180.0) % 360.0 - 180.0)
    return delta
end

local function positionIsValid(actual, expected, tolerances)
    local dx, dy, dz = actual.x - expected.x, actual.y - expected.y, actual.z - expected.z
    local distance = math.sqrt(dx * dx + dy * dy + dz * dz)
    local heading = angleDelta(actual.yaw, expected.yaw)
    return distance <= tonumber(tolerances.position_tolerance_m or 0.35), distance, heading
end

local function playerIsStill(player)
    local ok, velocity = pcall(function() return player:GetVelocity() end)
    if not ok or not velocity then return false, nil end
    local speed = math.sqrt(velocity.x * velocity.x + velocity.y * velocity.y + velocity.z * velocity.z)
    return speed <= tonumber(config.velocity_tolerance_mps or 0.02), speed
end

local function raycast(from, to)
    local ok, success, result = pcall(function()
        return Game.GetSpatialQueriesSystem():SyncRaycastByCollisionGroup(
            from, to, 'Static', false, false
        )
    end)
    if not ok or not success then return false, nil end
    return true, result
end

local teleport

local function stageGroundProbe(command)
    local pose = command.effective_pose or command.pose
    pose.z = pose.z + tonumber(config.ground_probe_staging_height_m or 3.0)
    command.ground_snap_complete = false
    return teleport(command)
end

local function groundProbe(position)
    local from = Vector4.new(position.x, position.y, position.z + config.ground_probe_up_m, 1.0)
    local to = Vector4.new(position.x, position.y, position.z - config.ground_probe_down_m, 1.0)
    return raycast(from, to)
end

local function hitPosition(result)
    if not result then return nil end
    if result.position then return result.position end
    if result.hitPosition then return result.hitPosition end
    if result.worldPosition then return result.worldPosition end
    return nil
end

local function applyGroundSnap()
    if state.command.ground_snap_complete then return true end
    local pose = state.command.effective_pose
    local success, result = groundProbe(pose)
    if not success then return false end
    local hit = hitPosition(result)
    if not hit then
        -- The collision result is still a valid streaming/ground fence even
        -- on game builds that do not expose its hit position to CET.
        state.command.ground_snap_complete = true
        return true
    end
    local targetZ = hit.z + tonumber(config.ground_offset_m or 0.1)
    local adjustment = targetZ - pose.z
    state.command.ground_snap_complete = true
    if math.abs(adjustment) > 0.01 then
        pose.z = targetZ
        local teleported, teleportError = teleport(state.command)
        if not teleported then failCommand('ground_snap_teleport_failed', teleportError) end
    end
    return true
end

local function tryNextLateralPose()
    local expected = state.command.expected or {}
    local maximum = tonumber(expected.lateral_search_m or 0.0)
    if maximum <= 0.0 then return false end
    state.command.lateral_index = (state.command.lateral_index or 0) + 1
    local index = state.command.lateral_index
    local stepNumber = math.floor((index + 1) / 2)
    local distance = stepNumber * 0.25
    if distance > maximum + 0.001 then return false end
    if index % 2 == 1 then distance = -distance end
    local original = state.command.pose
    local forward = expected.forward or { x = 0.0, y = 1.0 }
    local lateralX, lateralY = -forward.y, forward.x
    state.command.effective_pose = copyTable(original)
    state.command.effective_pose.x = original.x + lateralX * distance
    state.command.effective_pose.y = original.y + lateralY * distance
    local teleported, teleportError = stageGroundProbe(state.command)
    if not teleported then failCommand('lateral_teleport_failed', teleportError) end
    return teleported
end

local function anchorProbe(position, expected)
    if expected.category == 'road' then return groundProbe(position) end
    local anchor = expected.anchor_position
    if type(anchor) ~= 'table' then return false, nil end
    local from = Vector4.new(position.x, position.y, position.z + 0.8, 1.0)
    local to = Vector4.new(anchor.x, anchor.y, anchor.z + 0.8, 1.0)
    return raycast(from, to)
end

local function streamingIsComplete(groundReady, anchorReady)
    -- Destination collision is the streaming fence.  Do not query an
    -- undocumented GameOptions path here: missing options log an error on
    -- every update even when the Lua call is protected with pcall.
    return groundReady and anchorReady, 'destination collision probes'
end

local function runtimeLocation()
    local result = {}
    pcall(function()
        local prevention = Game.GetScriptableSystemsContainer():Get('PreventionSystem')
        local manager = prevention and prevention.districtManager or nil
        local district = manager and manager:GetCurrentDistrict() or nil
        if not district then return end
        local record = GetSingleton('gamedataTweakDBInterface'):GetDistrictRecord(district:GetDistrictID())
        local labels = {}
        while record do
            table.insert(labels, 1, Game.GetLocalizedText(record:LocalizedName()))
            record = record:ParentDistrict()
        end
        result.district = labels[1]
        result.subdistrict = labels[2]
        result.named_area = labels[#labels]
    end)
    pcall(function()
        result.interior_state = IsEntityInInteriorArea(Game.GetPlayer()) and 'interior' or 'exterior'
    end)
    return result
end

local function uiIsSuppressed(player)
    local width, height = GetDisplayResolution()
    local weaponHidden = hideCurrentWeapon(player)
    return settingsAreSuppressed()
        and effectsAreApplied(player)
        and state.notificationSuppressionActive
        and not state.phonePresentationActive
        and not state.overlayOpen
        and weaponHidden
        and width == config.expected_width
        and height == config.expected_height,
        width, height, weaponHidden
end

local function buildReadiness()
    local player = Game.GetPlayer()
    if not player then return { streaming_complete = false, reason = 'player unavailable' } end
    local requests = Game.GetSystemRequestsHandler()
    local attached = player:IsAttached() and requests and not requests:IsPreGame()
    local actual = getActualPose(player)
    local positionValid, positionDelta, headingDelta = positionIsValid(
        actual, state.command.effective_pose or state.command.pose, state.command.expected or {}
    )
    local still, speed = playerIsStill(player)
    local groundReady = groundProbe(actual)
    local anchorReady = anchorProbe(actual, state.command.expected or {})
    local streamingComplete, streamingSource = streamingIsComplete(groundReady, anchorReady)
    state.menuOpen = getMenuOpen()
    local paused = getPaused()
    local uiSuppressed, width, height, weaponHidden = uiIsSuppressed(player)
    local cameraAttached = player:GetFPPCameraComponent() ~= nil
    local evidence = {
        streaming_complete = streamingComplete,
        streaming_source = streamingSource,
        loading_screen = state.loadingScreen,
        menu_open = state.menuOpen,
        paused = paused,
        player_attached = attached,
        camera_attached = cameraAttached,
        position_valid = positionValid,
        position_delta_m = positionDelta,
        heading_delta_degrees = headingDelta,
        velocity_zero = still,
        velocity_mps = speed,
        ground_probe = groundReady,
        anchor_probe = anchorReady,
        ui_suppressed = uiSuppressed,
        weapon_suppressed = weaponHidden,
        display_width = width,
        display_height = height,
    }
    state.lastReadiness = evidence
    local ready = streamingComplete and not state.loadingScreen and not state.menuOpen and not paused
        and attached and cameraAttached and still and groundReady and anchorReady and weaponHidden
    return evidence, ready, actual
end

teleport = function(command)
    local pose = command.effective_pose or command.pose
    local player = Game.GetPlayer()
    local ok, errorValue = pcall(function()
        Game.GetTeleportationFacility():Teleport(
            player,
            Vector4.new(pose.x, pose.y, pose.z, 1.0),
            EulerAngles.new(pose.roll or 0.0, pose.pitch or 0.0, pose.yaw)
        )
    end)
    if not ok then return false, tostring(errorValue) end
    state.readyEvidence = nil
    if state.stage ~= 'waiting' then
        writeEvent('teleported', { effective_pose = pose })
    end
    return true, nil
end

local function acceptCommand(command)
    if command.schema_version ~= 1 then
        state.command = command
        failCommand('unsupported_schema', tostring(command.schema_version))
        return
    end
    if type(command.command_id) ~= 'string' or type(command.session_id) ~= 'string' then
        return
    end
    state.command = command
    state.lastCommandId = command.command_id
    if command.kind == 'restore' then
        local restored, verification = restoreCaptureMode('controller request')
        writeEvent('restored', {
            restoration_verified = restored == true,
            restoration = verification or {},
        })
        state.stage = 'idle'
        state.command = nil
        return
    end
    if command.kind ~= 'capture' or type(command.pose) ~= 'table' or type(command.profile) ~= 'table' then
        failCommand('malformed_command', 'capture command requires pose and profile')
        return
    end
    command.effective_pose = copyTable(command.pose)
    command.ground_snap_complete = false
    command.lateral_index = 0
    state.elapsed = 0.0
    state.preflightEvidence = nil
    state.lastReadiness = nil
    state.stage = 'preflight'
    writeEvent('accepted', {
        capture_mode_active = false,
        waiting_for_gameplay = true,
    })
end

local function beginCaptureWhenGameplayIsReady()
    if state.stage ~= 'preflight' or not state.command then return end
    local player = Game.GetPlayer()
    local requests = Game.GetSystemRequestsHandler()
    state.menuOpen = getMenuOpen()
    local attached = player ~= nil and player:IsAttached()
    local pregame = true
    if requests then
        local ok, value = pcall(function() return requests:IsPreGame() end)
        pregame = not ok or value == true
    end
    state.preflightEvidence = {
        player_available = player ~= nil,
        player_attached = attached,
        requests_available = requests ~= nil,
        pregame = pregame,
        loading_screen = state.loadingScreen,
        menu_open = state.menuOpen,
        paused = getPaused(),
    }
    -- Menu, pause, and loading state are final readiness predicates, not
    -- teleport gates.  Gating the teleport on them can deadlock on stale UI
    -- state left by a prior loading screen.  We only require a live attached
    -- gameplay player before entering capture mode and teleporting.
    if not attached or not requests or pregame then
        return
    end
    local entered, enterError = enterCaptureMode(state.command.profile)
    if not entered then
        failCommand('capture_mode_failed', enterError)
        return
    end
    local teleported, teleportError = stageGroundProbe(state.command)
    if not teleported then
        failCommand('teleport_failed', teleportError)
        return
    end
    state.elapsed = 0.0
    state.stage = 'waiting'
end

local function pollCommand()
    local command, readError = readJson(runtimePath('command.json'))
    if readError then
        if state.command then failCommand('malformed_command_file', readError) end
        return
    end
    if not command or command.command_id == state.lastCommandId then return end
    if state.stage ~= 'idle' then return end
    acceptCommand(command)
end

local function pollAck()
    if not state.command or state.stage == 'idle' then return end
    local ack = readJson(runtimePath('ack.json'))
    if not ack or ack.command_id ~= state.command.command_id then return end
    if ack.success ~= false and state.stage ~= 'ready' and state.stage ~= 'error' then return end
    writeEvent('completed', { success = ack.success == true, detail = ack.detail or {} })
    state.stage = 'idle'
    state.command = nil
    state.readyEvidence = nil
end

local function controllerHeartbeatIsAlive()
    local heartbeat = readJson(runtimePath('controller-heartbeat.json'))
    if not heartbeat or type(heartbeat.unix_seconds) ~= 'number' then return false end
    return math.abs(os.time() - heartbeat.unix_seconds)
        <= tonumber(config.controller_heartbeat_timeout_seconds or 5) + 1
end

local function writeHeartbeat()
    writeJsonAtomic(runtimePath('cet-heartbeat.json'), {
        schema_version = 1,
        timestamp = now(),
        unix_seconds = os.time(),
        capture_mode_active = state.active,
        stage = state.stage,
        frame = state.frame,
        preflight = state.preflightEvidence,
        readiness = state.lastReadiness,
    })
end

local function installObservers()
    Observe('LoadingScreenProgressBarController', 'SetProgress', function(_, progress)
        state.loadingScreen = tonumber(progress) < 1.0
    end)
    local popupEvents = {
        PhoneDialerGameController = { Show = true, Hide = false },
        PhoneMessagePopupGameController = { OnInitialize = true, OnUninitialize = false },
        MessengerDialogViewController = { OnInitialize = true, OnUninitialize = false },
    }
    for controllerName, events in pairs(popupEvents) do
        for eventName, active in pairs(events) do
            local observedController = controllerName
            local observedEvent = eventName
            local observedActive = active
            pcall(function()
                Observe(observedController, observedEvent, function(controller)
                    if observedActive then
                        rememberPopupController(controller)
                    else
                        forgetPopupController(controller)
                    end
                    state.phonePresentationActive = next(state.popupControllers) ~= nil
                    if state.active and observedActive then suppressPopupController(controller) end
                end)
            end)
        end
    end
    pcall(function()
        Observe('HudPhoneMessageController', 'OnInitialize', function(controller)
            rememberPopupController(controller)
            if state.active then suppressPopupController(controller) end
        end)
    end)
    pcall(function()
        Observe('HudPhoneMessageController', 'ShowMessage', function(controller)
            rememberPopupController(controller)
            if state.active then suppressPopupController(controller) end
        end)
    end)
    pcall(function()
        Observe('HudPhoneMessageController', 'OnStateChanged', function(controller)
            rememberPopupController(controller)
            if state.active then suppressPopupController(controller) end
        end)
    end)
    pcall(function()
        Observe('HudPhoneMessageController', 'OnUninitialize', function(controller)
            forgetPopupController(controller)
        end)
    end)
    local messengerEvents = {
        OnInitialize = true,
        SetNotificationData = true,
        OnNotificationResumed = true,
        OnNotificationShown = true,
        OnUninitialize = false,
    }
    for eventName, present in pairs(messengerEvents) do
        local observedEvent = eventName
        local observedPresent = present
        pcall(function()
            Observe('MessengerNotification', observedEvent, function(controller)
                if observedPresent then
                    rememberPopupController(controller)
                    if state.active then suppressPopupController(controller) end
                else
                    forgetPopupController(controller)
                end
            end)
        end)
    end
    local phoneHudEvents = {
        OnInitialize = true,
        OnNotificationsQueueChanged = true,
        PushSMSNotification = true,
        ResolveVisibility = true,
        OnUninitialize = false,
    }
    for eventName, present in pairs(phoneHudEvents) do
        local observedEvent = eventName
        local observedPresent = present
        pcall(function()
            Observe('NewHudPhoneGameController', observedEvent, function(controller)
                if observedPresent then
                    rememberPopupController(controller)
                    if state.active then hideController(controller) end
                else
                    forgetPopupController(controller)
                end
            end)
        end)
    end
    pcall(function()
        Observe('PhoneMessagePopupGameController', 'SetTimeDilatation', function(controller, active)
            if state.active then
                state.phonePresentationActive = active == true
                if active then hideController(controller) end
            end
        end)
    end)
end

registerForEvent('onInit', function()
    config = readJson('config.json')
    if not config then
        config = readJson('config.example.json')
        log('warning', 'config.json missing; using config.example.json')
    end
    if not config then
        log('error', 'no valid config found')
        return
    end
    installObservers()
    writeHeartbeat()
    log('info', 'runtime initialized')
end)

registerForEvent('onUpdate', function(delta)
    if not config then return end
    state.heartbeatElapsed = state.heartbeatElapsed + delta
    if state.heartbeatElapsed >= 0.5 then
        state.heartbeatElapsed = 0.0
        writeHeartbeat()
    end
    if state.command and state.stage ~= 'idle' and not controllerHeartbeatIsAlive() then
        if state.command then failCommand('controller_heartbeat_lost', 'controller heartbeat expired') end
        if state.active then restoreCaptureMode('controller heartbeat lost') end
        state.stage = 'idle'
        state.command = nil
        return
    end
    if state.active then dismissNotifications() end
    pollAck()
    pollCommand()
    beginCaptureWhenGameplayIsReady()
    if state.stage == 'waiting' and state.command then
        state.elapsed = state.elapsed + delta
        if applyGroundSnap() and state.stage == 'waiting' then
            local evidence, ready, actual = buildReadiness()
            if ready then
                state.readyEvidence = { evidence = evidence, actual = actual }
                state.stage = 'armed'
            elseif state.elapsed >= tonumber(config.loading_timeout_seconds or 45) then
                failCommand('streaming_timeout', json.encode(evidence))
            end
        end
    end
end)

registerForEvent('onDraw', function()
    if not config then return end
    state.frame = state.frame + 1
    if state.stage == 'armed' and state.command and state.readyEvidence then
        local evidence = state.readyEvidence.evidence
        evidence.presented_frame = state.frame
        local camera = Game.GetPlayer():GetFPPCameraComponent()
        local actualFov = nil
        pcall(function() actualFov = camera:GetFOV() end)
        writeEvent('ready', {
            readiness = evidence,
            actual_pose = state.readyEvidence.actual,
            effective_pose = state.command.effective_pose,
            actual_fov = actualFov,
            runtime_location = runtimeLocation(),
            teleport_to_ready_ms = state.elapsed * 1000.0,
        })
        state.stage = 'ready'
    end
end)

registerForEvent('onOverlayOpen', function() state.overlayOpen = true end)
registerForEvent('onOverlayClose', function() state.overlayOpen = false end)

registerHotkey(
    'world_location_capture_emergency_restore',
    'World Location Capture: emergency restore',
    function()
        if state.command then failCommand('emergency_restore', 'emergency hotkey pressed') end
        restoreCaptureMode('emergency hotkey')
        state.stage = 'idle'
        state.command = nil
    end
)

registerForEvent('onShutdown', function()
    restoreCaptureMode('CET shutdown or Lua reload')
end)
