-- Exercise the real CET callbacks: a failed query must not suppress a normal
-- navigation-enabled NPC command, and it must remain failed in the walk report.
local events, clicked, sent, lastReport = {}, '', 0, nil
local point = {x=0,y=0,z=0}
local validEndpoints=true
local jumpOnSend=false
local pathPass=false
local npc={}
function npc:GetWorldPosition() return point end
function npc:GetWorldOrientation() return {} end
function npc:IsNPC() return true end
function npc:GetNPCType() return 1 end
function npc:GetAIControllerComponent() return {
 SendCommand=function(_,command) assert(command.ignoreNavigation==false);sent=sent+1;if jumpOnSend then point={x=3,y=0,z=0} end;return true end,
 CancelCommand=function() end} end
Game={GetPlayer=function()return npc end,GetTargetingSystem=function()return {GetLookAtObject=function()return npc end}end,
 GetAINavigationSystem=function()return {FindPointInBoxForCharacter=function(_,p) return {point=validEndpoints and p or nil,status=0}end,
 StartPathfinding=function(_,query)assert(query.source and query.target);return 7 end,
 StopPathfinding=function()end,
 GetResult=function(_,id,result)assert(id==7);result.hasFailed=not pathPass;result.hasPath=pathPass;
 result.hasClosestReachablePoint=true;result.closestReachablePoint={x=0,y=0,z=0};return true end,
 CalculatePathForCharacter=function()return {path=pathPass and {{x=0,y=0,z=0},{x=3,y=0,z=0}} or {}}end}end}
Vector4={new=function(x,y,z,w)return{x=x,y=y,z=z,w=w}end}
Quaternion={ToEulerAngles=function()return{}end}
WorldPosition={new=function()return{}end,SetVector4=function()end,ToVector4=function(p)return p end}
AINavigationSystemQuery={new=function()return{}end};AINavigationSystemResult={new=function()return{}end}
AIPositionSpec={new=function()return{}end,SetWorldPosition=function()end}
AIMoveToCommand={new=function()return{}end}
moveMovementType={Walk=1};gamedataNPCType={Human=1}
registerForEvent=function(name,callback)events[name]=callback end
ImGui={Begin=function()return true end,End=function()end,TextWrapped=function()end,SameLine=function()end,
 RadioButton=function()return false end,InputText=function(_,text)return text end,Button=function(label)return label==clicked end}
json={decode=function()return {layout_id='test',points={{name='start',world={0,0,0}},{name='end',world={3,0,0}}},doors={}}end,
 encode=function(report)lastReport=report;return '{}'end}
io.open=function()return {read=function()return '{}'end,write=function()end,close=function()end}end
assert(loadfile('tools/building_runtime_cet/init.lua'))()
events.onInit();events.onOverlayOpen()
clicked='Bind looked-at NPC';events.onDraw()
clicked='Walk NPC to end';events.onDraw();assert(sent==0,'Failed native paths must not trigger engine teleport fallback')
events.onUpdate(.11);assert(lastReport.ai_query.completed and lastReport.ai_query.has_failed)
pathPass=true;events.onDraw();assert(sent==1)
for i=1,6 do point={x=i*.5,y=0,z=0};events.onUpdate(.11) end
assert(lastReport and lastReport.npc_movement_passed,'Actual continuous movement was not recorded')
assert(lastReport.native_query_passed==true)
assert(lastReport.movement_attempted_after_failed_query==false)
point={x=0,y=0,z=0};validEndpoints=false;events.onDraw();assert(sent==1,'Missing navigation endpoints should prevent a walk attempt')
print('CET callback regression passed: failed query blocks command, continuous walk passes, missing endpoints rejected')

validEndpoints=true;jumpOnSend=true;point={x=0,y=0,z=0}
events.onDraw();assert(sent==2);events.onUpdate(.11)
assert(lastReport.teleport_detected==true and lastReport.npc_movement_passed==false)
assert(lastReport.message:find('teleport%-sized jump'))
print('Synchronous engine jump detected from pre-command position and rejected')
