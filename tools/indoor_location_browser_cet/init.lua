-- Standalone browser for Ghostline's offline indoor-location candidate catalog.

local state = {
    overlayOpen = false,
    locations = {},
    filtered = {},
    selected = nil,
    query = '',
    ownership = 'likely_unowned',
    minimumScore = 0,
    hideRetail = true,
    hideRejected = true,
    favoritesOnly = false,
    zOffset = 0.5,
    previousPosition = nil,
    reviews = {},
    status = 'Not loaded',
}

local function log(level, message)
    local text = '[ghostline_indoor_locations] ' .. tostring(message)
    if spdlog and spdlog[level] then spdlog[level](text) else print(text) end
end

local function readJson(path)
    local file = io.open(path, 'r')
    if not file then return nil, 'cannot open ' .. path end
    local contents = file:read('*a')
    file:close()
    local ok, value = pcall(function() return json.decode(contents) end)
    if not ok or type(value) ~= 'table' then return nil, 'malformed JSON in ' .. path end
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
    os.remove(path)
    local renamed, err = os.rename(temporary, path)
    if not renamed then os.remove(temporary) return false, tostring(err) end
    return true, nil
end

local function inspectorNumber(value, key)
    if value == nil then return nil end
    local ok, result = pcall(function() return tonumber(value[key]) end)
    return ok and result or nil
end

local function inspectorVector(value)
    if value == nil then return nil end
    local x, y, z = inspectorNumber(value, 'x'), inspectorNumber(value, 'y'), inspectorNumber(value, 'z')
    if x == nil or y == nil or z == nil then return nil end
    return {x = x, y = y, z = z, w = inspectorNumber(value, 'w')}
end

local function inspectorQuaternion(value)
    if value == nil then return nil end
    local i, j, k, r = inspectorNumber(value, 'i'), inspectorNumber(value, 'j'), inspectorNumber(value, 'k'), inspectorNumber(value, 'r')
    if i == nil or j == nil or k == nil or r == nil then return nil end
    return {i = i, j = j, k = k, r = r}
end

local function inspectorString(value)
    if value == nil then return nil end
    local result = tostring(value)
    return result ~= '' and result or nil
end

local function copyWorldInspectorTarget()
    local redHotTools = GetMod and GetMod('RedHotTools') or nil
    if not redHotTools or type(redHotTools.GetWorldInspectorTarget) ~= 'function' then
        state.status = 'RedHotTools World Inspector API unavailable'
        return
    end

    local target = redHotTools.GetWorldInspectorTarget()
    if type(target) ~= 'table' then
        state.status = 'No World Inspector target selected'
        return
    end

    local capture = {
        schema_version = 1,
        captured_by = 'ghostline_indoor_locations',
        removal = {
            sector = inspectorString(target.sectorPath),
            expected_nodes = tonumber(target.nodeCount),
            index = tonumber(target.nodeIndex),
            type = inspectorString(target.nodeType),
        },
        node = {
            id = inspectorString(target.nodeID),
            ref = inspectorString(target.nodeRef),
            position = inspectorVector(target.nodePosition),
            orientation = inspectorQuaternion(target.nodeOrientation),
            instance_index = tonumber(target.instanceIndex),
            instance_count = tonumber(target.instanceCount),
            debug_name = inspectorString(target.debugName),
            source_prefab_hash = inspectorString(target.sourcePrefabHash),
            collision_actor_index = tonumber(target.actorIndex),
            collision_actor_count = tonumber(target.actorCount),
            collision_shape_index = tonumber(target.shapeIndex),
            collision_shape_count = tonumber(target.shapeCount),
        },
        entity = {
            type = inspectorString(target.entityType),
            id = inspectorString(target.entityID),
            template = inspectorString(target.templatePath),
            appearance = inspectorString(target.appearanceName),
            position = inspectorVector(target.entityPosition),
            orientation = inspectorQuaternion(target.entityOrientation),
        },
        component = {
            type = inspectorString(target.componentType),
            name = inspectorString(target.componentName),
        },
    }

    local ok, payload = pcall(function() return json.encode(capture) end)
    if not ok then
        state.status = 'Could not encode World Inspector target: ' .. tostring(payload)
        return
    end
    ImGui.SetClipboardText(payload)
    state.status = ('Copied World Inspector node %s as JSON'):format(capture.removal.index or '?')
end

local function saveReviews()
    local ok, err = writeJsonAtomic('reviews.json', {schema_version = 1, reviews = state.reviews})
    if not ok then state.status = 'Could not save reviews: ' .. tostring(err) log('error', state.status) end
end

local function loadReviews()
    local document = readJson('reviews.json')
    if document and document.schema_version == 1 and type(document.reviews) == 'table' then
        state.reviews = document.reviews
    else
        state.reviews = {}
    end
end

local function folded(value) return string.lower(tostring(value or '')) end

local function locationSearchText(location)
    local questIds = table.concat(location.quest_ids or {}, ' ')
    return folded(table.concat({location.id, location.name, location.ownership, location.sector, questIds}, ' '))
end

local function applyFilters()
    state.filtered = {}
    local query = folded(state.query)
    for index, location in ipairs(state.locations) do
        local ownershipMatches = state.ownership == 'all' or location.ownership == state.ownership
        local scoreMatches = tonumber(location.score or 0) >= state.minimumScore
        local queryMatches = query == '' or string.find(locationSearchText(location), query, 1, true) ~= nil
        local review = state.reviews[location.id]
        local retailMatches = not state.hideRetail or location.retail ~= true
        local reviewMatches = (not state.hideRejected or review ~= 'rejected') and (not state.favoritesOnly or review == 'favorite')
        if ownershipMatches and scoreMatches and queryMatches and retailMatches and reviewMatches then table.insert(state.filtered, index) end
    end
    if #state.filtered == 0 then
        state.selected = nil
    elseif not state.selected then
        state.selected = state.filtered[1]
    else
        local visible = false
        for _, index in ipairs(state.filtered) do
            if index == state.selected then visible = true break end
        end
        if not visible then state.selected = state.filtered[1] end
    end
end

local function loadLocations()
    loadReviews()
    local document, err = readJson('locations.json')
    if not document then
        state.locations = {}
        state.status = err
        log('error', err)
        applyFilters()
        return
    end
    if document.schema_version ~= 1 or type(document.locations) ~= 'table' then
        state.locations = {}
        state.status = 'Unsupported locations.json schema'
        log('error', state.status)
        applyFilters()
        return
    end
    state.locations = document.locations
    state.status = ('Loaded %d locations'):format(#state.locations)
    applyFilters()
    log('info', state.status)
end

local playerPosition

local function selectNearestToPlayer()
    local position = playerPosition()
    if not position then state.status = 'Player unavailable' return end
    local bestIndex = nil
    local bestDistance = nil
    for index, location in ipairs(state.locations) do
        local dx, dy, dz = location.x - position.x, location.y - position.y, location.z - position.z
        local candidateDistance = math.sqrt(dx * dx + dy * dy + dz * dz)
        if not bestDistance or candidateDistance < bestDistance then
            bestDistance = candidateDistance
            bestIndex = index
        end
    end
    if bestIndex then
        state.query = ''
        state.ownership = 'all'
        state.hideRetail = false
        state.hideRejected = false
        state.favoritesOnly = false
        applyFilters()
        state.selected = bestIndex
        state.status = ('Selected nearest candidate at %.2fm'):format(bestDistance)
    end
end

playerPosition = function()
    local player = Game.GetPlayer()
    if not player then return nil end
    local position = player:GetWorldPosition()
    if not position then return nil end
    return {x = position.x, y = position.y, z = position.z}
end

local function teleportPosition(position)
    local player = Game.GetPlayer()
    local facility = Game.GetTeleportationFacility()
    if not player or not facility then
        state.status = 'Player or teleportation facility unavailable'
        return false
    end
    local ok, err = pcall(function()
        facility:Teleport(player, Vector4.new(position.x, position.y, position.z, 1.0), EulerAngles.new(0, 0, 0))
    end)
    if not ok then
        state.status = 'Teleport failed: ' .. tostring(err)
        log('error', state.status)
        return false
    end
    state.status = ('Teleported to %.2f, %.2f, %.2f'):format(position.x, position.y, position.z)
    return true
end

local function teleportSelected()
    local location = state.selected and state.locations[state.selected] or nil
    if not location then state.status = 'No location selected' return end
    local origin = playerPosition()
    if teleportPosition({x = location.x, y = location.y, z = location.z + state.zOffset}) then
        state.previousPosition = origin
    end
end

local function selectRelative(delta)
    if #state.filtered == 0 then return end
    local position = 1
    for index, sourceIndex in ipairs(state.filtered) do
        if sourceIndex == state.selected then position = index break end
    end
    position = ((position - 1 + delta) % #state.filtered) + 1
    state.selected = state.filtered[position]
end

local function drawOwnershipButton(value, label)
    if state.ownership == value then ImGui.BeginDisabled() end
    local pressed = ImGui.Button(label)
    if state.ownership == value then ImGui.EndDisabled() end
    if pressed then state.ownership = value applyFilters() end
end

local function toggleButton(active, label)
    return ImGui.Button((active and '[x] ' or '[ ] ') .. label)
end

local function drawWindow()
    ImGui.SetNextWindowSize(760, 620, ImGuiCond.FirstUseEver)
    if not ImGui.Begin('Ghostline Indoor Locations') then ImGui.End() return end

    ImGui.Text(state.status)
    local query, queryChanged = ImGui.InputTextWithHint('##indoorSearch', 'Search name, sector, ID, or quest...', state.query, 200)
    if queryChanged then state.query = query applyFilters() end

    drawOwnershipButton('likely_unowned', 'Likely unowned')
    ImGui.SameLine()
    drawOwnershipButton('quest_linked', 'Quest linked')
    ImGui.SameLine()
    drawOwnershipButton('all', 'All')
    ImGui.SameLine()
    if ImGui.Button('Reload JSON') then loadLocations() end

    if toggleButton(state.hideRetail, 'Hide retail/services') then state.hideRetail = not state.hideRetail applyFilters() end
    ImGui.SameLine()
    if toggleButton(state.hideRejected, 'Hide rejected') then state.hideRejected = not state.hideRejected applyFilters() end
    ImGui.SameLine()
    if toggleButton(state.favoritesOnly, 'Favorites only') then state.favoritesOnly = not state.favoritesOnly applyFilters() end

    local minimumScore, scoreChanged = ImGui.InputInt('Minimum score', state.minimumScore, 1, 10, ImGuiInputTextFlags.None)
    if scoreChanged then state.minimumScore = math.max(0, math.min(100, minimumScore)) applyFilters() end
    local zOffset, zChanged = ImGui.InputFloat('Teleport Z offset', state.zOffset, 0.25, 1.0, '%.2f')
    if zChanged then state.zOffset = zOffset end
    ImGui.Text(('%d shown / %d total'):format(#state.filtered, #state.locations))

    ImGui.BeginChild('##indoorList', 0, 310, true)
    for _, sourceIndex in ipairs(state.filtered) do
        local location = state.locations[sourceIndex]
        local review = state.reviews[location.id]
        local marker = review == 'favorite' and '[FAV] ' or (review == 'rejected' and '[NO] ' or '')
        local label = ('[%d] %s%s (%s)##%s'):format(location.score or 0, marker, location.name or location.id, location.site_type or 'unclassified', location.id)
        if ImGui.Selectable(label, state.selected == sourceIndex) then state.selected = sourceIndex end
    end
    ImGui.EndChild()

    local selected = state.selected and state.locations[state.selected] or nil
    if selected then
        ImGui.TextWrapped(('%s | %s | %s | score %d'):format(selected.id, selected.ownership, selected.site_type or 'unclassified', selected.score or 0))
        ImGui.TextWrapped(selected.sector or '')
        ImGui.Text(('XYZ %.3f, %.3f, %.3f'):format(selected.x, selected.y, selected.z))
        if selected.quest_ids and #selected.quest_ids > 0 then
            ImGui.TextWrapped('Vanilla IDs: ' .. table.concat(selected.quest_ids, ', '))
        end
    end

    if ImGui.Button('Previous') then selectRelative(-1) end
    ImGui.SameLine()
    if ImGui.Button('Teleport selected') then teleportSelected() end
    ImGui.SameLine()
    if ImGui.Button('Next') then selectRelative(1) end
    ImGui.SameLine()
    if not state.previousPosition then ImGui.BeginDisabled() end
    local returnPressed = ImGui.Button('Return')
    if not state.previousPosition then ImGui.EndDisabled() end
    if returnPressed and state.previousPosition then
        local destination = state.previousPosition
        state.previousPosition = playerPosition()
        teleportPosition(destination)
    end
    if ImGui.Button('Nearest to player') then selectNearestToPlayer() end
    ImGui.SameLine()
    if ImGui.Button('Copy inspected node JSON') then copyWorldInspectorTarget() end

    local selectedReview = selected and state.reviews[selected.id] or nil
    if ImGui.Button(selectedReview == 'favorite' and 'Unfavorite' or 'Favorite') and selected then
        state.reviews[selected.id] = selectedReview == 'favorite' and nil or 'favorite'
        saveReviews()
        applyFilters()
    end
    ImGui.SameLine()
    if ImGui.Button(selectedReview == 'rejected' and 'Undo reject' or 'Reject') and selected then
        state.reviews[selected.id] = selectedReview == 'rejected' and nil or 'rejected'
        saveReviews()
        applyFilters()
    end
    ImGui.End()
end

registerForEvent('onInit', loadLocations)
registerForEvent('onOverlayOpen', function() state.overlayOpen = true end)
registerForEvent('onOverlayClose', function() state.overlayOpen = false end)
registerForEvent('onDraw', function() if state.overlayOpen then drawWindow() end end)

registerHotkey('ghostline_indoor_teleport', 'Ghostline indoors: teleport selected', teleportSelected)
registerHotkey('ghostline_indoor_previous', 'Ghostline indoors: select previous', function() selectRelative(-1) end)
registerHotkey('ghostline_indoor_next', 'Ghostline indoors: select next', function() selectRelative(1) end)
registerHotkey('ghostline_indoor_copy_inspected', 'Ghostline indoors: copy inspected node JSON', copyWorldInspectorTarget)
