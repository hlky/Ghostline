-- Run with lua tests/freefly_scout_harness.lua [path/to/scout.lua].
local path = arg[1] or "tools/freefly_scout_cet/scout.lua"
local scout = dofile(path)
local effects, godModes, timeDilation, radioCalls = {}, {}, {}, {}
local invisible, upperBody, failAdd = false, 0, false
PocketRadioRestrictions = {UpperBodyState = 1, SceneTier = 0, PhoneCall = 7, BlockFastTravel = 4}
gameGodModeType = {Invulnerable = 2}
gamePSMUpperBodyStates = {ForceEmptyHands = 6}
TweakDBID = {new = function(value) return value end}
function EnumInt(value) return value end
function GetAllBlackboardDefs() return {PlayerStateMachine = {UpperBody = "UpperBody"}} end
local radio = {}
local hook
local function originalRestriction(restriction, restricted)
    radioCalls[restriction] = restricted
end
function radio:HandleRestriction(restriction, restricted)
    return hook(self, restriction, restricted, originalRestriction)
end
function Override(class, method, fn)
    assert(class == "PocketRadio" and method == "HandleRestriction")
    hook = fn
end
local player = {}
function player:GetEntityID() return 42 end
function player:GetRecordID() return "Player" end
function player:IsInvisible() return invisible end
function player:SetInvisible(value) invisible = value end
function player:GetPocketRadio() return radio end
function player:GetPlayerStateMachineBlackboard()
    return {GetInt = function() return upperBody end}
end
local currentPlayer = player
function GetPlayer() return currentPlayer end
local status = {}
function status:HasStatusEffect(id, effect) assert(id == 42); return effects[effect] == true end
function status:ApplyStatusEffect(id, effect) assert(id == 42); effects[effect] = true end
function status:RemoveStatusEffect(id, effect) assert(id == 42); effects[effect] = nil end
local god = {}
function god:AddGodMode(id, kind, source)
    if failAdd then return false end
    godModes[source] = true
    return true
end
function god:RemoveGodMode(id, kind, source) godModes[source] = nil end
local time = {}
function time:SetTimeDilation(source, value) timeDilation[source] = value end
function time:UnsetTimeDilation(source) timeDilation[source] = nil end
Game = {
    GetStatusEffectSystem = function() return status end,
    GetGodModeSystem = function() return god end,
    GetTimeSystem = function() return time end,
}
local mod = {settings = {noWeapon = true, timeStop = false}, runtimeData = {active = true}}
scout.install()
local combat = "GameplayRestriction.NoCombat"

-- The weapon lock stays applied while its radio restriction is bypassed.
godModes.OtherMod = true
timeDilation.OtherMod = 0.5
scout.setFlight(mod, true)
assert(scout.active and invisible and effects[combat])
assert(godModes.GhostlineFreeflyScout)
radio:HandleRestriction(PocketRadioRestrictions.UpperBodyState, true)
assert(radioCalls[PocketRadioRestrictions.UpperBodyState] == false)
for _, restriction in ipairs({0, 7, 4}) do
    radio:HandleRestriction(restriction, true)
    assert(radioCalls[restriction] == true, "Unrelated radio restriction must be preserved")
end
invisible = false -- Simulate a spawn/camo visibility timer firing in flight.
scout.update(mod)
assert(invisible)
mod.settings.noWeapon = false
scout.update(mod)
assert(not effects[combat])
radio:HandleRestriction(PocketRadioRestrictions.UpperBodyState, true)
assert(radioCalls[PocketRadioRestrictions.UpperBodyState] == true)
mod.settings.noWeapon = true
scout.update(mod)
assert(effects[combat])
scout.setFlight(mod, false)
assert(not scout.active and not invisible and next(effects) == nil)
assert(not godModes.GhostlineFreeflyScout and godModes.OtherMod)
assert(timeDilation.OtherMod == 0.5)
radio:HandleRestriction(PocketRadioRestrictions.UpperBodyState, true)
assert(radioCalls[PocketRadioRestrictions.UpperBodyState] == true)
scout.stop(true) -- Idempotent shutdown.

-- Existing protections/restrictions belong to their original owner.
invisible = true
effects[combat] = true
effects["GameplayRestriction.NoMovement"] = true
mod.settings.timeStop = true
scout.setFlight(mod, true)
radio:HandleRestriction(PocketRadioRestrictions.UpperBodyState, true)
assert(radioCalls[PocketRadioRestrictions.UpperBodyState] == true)
assert(timeDilation.GhostlineFreeflyScout)
currentPlayer = nil -- Session ended: cleanup uses the captured player.
scout.stop(false)
assert(invisible and effects[combat] and effects["GameplayRestriction.NoMovement"])
assert(not timeDilation.GhostlineFreeflyScout and timeDilation.OtherMod == 0.5)

-- Failed/missing-player activation rolls back rather than flying unprotected.
mod.runtimeData.active = true
scout.setFlight(mod, true)
assert(not scout.active and not mod.runtimeData.active)
currentPlayer = player
effects, invisible, failAdd = {}, false, true
mod.runtimeData.active = true
scout.setFlight(mod, true)
assert(not scout.active and not mod.runtimeData.active and not invisible)
assert(next(effects) == nil and godModes.OtherMod)
print("FreeFly Scout lifecycle, radio scope, state ownership, and rollback checks passed")
