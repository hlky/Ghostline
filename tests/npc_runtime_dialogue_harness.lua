-- The real UI module must not let one runtime owner hide the other's choices.
local observers = {}
Observe=function(class, method, callback) observers[class..method]=callback end
Override=function() end
local ctor=function() return {} end
DialogChoiceHubs={new=ctor}
gameinteractionsvisListChoiceHubData={new=ctor}
gameinteractionsvisListChoiceData={new=ctor}
gameinteractionsChoiceTypeWrapper={new=function() return {SetType=function() end} end}
gameinteractionsvisEVisualizerActivityState={Active=1}
gameinteractionsChoiceType={QuestImportant=1}
CName={new=function(v) return v end}
FromVariant=function(v) return v end
GetAllBlackboardDefs=function() return {UIInteractions={DialogChoiceHubs=1}} end
local native={choiceHubs={}}
Game={GetBlackboardSystem=function() return {Get=function() return {GetVariant=function() return native end} end} end}
local controller={UpdateDialogsData=function() end, OnInteractionsChanged=function() end,
  UpdateListBlackboard=function() end, OnDialogsActivateHub=function() end,
  OnDialogsSelectIndex=function() end, OnDialogsData=function() end}
local dialogue=dofile("projects/experiments/npc-runtime/source/resources/bin/x64/plugins/cyber_engine_tweaks/mods/ghostline_npc_runtime/dialogue.lua")
dialogue.init(function() end)
observers.InteractionUIBaseOnInitialize(controller)
local options={{label="Choice", callback=function() end}}
assert(dialogue.show(options))
assert(not dialogue.show(options,{owner="job",title="Job",id=2}))
dialogue.hide("job"); assert(dialogue.active and dialogue.owner=="npc")
dialogue.hide("npc"); assert(not dialogue.active)
assert(dialogue.show(options,{owner="job",title="Job",id=2}))
assert(dialogue.hub.title=="Job")
dialogue.hide("npc"); assert(dialogue.active)
dialogue.hide("job"); assert(not dialogue.active)
native.choiceHubs={{id=77}}
assert(not dialogue.show(options), "authored choices must retain priority")
print("Native dialogue ownership and authored-choice priority checks passed")
