-- Optional manual test harness. Not part of the native runtime package.
local effects = {
  "BaseStatusEffect.GhostlineHeartbreakerShortBlind",
  "BaseStatusEffect.GhostlineHeartbreakerVision"
}
local lastTarget = nil

local function player()
  local value = Game.GetPlayer()
  if not value then print("[Heartbreaker] Load a save first.") end
  return value
end

local function apply(target)
  if not target then return end
  local component = target:FindComponentByName(CName.new("ghostline_heartbreaker_fx"))
  print("[Heartbreaker] Native FX spawner present=" .. tostring(component ~= nil))
  local configured = TweakDB:GetFlat("BaseStatusEffect.GhostlineHeartbreakerVision.VFX")
  print("[Heartbreaker] Runtime VFX records=" .. tostring(configured and #configured or 0))
  if not component then
    print("[Heartbreaker] This entity has no Heartbreaker patch. Status can blind it, but hearts cannot play.")
  end
  local system = Game.GetStatusEffectSystem()
  local id = target:GetEntityID()
  for _, effect in ipairs(effects) do
    system:RemoveStatusEffect(id, TweakDBID.new(effect))
  end
  for _, effect in ipairs(effects) do
    local accepted = system:ApplyStatusEffect(id, TweakDBID.new(effect))
    print("[Heartbreaker] " .. effect .. " accepted=" .. tostring(accepted))
  end
  lastTarget = target
end

registerHotkey("heartbreaker_give_items", "Heartbreaker: give quickhack and 10 self-tests", function()
  if not player() then return end
  Game.AddToInventory("Items.GhostlineHeartbreakerProtocol", 1)
  Game.AddToInventory("Items.GhostlineHeartbreakerSelfTest", 10)
  print("[Heartbreaker] Added prototype items; equip the quickhack in your cyberdeck.")
end)

registerHotkey("heartbreaker_apply_v", "Heartbreaker: apply native status to V", function()
  apply(player())
end)

registerHotkey("heartbreaker_apply_npc", "Heartbreaker: apply native status to looked-at NPC", function()
  local value = player()
  if not value then return end
  local target = Game.GetTargetingSystem():GetLookAtObject(value, false, false)
  if not target or not target:IsNPC() then
    print("[Heartbreaker] Look directly at a supported human NPC.")
    return
  end
  apply(target)
end)

registerHotkey("heartbreaker_clear", "Heartbreaker: clear V and last tested target (test outro)", function()
  local system = Game.GetStatusEffectSystem()
  for _, target in ipairs({player(), lastTarget}) do
    if target then
      for _, effect in ipairs(effects) do
        system:RemoveStatusEffect(target:GetEntityID(), TweakDBID.new(effect))
      end
    end
  end
  lastTarget = nil
end)
