"""Interactive scouting, recorded routes and bounded autonomous exploration."""
from __future__ import annotations

from contextlib import contextmanager
import math
import threading
import time

from .core import ScoutError, angles, distance, identifier, number, point


class Scout:
    def __init__(self, bridge, library, images):
        self.bridge, self.library, self.images = bridge, library, images
        self.gate = threading.Lock()
        self.cancelled = threading.Event()
        self.recording = None
        previous_jobs = self.library.list('job',limit=1)
        self.job = previous_jobs[0]['data'] if previous_jobs else None
        if self.job and self.job.get('status') == 'running':
            self.job.update(status='interrupted',stop_reason='server_restarted')
            self.library.put('job',self.job['kind'],self.job,self.job['id'])
        self.job_thread = None
        self.last_observation = None
        self.job_deadline = None

    @contextmanager
    def operation(self):
        if not self.gate.acquire(blocking=False):
            raise ScoutError('Another scout operation is running; use job_status or stop')
        try:
            self.cancelled.clear()
            yield
        finally:
            self.gate.release()

    def _active(self):
        if self.cancelled.is_set():
            raise ScoutError('Operation stopped')
        if not self.bridge.session:
            self.bridge.begin()
        state = self.bridge.state()
        if state.get('session') != self.bridge.session:
            self.bridge.release()
            return self.bridge.begin()
        return state

    def _view(self, save=False, name='Scout view', require_ready=True):
        timeout = 40 if self.job_deadline is None else min(40,max(0.1,self.job_deadline-time.monotonic()))
        image, evidence = self.images.frame(self.bridge.state,require_ready=require_ready,cancelled=self.cancelled.is_set,timeout=timeout)
        evidence['aspect'] = image.width/image.height
        self.last_observation = evidence
        result = {'observation':evidence,'preview_jpeg':self.images.preview(image)}
        if save:
            result['saved_image'] = self.images.save(image,evidence,name)
        return result

    def observe(self):
        # During a job, return the heartbeat without starting a competing WGC session.
        if self.gate.locked():
            return {'state':self.bridge.state(),'job':self.job}
        with self.operation():
            return self._view(require_ready=False)

    def begin(self, hide_hud=True):
        with self.operation():
            self.bridge.begin(hide_hud)
            return self._view()

    def end(self):
        with self.operation():
            return self.bridge.end()

    def stop(self):
        self.cancelled.set()
        self.bridge.stop()
        return {'stop_requested':True,'job':self.job}

    def job_status(self):
        return {'job':dict(self.job) if self.job else None,'recording_route_id':self.recording}

    def _append(self, pose, capture=False):
        if self.recording:
            record = self.library.get(self.recording)
            record['data']['waypoints'].append({'pose':pose,'capture':capture})
            self.library.put('route',record['name'],record['data'],record['id'])

    def _goto(self, pose, duration=2, allow_teleport=False, collision=True, record=True):
        self._active()
        pose = {**point(pose),'yaw':number(pose['yaw'],-36000,36000,'yaw')%360,
                'pitch':number(pose['pitch'],-85,85,'pitch')}
        duration = number(duration,0.1,10,'duration')
        current = self.bridge.state()['camera']
        length = distance(current,pose)
        if length>50 and not allow_teleport:
            raise ScoutError('Moves over 50 m require allow_teleport=true')
        timeout = 40 if self.job_deadline is None else min(40,max(0.1,self.job_deadline-time.monotonic()))
        result = self.bridge.command('pose',timeout=timeout,pose=pose,duration=duration,teleport=bool(allow_teleport),collision=bool(collision))
        self.library.visit(result['camera'])
        if record:
            self._append(result['camera'])
        return result

    def move(self, forward=0, right=0, up=0, duration=2, collision=True):
        with self.operation():
            current = self._active()['camera']
            forward, right, up = (number(v,-50,50,n) for v,n in [(forward,'forward'),(right,'right'),(up,'up')])
            y,p = math.radians(current['yaw']),math.radians(current['pitch'])
            target = {**current, 'x':current['x']-math.sin(y)*math.cos(p)*forward+math.cos(y)*right,
                      'y':current['y']+math.cos(y)*math.cos(p)*forward+math.sin(y)*right,
                      'z':current['z']+math.sin(p)*forward+up}
            self._goto(target,duration,collision=collision)
            return self._view()

    def go_to(self, pose=None, viewpoint_id=None, duration=2, allow_teleport=False, collision=True):
        with self.operation():
            if viewpoint_id:
                record = self.library.get(viewpoint_id)
                if record['kind'] != 'viewpoint':
                    raise ScoutError('viewpoint_id must identify a saved viewpoint')
                pose = record['data']['pose']
            if not pose:
                raise ScoutError('Specify pose or viewpoint_id')
            self._goto(pose,duration,allow_teleport,collision)
            return self._view()

    def look(self, yaw_delta=0, pitch_delta=0, target=None):
        with self.operation():
            pose = self._active()['camera']
            if target:
                pose = {**pose,**angles(pose,point(target))}
            else:
                pose = {**pose,'yaw':pose['yaw']+number(yaw_delta,-360,360,'yaw_delta'),
                        'pitch':pose['pitch']+number(pitch_delta,-85,85,'pitch_delta')}
            self._goto(pose,duration=0.2)
            return self._view()

    def inspect(self, u=0.5, v=0.5, range_m=100):
        with self.operation():
            self._active()
            if not self.last_observation:
                raise ScoutError('Observe first; inspect uses the latest image camera and aspect ratio')
            before = self.last_observation['state']
            current = self.bridge.state()
            if current['boot'] != before['boot'] or distance(current['camera'],before['camera'])>0.05 or abs((current['camera']['yaw']-before['camera']['yaw']+180)%360-180)>0.5 or abs(current['camera']['pitch']-before['camera']['pitch'])>0.5:
                raise ScoutError('Camera moved since the last image; observe again before inspecting')
            return self.bridge.command('inspect',u=number(u,0,1,'u'),v=number(v,0,1,'v'),
                range_m=number(range_m,0.1,500,'range_m'), camera=before['camera'],aspect=before.get('aspect',16/9))

    def capture(self, name='Scout capture'):
        with self.operation():
            self._active()
            result = self._view(save=True,name=name)
            self._append(result['observation']['state']['camera'],capture=True)
            return result

    def save_viewpoint(self, name, notes='', tags=None, location_id=None):
        with self.operation():
            self._active()
            if location_id and self.library.get(location_id)['kind'] != 'location':
                raise ScoutError('location_id must identify a location')
            result = self._view(save=True,name=name)
            record = self.library.put('viewpoint',name,{'pose':result['observation']['state']['camera'],
                'image_id':result['saved_image']['id'],'location_id':location_id,'notes':notes,'tags':tags or []})
            if location_id:
                location = self.library.get(location_id)
                location['data'].setdefault('viewpoint_ids',[]).append(record['id'])
                self.library.put('location',location['name'],location['data'],location_id)
            return {**result,'viewpoint':record}

    def save_location(self, name, description='', tags=None, viewpoint_ids=None, location_id=None):
        records = [self.library.get(v) for v in (viewpoint_ids or [])]
        if any(v['kind'] != 'viewpoint' for v in records):
            raise ScoutError('Every viewpoint ID must identify a viewpoint')
        if location_id and self.library.get(location_id)['kind'] != 'location':
            raise ScoutError('location_id must identify a location')
        return self.library.put('location',name,{'description':description,'tags':tags or [],'viewpoint_ids':[v['id'] for v in records]},location_id)

    def connect(self, from_id, to_id, kind, description='', bidirectional=True):
        for rid in (from_id,to_id):
            if self.library.get(rid)['kind'] != 'location':
                raise ScoutError('Connections join saved locations')
        if from_id == to_id:
            raise ScoutError('Connections require two different locations')
        return self.library.put('connection',kind,dict(from_id=from_id,to_id=to_id,kind=kind,description=description,bidirectional=bidirectional))

    def record_route(self, name=None):
        with self.operation():
            if name:
                if self.recording:
                    raise ScoutError('A route is already being recorded')
                pose = self._active()['camera']
                route = self.library.put('route',name,{'waypoints':[{'pose':pose,'capture':False}]})
                self.recording = route['id']
                return route
            if not self.recording:
                raise ScoutError('No route is being recorded')
            result = self.library.get(self.recording)
            self.recording = None
            return result

    def _sweep(self, yaw_offsets, pitch=None, save=True, name='Sweep'):
        origin = self._active()['camera']
        views, previews = [], []
        for offset in yaw_offsets:
            if self.cancelled.is_set():
                raise ScoutError('Operation stopped')
            pose = {**origin,'yaw':origin['yaw']+number(offset,-360,360,'yaw offset')}
            if pitch is not None:
                pose['pitch'] = number(pitch,-85,85,'pitch')
            self._goto(pose,0.2)
            view = self._view(save=save,name=f'{name} {offset:+g} deg')
            previews.append(view['preview_jpeg'])
            views.append({k:v for k,v in view.items() if k != 'preview_jpeg'})
        return {'views':views,'preview_jpegs':previews}

    def sweep(self, yaw_offsets=None, pitch=None, save=True):
        offsets = yaw_offsets or [-45,0,45]
        if not 1 <= len(offsets) <= 12:
            raise ScoutError('Sweep needs 1–12 headings')
        with self.operation():
            return self._sweep(offsets,pitch,save)

    def orbit(self, center, radius_m=5, height_m=0, count=4, save=True):
        center = point(center)
        radius_m = number(radius_m,1,20,'radius_m')
        height_m = number(height_m,-20,20,'height_m')
        count = int(number(count,2,12,'count'))
        with self.operation():
            origin = self._active()['camera']
            start = math.atan2(origin['y']-center['y'],origin['x']-center['x'])
            views, previews = [], []
            for step in range(count):
                theta = start+step*2*math.pi/count
                pose = {'x':center['x']+radius_m*math.cos(theta),'y':center['y']+radius_m*math.sin(theta),'z':center['z']+height_m}
                pose.update(angles(pose,center))
                try:
                    self._goto(pose,2)
                except ScoutError as error:
                    if 'blocked_path' not in str(error):
                        raise
                    views.append({'skipped':True,'reason':str(error),'pose':pose})
                    continue
                view = self._view(save=save,name=f'Orbit {step+1}')
                previews.append(view.pop('preview_jpeg'))
                views.append(view)
            return {'views':views,'preview_jpegs':previews}

    def start_job(self, kind, **options):
        if not self.gate.acquire(blocking=False):
            raise ScoutError('Another scout operation is running')
        self.cancelled.clear()
        try:
            self.job = {'id':identifier('job'),'kind':kind,'status':'running','completed':0,'records':[]}
            self.job['options'] = options
            self.library.put('job',kind,self.job,self.job['id'])
        except BaseException:
            self.gate.release()
            raise
        def run():
            try:
                if kind == 'replay':
                    self._replay(**options)
                else:
                    self._scout(**options)
                self.job['status'] = 'cancelled' if self.cancelled.is_set() else 'completed'
            except Exception as error:
                self.job.update(status='cancelled' if self.cancelled.is_set() else 'failed',error=str(error))
            finally:
                self.job_deadline = None
                try:
                    self.library.put('job',kind,self.job,self.job['id'])
                finally:
                    self.gate.release()
        self.job_thread = threading.Thread(target=run,daemon=True)
        try:
            self.job_thread.start()
        except BaseException:
            self.gate.release()
            raise
        return dict(self.job)

    def _replay(self, route_id, capture=True, allow_teleport=False, maximum_seconds=600, start_index=0):
        route = self.library.get(route_id)
        if route['kind'] != 'route':
            raise ScoutError('Replay needs a saved route')
        waypoints = route['data']['waypoints']
        if not 1 <= len(waypoints) <= 500:
            raise ScoutError('Routes must contain 1–500 waypoints')
        deadline = time.monotonic()+number(maximum_seconds,1,7200,'maximum_seconds')
        self.job_deadline = deadline
        start_index = int(number(start_index,0,len(waypoints)-1,'start_index'))
        self.job.update(route_id=route_id,next_index=start_index)
        for index,step in enumerate(waypoints[start_index:],start=start_index):
            if self.cancelled.is_set() or time.monotonic() >= deadline:
                if not self.cancelled.is_set():
                    self.job['stop_reason'] = 'time_budget'
                break
            self._goto(step['pose'],2,allow_teleport,record=False)
            if capture or step.get('capture'):
                view = self._view(save=True,name=route['name'])
                self.job['records'].append(view['saved_image']['id'])
            self.job['completed'] += 1
            self.job['next_index'] = index+1
            self.library.put('job','replay',self.job,self.job['id'])

    def _scout(self, maximum_steps=20, radius_m=100, step_m=8, maximum_seconds=600):
        maximum_steps = int(number(maximum_steps,1,100,'maximum_steps'))
        radius_m = number(radius_m,1,500,'radius_m')
        step_m = number(step_m,1,20,'step_m')
        deadline = time.monotonic()+number(maximum_seconds,1,3600,'maximum_seconds')
        self.job_deadline = deadline
        origin = self._active()['camera']
        route = self.library.put('route','Autonomous scout',{'waypoints':[{'pose':origin,'capture':True}],
            'strategy':'3D coverage novelty and collision clearance; model can inspect saved images for semantic choices'})
        self.job['route_id'] = route['id']
        for _ in range(maximum_steps):
            if self.cancelled.is_set() or time.monotonic() >= deadline:
                self.job['stop_reason'] = 'cancelled' if self.cancelled.is_set() else 'time_budget'
                break
            pose = self._active()['camera']
            candidates = []
            for offset in (0,-45,45,-90,90,180):
                yaw = (pose['yaw']+offset)%360
                target = {**pose,'x':pose['x']-math.sin(math.radians(yaw))*step_m,
                          'y':pose['y']+math.cos(math.radians(yaw))*step_m,'yaw':yaw,'pitch':0}
                if distance(origin,target)<=radius_m:
                    candidates.append((self.library.visits(target),abs(offset),target))
            moved = False
            for _,_,target in sorted(candidates,key=lambda c:(c[0],c[1])):
                try:
                    self._goto(target,2,record=False)
                    moved = True
                    break
                except ScoutError as error:
                    if 'blocked_path' not in str(error):
                        raise
            if not moved:
                self.job['stop_reason'] = 'no_clear_frontier'; break
            view = self._view(save=True,name='Autonomous scout')
            self.job['records'].append(view['saved_image']['id'])
            route['data']['waypoints'].append({'pose':view['observation']['state']['camera'],'capture':True})
            self.library.put('route',route['name'],route['data'],route['id'])
            self.job.update(completed=self.job['completed']+1,route_id=route['id'])
            self.library.put('job','scout',self.job,self.job['id'])
