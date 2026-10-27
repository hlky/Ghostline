local events, report = {}, nil
local auto, opened, occupants, restores, closes = false, true, 0, 0, 0
local streamed=true
local ps={IsClosingAutomatically=function()return auto end,
  SetCloseItself=function(_,value)auto=value;restores=restores+1 end,
  IsOpen=function()return opened end,IsBusy=function()return false end,IsON=function()return true end}
local entity={GetDevicePS=function()return ps end,
  QueueEvent=function()if occupants==0 then opened=false;closes=closes+1 end end,
  FindComponentByName=function()return {GetNumberOverlappingActivators=function()return occupants end}end}
Game={GetPlayer=function()return {}end,FindEntityByID=function()if streamed then return entity end end}
ResolveNodeRef=function()return {hash=123}end
CreateEntityReference=function()return {reference={}}end
GlobalNodeID={GetRoot=function()return {}end};EntityID={new=function(v)return v end}
DoorTriggerDelayedEvent={new=function()return {}end}
registerForEvent=function(name,callback)events[name]=callback end
json={decode=function()return {layout_id='shutter-test',points={},doors={},restore_auto_close={'garage'}}end,
  encode=function(value)report=value;return '{}'end}
io.open=function()return {read=function()return '{}'end,write=function()end,close=function()end}end
assert(loadfile('tools/building_runtime_cet/init.lua'))()
events.onInit();events.onUpdate(.6)
assert(auto and not opened and restores==1 and closes==1)
assert(report.doors.garage.auto_close_before==false)
-- Do not fight an intentional quickhack later in the same streamed instance.
auto=false;opened=true;events.onUpdate(.6)
assert(restores==1 and opened)
-- Streaming a new instance restores setup but occupancy prevents a close.
streamed=false;events.onUpdate(.6)
streamed=true;occupants=1;events.onUpdate(.6)
assert(auto and opened and restores==2 and closes==1)
print('Shutter migration passed: stale setting repaired, native occupancy respected, later quickhack unchanged')
