-- Native hub presentation owned only while this experiment has the conversation.
local M = { controller = nil, active = false, hub = nil, index = 0, callbacks = {}, owner = nil }
local cancel = function() end

local function refresh()
  if not M.controller then return end
  local data = DialogChoiceHubs.new()
  if M.active then data.choiceHubs = { M.hub } end
  M.controller.AreDialogsOpen = M.active
  M.controller.dialogIsScrollable = M.active and #M.hub.choices > 1
  M.controller:UpdateDialogsData(data)
  M.controller:OnInteractionsChanged()
  M.controller:UpdateListBlackboard()
  if M.active then
    M.controller:OnDialogsActivateHub(M.hub.id)
    M.controller:OnDialogsSelectIndex(M.index)
  end
end

function M.hide(owner)
  if owner and owner ~= M.owner then return end
  if not M.active then return end
  M.active = false
  refresh()
  local board = Game.GetBlackboardSystem():Get(GetAllBlackboardDefs().UIInteractions)
  local original = board:GetVariant(GetAllBlackboardDefs().UIInteractions.DialogChoiceHubs)
  M.controller:OnDialogsData(original)
  M.callbacks = {}
  M.owner = nil
end

function M.show(options, context)
  context = context or {owner = "npc", title = "Patch", id = 187320001}
  if M.active and M.owner ~= context.owner then return false, "Another runtime interaction owns choices" end
  if not M.controller then return false, "Native dialogue controller is not ready" end
  local board = Game.GetBlackboardSystem():Get(GetAllBlackboardDefs().UIInteractions)
  local native = FromVariant(board:GetVariant(GetAllBlackboardDefs().UIInteractions.DialogChoiceHubs))
  if native and native.choiceHubs and #native.choiceHubs > 0 then
    return false, "An authored conversation currently owns dialogue choices"
  end
  M.hub = gameinteractionsvisListChoiceHubData.new()
  M.hub.id = context.id
  M.hub.title = context.title
  M.hub.hubPriority = 1
  M.hub.activityState = gameinteractionsvisEVisualizerActivityState.Active
  local choices = {}
  M.callbacks = {}
  for i, option in ipairs(options) do
    local choice = gameinteractionsvisListChoiceData.new()
    choice.localizedName = option.label
    choice.inputActionName = CName.new("None")
    local style = gameinteractionsChoiceTypeWrapper.new()
    style:SetType(gameinteractionsChoiceType.QuestImportant)
    choice.type = style
    choices[i] = choice
    M.callbacks[i] = option.callback
  end
  M.hub.choices = choices
  M.index, M.active, M.owner = 0, true, context.owner
  refresh()
  return true
end

function M.init(onCancel)
  cancel = onCancel
  Observe("InteractionUIBase", "OnInitialize", function(this) M.controller = this end)
  Override("InteractionUIBase", "OnDialogsData", function(this, value, wrapped)
    M.controller = this
    if M.active then
      local incoming = FromVariant(value)
      if incoming and incoming.choiceHubs and #incoming.choiceHubs > 0 then
        cancel("authored dialogue took priority")
      else
        return -- Keep our hub while vanilla has no conversation.
      end
    end
    wrapped(value)
  end)
  Override("InteractionUIBase", "OnDialogsSelectIndex", function(_, index, wrapped)
    if M.active and index ~= M.index then return end
    wrapped(index)
  end)
  Override("dialogWidgetGameController", "OnDialogsActivateHub", function(_, id, wrapped)
    if M.active and id ~= M.hub.id then return end
    wrapped(id)
  end)
  Observe("PlayerPuppet", "OnAction", function(_, action)
    if not M.active or action:GetType(action).value ~= "BUTTON_PRESSED" then return end
    local name = Game.NameToString(action:GetName(action))
    if name == "ChoiceScrollUp" then
      M.index = (M.index - 1) % #M.hub.choices
    elseif name == "ChoiceScrollDown" then
      M.index = (M.index + 1) % #M.hub.choices
    elseif name == "ChoiceApply" then
      local callback = M.callbacks[M.index + 1]
      M.hide()
      if callback then callback() end
      return
    else
      return
    end
    M.controller:OnDialogsSelectIndex(M.index)
    Game.GetBlackboardSystem():Get(GetAllBlackboardDefs().UIInteractions)
      :SetInt(GetAllBlackboardDefs().UIInteractions.SelectedIndex, M.index)
  end)
end

function M.reset()
  M.active, M.controller, M.callbacks, M.owner = false, nil, {}, nil
end

return M
