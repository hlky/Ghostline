import { useEffect, useState, useSyncExternalStore } from "react";
import {
  Box,
  Blocks,
  FolderOpen,
  Workflow,
  MousePointer2,
  Square,
  DoorOpen,
  MoveHorizontal,
  Columns2,
  Layers,
  Undo2,
  Redo2,
  Save,
  Download,
  Library as LibraryIcon,
  MapPin,
  Plus,
  ChevronRight,
  Check,
  LoaderCircle,
  PanelLeftClose,
  PanelLeftOpen,
} from "lucide-react";
import type { EditorStore } from "./store";
import type { Tool } from "./types";
import { pretty } from "./api";
import { Button, Field, Section, Select } from "./components/primitives";
import { Inspector, ProjectPanel } from "./components/Inspector";
import { Plan, Geometry } from "./components/Canvas";
import { Library } from "./components/Library";
import { EditorDialog } from "./components/Dialogs";
const tools: {
  id: Tool;
  name: string;
  icon: typeof Square;
  shortcut: string;
}[] = [
  { id: "select", name: "Select", icon: MousePointer2, shortcut: "1" },
  { id: "room", name: "Draw room", icon: Square, shortcut: "2" },
  { id: "doorway", name: "Doorway", icon: DoorOpen, shortcut: "3" },
  { id: "passage", name: "Open bay", icon: MoveHorizontal, shortcut: "4" },
  { id: "door_auto", name: "Auto door", icon: DoorOpen, shortcut: "5" },
  { id: "door_manual", name: "Manual door", icon: DoorOpen, shortcut: "6" },
  { id: "stair", name: "Stairs", icon: Layers, shortcut: "7" },
  { id: "wall", name: "Walls", icon: Columns2, shortcut: "8" },
];
const hints: Record<Tool, string> = {
  select:
    "Select a room or object. Drag rooms to move; use the corner to resize.",
  room: "Drag on the grid to draw a room in 3 m steps.",
  doorway: "Click a wall bay to add a doorway. Click again to restore it.",
  passage: "Click a wall bay to open it. Click again to close it.",
  door_auto: "Click a wall bay to place an automatic door.",
  door_manual: "Click a wall bay to place an interactive door.",
  stair:
    "Click the south-west corner of a 3 × 9 m flight. Both floors need landings.",
  wall: "Click a wall to inspect it, or two empty grid points to draw a partition.",
  partition: "Click two endpoints to draw a partition. Escape cancels.",
  module: "Click the plan to place the chosen object at its original size.",
};
export default function App({ store }: { store: EditorStore }) {
  const s = useSyncExternalStore(store.subscribe, store.getSnapshot),
    [dialog, setDialog] = useState(""),
    [objectSearch, setObjectSearch] = useState(""),
    [showInspector, setShowInspector] = useState(true);
  useEffect(() => {
    store.init();
  }, [store]);
  useEffect(() => {
    function key(e: KeyboardEvent) {
      if (document.querySelector("dialog[open]")) return;
      const typing = (e.target as HTMLElement)?.closest(
        'input,select,textarea,[contenteditable="true"]',
      );
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "s") {
        e.preventDefault();
        // Commit the focused draft field before enqueueing the save request.
        (document.activeElement as HTMLElement | null)?.blur();
        store.save();
        return;
      }
      if (typing || !s.layout) return;
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "z") {
        e.preventDefault();
        store.history(e.shiftKey ? "redo" : "undo");
      } else if (e.key === "Escape") {
        store.tool("select");
        store.patch({ drag: null });
      } else if (tools.some((t) => t.shortcut === e.key))
        store.tool(tools.find((t) => t.shortcut === e.key)!.id);
      else if (e.key === "Delete") {
        if (s.selectedModule) {
          const m = s.layout.modules.find((m) => m.id === s.selectedModule);
          if (m?.reference_only) return;
          store.mutate((d) => {
            d.modules = d.modules.filter((m) => m.id !== s.selectedModule);
          }, "Object removed");
        } else if (s.selected)
          store.mutate((d) => {
            d.rooms = d.rooms.filter((r) => r.id !== s.selected);
          }, "Room removed");
      }
    }
    window.addEventListener("keydown", key);
    return () => window.removeEventListener("keydown", key);
  }, [s, store]);
  if (!s.layout || !s.scene)
    return (
      <div className="grid h-screen place-items-center bg-app p-8">
        <div role="status" className="text-center">
          <Blocks className="mx-auto mb-4 text-accent" size={32} />
          <h1 className="text-xl">Building Lab</h1>
          <p className={`mt-3 ${s.error ? "text-red-300" : "text-slate-400"}`}>
            {s.message}
          </p>
          {s.error && (
            <Button className="mt-4" onClick={store.init}>
              Retry
            </Button>
          )}
        </div>
      </div>
    );
  const l = s.layout,
    scene = s.scene;
  const selectRoom = (id: string) => {
    store.patch({
      selected: id,
      selectedModule: null,
      door: null,
      tab: "build",
    });
    store.tool("select");
  };
  const modules = l.modules?.filter((m) => m.level === s.level) || [];
  const references = modules.filter((m) => m.reference_only);
  const placed = modules.filter((m) => !m.reference_only);
  return (
    <div className="app-shell">
      <header className="app-header">
        <a href="#workspace" className="skip-link">
          Skip to workspace
        </a>
        <div className="flex items-center gap-3">
          <div className="grid h-9 w-9 place-items-center rounded-lg border border-accent/30 bg-accent/10 text-accent">
            <Blocks size={21} />
          </div>
          <div>
            <h1 className="text-sm font-semibold tracking-wide">
              BUILDING LAB
            </h1>
            <span className="text-[10px] uppercase tracking-[.2em] text-slate-500">
              Ghostline / World authoring
            </span>
          </div>
        </div>
        <div className="min-w-0 flex-1 px-5">
          <Field
            label="Building name"
            value={l.name}
            onCommit={(v) =>
              store.mutate((d) => {
                d.name = v;
              }, "Building renamed")
            }
          />
        </div>
        <span className="save-label" role="status">
          {s.busy ? (
            <LoaderCircle size={13} className="animate-spin" />
          ) : (
            <Check size={13} />
          )}{" "}
          {s.busy ? "Working…" : s.dirty ? "Unsaved draft" : "Saved to project"}
        </span>
        <div className="flex items-center gap-2">
          <Button
            title="Undo (Ctrl+Z)"
            disabled={!s.undo.length || s.busy}
            onClick={() => store.history("undo")}
          >
            <Undo2 size={16} />
          </Button>
          <Button
            title="Redo (Ctrl+Shift+Z)"
            disabled={!s.redo.length || s.busy}
            onClick={() => store.history("redo")}
          >
            <Redo2 size={16} />
          </Button>
          <Button disabled={s.busy} onClick={store.save}>
            <Save size={15} />
            <span>Save</span>
          </Button>
          <Button primary disabled={s.busy} onClick={() => setDialog("export")}>
            <Download size={15} />
            Export
          </Button>
        </div>
      </header>
      <nav className="mode-rail" aria-label="Editor panels">
        {(
          [
            { id: "build", label: "Build", icon: Blocks },
            { id: "objects", label: "Objects", icon: Box },
            { id: "quest", label: "Quest", icon: Workflow },
            { id: "project", label: "Project", icon: FolderOpen },
          ] as const
        ).map((t) => (
          <button
            key={t.id}
            className={`mode-button ${s.tab === t.id ? "active" : ""}`}
            aria-pressed={s.tab === t.id}
            onClick={() => store.patch({ tab: t.id })}
          >
            <t.icon size={21} />
            <span>{t.label}</span>
          </button>
        ))}
      </nav>
      <aside className="scene-panel" aria-label="Scene and tools">
        <div className="panel-heading">
          <h2>{pretty(s.tab)}</h2>
          <span className="badge">
            {s.level === 0 ? "Ground" : `Floor ${s.level + 1}`}
          </span>
        </div>
        {s.tab === "project" ? (
          <ProjectPanel state={s} store={store} open={setDialog} />
        ) : (
          <>
            {s.tab === "build" && (
              <>
                <Section title="Construction tools">
                  <div className="grid grid-cols-2 gap-2">
                    {tools.map((t) => (
                      <button
                        key={t.id}
                        className={`tool-button ${s.tool === t.id ? "active" : ""}`}
                        aria-pressed={s.tool === t.id}
                        onClick={() => store.tool(t.id)}
                      >
                        <t.icon size={16} />
                        <span>{t.name}</span>
                        <kbd>{t.shortcut}</kbd>
                      </button>
                    ))}
                  </div>
                  <p className="hint mt-3">{hints[s.tool]}</p>
                  {s.tool === "wall" && (
                    <Button
                      className="mt-3 w-full"
                      onClick={() => store.tool("partition")}
                    >
                      Draw partition
                    </Button>
                  )}
                  <Button
                    className="mt-3 w-full"
                    disabled={!l.stairs.some((x) => x.level === s.level)}
                    onClick={() =>
                      store.mutate((d) => {
                        const i = d.stairs.findLastIndex(
                          (x) => x.level === s.level,
                        );
                        if (i >= 0) d.stairs.splice(i, 1);
                      }, "Stair flight removed")
                    }
                  >
                    Remove last stair flight
                  </Button>
                </Section>
                <Section title="Room kit">
                  <Select
                    label="Construction kit"
                    value={l.kit}
                    options={s.catalogs.map((k) => ({
                      value: k.id,
                      label: k.name,
                    }))}
                    onChange={(id) => {
                      const k = s.catalogs.find((k) => k.id === id)!;
                      store.mutate((d) => {
                        d.kit = id;
                        d.wall_appearance = k.wall_appearances[0];
                        if (!k.floor_appearances.includes(d.floor_appearance))
                          d.floor_appearance = k.floor_appearances[0];
                      }, "Kit changed");
                    }}
                  />
                </Section>
              </>
            )}
            {s.tab === "objects" && (
              <Section title="Add to your building">
                <Button
                  primary
                  className="w-full"
                  onClick={() => setDialog("library")}
                >
                  <LibraryIcon size={16} />
                  Browse module library
                </Button>
                <p className="hint mt-3">
                  Architecture, furniture and equipment. Place measured geometry
                  without resizing it.
                </p>
              </Section>
            )}
            {s.tab === "quest" && (
              <Section title="Quest-ready spaces">
                <p className="hint">
                  Workstations connect chairs, actors and computers to stable
                  quest references. Select a fixture in the inspector to
                  configure its worker and activation.
                </p>
                <Button
                  className="mt-3 w-full"
                  onClick={() => setShowInspector(true)}
                >
                  Show quest inspector
                </Button>
              </Section>
            )}
            <Section
              title="Rooms"
              action={
                <Button
                  title="Draw another room"
                  onClick={() => store.tool("room")}
                >
                  <Plus size={14} />
                </Button>
              }
            >
              <div className="space-y-2">
                {l.rooms
                  .filter((r) => r.level === s.level)
                  .map((r) => (
                    <button
                      className={`scene-row ${s.selected === r.id && !s.selectedModule ? "selected" : ""}`}
                      key={r.id}
                      onClick={() => selectRoom(r.id)}
                    >
                      <Square size={15} />
                      <span className="min-w-0 flex-1">
                        <strong className="block truncate font-medium">
                          {r.name}
                        </strong>
                        <small>
                          {r.width} × {r.depth} m
                        </small>
                      </span>
                      <ChevronRight size={13} />
                    </button>
                  ))}
                {!l.rooms.some((r) => r.level === s.level) && (
                  <p className="hint">
                    No grid rooms on this floor. Draw a room or place a module
                    to begin.
                  </p>
                )}
              </div>
            </Section>
            <Section title={`Placed objects · ${placed.length}`}>
              <label className="field">
                <span className="sr-only">Filter placed objects</span>
                <input
                  aria-label="Filter placed objects"
                  placeholder="Find in this scene…"
                  value={objectSearch}
                  onChange={(e) => setObjectSearch(e.target.value)}
                />
              </label>
              <div className="space-y-1">
                {placed
                  .filter((m) =>
                    (
                      scene.instances.find((i) => i.id === "module:" + m.id)
                        ?.name || m.id
                    )
                      .toLowerCase()
                      .includes(objectSearch.toLowerCase()),
                  )
                  .map((m) => (
                    <button
                      key={m.id}
                      className={`scene-row ${s.selectedModule === m.id ? "selected" : ""}`}
                      onClick={() =>
                        store.patch({
                          selectedModule: m.id,
                          selected: null,
                          door: null,
                          tool: "select",
                          tab: "objects",
                        })
                      }
                    >
                      <Box size={14} />
                      <span className="min-w-0">
                        <strong className="block truncate font-normal">
                          {pretty(
                            scene.instances.find(
                              (i) => i.id === "module:" + m.id,
                            )?.name || m.id,
                          )}
                        </strong>
                        <small>{m.id}</small>
                      </span>
                    </button>
                  ))}
              </div>
              {references.length > 0 && (
                <details className="mt-4">
                  <summary>
                    {references.length} existing shell references
                  </summary>
                  {references.map((m) => (
                    <button
                      key={m.id}
                      className="scene-row mt-2"
                      onClick={() =>
                        store.patch({ selectedModule: m.id, selected: null })
                      }
                    >
                      <span className="truncate">{m.id} · Preview only</span>
                    </button>
                  ))}
                </details>
              )}
            </Section>
          </>
        )}
      </aside>
      <main id="workspace" className="workspace-main" tabIndex={-1}>
        <div className="workspace-toolbar">
          <Select
            label="Active floor"
            value={String(s.level)}
            onChange={(v) =>
              store.patch({
                level: Number(v),
                selected: null,
                selectedModule: null,
                door: null,
                fitVersion: s.fitVersion + 1,
              })
            }
            options={[0, 1, 2, 3].map((v) => ({
              value: String(v),
              label:
                v === 0
                  ? "01 · Ground"
                  : `${String(v + 1).padStart(2, "0")} · Upper`,
            }))}
          />
          <div className="view-tabs" role="group" aria-label="Workspace view">
            {(["plan", "split", "three"] as const).map((v) => (
              <button
                key={v}
                aria-pressed={s.view === v}
                onClick={() => store.patch({ view: v })}
              >
                {v === "three" ? "3D" : pretty(v)}
              </button>
            ))}
          </div>
          <Button
            className="anchor-button"
            title="Edit world placement"
            onClick={() => setDialog("origin")}
          >
            <MapPin size={14} />
            {[l.origin.x, l.origin.y, l.origin.z]
              .map((v) => v.toFixed(1))
              .join(", ")}
          </Button>
          <Button
            title={showInspector ? "Hide inspector" : "Show inspector"}
            onClick={() => setShowInspector(!showInspector)}
          >
            {showInspector ? (
              <PanelLeftClose size={16} />
            ) : (
              <PanelLeftOpen size={16} />
            )}
          </Button>
        </div>
        <div className={`canvas-grid ${s.view}`}>
          <div className={s.view === "three" ? "hidden" : "canvas-slot"}>
            <Plan state={s} store={store} />
          </div>
          <div className={s.view === "plan" ? "hidden" : "canvas-slot"}>
            <Geometry state={s} store={store} />
          </div>
        </div>
        <div className="tool-status">
          <MousePointer2 size={13} />
          <span>{hints[s.tool]}</span>
          <kbd>Esc · Select</kbd>
        </div>
      </main>
      {showInspector && <Inspector state={s} store={store} open={setDialog} />}
      <footer className="app-footer">
        <span className="flex items-center gap-2">
          <span className="h-1.5 w-1.5 rounded-full bg-accent" />
          {scene.stats.area} m²{" "}
          <span className="text-slate-500">
            / {scene.stats.rooms} rooms / {scene.stats.meshes} pieces
          </span>
        </span>
        <span
          role={s.error ? "alert" : "status"}
          className={`truncate ${s.error ? "text-red-300" : ""}`}
        >
          {s.busy ? "Working…" : s.message}
        </span>
        <Button onClick={() => setDialog("export")}>Build details</Button>
      </footer>
      {dialog === "library" ? (
        <Library store={store} onClose={() => setDialog("")} />
      ) : (
        dialog && (
          <EditorDialog
            key={dialog}
            kind={dialog}
            state={s}
            store={store}
            onClose={() => setDialog("")}
          />
        )
      )}
    </div>
  );
}
