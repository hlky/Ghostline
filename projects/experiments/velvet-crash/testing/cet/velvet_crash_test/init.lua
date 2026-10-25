-- Optional manual test harness. Not part of the native runtime package.
local effects = {
  "BaseStatusEffect.GhostlineVelvetCrashShortBlind",
  "BaseStatusEffect.GhostlineVelvetCrashVision"
}
local lastTarget = nil

local function player()
  local value = Game.GetPlayer()
  if not value then print("[Velvet Crash] Load a save first.") end
  return value
end

local function apply(target)
  if not target then return end
  local component = target:FindComponentByName(CName.new("ghostline_velvet_crash_fx"))
  print("[Velvet Crash] Native FX spawner present=" .. tostring(component ~= nil))
  local configured = TweakDB:GetFlat("BaseStatusEffect.GhostlineVelvetCrashVision.VFX")
  print("[Velvet Crash] Runtime VFX records=" .. tostring(configured and #configured or 0))
  if not component then
    print("[Velvet Crash] This entity has no VelvetCrash patch. Status can blind it, but hearts cannot play.")
  end
  local system = Game.GetStatusEffectSystem()
  local id = target:GetEntityID()
  for _, effect in ipairs(effects) do
    system:RemoveStatusEffect(id, TweakDBID.new(effect))
  end
  for _, effect in ipairs(effects) do
    local accepted = system:ApplyStatusEffect(id, TweakDBID.new(effect))
    print("[Velvet Crash] " .. effect .. " accepted=" .. tostring(accepted))
  end
  lastTarget = target
end

registerHotkey("velvet_crash_give_items", "Velvet Crash: give quickhack and 10 self-tests", function()
  if not player() then return end
  Game.AddToInventory("Items.GhostlineVelvetCrashProtocol", 1)
  Game.AddToInventory("Items.GhostlineVelvetCrashSelfTest", 10)
  print("[Velvet Crash] Added prototype items; equip the quickhack in your cyberdeck.")
end)

registerHotkey("velvet_crash_apply_v", "Velvet Crash: apply native status to V", function()
  apply(player())
end)

registerHotkey("velvet_crash_apply_npc", "Velvet Crash: apply native status to looked-at NPC", function()
  local value = player()
  if not value then return end
  local target = Game.GetTargetingSystem():GetLookAtObject(value, false, false)
  if not target or not target:IsNPC() then
    print("[Velvet Crash] Look directly at a supported human NPC.")
    return
  end
  apply(target)
end)

registerHotkey("velvet_crash_clear", "Velvet Crash: clear V and last tested target (test outro)", function()
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
