-- Flight-only scouting protections for keanuWheeze's installed FreeFly.
-- Uses the game's spawn-grace visibility and named GodMode APIs.
local scout = { active = false, effects = {} }
local source = "GhostlineFreeflyScout"
local combatEffect = "GameplayRestriction.NoCombat"

local function acquireEffect(effect)
    local player = scout.player
    local system = Game.GetStatusEffectSystem()
    if not system:HasStatusEffect(player:GetEntityID(), TweakDBID.new(effect)) then
        scout.effects[effect] = true
        system:ApplyStatusEffect(player:GetEntityID(), effect, player:GetRecordID(), player:GetEntityID())
    end
end

local function releaseEffect(effect)
    if scout.effects[effect] then
        Game.GetStatusEffectSystem():RemoveStatusEffect(scout.player:GetEntityID(), effect)
        scout.effects[effect] = nil
    end
end

function scout.syncWeapons(mod)
    if not scout.active then return end
    if mod.settings.noWeapon then
        acquireEffect(combatEffect)
    else
        releaseEffect(combatEffect)
    end
end

function scout.install()
    Override("PocketRadio", "HandleRestriction", function(this, restriction, restricted, wrapped)
        -- Keep every other radio restriction, including phone calls and scenes.
        -- Only bypass the forced-hands restriction caused by our own weapon lock.
        if scout.active and scout.effects[combatEffect]
            and restriction == PocketRadioRestrictions.UpperBodyState then
            restricted = false
        end
        return wrapped(restriction, restricted)
    end)
end

function scout.stop(refreshRadio)
    local player = scout.player
    scout.active = false
    if not player then return end
    local function cleanup(label, callback)
        local ok, err = pcall(callback)
        if not ok then print("[FreeFly Scout] Cleanup " .. label .. ": " .. tostring(err)) end
    end
    -- One failed cleanup must not prevent the remaining protections being removed.
    for effect in pairs(scout.effects) do
        cleanup(effect, function() releaseEffect(effect) end)
    end
    cleanup("god mode", function()
        Game.GetGodModeSystem():RemoveGodMode(player:GetEntityID(), gameGodModeType.Invulnerable, source)
    end)
    cleanup("visibility", function() player:SetInvisible(scout.wasInvisible) end)
    cleanup("time", function() Game.GetTimeSystem():UnsetTimeDilation(source) end)
    if refreshRadio then
        cleanup("radio", function()
            local board = player:GetPlayerStateMachineBlackboard()
            local upperBody = board:GetInt(GetAllBlackboardDefs().PlayerStateMachine.UpperBody)
            player:GetPocketRadio():HandleRestriction(PocketRadioRestrictions.UpperBodyState,
                upperBody == EnumInt(gamePSMUpperBodyStates.ForceEmptyHands))
        end)
    end
    scout.effects = {}
    scout.player = nil
end

function scout.setFlight(mod, enabled)
    if not enabled then
        scout.stop(true)
        return
    end
    if scout.active then return end
    local player = GetPlayer()
    if not player then
        mod.runtimeData.active = false
        return
    end
    scout.player = player
    scout.wasInvisible = player:IsInvisible()
    scout.active = true
    local ok, err = pcall(function()
        local added = Game.GetGodModeSystem():AddGodMode(player:GetEntityID(), gameGodModeType.Invulnerable, source)
        if added == false then error("Could not enable invulnerability") end
        player:SetInvisible(true)
        acquireEffect("GameplayRestriction.NoZooming")
        acquireEffect("GameplayRestriction.NoMovement")
        scout.syncWeapons(mod)
        if scout.effects[combatEffect] then
            player:GetPocketRadio():HandleRestriction(PocketRadioRestrictions.UpperBodyState, false)
        end
        if mod.settings.timeStop then
            Game.GetTimeSystem():SetTimeDilation(source, 0.000000001)
        end
    end)
    if not ok then
        mod.runtimeData.active = false
        scout.stop(true)
        print("[FreeFly Scout] Flight cancelled: " .. tostring(err))
    end
end

function scout.update(mod)
    if not scout.active then return end
    scout.syncWeapons(mod)
    -- Spawn-grace and optical-camo timers can restore AI visibility during flight.
    if not scout.player:IsInvisible() then scout.player:SetInvisible(true) end
end

return scout
