-- Location captures only. Link diagnostics disabled. No spawning, teleporting or fact writes.
local path = 'love-actually-locations.json'
local state = {schema_version = 1, quest = 'gq004', captures = {}}
local targets, selected, visible = {}, 1, false
local fatal, status, height = '', '', 0

local function loadJson(name)
  local file = io.open(name, 'r')
  if not file then return nil end
  local raw = file:read('*a'); file:close()
  local ok, value = pcall(json.decode, raw)
  if not ok then fatal = 'Invalid JSON: ' .. name; return nil end
  return value
end

local function finite(n)
  return type(n) == 'number' and n == n and n ~= math.huge and n ~= -math.huge
end

local function validPose(p)
  return type(p) == 'table' and finite(p.x) and finite(p.y) and finite(p.z) and finite(p.yaw)
end

local function select(index)
  selected = math.max(1, math.min(#targets, index))
  height = targets[selected] and targets[selected].height or 0
end

local function nextMissing()
  for offset = 1, #targets do
    local index = (selected + offset - 1) % #targets + 1
    if not state.captures[targets[index].id] then select(index); return end
  end
end

local function save(candidate)
  local file = io.open(path .. '.tmp', 'w')
  if not file then return false, 'Could not write log. Retry after checking mod-folder permissions.' end
  local ok, result = pcall(function() return file:write(json.encode(candidate)) end)
  local closed = file:close()
  if not ok or not result or not closed then return false, 'Could not finish writing log. Previous captures retained.' end
  os.remove(path .. '.bak')
  local existing = io.open(path, 'r')
  if existing then
    existing:close()
    if not os.rename(path, path .. '.bak') then return false, 'Could not back up log. Previous captures retained.' end
  end
  if not os.rename(path .. '.tmp', path) then
    os.rename(path .. '.bak', path)
    return false, 'Could not publish log. Previous captures restored; retry recording.'
  end
  return true
end

local function capture(group)
  if fatal ~= '' then return end
  local player = Game.GetPlayer()
  if not player or not targets[selected] then status = 'Load a save and stand on foot first.'; return end
  local p, f = player:GetWorldPosition(), player:GetWorldForward()
  -- Local +Y is forward. This yaw matches the generator's Z-axis quaternion.
  local yaw = math.deg(math.atan2(-f.x, f.y))
  if not finite(p.x) or not finite(p.y) or not finite(p.z) or not finite(yaw) or not finite(height) then
    status = 'Invalid player pose; nothing recorded.'; return
  end
  local candidate = {schema_version = 1, quest = 'gq004', captures = {}}
  for key, value in pairs(state.captures) do candidate.captures[key] = value end
  local count = 0
  for index, target in ipairs(targets) do
    if (group and target.group == group) or (not group and index == selected) then
      local offset = group and 0 or height
      candidate.captures[target.id] = {x=p.x, y=p.y, z=p.z + offset, yaw=yaw,
        height_offset=offset, forward_x=f.x, forward_y=f.y}
      count = count + 1
    end
  end
  if count == 0 then status = 'No matching targets.'; return end
  local ok, message = save(candidate)
  if not ok then status = message; return end
  state = candidate
  status = 'Saved ' .. count .. ' placement(s).'
  nextMissing()
end

registerForEvent('onInit', function()
  targets = loadJson('targets.json') or {}
  if type(targets) ~= 'table' or #targets == 0 then fatal = 'targets.json is missing or empty. Reinstall the scout helper.'; targets = {}; return end
  local seen = {}
  for _, target in ipairs(targets) do
    if type(target) ~= 'table' or type(target.id) ~= 'string' or type(target.label) ~= 'string' or seen[target.id] or (target.height ~= nil and not finite(target.height)) then
      fatal = 'Invalid or duplicate target in targets.json. Reinstall the scout helper.'; return
    end
    seen[target.id] = true
  end
  local loaded = loadJson(path)
  if loaded then
    if type(loaded) ~= 'table' or loaded.quest ~= 'gq004' or loaded.schema_version ~= 1 or type(loaded.captures) ~= 'table' then
      fatal = 'Wrong location-log schema. Preserve the log and repair it before recording.'
    else
      for _, pose in pairs(loaded.captures) do
        if not validPose(pose) then fatal = 'Invalid saved pose. Preserve the log and repair it before recording.'; return end
      end
      state = loaded
    end
  end
  select(#targets); nextMissing()
end)
registerForEvent('onOverlayOpen', function() visible = true end)
registerForEvent('onOverlayClose', function() visible = false end)
registerHotkey('gq004_capture_location', 'Love Actually: capture selected placement', function() capture() end)
registerForEvent('onDraw', function()
  if not visible then return end
  if ImGui.Begin('Love, Actually.exe - locations') then
    if fatal ~= '' then ImGui.TextWrapped('STOP: ' .. fatal); ImGui.End(); return end
    ImGui.TextWrapped('On foot: stand at the intended position and face the desired direction. Group buttons fill co-located centres; individual targets can be refined afterwards.')
    if ImGui.Button('Record meeting group here (8)') then capture('meeting') end
    ImGui.SameLine()
    if ImGui.Button('Record operation centres here (3)') then capture('operation') end
    if ImGui.Button('Previous') then select(selected - 1) end
    ImGui.SameLine()
    if ImGui.Button('Next') then select(selected + 1) end
    ImGui.SameLine()
    if ImGui.Button('Next missing') then nextMissing() end
    local target = targets[selected]
    if target then
      ImGui.Text(tostring(selected) .. '/' .. tostring(#targets) .. '  ' .. target.label)
      ImGui.TextWrapped(target.hint or target.id)
      ImGui.Text(string.format('Height above feet: %.2f m', height))
      if ImGui.Button('Height -0.10 m') then height = height - 0.1 end
      ImGui.SameLine()
      if ImGui.Button('Height +0.10 m') then height = height + 0.1 end
      ImGui.SameLine()
      if ImGui.Button('Reset target height') then height = target.height or 0 end
      local pose = state.captures[target.id]
      if validPose(pose) then ImGui.Text(string.format('Saved: %.3f, %.3f, %.3f / %.1f degrees', pose.x,pose.y,pose.z,pose.yaw)) end
      if ImGui.Button('Record selected position and facing') then capture() end
    end
    local count = 0
    for _, targetRow in ipairs(targets) do if state.captures[targetRow.id] then count = count + 1 end end
    ImGui.Text('Saved ' .. count .. '/' .. #targets .. ' - ' .. path)
    if count == #targets and count > 0 then ImGui.TextWrapped('Complete. Return to the Ghostline chat and say captured. The saved JSON is ready for local import.') end
    if status ~= '' then ImGui.TextWrapped(status) end
    if fatal ~= '' then ImGui.TextWrapped('STOP: ' .. fatal) end
  end
  ImGui.End()
end)
