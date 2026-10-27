# Building Lab frontend

React 19, strict TypeScript, Tailwind 4 and Vite. This is the actual editor,
using the existing Python API and building compiler, not a separate mockup.
The local production URL remains `http://127.0.0.1:8792`.

## Run

From the repository root, with Node 20.17+ (the tested local runtime):

```powershell
npm ci --prefix tools/building_ui --ignore-scripts
npm run build --prefix tools/building_ui
.venv/Scripts/python.exe -B tools/building_ui.py --port 8792
```

For hot reload, keep the Python backend running and use
`npm run dev --prefix tools/building_ui`. Open loopback port 5174. Its proxy
forwards only the existing local API, geometry and export paths. Production
serves the built `dist` through Python; it needs no Node server. `dist` and
`node_modules` are generated and ignored. Rebuild after editing the frontend.
Vite 6 is intentional for the repository's Node 20.17 runtime. Upgrade that
runtime before selecting a Vite major that requires Node 20.19+.

## Ownership

| File | Responsibility |
| --- | --- |
| `src/types.ts` | Layout, compiled scene, workstation, library and editor contracts. Extension data remains intact. |
| `src/api.ts` | JSON request errors, IDs, display names and downloads. |
| `src/store.ts` | Serialized compile/save/load/edit transactions, undo/redo, browser drafts, selection and saved state. No DOM access. |
| `src/App.tsx` | Workspace composition, scene tree, tools, shortcuts and panel navigation. |
| `src/components/Inspector.tsx` | Selection properties, worker binding, project transfer and advanced navigation. |
| `src/components/Library.tsx` | Debounced, abortable search, asset selection, dimensions and appearance choice. |
| `src/components/Dialogs.tsx` | Native export lifecycle, origin, routes, surveyed shell patches and new-layout confirmation. |
| `src/components/primitives.tsx` | Shared accessible controls, draft-field commits and native modal focus management. |
| `src/components/Canvas.tsx` | React lifecycle boundary for the plan, building renderer and asset preview. |
| `src/plan-adapter.js` | Retained measured SVG drawing and pointer interactions; owns only the SVG children/listeners. |
| `viewer.js` | Retained Three.js geometry renderer and cache; explicit disposal on unmount. |
| `wall-controls.js` | Existing pure authoring operations used by both the canvas and tests. |
| `src/styles.css` | Tailwind theme, reusable chrome classes, responsive layout and SVG appearance. |

React owns the UI and state. The retained drawing/rendering adapters are
JavaScript, with `allowJs` at this boundary; the React application, API, store
and data contracts are checked with strict TypeScript. Do not reintroduce
document-wide ID bindings or a second mutable UI controller. A renderer may
manipulate its own canvas/SVG subtree, never React-owned forms or panels.
The former app controller and CSS are removed from active source; local
baseline copies are under the migration evidence directory.

All layout mutations go through `store.mutate`, then the Python compile API.
Failed compilation retains the previous scene/history. Save, open, import and
history operations share the mutation queue to prevent stale response races.
New layouts start with explicit authoring fields, clearing inherited shell
removals, resource overrides and workstation actors. Future controls must
preserve unknown layout extensions, native NodeRefs and source hash pins.
No browser code installs packages into Cyberpunk.

## Checks

```powershell
npm run typecheck --prefix tools/building_ui
npm run test --prefix tools/building_ui
npm run format:check --prefix tools/building_ui
npm run build --prefix tools/building_ui
.venv/Scripts/python.exe -B -m unittest discover -s tests -p 'test_building*.py'
```

The frontend tests cover transaction ordering, failed edits, undo/redo, saved
state, extension preservation, new-layout isolation and corrupt-draft recovery.
The shared wall tests cover removing incompatible door state and reversible
wall openings. The Python suite owns compilation, source and export contracts.
Browser smoke testing must also cover loaded game geometry, selected-object
editing, invalid-room recovery, drawing, library preview, saving and native
export completion. Successful native export does not prove in-game behavior.

## UX review and evidence

See [the UX review](../../docs/authoring/building-editor-ux-review.md).
Local capture/readback evidence lives under
`projects/experiments/building-lab/generated/react-migration`.
The initial React native-export proof is
`generated/building-editor/exports/9b370777bfd3`, with eight native readbacks.
No installed game payload was changed by this migration.
