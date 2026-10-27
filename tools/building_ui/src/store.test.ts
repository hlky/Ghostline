import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { createEditorStore } from "./store";
import type { Layout, Scene, Project } from "./types";
import type { api } from "./api";
const layout = JSON.parse(
  readFileSync(
    new URL(
      "../../../projects/experiments/building-lab/buildings/akpp-logistics-open-shell.building.json",
      import.meta.url,
    ),
    "utf8",
  ),
) as Layout;
function scene(l: Layout): Scene {
  return {
    layout: structuredClone(l),
    removed_openings: [],
  } as unknown as Scene;
}
function setup() {
  const values = new Map<string, string>(),
    calls: string[] = [];
  let reject = false;
  const request = (async (path: string, body?: { layout: Layout }) => {
    calls.push(path);
    await new Promise((r) => setTimeout(r, 2));
    if (path === "/api/compile") {
      if (reject) {
        reject = false;
        throw new Error("Invalid room dimensions");
      }
      return scene(body!.layout);
    }
    if (path.startsWith("/api/layout/"))
      return scene({ ...layout, name: "Opened layout" });
    if (path === "/api/save") return { path: "test.json" };
    return {
      scene: scene(layout),
      files: [],
      kits: [
        {
          id: layout.kit,
          wall_appearances: ["concrete_bare"],
          floor_appearances: ["tiles_grey"],
        },
      ],
    } as unknown as Project;
  }) as typeof api;
  const store = createEditorStore(request, {
    getItem: (k) => values.get(k) || null,
    setItem: (k, v) => {
      values.set(k, v);
    },
  });
  return {
    store,
    calls,
    values,
    rejectNext: () => {
      reject = true;
    },
  };
}
test("queued edits compose against the last successful layout; failed compilation preserves history", async () => {
  const t = setup();
  await t.store.init();
  t.rejectNext();
  assert.equal(
    await t.store.mutate((l) => {
      l.name = "Rejected";
    }),
    false,
  );
  assert.equal(t.store.getSnapshot().layout!.name, layout.name);
  assert.equal(t.store.getSnapshot().undo.length, 0);
  await Promise.all([
    t.store.mutate((l) => {
      l.name = "First";
    }),
    t.store.mutate((l) => {
      l.name += " then second";
    }),
  ]);
  assert.equal(t.store.getSnapshot().layout!.name, "First then second");
  assert.equal(t.store.getSnapshot().undo.length, 2);
  await t.store.history("undo");
  assert.equal(t.store.getSnapshot().layout!.name, "First");
  await t.store.history("redo");
  assert.equal(t.store.getSnapshot().layout!.name, "First then second");
});
test("saving and loading serialize with pending edits and preserve extensions", async () => {
  const t = setup();
  await t.store.init();
  await Promise.all([
    t.store.mutate((l) => {
      l.name = "Before save";
    }),
    t.store.save(),
    t.store.mutate((l) => {
      l.name = "After save";
    }),
  ]);
  assert.equal(t.store.getSnapshot().dirty, true);
  assert.equal(t.store.getSnapshot().layout!.name, "After save");
  assert.deepEqual(
    t.store.getSnapshot().layout!.workstations,
    layout.workstations,
  );
  assert.deepEqual(t.store.getSnapshot().layout!.retrofit, layout.retrofit);
  await t.store.open(layout.id);
  assert.equal(t.store.getSnapshot().layout!.name, "Opened layout");
  await t.store.history("undo");
  assert.equal(t.store.getSnapshot().layout!.name, "After save");
});
test("new layouts clear shell removals, workstations and source furniture rather than leaking them into another building", async () => {
  const t = setup();
  await t.store.init();
  await t.store.fresh();
  const next = t.store.getSnapshot().layout!;
  assert.deepEqual(next.rooms, []);
  assert.deepEqual(next.modules, []);
  assert.equal(next.workstations, undefined);
  assert.equal(next.retrofit, undefined);
  assert.equal(next.shell_blockers, undefined);
  assert.equal(next.archive_name, undefined);
  assert.equal(t.store.getSnapshot().tool, "room");
  assert.notEqual(next.id, layout.id);
});
test("a corrupt browser draft reports recovery and does not replace the project with invalid data", async () => {
  const t = setup();
  t.values.set("ghostline-building-layout-v1", "broken JSON");
  await t.store.init();
  assert.equal(t.store.getSnapshot().layout!.id, layout.id);
  assert.equal(t.store.getSnapshot().error, true);
  assert.match(t.store.getSnapshot().message, /could not be restored/);
});
