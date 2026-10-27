-- Manually operated shortcut for the Allen Street residential walkthrough.
local visible = false
local previous = nil
local message = 'Load a save, then teleport to the public approach.'

local function teleportOutside()
  local player = Game.GetPlayer()
  if not player then message = 'Load a save first.'; return end
  if not previous then
    local p = player:GetWorldPosition()
    previous = {
      point = Vector4.new(p.x, p.y, p.z, 1),
      rotation = Quaternion.ToEulerAngles(player:GetWorldOrientation())
    }
  end
  -- Three metres east of the surveyed door, facing back toward the entrance.
  Game.GetTeleportationFacility():Teleport(player,
    Vector4.new(-1060.447, 1782.181, 28.565, 1), EulerAngles.new(0, 0, 90.696))
  message = 'Outside Allen Street entrance. Allow the area to stream before walking.'
end

local function returnPlayer()
  local player = Game.GetPlayer()
  if not player then message = 'Load a save first.'; return end
  if not previous then message = 'No return position stored.'; return end
  Game.GetTeleportationFacility():Teleport(player, previous.point, previous.rotation)
  previous = nil
  message = 'Returned to your original position.'
end

local function safely(action)
  local ok, err = pcall(action)
  if not ok then message = tostring(err); print('[Allen teleport] ' .. message) end
end

registerHotkey('ghostline_allen_outside', 'Allen Street: teleport outside entrance', function()
  safely(teleportOutside)
end)
registerForEvent('onOverlayOpen', function() visible = true end)
registerForEvent('onOverlayClose', function() visible = false end)
registerForEvent('onDraw', function()
  if not visible then return end
  if ImGui.Begin('Ghostline - Allen Street teleport') then
    ImGui.TextWrapped(message)
    if ImGui.Button('Teleport outside Allen Street') then safely(teleportOutside) end
    if ImGui.Button('Return to previous position') then safely(returnPlayer) end
  end
  ImGui.End()
end)
