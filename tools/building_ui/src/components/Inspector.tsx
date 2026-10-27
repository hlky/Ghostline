import { useState } from "react";
import { Trash2, Copy, FileJson } from "lucide-react";
import { setWallMode } from "../../wall-controls.js";
import type { EditorState, Layout, Workstation } from "../types";
import type { EditorStore } from "../store";
import { pretty, download } from "../api";
import { Button, Field, Select, Section, Toggle } from "./primitives";
export function Inspector({
  state: s,
  store,
  open,
}: {
  state: EditorState;
  store: EditorStore;
  open: (kind: string) => void;
}) {
  if (!s.scene || !s.layout) return null;
  const l = s.layout,
    scene = s.scene;
  const room = l.rooms.find((r) => r.id === s.selected),
    module = l.modules?.find((m) => m.id === s.selectedModule),
    door = scene.doors.find((d) => d.id === s.door);
  const updateRoom = (key: string, value: string) =>
    store.mutate((d) => {
      const r = d.rooms.find((r) => r.id === s.selected)!;
      Object.assign(r, { [key]: key === "name" ? value : Number(value) });
    });
  const updateModule = (key: string, value: string) =>
    store.mutate((d) => {
      const m = d.modules.find((m) => m.id === s.selectedModule)!;
      Object.assign(m, { [key]: key === "yaw" ? Number(value) : value });
    });
  return (
    <aside className="inspector-panel" aria-label="Selection inspector">
      <div className="border-b border-line px-4 py-3">
        <h2 className="eyebrow">Inspector</h2>
        <p className="mt-1 truncate text-sm font-medium">
          {module
            ? pretty(module.id)
            : door
              ? "Door settings"
              : room?.name || "Nothing selected"}
        </p>
      </div>
      {s.wall && ["wall", "partition"].includes(s.tool) && (
        <Section title="Selected wall">
          <p className="hint mb-3">
            {s.wall.startsWith("edge:")
              ? "3 m wall bay"
              : "Shell wall / partition"}
          </p>
          <div className="grid grid-cols-3 gap-2">
            {["solid", "doorway", "open"].map((mode) => (
              <Button
                key={mode}
                onClick={() =>
                  store.mutate(
                    (d) => setWallMode(d, s.wall!, mode),
                    `Wall changed to ${mode}`,
                  )
                }
              >
                {pretty(mode)}
              </Button>
            ))}
          </div>
        </Section>
      )}
      {module ? (
        <Section
          title={module.reference_only ? "Shell reference" : "Object placement"}
          action={
            !module.reference_only && (
              <Button
                title="Delete selected object"
                danger
                onClick={() =>
                  store.mutate((d) => {
                    d.modules = d.modules.filter((m) => m.id !== module.id);
                  })
                }
              >
                <Trash2 size={14} />
              </Button>
            )
          }
        >
          {module.reference_only && (
            <p className="hint mb-3">
              Existing game geometry. Preview only; excluded from exports.
            </p>
          )}
          <div className="grid grid-cols-2 gap-3">
            {["X", "Y", "Z"].map((axis, i) => (
              <Field
                key={axis}
                label={`${axis} position (m)`}
                type="number"
                step={0.05}
                value={module.position[i]}
                disabled={module.reference_only}
                onCommit={(v) =>
                  store.mutate((d) => {
                    d.modules.find((m) => m.id === module.id)!.position[i] =
                      Number(v);
                  }, "Object moved")
                }
              />
            ))}
            <Field
              label="Rotation (°)"
              type="number"
              step={5}
              value={module.yaw}
              disabled={module.reference_only}
              onCommit={(v) => updateModule("yaw", v)}
            />
          </div>
          <Select
            label="Anchor"
            value={module.anchor}
            disabled={module.reference_only}
            options={[
              { value: "base-center", label: "Base centre" },
              { value: "pivot", label: "Original mesh pivot" },
            ]}
            onChange={(v) => updateModule("anchor", v)}
          />
          <Select
            label="Collision"
            value={module.collision}
            disabled={module.reference_only}
            options={[
              { value: "none", label: "No additional collision" },
              { value: "box", label: "Solid box (structural modules only)" },
            ]}
            onChange={(v) => updateModule("collision", v)}
          />
          <Select
            label="Object appearance"
            value={module.appearance}
            disabled={module.reference_only}
            options={(
              scene.instances.find((i) => i.id === "module:" + module.id)
                ?.appearances || [module.appearance]
            ).map((v) => ({ value: v, label: pretty(v) }))}
            onChange={(v) => updateModule("appearance", v)}
          />
        </Section>
      ) : room ? (
        <Section
          title="Room dimensions"
          action={
            <Button
              title="Delete selected room"
              danger
              onClick={() =>
                store.mutate((d) => {
                  d.rooms = d.rooms.filter((r) => r.id !== room.id);
                }, "Room deleted")
              }
            >
              <Trash2 size={14} />
            </Button>
          }
        >
          <Field
            label="Room name"
            value={room.name}
            onCommit={(v) => updateRoom("name", v)}
          />
          <div className="grid grid-cols-2 gap-3">
            {(["width", "depth", "x", "y"] as const).map((key) => (
              <Field
                key={key}
                label={`${pretty(key)} (m)`}
                value={room[key]}
                type="number"
                step={3}
                onCommit={(v) => updateRoom(key, v)}
              />
            ))}
          </div>
          <p className="hint mt-3">
            {room.width * room.depth} m² ·{" "}
            {room.ceiling_height ?? scene.kit.wall_height} m clear height
          </p>
        </Section>
      ) : (
        !door && (
          <Section title="Make a selection">
            <p className="hint">
              Select a room, wall or object on the plan or in the scene list to
              edit its properties.
            </p>
          </Section>
        )
      )}
      {door && (
        <Section title="Interactive door">
          <Select
            label="Door initial state"
            value={door.state}
            options={["CLOSED", "OPEN", "LOCKED"].map((v) => ({
              value: v,
              label: pretty(v),
            }))}
            onChange={(v) =>
              store.mutate((d) => {
                d.door_states ||= {};
                d.door_states[door.id] = v;
              }, "Door state updated")
            }
          />
          <p className="hint">
            {door.id} · {door.mode.toLowerCase()}
          </p>
        </Section>
      )}
      {s.tab === "quest" ? (
        <QuestPanel state={s} store={store} />
      ) : (
        <Section title="Room finishes">
          {(["wall", "floor"] as const).map((key) => (
            <Select
              key={key}
              label={`${pretty(key)} finish`}
              value={l[`${key}_appearance`]}
              options={scene.kit[`${key}_appearances`].map((v) => ({
                value: v,
                label: pretty(v),
              }))}
              onChange={(v) =>
                store.mutate((d) => {
                  d[`${key}_appearance`] = v;
                }, "Finish updated")
              }
            />
          ))}
          <p className="hint">
            Appearances are exported. The preview uses neutral materials.
          </p>
        </Section>
      )}
      <Section title="Validation">
        <p className="hint">
          {scene.navigation.stats.triangles} route faces ·{" "}
          {scene.navigation.stats.islands} islands
        </p>
        <Button className="mt-3 w-full" onClick={() => open("route")}>
          Check a route
        </Button>
        <details className="mt-4">
          <summary>Advanced navigation</summary>
          <div className="mt-3 grid grid-cols-2 gap-3">
            <Field
              label="Agent radius (m)"
              type="number"
              step={0.05}
              value={scene.navigation.radius}
              onCommit={(v) =>
                store.mutate((d) => {
                  d.navigation.radius = Number(v);
                })
              }
            />
            <Field
              label="Native layer"
              type="number"
              value={l.navigation?.layer || 0}
              onCommit={(v) =>
                store.mutate((d) => {
                  d.navigation.layer = Number(v);
                })
              }
            />
          </div>
          <Toggle
            label="Experimental native navigation"
            checked={l.navigation?.export === true}
            onChange={(v) =>
              store.mutate((d) => {
                d.navigation.export = v;
              })
            }
          />
          <p className="hint mt-3">
            Offline connectivity does not establish game AI reachability.
          </p>
          <Button
            className="mt-3"
            onClick={() =>
              store.mutate((d) => {
                d.navigation.connections?.pop();
              })
            }
          >
            Remove last entrance link
          </Button>
        </details>
      </Section>
    </aside>
  );
}
export function QuestPanel({
  state: s,
  store,
}: {
  state: EditorState;
  store: EditorStore;
}) {
  const [choice, setChoice] = useState("");
  const items = s.scene?.workstations || [],
    w = items.find((w) => w.id === choice) || items[0];
  const edit = (key: keyof Workstation["actor"], value: string | boolean) =>
    store.mutate((d) => {
      const item = d.workstations?.find((x) => x.id === w.id);
      if (item) Object.assign(item.actor, { [key]: value });
    }, "Worker binding updated");
  return (
    <Section title="Quest workstation">
      {w ? (
        <>
          <Select
            label="Workstation"
            value={w.id}
            onChange={setChoice}
            options={items.map((w) => ({ value: w.id, label: pretty(w.id) }))}
          />
          <Field
            label="Worker record"
            value={w.actor.record}
            onCommit={(v) => edit("record", v)}
          />
          <Field
            label="Worker appearance"
            value={w.actor.appearance}
            onCommit={(v) => edit("appearance", v)}
          />
          <Toggle
            label="Worker active on load"
            checked={w.actor.active_on_start !== false}
            onChange={(v) => edit("active_on_start", v)}
          />
          <p className="hint my-3">
            The chair anchors the workspot; the desk anchors the computer.
            Disable activation when a quest owns the worker lifecycle.
          </p>
          <details>
            <summary>Quest block bindings</summary>
            <pre className="code-panel mt-3">
              {JSON.stringify(
                {
                  community: w.community,
                  entry: "worker",
                  phase: "default",
                  workspot: w.seat,
                  computer: w.computer_ref,
                  completion_fact: w.read_fact,
                },
                null,
                2,
              )}
            </pre>
            <Button
              onClick={() => {
                navigator.clipboard
                  .writeText(
                    JSON.stringify(
                      {
                        community: w.community,
                        workspot: w.seat,
                        computer: w.computer_ref,
                        completion_fact: w.read_fact,
                      },
                      null,
                      2,
                    ),
                  )
                  .then(
                    () => store.message("Quest bindings copied"),
                    () => store.message("Could not access clipboard", true),
                  );
              }}
            >
              <Copy size={14} />
              Copy bindings
            </Button>
          </details>
        </>
      ) : (
        <p className="hint">
          This layout has no workstation fixture. Workstations bind authored
          desks and chairs to native communities and computers.
        </p>
      )}
    </Section>
  );
}
export function ProjectPanel({
  state: s,
  store,
  open,
}: {
  state: EditorState;
  store: EditorStore;
  open: (kind: string) => void;
}) {
  return (
    <>
      <Section title="Saved layouts">
        <Select
          label="Open layout"
          value=""
          onChange={store.open}
          options={[
            { value: "", label: "Choose a saved layout…" },
            ...s.files.map((f) => ({ value: f.id, label: f.name })),
          ]}
        />
        <Button className="w-full" onClick={() => open("new")}>
          New building
        </Button>
        <Button
          className="mt-2 w-full"
          onClick={async () => {
            if (
              await store.mutate((d) => {
                d.id = crypto
                  .randomUUID()
                  .slice(0, 8)
                  .replace(/^/, "building_");
              }, "Working copy created")
            )
              await store.save();
          }}
        >
          Save as a new copy
        </Button>
      </Section>
      <Section title="Transfer layout">
        <Button
          className="mb-3 w-full"
          onClick={() => download(s.layout, `${s.layout!.id}.building.json`)}
        >
          <FileJson size={15} />
          Download JSON
        </Button>
        <label className="btn cursor-pointer">
          Import layout JSON
          <input
            className="sr-only"
            type="file"
            accept=".json"
            onChange={async (e) => {
              const file = e.target.files?.[0];
              if (!file) return;
              try {
                if (file.size > 512000)
                  throw new Error("Layout exceeds 512 KB");
                await store.importLayout(
                  JSON.parse(await file.text()) as Layout,
                );
              } catch (error) {
                store.message(String(error), true);
              }
              e.target.value = "";
            }}
          />
        </label>
      </Section>
      <Section title="Existing building shell">
        <p className="hint mb-3">
          Manage surveyed facade and collision patches.
        </p>
        <Button onClick={() => open("retrofit")}>Shell entrance patches</Button>
      </Section>
    </>
  );
}
