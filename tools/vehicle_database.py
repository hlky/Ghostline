"""Build, preview and browse the local Ghostline vehicle database."""
from __future__ import annotations

import argparse
from contextlib import closing
import hashlib
import http.server
import json
from pathlib import Path
import shutil
import subprocess
import sys
import urllib.parse
import webbrowser

from PIL import Image

from item_catalog import extract_localization
from toolchain import default_tool_path
from vehicle_catalog import VehicleError, build, connect, query, summary
from vehicle_previews import Resources, extract_previews

ROOT = Path(__file__).resolve().parents[1]
GALLERY = ROOT / 'tools/vehicle_gallery'
DEFAULT_OUTPUT = ROOT / 'converted/vehicle-database'


class GalleryHandler(http.server.SimpleHTTPRequestHandler):
    database: Path
    output: Path

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(GALLERY), **kwargs)

    def send_json(self, value, status=200):
        body = json.dumps(value, ensure_ascii=False, allow_nan=False).encode()
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        try:
            if parsed.path == '/api/summary':
                with closing(connect(self.database)) as db:
                    result = summary(db)
                    tables = {r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
                    result['appearance_variants'] = db.execute('SELECT count(*) FROM vehicle_variants').fetchone()[0] if 'vehicle_variants' in tables else 0
                    result['rendered_variants'] = db.execute('SELECT count(*) FROM variant_previews JOIN vehicle_variants USING(variant_id)').fetchone()[0] if 'variant_previews' in tables else 0
                    self.send_json(result)
                return
            if parsed.path == '/api/vehicles':
                params = urllib.parse.parse_qs(parsed.query)
                get = lambda key, default='': params.get(key, [default])[0]
                limit, offset = int(get('limit', '48')), int(get('offset', '0'))
                if not 1 <= limit <= 200 or not 0 <= offset <= 100000:
                    raise VehicleError('Invalid page range')
                with closing(connect(self.database)) as db:
                    selected_query = query
                    if get('variants') == '1':
                        from vehicle_variants import query_variants
                        selected_query = query_variants
                    result = selected_query(db, get('q'), get('manufacturer'), get('type'), get('player') == '1',
                                   get('rendered') == '1', get('sort', 'name'), limit, offset,
                                   preview_kind='studio' if get('studio') == '1' else '')
                def image_url(filename):
                    if filename:
                        path = Path(filename).resolve()
                        if path.is_relative_to(self.output.resolve()) and path.is_file():
                            return '/images/' + urllib.parse.quote(path.relative_to(self.output.resolve()).as_posix())
                    return None
                for row in result['vehicles']:
                    row['image_url'] = image_url(row['preview_path'])
                    row['image_views'] = {name: url for name, filename in
                                          (row.get('preview_metadata') or {}).get('images', {}).items()
                                          if (url := image_url(filename))}
                    row.pop('preview_path', None)
                self.send_json(result)
                return
            if parsed.path.startswith('/images/'):
                path = (self.output / urllib.parse.unquote(parsed.path[len('/images/'):])).resolve()
                if not path.is_relative_to(self.output.resolve()) or path.suffix.lower() not in ('.png', '.jpg', '.jpeg', '.webp'):
                    self.send_error(403); return
                if not path.is_file():
                    self.send_error(404); return
                body = path.read_bytes()
                self.send_response(200)
                self.send_header('Content-Type', {'.png': 'image/png', '.webp': 'image/webp'}.get(path.suffix.lower(), 'image/jpeg'))
                self.send_header('Content-Length', str(len(body)))
                self.end_headers(); self.wfile.write(body)
                return
            if parsed.path not in ('/', '/index.html', '/app.js', '/style.css', '/favicon.ico'):
                self.send_error(404); return
            super().do_GET()
        except (ValueError, VehicleError) as exc:
            self.send_json({'error': str(exc)}, 400)


def serve(output, host, port, open_browser=False):
    if host not in ('127.0.0.1', 'localhost'):
        raise VehicleError('Vehicle gallery only binds to loopback')
    database = output / 'vehicles.sqlite3'
    if not database.exists():
        raise VehicleError('Build the vehicle database first')
    handler = type('VehicleGallery', (GalleryHandler,), {'database': database, 'output': output})
    server = http.server.ThreadingHTTPServer((host, port), handler)
    url = f'http://{host}:{server.server_port}'
    print(f'Vehicle database: {url}', flush=True)
    if open_browser:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


def attach_preview(output, record_id, image_path):
    if image_path.suffix.lower() not in ('.png', '.jpg', '.jpeg', '.webp'):
        raise VehicleError('Studio previews must be PNG, JPEG or WebP images')
    with connect(output / 'vehicles.sqlite3') as db:
        if not db.execute('SELECT 1 FROM vehicles WHERE record_id=?', (record_id,)).fetchone():
            raise VehicleError('Unknown vehicle record')
        with Image.open(image_path) as image:
            image.verify()
        destination = output / 'previews' / (hashlib.sha256(image_path.read_bytes()).hexdigest() + image_path.suffix.lower())
        destination.parent.mkdir(parents=True, exist_ok=True)
        if image_path.resolve() != destination.resolve():
            shutil.copy2(image_path, destination)
        db.execute('INSERT OR REPLACE INTO previews VALUES(?,?,?,?)',
                   (record_id, str(destination.resolve()), 'studio', json.dumps({'source': str(image_path.resolve())})))
    return {'record_id': record_id, 'path': str(destination.resolve()), 'kind': 'studio'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument('--gamepath', type=Path, default=default_tool_path('game'))
    commands = parser.add_subparsers(dest='command', required=True)
    builder = commands.add_parser('build')
    builder.add_argument('--localization', type=Path, action='append', default=[])
    builder.add_argument('--extract-localization', action='store_true')
    builder.add_argument('--ghostline-red', type=Path, default=default_tool_path('ghostline_red'))
    builder.add_argument('--schema', type=Path, default=ROOT / 'red-schema.json')
    previews = commands.add_parser('previews')
    previews.add_argument('--ghostline-red', type=Path, default=default_tool_path('ghostline_red'))
    previews.add_argument('--schema', type=Path, default=ROOT / 'red-schema.json')
    previews.add_argument('--wolvenkit', type=Path, default=default_tool_path('wolvenkit'))
    attach = commands.add_parser('attach-preview')
    attach.add_argument('--record', required=True)
    attach.add_argument('--image', type=Path, required=True)
    renders = commands.add_parser('render', help='Render exact vehicle game models; defaults to player variants')
    renders.add_argument('--record', action='append', default=[])
    renders.add_argument('--all', action='store_true', dest='all_vehicles')
    renders.add_argument('--workers', type=int, default=4)
    renders.add_argument('--device', choices=['cpu', 'hip'], default='cpu')
    renders.add_argument('--resolution', type=int, default=1536)
    renders.add_argument('--views', default=None)
    renders.add_argument('--ghostline-red', type=Path, default=default_tool_path('ghostline_red'))
    renders.add_argument('--schema', type=Path, default=ROOT / 'red-schema.json')
    renders.add_argument('--blender', type=Path, default=default_tool_path('blender'))
    renders.add_argument('--wolvenkit', type=Path, default=default_tool_path('wolvenkit'))
    browser = commands.add_parser('serve')
    browser.add_argument('--host', default='127.0.0.1')
    browser.add_argument('--port', type=int, default=8767)
    browser.add_argument('--open', action='store_true')
    args = parser.parse_args()
    output, game = args.output.resolve(), args.gamepath.resolve()
    try:
        if args.command == 'build':
            paths = args.localization
            if args.extract_localization:
                paths = [*paths, *extract_localization(output / 'cache', default_tool_path('wolvenkit'), game)]
            if not paths:
                paths = [p for p in (ROOT / 'converted/item-database/cache/localization').glob('*/serialized/onscreens.json.json')]
            print(json.dumps(build(game, output, paths, speed_tools={
                'red': args.ghostline_red.resolve(), 'schema': args.schema.resolve(),
            }), indent=2))
        elif args.command == 'previews':
            resources = Resources(game, output, args.ghostline_red.resolve(), args.schema.resolve(), args.wolvenkit.resolve())
            result = extract_previews(output / 'vehicles.sqlite3', output, resources)
            print(json.dumps(result, indent=2))
            return int(bool(result['failures']))
        elif args.command == 'attach-preview':
            print(json.dumps(attach_preview(output, args.record, args.image), indent=2))
        elif args.command == 'render':
            from vehicle_variant_render import render_variant_batch
            result = render_variant_batch(output, game, args.ghostline_red.resolve(), args.schema.resolve(),
                                          args.blender.resolve(), args.wolvenkit.resolve(), records=args.record,
                                          all_vehicles=args.all_vehicles, resolution=args.resolution,
                                          views=args.views or ('hero' if args.all_vehicles else 'hero,front,back,left'),
                                          workers=args.workers, device=args.device)
            print(json.dumps(result, indent=2))
            return int(bool(result['failures']))
        else:
            serve(output, args.host, args.port, args.open)
    except (VehicleError, ValueError, OSError, subprocess.CalledProcessError) as exc:
        print(f'error: {exc}', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
