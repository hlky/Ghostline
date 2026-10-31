-- Game Scout MCP runtime. Separate protocol and state from world capture.
local Engine=require('engine')
local engine=Engine.new()
local boot=tostring(os.time())..'_'..tostring(math.random(1,2147483647))
local session,pending,lastCommand,lastStop=nil,nil,nil,nil
local elapsed=0
local outbox={}
local function read(name)
    local file=io.open('runtime/'..name..'.json','r')
    if not file then return nil end
    local raw=file:read('*a'); file:close()
    local ok,data=pcall(json.decode,raw)
    return ok and type(data)=='table' and data or nil
end
local function write(name,data)
    outbox[name]=json.encode(data)
end
local function flush()
    for name,raw in pairs(outbox) do
    local path='runtime/'..name..'.json'
    local temporary=path..'.tmp'
    local file=io.open(temporary,'w')
    if file then
        file:write(raw); file:close()
        os.remove(path)
        if os.rename(temporary,path) then outbox[name]=nil end
    end
    end
end
local function status()
    local result=engine:status()
    result.protocol=1; result.boot=boot; result.session=session; result.timestamp=os.time()
    return result
end
local function respond(command,ok,result)
    write('response',{id=command.id,session=command.session,boot=boot,ok=ok,
        result=ok and result or nil,error=not ok and tostring(result) or nil})
end
local function stop(reason)
    local result=engine:release()
    if pending then respond(pending,false,reason or 'Operation stopped'); pending=nil end
    session=nil
    write('state',status())
    return result
end
local function poll()
    local request=read('stop')
    if request and request.id~=lastStop then
        lastStop=request.id
        if session and request.session==session then stop('Operation stopped') end
    end
    if session then
        local lease=read('lease')
        if not lease or lease.session~=session or os.time()-lease.timestamp>5 then stop('Controller lease expired') end
    end
    local command=read('command')
    if not command or command.id==lastCommand then return end
    lastCommand=command.id
    if command.boot~=boot or type(command.expires)~='number' or command.expires<os.time() then
        respond(command,false,'Stale command'); return
    end
    if pending then respond(command,false,'Runtime busy'); return end
    local ok,result=pcall(function()
        if command.kind=='begin' then
            if session and session~=command.session then error('Another scout session owns the runtime') end
            local lease=read('lease')
            if not lease or lease.session~=command.session or os.time()-lease.timestamp>5 then error('No current controller lease') end
            engine:begin(command.arguments.hide_hud~=false)
            session=command.session
            return status()
        end
        if command.session~=session then error('Session mismatch') end
        if command.kind=='end' then return stop('Session ended') end
        if command.kind=='inspect' then return engine:inspect(command.arguments) end
        if command.kind=='pose' then engine:pose(command.arguments); pending=command; return nil end
        error('Unknown command')
    end)
    if not ok or not pending then respond(command,ok,result) end
    write('state',status())
end

registerForEvent('onInit',function() engine:observers(); write('state',status()); flush() end)
registerForEvent('onUpdate',function(delta)
    elapsed=elapsed+math.max(0,delta)
    local ok,err=pcall(function()
        -- Poll stop/lease before moving, including during a pending operation.
        if elapsed>=0.1 then poll() end
        if pending and pending.expires<os.time() then stop('Command expired'); return end
        local completed=engine:update(delta)
        if completed and pending then local command=pending; pending=nil; respond(command,true,status()) end
        if elapsed>=0.1 then elapsed=0; write('state',status()); flush() end
    end)
    if not ok then
        pcall(function() stop(tostring(err)) end)
        print('[Game Scout] '..tostring(err))
    end
end)
registerForEvent('onDraw',function() engine:hide() end)
registerForEvent('onOverlayOpen',function() engine.overlay=true end)
registerForEvent('onOverlayClose',function() engine.overlay=false end)
registerForEvent('onShutdown',function() pcall(function() stop('CET shutdown'); flush() end) end)
registerHotkey('game_scout_stop','Game Scout: emergency stop',function() stop('Emergency stop') end)
registerHotkey('game_scout_demo_environment','Game Scout: clear weather and midday',function() engine:demoEnvironment() end)
return {engine=engine,stop=stop,status=status,demoEnvironment=function() return engine:demoEnvironment() end}
