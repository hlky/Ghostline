"""Small file transport, ownership lease, geometry and persistent scout library."""
from __future__ import annotations

from contextlib import ExitStack, contextmanager
from datetime import UTC, datetime
import json
import math
import os
from pathlib import Path
import sqlite3
import threading
import time
import uuid


class ScoutError(RuntimeError):
    pass


def now():
    return datetime.now(UTC).isoformat()


def identifier(prefix):
    return prefix + '_' + uuid.uuid4().hex


def atomic_json(path: Path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + '.' + uuid.uuid4().hex + '.tmp')
    try:
        temporary.write_text(json.dumps(value, allow_nan=False), encoding='utf-8')
        for attempt in range(20):
            try:
                os.replace(temporary, path)
                break
            except PermissionError:
                if attempt == 19:
                    raise
                time.sleep(0.01)
    finally:
        temporary.unlink(missing_ok=True)


def read_json(path: Path):
    for _ in range(3):
        try:
            return json.loads(path.read_text(encoding='utf-8'))
        except (FileNotFoundError, PermissionError, json.JSONDecodeError):
            time.sleep(0.005)
    raise ScoutError(f'No readable runtime data: {path}. Load the Game Scout CET mod.')


def number(value, minimum, maximum, name):
    if isinstance(value, bool) or not isinstance(value, (float, int)) or not math.isfinite(value) or not minimum <= value <= maximum:
        raise ScoutError(f'{name} must be finite and between {minimum} and {maximum}')
    return float(value)


def point(value):
    return {a: number(value[a], -100000, 100000, a) for a in 'xyz'}


def distance(a, b):
    return math.sqrt(sum((a[k]-b[k])**2 for k in 'xyz'))


def angles(origin, target):
    delta = {k: target[k]-origin[k] for k in 'xyz'}
    if distance(origin, target) < 0.01:
        raise ScoutError('Look-at target is at the camera origin')
    return dict(yaw=math.degrees(math.atan2(-delta['x'], delta['y'])) % 360,
                pitch=math.degrees(math.atan2(delta['z'], math.hypot(delta['x'], delta['y']))))


def cell(pose, size=8):
    # Full 3D cells keep balconies and spaces under bridges distinct.
    return ':'.join(str(math.floor(pose[a]/size)) for a in 'xyz')


@contextmanager
def file_lock(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a+b') as stream:
        stream.seek(0, 2)
        if stream.tell() == 0:
            stream.write(b'0'); stream.flush()
        stream.seek(0)
        try:
            if os.name == 'nt':
                import msvcrt
                msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as error:
            raise ScoutError(f'Another controller owns the game ({path})') from error
        try:
            yield
        finally:
            if os.name == 'nt':
                stream.seek(0)
                msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(stream, fcntl.LOCK_UN)


class Bridge:
    def __init__(self, runtime: Path, competing_lock: Path | None = None):
        self.root, self.competing_lock = runtime, competing_lock
        self.session = None
        self.stack = None
        self._cancel = threading.Event()
        self._closed = threading.Event()
        self._requests = threading.Lock()
        self._lifecycle = threading.RLock()
        self._pulse = threading.Thread(target=self._heartbeat, daemon=True)
        self._pulse.start()

    def state(self):
        state = read_json(self.root/'state.json')
        if state.get('protocol') != 1 or time.time()-state.get('timestamp', 0) > 4:
            raise ScoutError('Game Scout heartbeat is stale or incompatible; reload its CET mod')
        return state

    def _heartbeat(self):
        while not self._closed.wait(0.5):
            if self.session and not self._cancel.is_set():
                try:
                    atomic_json(self.root/'lease.json', {'session':self.session, 'timestamp':time.time()})
                except OSError:
                    pass

    def begin(self, hide_hud=True):
        if self.session:
            state = self.state()
            if state.get('session') == self.session and not self._cancel.is_set():
                return state
            if state.get('session') == self.session:
                raise ScoutError('Stop is being processed; wait for the runtime to release control')
            self.release()
        stack = ExitStack()
        try:
            stack.enter_context(file_lock(self.root/'controller.lock'))
            if self.competing_lock:
                stack.enter_context(file_lock(self.competing_lock))
            state = self.state()
            if state.get('session'):
                # Owning the OS locks proves no live controller owns this
                # leftover game session. Release it before taking a new lease.
                atomic_json(self.root/'stop.json',{'session':state['session'],'id':identifier('stop')})
                deadline = time.monotonic()+1.5
                while self.state().get('session') and time.monotonic()<deadline:
                    time.sleep(0.025)
                if self.state().get('session'):
                    raise ScoutError('Waiting for an abandoned game session to release control')
            self.session = identifier('session')
            self._cancel.clear()
            atomic_json(self.root/'lease.json', {'session':self.session, 'timestamp':time.time()})
            self.stack = stack
            return self.command('begin', hide_hud=hide_hud)
        except BaseException:
            self.session = None
            self.stack = None
            stack.close()
            raise

    def command(self, kind, timeout=40, **arguments):
        if not self.session:
            raise ScoutError('Begin a scouting session first')
        with self._requests:
            if self._cancel.is_set() and kind != 'end':
                raise ScoutError('Operation stopped')
            state = self.state()
            request = {'id':identifier('command'), 'boot':state['boot'], 'session':self.session,
                       'kind':kind, 'arguments':arguments, 'expires':time.time()+timeout}
            atomic_json(self.root/'command.json', request)
            deadline = time.monotonic()+timeout
            while time.monotonic() < deadline:
                if self._cancel.is_set() and kind != 'end':
                    raise ScoutError('Operation stopped')
                try:
                    response = read_json(self.root/'response.json')
                except ScoutError:
                    response = {}
                if response.get('id') == request['id']:
                    if response.get('session') != self.session or response.get('boot') != request['boot']:
                        raise ScoutError('Stale command response')
                    if not response.get('ok'):
                        raise ScoutError(response.get('error', 'Game command failed'))
                    return response['result']
                current = self.state()
                if current['boot'] != request['boot']:
                    raise ScoutError('CET restarted during the operation')
                time.sleep(0.025)
            self.stop()
            raise ScoutError(f'{kind} timed out; stop requested')

    def stop(self):
        self._cancel.set()
        if self.session:
            session = self.session
            try:
                atomic_json(self.root/'stop.json', {'session':session, 'id':identifier('stop')})
            except OSError:
                # Stop renewing the lease even if Windows refuses the stop file.
                # The game-side watchdog then releases camera control within 5 s.
                pass
            def release_after_stop():
                deadline = time.monotonic()+6
                while self.session == session and time.monotonic() < deadline:
                    try:
                        if self.state().get('session') != session:
                            break
                    except ScoutError:
                        pass
                    time.sleep(0.05)
                with self._lifecycle:
                    if self.session == session:
                        self.release()
            threading.Thread(target=release_after_stop,daemon=True).start()

    def release(self):
        with self._lifecycle:
            self.session = None
            if self.stack:
                self.stack.close()
                self.stack = None

    def end(self):
        try:
            if self.session and self.state().get('session') != self.session:
                return {'released':True}
            return self.command('end') if self.session else {'session':None}
        finally:
            self.release()

    def close(self):
        self.stop()
        self._closed.set()
        deadline = time.monotonic()+1
        while self.session and time.monotonic()<deadline:
            try:
                if self.state().get('session') != self.session:
                    break
            except ScoutError:
                break
            time.sleep(0.025)
        self.release()


class Library:
    def __init__(self, root: Path):
        self.root = root
        root.mkdir(parents=True, exist_ok=True)
        self.path = root/'scout.sqlite3'
        with self.connect() as db:
            db.executescript('''
                CREATE TABLE IF NOT EXISTS records(
                    id TEXT PRIMARY KEY, kind TEXT NOT NULL, name TEXT NOT NULL,
                    created_at TEXT NOT NULL, updated_at TEXT NOT NULL, data TEXT NOT NULL);
                CREATE INDEX IF NOT EXISTS record_kind ON records(kind);
                CREATE TABLE IF NOT EXISTS coverage(
                    cell TEXT NOT NULL, heading INTEGER NOT NULL, visits INTEGER NOT NULL,
                    last_at TEXT NOT NULL, PRIMARY KEY(cell,heading));
            ''')

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.path, timeout=10)
        try:
            with db:
                yield db
        finally:
            db.close()

    def put(self, kind, name, data, record_id=None):
        rid = record_id or identifier(kind)
        with self.connect() as db:
            db.execute('''INSERT INTO records VALUES(?,?,?,?,?,?) ON CONFLICT(id)
                DO UPDATE SET name=excluded.name,updated_at=excluded.updated_at,data=excluded.data''',
                (rid, kind, name, now(), now(), json.dumps(data, allow_nan=False)))
        return self.get(rid)

    def get(self, rid):
        with self.connect() as db:
            row = db.execute('SELECT id,kind,name,created_at,updated_at,data FROM records WHERE id=?',(rid,)).fetchone()
        if row is None:
            raise ScoutError(f'Unknown library ID: {rid}')
        return dict(zip(('id','kind','name','created_at','updated_at','data'), (*row[:5],json.loads(row[5]))))

    def list(self, kind=None, query='', limit=50):
        limit = int(number(limit, 1, 200, 'limit'))
        with self.connect() as db:
            rows = db.execute('''SELECT id FROM records WHERE (? IS NULL OR kind=?)
                AND (instr(lower(name),lower(?))>0 OR instr(lower(data),lower(?))>0)
                ORDER BY updated_at DESC LIMIT ?''',(kind,kind,query,query,limit)).fetchall()
        return [self.get(row[0]) for row in rows]

    def visit(self, pose):
        heading = int((pose['yaw']%360)/45)
        with self.connect() as db:
            db.execute('''INSERT INTO coverage VALUES(?,?,1,?) ON CONFLICT(cell,heading)
                DO UPDATE SET visits=visits+1,last_at=excluded.last_at''',(cell(pose),heading,now()))

    def visits(self, pose):
        with self.connect() as db:
            return db.execute('SELECT coalesce(sum(visits),0) FROM coverage WHERE cell=?',(cell(pose),)).fetchone()[0]

    def coverage(self, limit=200):
        limit = int(number(limit,1,1000,'limit'))
        with self.connect() as db:
            rows = [dict(zip(('cell','heading','visits','last_at'),r)) for r in db.execute('SELECT * FROM coverage ORDER BY last_at DESC LIMIT ?',(limit,))]
            total = db.execute('SELECT count(DISTINCT cell),coalesce(sum(visits),0) FROM coverage').fetchone()
        return {'cell_size_m':8,'heading_sector_degrees':45,'unique_cells':total[0],'total_visits':total[1],'cells':rows}

    def export(self):
        with self.connect() as db:
            ids = [r[0] for r in db.execute('SELECT id FROM records ORDER BY created_at')]
            coverage = [dict(zip(('cell','heading','visits','last_at'),r)) for r in db.execute('SELECT * FROM coverage')]
        destination = self.root/'exports'/f'{identifier("scout")}.json'
        atomic_json(destination, {'schema_version':1,'exported_at':now(), 'records':[self.get(r) for r in ids], 'coverage':coverage})
        return str(destination)
