import { api, uid } from "./api";
import type { EditorState, Layout, Scene, Project, Tool } from "./types";
const STORAGE = "ghostline-building-layout-v1";
export function createEditorStore(
  request: typeof api = api,
  storage: Pick<Storage, "getItem" | "setItem"> = localStorage,
) {
  let state: EditorState = {
    scene: null,
    layout: null,
    catalogs: [],
    files: [],
    selected: null,
    selectedModule: null,
    door: null,
    wall: null,
    tool: "select",
    level: 0,
    route: [],
    preview: {
      cutaway: true,
      roof: false,
      collision: false,
      navigation: false,
      zones: true,
    },
    view: "split",
    tab: "build",
    pendingModule: null,
    pendingAppearance: null,
    message: "Opening editor…",
    error: false,
    busy: false,
    dirty: false,
    undo: [],
    redo: [],
    fitVersion: 0,
  };
  const listeners = new Set<() => void>();
  const savedLayouts = new Map<string, string>();
  let queue: Promise<unknown> = Promise.resolve();
  const patch = (next: Partial<EditorState>) => {
    state = { ...state, ...next };
    listeners.forEach((f) => f());
  };
  const message = (text: string, error = false) =>
    patch({ message: text, error });
  function enqueue<T>(task: () => Promise<T>) {
    const result = queue.then(task, task);
    queue = result;
    return result;
  }
  function adopt(scene: Scene, changes: Partial<EditorState> = {}) {
    let selected = state.selected,
      selectedModule = state.selectedModule;
    if (!scene.layout.rooms.some((r) => r.id === selected))
      selected =
        scene.layout.rooms.find((r) => r.level === state.level)?.id || null;
    if (!scene.layout.modules?.some((m) => m.id === selectedModule))
      selectedModule = null;
    patch({
      scene,
      layout: scene.layout,
      selected,
      selectedModule,
      route: [],
      dirty: savedLayouts.get(scene.layout.id) !== JSON.stringify(scene.layout),
      ...changes,
    });
    try {
      storage.setItem(STORAGE, JSON.stringify(scene.layout));
    } catch {
      message("Draft storage is full. Save the layout to the project.", true);
    }
  }
  async function init() {
    try {
      const project = await request<Project>("/api/project");
      patch({ catalogs: project.kits, files: project.files });
      let scene = project.scene;
      savedLayouts.set(scene.layout.id, JSON.stringify(scene.layout));
      const draft = storage.getItem(STORAGE);
      if (draft) {
        try {
          scene = await request<Scene>("/api/compile", {
            layout: JSON.parse(draft),
          });
          if (project.files.some((file) => file.id === scene.layout.id)) {
            try {
              const saved = await request<Scene>(
                `/api/layout/${encodeURIComponent(scene.layout.id)}`,
              );
              savedLayouts.set(scene.layout.id, JSON.stringify(saved.layout));
            } catch {
              /* An offline draft remains editable even if its saved file is unavailable. */
            }
          }
        } catch {
          message(
            "Previous draft could not be restored. Opened the project example.",
            true,
          );
        }
      }
      adopt(scene, { fitVersion: state.fitVersion + 1 });
      if (!state.error)
        message("Ready · changes stay in your browser until saved");
    } catch (error) {
      message(String(error), true);
    }
  }
  function mutate(
    operation: (layout: Layout) => void,
    success = "Layout updated",
  ): Promise<boolean> {
    const task = async () => {
      if (!state.layout) return false;
      const previous = structuredClone(state.layout),
        next = structuredClone(state.layout);
      patch({ busy: true });
      try {
        operation(next);
        if (JSON.stringify(previous) === JSON.stringify(next)) return true;
        const scene = await request<Scene>("/api/compile", {
          layout: next,
          reconcile: true,
        });
        adopt(scene, {
          undo: [...state.undo, previous].slice(-80),
          redo: [],
        });
        message(
          success +
            (scene.removed_openings?.length
              ? ` · ${scene.removed_openings.length} displaced openings removed; Undo restores them`
              : ""),
        );
        return true;
      } catch (error) {
        message(error instanceof Error ? error.message : String(error), true);
        return false;
      } finally {
        patch({ busy: false });
      }
    };
    return enqueue(task);
  }
  function history(direction: "undo" | "redo") {
    return enqueue(async () => {
      const stack = state[direction];
      const candidate = stack.at(-1);
      if (!candidate || !state.layout) return;
      try {
        const scene = await request<Scene>("/api/compile", {
          layout: candidate,
        });
        const other = direction === "undo" ? "redo" : "undo";
        adopt(scene, {
          [direction]: stack.slice(0, -1),
          [other]: [...state[other], structuredClone(state.layout)],
        });
        message(direction === "undo" ? "Change undone" : "Change restored");
      } catch (error) {
        message(String(error), true);
      }
    });
  }
  function open(id: string) {
    return enqueue(async () => {
      if (!id) return;
      try {
        const scene = await request<Scene>(
          `/api/layout/${encodeURIComponent(id)}`,
        );
        savedLayouts.set(scene.layout.id, JSON.stringify(scene.layout));
        adopt(scene, {
          undo: state.layout
            ? [...state.undo, structuredClone(state.layout)]
            : [],
          redo: [],
          dirty: false,
          selected: null,
          selectedModule: null,
          door: null,
          level: scene.layout.rooms[0]?.level || 0,
          fitVersion: state.fitVersion + 1,
        });
        message("Saved layout opened; Undo restores the previous draft");
      } catch (error) {
        message(String(error), true);
      }
    });
  }
  function save() {
    return enqueue(async () => {
      if (!state.layout) return;
      patch({ busy: true });
      try {
        await request("/api/save", { layout: state.layout });
        savedLayouts.set(state.layout.id, JSON.stringify(state.layout));
        const project = await request<Project>("/api/project");
        patch({ files: project.files, dirty: false });
        message("Saved to project");
      } catch (error) {
        message(String(error), true);
      } finally {
        patch({ busy: false });
      }
    });
  }
  function importLayout(layout: Layout) {
    return enqueue(async () => {
      try {
        const scene = await request<Scene>("/api/compile", { layout });
        adopt(scene, {
          undo: state.layout
            ? [...state.undo, structuredClone(state.layout)]
            : [],
          redo: [],
          dirty: true,
          fitVersion: state.fitVersion + 1,
        });
        message("Layout imported as a draft");
      } catch (error) {
        message(String(error), true);
      }
    });
  }
  function tool(tool: Tool) {
    patch({ tool, wallStart: null, tab: "build" });
  }
  async function fresh() {
    await mutate((layout) => {
      const kit = state.catalogs.find((k) => k.id === layout.kit)!;
      Object.keys(layout).forEach((k) => delete layout[k]);
      Object.assign(layout, {
        schema_version: 1,
        id: uid("building"),
        name: "Untitled building",
        kit: kit.id,
        origin: { x: 0, y: 0, z: 0, yaw: 0 },
        rooms: [],
        modules: [],
        openings: {},
        stairs: [],
        navigation: { export: false },
        wall_appearance: kit.wall_appearances[0],
        floor_appearance: kit.floor_appearances[0],
      });
    }, "Draw a room to start");
    patch({
      selected: null,
      selectedModule: null,
      door: null,
      wall: null,
      level: 0,
      fitVersion: state.fitVersion + 1,
    });
    tool("room");
  }
  return {
    getSnapshot: () => state,
    subscribe: (f: () => void) => {
      listeners.add(f);
      return () => {
        listeners.delete(f);
      };
    },
    patch,
    message,
    init,
    adopt,
    mutate,
    history,
    open,
    save,
    importLayout,
    tool,
    fresh,
    wait: () => queue,
  };
}
export type EditorStore = ReturnType<typeof createEditorStore>;
