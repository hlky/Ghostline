-- In-game location scout for Ghostline gq003, "Black Lantern".

local LOG_PATH = 'black-lantern-locations.json'

local slots = {
    {id = 'iris_safe_site', label = 'Iris briefing / safe site', need = 'Scene access, Mara staging, road and temporary vehicle space', targets = {
        {id = 'site_origin', label = 'Site world origin', role = 'origin'},
        {id = 'briefing_scene', label = 'Briefing scene placement', role = 'scene'},
        {id = 'reconstruction_report', label = 'Reconstruction report terminal', role = 'device'},
        {id = 'safe_site_scene', label = 'Safe-site scene placement', role = 'scene'},
        {id = 'mara_staging', label = 'Mara retained staging', role = 'npc_staging'},
        {id = 'patch_vehicle', label = 'Patch vehicle spawn / boarding', role = 'vehicle'},
    }},
    {id = 'freight_yard', label = 'Freight yard', need = 'Terminal, plant target, access point, guard routes and stealth exits', targets = {
        {id = 'site_origin', label = 'Site world origin', role = 'origin'},
        {id = 'approach_trigger', label = 'Yard approach / reach trigger', role = 'trigger'},
        {id = 'security_encounter', label = 'Yard security encounter / patrols', role = 'patrol'},
        {id = 'transfer_board', label = 'Clue: transfer board', role = 'clue'},
        {id = 'neural_stabilizers', label = 'Clue: neural stabilizers', role = 'clue'},
        {id = 'restraint_case', label = 'Clue: restraint case', role = 'clue'},
        {id = 'beacon_mount', label = 'Routing beacon mount', role = 'device'},
        {id = 'dispatch_relay', label = 'Dispatch access point', role = 'device'},
        {id = 'cleanup_boundary', label = 'Yard exit / cleanup boundary', role = 'cleanup_boundary'},
    }},
    {id = 'memory_clinic', label = 'Memory clinic', need = 'Lockable door, Mara release, three escort gates, cover and defense anchors', targets = {
        {id = 'site_origin', label = 'Site world origin', role = 'origin'},
        {id = 'approach_trigger', label = 'Clinic approach / reach trigger', role = 'trigger'},
        {id = 'security_encounter', label = 'Clinic security encounter', role = 'patrol'},
        {id = 'neural_jammer', label = 'Neural jammer access point', role = 'device'},
        {id = 'mara_restraint', label = 'Mara restraint / release device', role = 'device'},
        {id = 'escort_gate_01', label = 'Mara escort gate 1', role = 'route_gate'},
        {id = 'escort_gate_02', label = 'Mara escort gate 2', role = 'route_gate'},
        {id = 'escort_gate_03', label = 'Mara escort gate 3', role = 'route_gate'},
        {id = 'stabilization_defense', label = 'Mara stabilization / defense', role = 'npc_staging'},
    }},
    {id = 'freight_interchange', label = 'Freight interchange', need = 'Drivable approach, parking and unobstructed carrier theft', targets = {
        {id = 'site_origin', label = 'Site world origin', role = 'origin'},
        {id = 'arrival_trigger', label = 'Patch drive arrival trigger', role = 'trigger'},
        {id = 'patch_vehicle_stop', label = 'Patch vehicle stop / cleanup', role = 'vehicle'},
        {id = 'pair_07b_parking', label = 'Pair 07-B carrier parking', role = 'vehicle'},
        {id = 'carrier_departure', label = 'Carrier departure route', role = 'route_gate'},
    }},
    {id = 'reconstruction_relay', label = 'Reconstruction relay', need = 'Access point/antenna, carrier parking, combat, three clues and cleanup route', targets = {
        {id = 'site_origin', label = 'Site world origin', role = 'origin'},
        {id = 'carrier_parking', label = 'Pair 07-B relay parking', role = 'vehicle'},
        {id = 'entrance_trigger', label = 'Relay entrance trigger', role = 'trigger'},
        {id = 'retrieval_encounter', label = 'Retrieval-team encounter / staging', role = 'patrol'},
        {id = 'carrier_rack', label = 'Clue: carrier rack', role = 'clue'},
        {id = 'reconstruction_core_clue', label = 'Clue: reconstruction core', role = 'clue'},
        {id = 'courier_ledger', label = 'Clue: courier ledger', role = 'clue'},
        {id = 'core_device', label = 'Outcome reconstruction-core device', role = 'device'},
        {id = 'cleanup_boundary', label = 'Relay exit / cleanup boundary', role = 'cleanup_boundary'},
    }},
    {id = 'delivery', label = 'Delivery drop point', need = 'Kabuki drop_point_009 or reviewed native deposit alternative', targets = {
        {id = 'site_origin', label = 'Site world origin', role = 'origin'},
        {id = 'drop_point', label = 'Package deposit interaction', role = 'device'},
    }},
}

-- Additional placements are separate checklist entries; repeatable targets can
-- hold any number of labelled patrol/route points without imposing an AI layout.
local extras = {
    iris_safe_site = {
        {'briefing_setup', 'Briefing setup trigger', 'trigger'},
        {'briefing_iris', 'Briefing Iris spawn / AI spot', 'npc_staging'},
        {'safe_site_setup', 'Safe-site setup trigger', 'trigger'},
        {'safe_site_iris', 'Safe-site Iris spawn / AI spot', 'npc_staging'},
        {'patch_staging', 'Patch spawn / boarding AI spot', 'npc_staging'},
        {'scene_proximity', 'Scene mood / awareness / engage boundaries (label each)', 'trigger'},
        {'patch_drive_route', 'Patch drive route points (label in order)', 'route_gate'},
    },
    freight_yard = {
        {'guard_spawn', 'Guard spawn points (label each guard)', 'npc_staging'},
        {'guard_patrol', 'Guard patrol points (label guard and order)', 'patrol'},
        {'stealth_boundary', 'Stealth encounter boundary', 'trigger'},
    },
    memory_clinic = {
        {'mara_spawn', 'Mara initial spawn / restraint AI spot', 'npc_staging'},
        {'guard_spawn', 'Clinic guard spawn points (label each guard)', 'npc_staging'},
        {'guard_patrol', 'Clinic guard patrol points (label guard and order)', 'patrol'},
        {'defense_attacker_spawn', 'Defense attacker spawn points (label each)', 'npc_staging'},
        {'defense_attacker_route', 'Defense attacker approach points (label in order)', 'route_gate'},
        {'defense_checkpoint', 'Pre-defense checkpoint player position', 'approach'},
    },
    freight_interchange = {
        {'carrier_route', 'Carrier drive route points (label in order)', 'route_gate'},
    },
    reconstruction_relay = {
        {'retrieval_spawn', 'Retrieval team spawn points (label each member)', 'npc_staging'},
        {'retrieval_patrol', 'Retrieval team patrol / approach points', 'patrol'},
    },
}
for _, slot in ipairs(slots) do
    for _, extra in ipairs(extras[slot.id] or {}) do
        table.insert(slot.targets, {id = extra[1], label = extra[2], role = extra[3]})
    end
    table.insert(slot.targets, {id = 'mappin', label = 'Quest mappin markers (label objective)', role = 'mappin'})
end

-- Conversation scouting leads, NOT validated spawn positions or accepted origins.
local presets = {
    {site = 'iris_safe_site', label = 'Iris Japantown rooftop', position = {x = -406.10, y = 724.73, z = 127}, note = 'Previously suggested Iris site; verify road access and Mara staging.'},
    {site = 'freight_yard', label = 'Anonymous Northside yard', position = {x = -2040, y = 2665, z = 18}, note = 'Approximate Northside industrial-lot lead from our discussion; identity and ground height need review. Separate from Ebunike.'},
    {site = 'freight_yard', label = 'Ebunike docks entrance (alternative)', position = {x = -1481, y = 2957, z = 7}, note = 'Published dock arrival coordinates, rounded. Check Chippin In ownership and access in your save.'},
    {site = 'freight_yard', label = 'Ebunike ship landmark (elevated)', position = {x = -1533, y = 3090, z = 20}, note = 'World-index antenna landmark, NOT a verified standing position. Elevated exploration only.'},
    {site = 'memory_clinic', label = 'Provisional medical-site lead', position = {x = -1021.21, y = 1442.01, z = 16.47}, note = 'Earlier coordinate suggestion; clinic identity, cells and access remain unverified. Not confirmed as either mission clinic discussed.'},
    {site = 'freight_interchange', label = 'Arroyo freight interchange search area', position = {x = -670, y = -920, z = 8}, note = 'Approximate search centre, not a selected lot. Explore X -740 to -600, Y -970 to -840; check ground and vanilla activity.'},
    {site = 'reconstruction_relay', label = 'Vista del Rey relay lead', position = {x = -669, y = -409, z = 15.6}, note = 'Earlier access-point scouting lead; verify ground height, carrier access and combat space.'},
    {site = 'delivery', label = 'Kabuki drop_point_009', position = {x = -1168.663, y = 1309.517, z = 19.977}, note = 'Previously runtime-confirmed provisional delivery target; verify arrival pose in this save.'},
}

local roles = {
    {id = 'mappin', label = 'Quest mappin'},
    {id = 'origin', label = 'World origin'},
    {id = 'approach', label = 'Approach / entry'},
    {id = 'trigger', label = 'Trigger'},
    {id = 'device', label = 'Device'},
    {id = 'clue', label = 'Clue'},
    {id = 'npc_staging', label = 'NPC staging'},
    {id = 'patrol', label = 'Patrol point'},
    {id = 'route_gate', label = 'Route / escort gate'},
    {id = 'vehicle', label = 'Vehicle / parking'},
    {id = 'scene', label = 'Scene placement'},
    {id = 'cleanup_boundary', label = 'Cleanup boundary'},
    {id = 'misc', label = 'Other'},
}

local state = {
    overlayOpen = false,
    slotIndex = 1,
    targetIndex = 1,
    roleIndex = 2,
    loadFailed = false,
    captures = {},
    selected = nil,
    nextId = 1,
    label = '',
    notes = '',
    previousPose = nil,
    status = 'Ready',
}

local function log(level, message)
    local text = '[ghostline_gq003_scout] ' .. tostring(message)
    if spdlog and spdlog[level] then spdlog[level](text) else print(text) end
end

local function writeJsonAtomic(path, value)
    local temporary = path .. '.tmp'
    local ok, payload = pcall(function() return json.encode(value) end)
    if not ok then return false, tostring(payload) end
    local file = io.open(temporary, 'w')
    if not file then return false, 'cannot open ' .. temporary end
    local wrote, writeError = file:write(payload)
    local flushed, flushError = file:flush()
    local closed, closeError = file:close()
    if not wrote or not flushed or not closed then
        return false, tostring(writeError or flushError or closeError)
    end
    local existing = io.open(path, 'r')
    if existing then
        existing:close()
        -- Find a fresh backup name; never overwrite an earlier recovery copy.
        local index, backup = 1, path .. '.bak.1'
        while true do
            local previous = io.open(backup, 'r')
            if not previous then break end
            previous:close()
            index = index + 1
            backup = path .. '.bak.' .. index
        end
        local moved, moveError = os.rename(path, backup)
        if not moved then return false, tostring(moveError) end
        local installed, installError = os.rename(temporary, path)
        if not installed then
            os.rename(backup, path)
            return false, 'Replacement failed; recovery copies retained: ' .. tostring(installError)
        end
        return true, nil
    end
    local renamed, err = os.rename(temporary, path)
    if not renamed then return false, tostring(err) end
    return true, nil
end

local function document()
    return {
        schema_version = 1,
        quest = 'gq003',
        title = 'Black Lantern',
        captured_by = 'ghostline_gq003_scout',
        next_id = state.nextId,
        captures = state.captures,
    }
end

local function save()
    if state.loadFailed then state.status = 'Saving blocked: repair the existing log and reload CET' return false end
    local ok, err = writeJsonAtomic(LOG_PATH, document())
    if not ok then
        state.status = 'Save failed: ' .. tostring(err)
        log('error', state.status)
        return false
    end
    return true
end

local function load()
    local file, openError, openCode = io.open(LOG_PATH, 'r')
    if not file then
        local recovery = io.open(LOG_PATH .. '.bak.1', 'r') or io.open(LOG_PATH .. '.tmp', 'r')
        if recovery or (openCode and openCode ~= 2) then
            if recovery then recovery:close() end
            state.loadFailed = true
            state.status = 'Log unavailable; saving blocked. Restore a recovery file or repair access, then reload CET: ' .. tostring(openError)
            return
        end
        state.status = 'New scout log'
        return
    end
    local contents = file:read('*a')
    file:close()
    local ok, value = pcall(function() return json.decode(contents) end)
    local valid = ok and type(value) == 'table' and value.schema_version == 1 and value.quest == 'gq003' and type(value.captures) == 'table'
    if valid then
        for _, capture in pairs(value.captures) do
            if type(capture) ~= 'table' or type(capture.position) ~= 'table' or type(capture.id) ~= 'string' then valid = false break end
            for _, axis in ipairs({'x', 'y', 'z'}) do
                local n = capture.position[axis]
                if type(n) ~= 'number' or n ~= n or math.abs(n) == math.huge then valid = false break end
            end
            if not valid then break end
        end
    end
    if not valid then
        state.loadFailed = true
        state.status = 'Existing scout log is malformed or unsupported; it was not changed'
        log('error', state.status)
        return
    end
    state.captures = value.captures
    state.loadFailed = false
    state.nextId = math.max(tonumber(value.next_id) or (#state.captures + 1), #state.captures + 1)
    state.status = ('Loaded %d captures'):format(#state.captures)
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

local function inspectorNumber(value, key)
    if value == nil then return nil end
    local ok, result = pcall(function() return tonumber(value[key]) end)
    return ok and result or nil
end

local function inspectorString(value)
    if value == nil then return nil end
    local result = tostring(value)
    return result ~= '' and result or nil
end

local function inspectorVector(value)
    if value == nil then return nil end
    local x, y, z = inspectorNumber(value, 'x'), inspectorNumber(value, 'y'), inspectorNumber(value, 'z')
    if x == nil or y == nil or z == nil then return nil end
    return {x = x, y = y, z = z, w = inspectorNumber(value, 'w')}
end

local function inspectorQuaternion(value)
    if value == nil then return nil end
    local i, j = inspectorNumber(value, 'i'), inspectorNumber(value, 'j')
    local k, r = inspectorNumber(value, 'k'), inspectorNumber(value, 'r')
    if i == nil or j == nil or k == nil or r == nil then return nil end
    return {i = i, j = j, k = k, r = r}
end

local function inspectedTarget()
    local redHotTools = GetMod and GetMod('RedHotTools') or nil
    if not redHotTools or type(redHotTools.GetWorldInspectorTarget) ~= 'function' then return nil end
    local target = redHotTools.GetWorldInspectorTarget()
    if type(target) ~= 'table' then return nil end
    return {
        sector = inspectorString(target.sectorPath),
        node_index = tonumber(target.nodeIndex),
        node_type = inspectorString(target.nodeType),
        node_id = inspectorString(target.nodeID),
        node_ref = inspectorString(target.nodeRef),
        debug_name = inspectorString(target.debugName),
        entity_template = inspectorString(target.templatePath),
        entity_appearance = inspectorString(target.appearanceName),
        node_position = inspectorVector(target.nodePosition),
        node_orientation = inspectorQuaternion(target.nodeOrientation),
        entity_position = inspectorVector(target.entityPosition),
        entity_orientation = inspectorQuaternion(target.entityOrientation),
    }
end

local function playerPose()
    local player = Game.GetPlayer()
    if not player then return nil end
    local position = player:GetWorldPosition()
    local forward = player:GetWorldForward()
    if not position or not forward then return nil end
    local yaw = math.deg(math.atan2(-forward.x, forward.y))
    if yaw < 0 then yaw = yaw + 360.0 end
    return {
        position = {x = position.x, y = position.y, z = position.z},
        orientation = {yaw = yaw, pitch = 0.0, roll = 0.0},
        forward = {x = forward.x, y = forward.y, z = forward.z},
    }
end

local function countForTarget(slotId, targetId)
    local count = 0
    for _, capture in ipairs(state.captures) do
        if capture.slot_id == slotId and capture.target_id == targetId then count = count + 1 end
    end
    return count
end

local function captureCurrent()
    if state.loadFailed then state.status = 'Capture blocked: repair the existing log and reload CET' return end
    local pose = playerPose()
    if not pose then state.status = 'Player position unavailable' return end
    local slot = slots[state.slotIndex]
    local target = slot.targets[state.targetIndex]
    local role = roles[state.roleIndex]
    local sequence = state.nextId
    local label = state.label
    if label == '' then label = ('%s candidate %d'):format(target.label, countForTarget(slot.id, target.id) + 1) end
    local capture = {
        id = ('gq003-%03d'):format(sequence),
        slot_id = slot.id,
        slot_label = slot.label,
        target_id = target.id,
        target_label = target.label,
        role_id = role.id,
        role_label = role.label,
        label = label,
        notes = state.notes,
        review = 'candidate',
        captured_at = os.date('!%Y-%m-%dT%H:%M:%SZ'),
        position = pose.position,
        orientation = pose.orientation,
        forward = pose.forward,
        runtime_location = runtimeLocation(),
        inspected_target = inspectedTarget(),
    }
    table.insert(state.captures, capture)
    state.selected = #state.captures
    state.nextId = sequence + 1
    if save() then
        state.label = ''
        state.notes = ''
        state.status = ('Captured %s at %.3f, %.3f, %.3f'):format(capture.id, pose.position.x, pose.position.y, pose.position.z)
        log('info', state.status)
    end
end

local function teleport(pose)
    local player = Game.GetPlayer()
    local facility = Game.GetTeleportationFacility()
    if not player or not facility or not pose or not pose.position then
        state.status = 'Teleport target unavailable'
        return false
    end
    local angle = pose.orientation or {roll = 0, pitch = 0, yaw = 0}
    local ok, err = pcall(function()
        facility:Teleport(player, Vector4.new(pose.position.x, pose.position.y, pose.position.z + 0.25, 1.0), EulerAngles.new(angle.roll or 0, angle.pitch or 0, angle.yaw or 0))
    end)
    if not ok then state.status = 'Teleport failed: ' .. tostring(err) return false end
    return true
end

local function teleportSelected()
    local capture = state.selected and state.captures[state.selected] or nil
    if not capture then state.status = 'No capture selected' return end
    local origin = playerPose()
    if teleport(capture) then state.previousPose = origin state.status = 'Teleported to ' .. capture.id end
end

local function returnToPrevious()
    if not state.previousPose then state.status = 'No previous position' return end
    local destination = state.previousPose
    local origin = playerPose()
    if teleport(destination) then state.previousPose = origin state.status = 'Returned to previous position' end
end

local function copyValue(value, description)
    local ok, payload = pcall(function() return json.encode(value) end)
    if not ok then state.status = 'JSON encoding failed: ' .. tostring(payload) return end
    ImGui.SetClipboardText(payload)
    state.status = description
end

local function setReview(value)
    if state.loadFailed then return end
    local capture = state.selected and state.captures[state.selected] or nil
    if not capture then return end
    capture.review = value
    if save() then state.status = capture.id .. ' marked ' .. value end
end

local function drawSlotButtons()
    for index, slot in ipairs(slots) do
        if index > 1 and index ~= 4 then ImGui.SameLine() end
        local prefix = state.slotIndex == index and '[x] ' or ''
        if ImGui.Button(prefix .. slot.label .. '##slot' .. index) then
            state.slotIndex = index
            state.targetIndex = 1
            local defaultRole = slot.targets[1].role
            for roleIndex, role in ipairs(roles) do
                if role.id == defaultRole then state.roleIndex = roleIndex break end
            end
        end
    end
end


local function drawTargetList(slot)
    ImGui.BeginChild('##gq003TargetList', 0, 145, true)
    for index, target in ipairs(slot.targets) do
        local count = countForTarget(slot.id, target.id)
        local label = ('%s %s (%d)##target%d'):format(count > 0 and '[captured]' or '[missing]', target.label, count, index)
        if ImGui.Selectable(label, state.targetIndex == index) then
            state.targetIndex = index
            for roleIndex, role in ipairs(roles) do
                if role.id == target.role then state.roleIndex = roleIndex break end
            end
        end
    end
    ImGui.EndChild()
end


local function drawRoleButtons()
    for index, role in ipairs(roles) do
        if index > 1 and ((index - 1) % 4) ~= 0 then ImGui.SameLine() end
        local prefix = state.roleIndex == index and '[x] ' or ''
        if ImGui.Button(prefix .. role.label .. '##role' .. index) then state.roleIndex = index end
    end
end

local function drawWindow()
    ImGui.SetNextWindowSize(820, 820, ImGuiCond.FirstUseEver)
    if not ImGui.Begin('Ghostline: Black Lantern Scout') then ImGui.End() return end
    ImGui.TextWrapped(state.status)
    ImGui.Separator()
    ImGui.Text('Capture for:')
    drawSlotButtons()
    local slot = slots[state.slotIndex]
    ImGui.TextWrapped('Review: ' .. slot.need)
    if ImGui.CollapsingHeader('Suggested exploration destinations') then
        ImGui.TextWrapped('Provisional leads: verify access and ground height. Teleporting does not capture or approve a location.')
        for index, preset in ipairs(presets) do
            if preset.site == slot.id then
                if ImGui.Button('Explore: ' .. preset.label .. '##preset' .. index) then
                    local origin = playerPose()
                    if teleport(preset) then state.previousPose = origin state.status = 'Exploring ' .. preset.label end
                end
                ImGui.TextWrapped(preset.note)
                ImGui.Text(('XYZ %.3f, %.3f, %.3f'):format(preset.position.x, preset.position.y, preset.position.z))
            end
        end
        if ImGui.Button('Return from exploration') then returnToPrevious() end
    end
    ImGui.Text(('Quest placement target (%d in this site):'):format(#slot.targets))
    drawTargetList(slot)
    ImGui.Text('Authoring role:')
    drawRoleButtons()
    local label, labelChanged = ImGui.InputTextWithHint('##gq003Label', 'Candidate label (optional)', state.label, 160)
    if labelChanged then state.label = label end
    local notes, notesChanged = ImGui.InputTextWithHint('##gq003Notes', 'Notes: access, ownership risks, routes, anchors...', state.notes, 500)
    if notesChanged then state.notes = notes end
    if ImGui.Button('Capture player pose') then captureCurrent() end
    ImGui.SameLine()
    if ImGui.Button('Copy current pose JSON') then copyValue(playerPose() or {}, 'Copied current player pose') end
    ImGui.SameLine()
    if ImGui.Button('Copy complete log JSON') then copyValue(document(), 'Copied complete scout log') end

    ImGui.Separator()
    ImGui.Text(('%d captures'):format(#state.captures))
    ImGui.BeginChild('##gq003CaptureList', 0, 190, true)
    for index, capture in ipairs(state.captures) do
        local marker = capture.review == 'selected' and '[SELECTED] ' or (capture.review == 'shortlisted' and '[SHORT] ' or (capture.review == 'rejected' and '[NO] ' or ''))
        local labelText = ('%s%s | %s | %s | %s##capture%d'):format(marker, capture.id, capture.slot_label or capture.slot_id, capture.target_label or capture.target_id or capture.role_label or capture.role_id or 'origin', capture.label or '', index)
        if ImGui.Selectable(labelText, state.selected == index) then
            state.selected = index
            for slotIndex, candidateSlot in ipairs(slots) do
                if candidateSlot.id == capture.slot_id then
                    state.slotIndex = slotIndex
                    state.targetIndex = 1
                    for targetIndex, candidateTarget in ipairs(candidateSlot.targets) do
                        if candidateTarget.id == capture.target_id then state.targetIndex = targetIndex break end
                    end
                    break
                end
            end
            for roleIndex, candidateRole in ipairs(roles) do
                if candidateRole.id == (capture.role_id or 'origin') then state.roleIndex = roleIndex break end
            end
        end
    end
    ImGui.EndChild()

    local selected = state.selected and state.captures[state.selected] or nil
    if selected then
        local place = selected.runtime_location or {}
        ImGui.TextWrapped(('%s | %s | %s'):format(selected.review or 'candidate', place.named_area or place.subdistrict or place.district or 'unknown area', place.interior_state or 'unknown'))
        ImGui.Text(('XYZ %.3f, %.3f, %.3f | yaw %.2f'):format(selected.position.x, selected.position.y, selected.position.z, (selected.orientation or {}).yaw or 0))
        ImGui.TextWrapped(selected.notes ~= '' and selected.notes or '(no notes)')
        if selected.inspected_target then
            ImGui.TextWrapped(('Inspector: %s | node %s | %s'):format(selected.inspected_target.sector or '?', selected.inspected_target.node_index or '?', selected.inspected_target.node_type or '?'))
        end
    end

    if ImGui.Button('Teleport selected') then teleportSelected() end
    ImGui.SameLine()
    if ImGui.Button('Return') then returnToPrevious() end
    ImGui.SameLine()
    if ImGui.Button('Copy selected JSON') and selected then copyValue(selected, 'Copied ' .. selected.id) end
    if ImGui.Button('Candidate') then setReview('candidate') end
    ImGui.SameLine()
    if ImGui.Button('Shortlist') then setReview('shortlisted') end
    ImGui.SameLine()
    if ImGui.Button('Select candidate') then setReview('selected') end
    ImGui.SameLine()
    if ImGui.Button('Reject') then setReview('rejected') end
    ImGui.End()
end

registerForEvent('onInit', load)
registerForEvent('onOverlayOpen', function() state.overlayOpen = true end)
registerForEvent('onOverlayClose', function() state.overlayOpen = false end)
registerForEvent('onDraw', function() if state.overlayOpen then drawWindow() end end)

registerHotkey('ghostline_gq003_capture', 'Black Lantern Scout: capture current location', captureCurrent)
registerHotkey('ghostline_gq003_teleport', 'Black Lantern Scout: teleport selected', teleportSelected)
registerHotkey('ghostline_gq003_return', 'Black Lantern Scout: return to previous position', returnToPrevious)
