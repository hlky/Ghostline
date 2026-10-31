-- Reproduce CET returning fresh Lua wrappers for the same native HUD object.
local callbacks, observers = {}, {}
registerForEvent = function(name, callback) callbacks[name] = callback end
registerHotkey = function() end
Observe = function(class, event, callback) observers[class .. ':' .. event] = callback end
package.path = arg[1]:gsub('init%.lua$', '?.lua') .. ';' .. package.path
dofile(arg[1])
local function up(fn, wanted, replacement)
    for index = 1, 100 do
        local name, value = debug.getupvalue(fn, index)
        if not name then break end
        if name == wanted then
            if replacement ~= nil then debug.setupvalue(fn, index, replacement) end
            return value
        end
    end
    error('missing upvalue ' .. wanted)
end
local function count(values)
    local size = 0
    for _ in pairs(values) do size = size + 1 end
    return size
end
local state = up(callbacks.onUpdate, 'state')
state.active = true
state.snapshot = {}
up(callbacks.onInit, 'installObservers')()
local visible, dismisses = true, 0
local widget = {IsVisible = function() return visible end, SetVisible = function(_, value) visible = value end}
local function wrapper()
    return {GetRootWidget = function() return widget end, Dismiss = function() dismisses = dismisses + 1 end}
end
local shown = observers['HudPhoneMessageController:ShowMessage']
for _ = 1, 20000 do shown(wrapper()) end
assert(count(state.popupControllers) == 1, 'fresh observer wrappers must not accumulate')
assert(count(state.hiddenControllers) == 1, 'saved widget references must be bounded')
assert(not visible, 'bounded retention must still hide HUD pixels')
observers['HudPhoneMessageController:OnUninitialize'](wrapper())
assert(count(state.popupControllers) == 0 and count(state.hiddenControllers) == 0,
    'a fresh uninitialization wrapper must remove the earlier wrapper')
-- Repeated notifications at a steady native object count must plateau in memory.
collectgarbage('collect')
local baseline = collectgarbage('count')
for _ = 1, 20000 do shown(wrapper()) end
collectgarbage('collect')
assert(collectgarbage('count') - baseline < 64, 'controller retention grew after collection')

-- Area/hostile/quest banners bypass HUD settings and may show their roots again
-- after an animation starts. Hide presentation callbacks and each capture draw.
local hudShown = {
    ZoneAlertNotificationQueue = 'OnSecurityDataChange',
    ZoneAlertNotification = 'SetNotificationData',
    JournalNotificationQueue = 'OnJournalUpdate',
    JournalNotification = 'SetNotificationData',
    NewLocationNotification = 'SetNotificationData',
    NewAreaGameController = 'PlayIntroAnimation',
    CustomQuestNotificationGameController = 'PlayAnimation',
    StealthZonesGameController = 'OnPlayerAttach',
    interactionWidgetGameController = 'OnUpdateInteraction',
    dialogWidgetGameController = 'OnInteractionsChanged',
    InteractionsHubGameController = 'OnShowTooltips',
    LootingGameController = 'OnUpdateData',
}
local hudHide = up(callbacks.onDraw, 'hideHudNotifications')
local beforeDismiss = dismisses
for className, event in pairs(hudShown) do
    local present = observers[className .. ':' .. event]
    assert(present, 'missing HUD presentation hook: ' .. className)
    visible = true
    for _ = 1, 2000 do present(wrapper()) end
    assert(not visible, 'HUD banner must hide on presentation: ' .. className)
    visible = true
    hudHide()
    assert(not visible, 'HUD animation must not re-show a capture banner')
end
assert(count(state.hudControllers) == 12, 'HUD references must be bounded by known class count')
assert(dismisses == beforeDismiss, 'HUD suppression must not dismiss or block notification delivery')
state.active = false;visible = true
hudHide();assert(visible, 'normal gameplay HUD must not be hidden')
state.active = true
for className in pairs(hudShown) do observers[className .. ':OnUninitialize'](wrapper()) end
assert(count(state.hudControllers) == 0, 'destroyed HUD controllers must be released')

local definitionsRead, boolWrites, variantWrites, messages = 0, 0, 0, 0
local contacts = true
local board = {
    GetBool = function() return contacts end,
    SetBool = function(_, _, value) contacts = value; boolWrites = boolWrites + 1 end,
    SetVariant = function(_, _, _, signal)
        assert(not signal, 'empty notifications must not trigger HUD callback storms')
        variantWrites = variantWrites + 1
    end,
}
Game = {
    GetAllBlackboardDefs = function()
        definitionsRead = definitionsRead + 1
        return {UI_Notifications = {OnscreenMessage = 'screen', WarningMessage = 'warning'}, UI_ComDevice = {ContactsActive = 'contacts'}}
    end,
    GetBlackboardSystem = function() return {Get = function() return board end} end,
}
SimpleScreenMessage = {new = function() messages = messages + 1; return {} end}
ToVariant = function(value) return value end
local dismiss = up(callbacks.onUpdate, 'dismissNotifications')
local previousDismisses = dismisses
for _ = 1, 1000 do dismiss() end
assert(dismisses == previousDismisses, 'polling must not repeatedly Dismiss controllers')
assert(definitionsRead == 1 and messages == 1, 'native notification resources must be reused')
assert(boolWrites == 1 and contacts == false, 'unchanged contacts must not fire notifications')
assert(variantWrites == 2000)

local build = up(callbacks.onUpdate, 'buildReadiness')
local location = up(build, 'runtimeLocation')
local traversals = 0
local function districtRecord(id, label, parent)
    return {
        GetID = function() return id end,
        LocalizedName = function() return label end,
        ParentDistrict = function() traversals = traversals + 1; return parent() end,
    }
end
local root
root = districtRecord('root', 'District', function() return root end)
local leaf = districtRecord('leaf', 'Subdistrict', function() return root end)
local currentRecord = leaf
Game.GetScriptableSystemsContainer = function() return {Get = function() return {
    districtManager = {GetCurrentDistrict = function() return {GetDistrictID = function() return 'leaf' end} end},
} end} end
Game.GetLocalizedText = function(label) return label end
Game.GetPlayer = function() return {} end
GetSingleton = function() return {GetDistrictRecord = function() return currentRecord end} end
IsEntityInInteriorArea = function() return false end
local result = location()
assert(traversals == 2 and result.district == 'District' and result.subdistrict == 'Subdistrict',
    'cyclic native parent records must terminate without discarding useful labels')
-- Different wrappers for the same record are recognized by their native ID.
traversals = 0
local function wrappedRoot() return districtRecord('same', 'Root', wrappedRoot) end
currentRecord = wrappedRoot()
location()
assert(traversals == 1, 'cycle detection must use native record IDs')
-- Even an endless stream of different records cannot monopolize the game thread.
traversals = 0
local sequence = 0
local function endless()
    sequence = sequence + 1
    return districtRecord(sequence, 'Deep', endless)
end
currentRecord = endless()
location()
assert(traversals == 8, 'district ancestry needs a hard native-call bound')
print('CET reference lifetime checks passed')
