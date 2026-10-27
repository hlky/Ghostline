import { useState } from "react";
import { Download, CheckCircle2 } from "lucide-react";
import { api, uid } from "../api";
import type { EditorState, Layout, SectorPatch } from "../types";
import type { EditorStore } from "../store";
import { Button, Field, Modal, Toggle } from "./primitives";
export function EditorDialog({
  kind,
  state: s,
  store,
  onClose,
}: {
  kind: string;
  state: EditorState;
  store: EditorStore;
  onClose: () => void;
}) {
  const [origin, setOrigin] = useState(s.layout!.origin),
    [start, setStart] = useState("3, 3, 0"),
    [end, setEnd] = useState("3, 4, 0"),
    [result, setResult] = useState(""),
    [busy, setBusy] = useState(false),
    [error, setError] = useState(""),
    [exported, setExported] = useState<{ url: string; sha256: string } | null>(
      null,
    );
  const [survey, setSurvey] = useState<{
      selection: SectorPatch;
      candidates: {
        index: number;
        type: string;
        actor?: number;
        render_instance?: number;
        expectedInstances?: number;
        expectedActors?: number;
        world_position?: number[];
      }[];
    } | null>(null),
    [selected, setSelected] = useState<number[]>([]);
  const l = s.layout!,
    scene = s.scene!;
  const parse = (value: string) => {
    const points = value.split(",").map(Number);
    if (points.length !== 3 || points.some((n) => !Number.isFinite(n)))
      throw new Error("Enter three numbers separated by commas");
    return points;
  };
  async function run(action: () => Promise<void>) {
    setBusy(true);
    setError("");
    try {
      await store.wait();
      await action();
    } catch (e) {
      setError(e instanceof Error ? e.message : String(e));
    } finally {
      setBusy(false);
    }
  }
  if (kind === "new")
    return (
      <Modal title="Start a new building?" onClose={onClose}>
        <p className="hint">
          Your current draft stays in Undo. Save it to the project first if you
          want to keep it between sessions. Shell patches, workstations and
          furnishings will be cleared in the new layout.
        </p>
        <div className="dialog-actions">
          <Button onClick={onClose}>Keep editing</Button>
          <Button
            primary
            onClick={() => {
              store.fresh();
              onClose();
            }}
          >
            Create new building
          </Button>
        </div>
      </Modal>
    );
  if (kind === "origin")
    return (
      <Modal title="World placement" onClose={onClose}>
        <p className="hint mb-4">
          The plan uses local coordinates. This anchor places exports in Night
          City.
        </p>
        <div className="grid grid-cols-2 gap-3">
          {(["x", "y", "z", "yaw"] as const).map((key) => (
            <Field
              key={key}
              label={
                key === "yaw"
                  ? "World yaw (°)"
                  : `World ${key.toUpperCase()} (m)`
              }
              type="number"
              step={0.01}
              value={origin[key]}
              onCommit={(v) => setOrigin({ ...origin, [key]: Number(v) })}
            />
          ))}
        </div>
        <div className="dialog-actions">
          <Button onClick={onClose}>Cancel</Button>
          <Button
            primary
            disabled={s.busy}
            onClick={async () => {
              if (
                await store.mutate((d) => {
                  d.origin = origin;
                }, "World anchor updated")
              )
                onClose();
            }}
          >
            Apply anchor
          </Button>
        </div>
      </Modal>
    );
  if (kind === "export")
    return (
      <Modal
        title={exported ? "Project exported" : "Review project export"}
        locked={busy}
        onClose={onClose}
      >
        <p className="hint mb-4">
          Exports build an editable WolvenKit project and verify native resource
          readback. Exporting does not install files into the game.
        </p>
        <dl className="stats-grid">
          {Object.entries({
            Building: l.name,
            "Floor area": `${scene.stats.area} m²`,
            Rooms: scene.stats.rooms,
            "Mesh instances": scene.stats.meshes,
            "Collision boxes": scene.stats.colliders,
            "World anchor": `${l.origin.x.toFixed(2)}, ${l.origin.y.toFixed(2)}, ${l.origin.z.toFixed(2)}`,
          }).map(([k, v]) => (
            <div key={k}>
              <dt>{k}</dt>
              <dd>{v}</dd>
            </div>
          ))}
        </dl>
        <details className="mt-4" open={scene.warnings.length > 0}>
          <summary>{scene.warnings.length} validation notes</summary>
          {scene.warnings.map((v, i) => (
            <p
              key={i}
              className="hint mt-3 border-l-2 border-amber-300/50 pl-3"
            >
              {v}
            </p>
          ))}
        </details>
        {exported && (
          <div className="mt-4 rounded-lg border border-accent/30 bg-accent/5 p-4">
            <p className="flex items-center gap-2 text-accent">
              <CheckCircle2 size={16} />
              Native readback checked
            </p>
            <a
              className="btn btn-primary mt-3"
              href={exported.url}
              download={`${l.id}-building-project.zip`}
            >
              <Download size={15} />
              Download project ZIP
            </a>
            <p className="hint mt-3 break-all">SHA-256: {exported.sha256}</p>
          </div>
        )}
        {error && (
          <p role="alert" className="mt-4 text-red-300">
            {error}
          </p>
        )}
        <div className="dialog-actions">
          <Button disabled={busy} onClick={onClose}>
            Close
          </Button>
          <Button
            primary
            disabled={busy || !!exported}
            onClick={() =>
              run(async () => {
                const r = await api<{ url: string; sha256: string }>(
                  "/api/export",
                  { layout: store.getSnapshot().layout },
                );
                setExported(r);
                store.message("Project exported · native readback checked");
              })
            }
          >
            {busy ? "Building native resources…" : "Build export"}
          </Button>
        </div>
      </Modal>
    );
  if (kind === "route")
    return (
      <Modal title="Check floor connectivity" onClose={onClose}>
        <p className="hint mb-4">
          Enter local X, Y, Z. This checks generated surfaces and door links,
          not game AI.
        </p>
        <Field label="Route start X, Y, Z" value={start} onCommit={setStart} />
        <Field label="Route end X, Y, Z" value={end} onCommit={setEnd} />
        <p role="status" className="mt-3 text-accent">
          {result}
        </p>
        {error && (
          <p role="alert" className="text-red-300">
            {error}
          </p>
        )}
        <div className="dialog-actions">
          <Button
            disabled={busy}
            onClick={() =>
              run(async () => {
                const from = parse(start),
                  to = parse(end);
                if (
                  await store.mutate((d) => {
                    d.navigation.connections ||= [];
                    d.navigation.connections.push({
                      id: uid("entrance"),
                      from,
                      to,
                    });
                  }, "Entrance link added")
                )
                  setResult(
                    "Entrance link added. Verify its external endpoint in game.",
                  );
              })
            }
          >
            Add entrance link
          </Button>
          <Button
            primary
            disabled={busy}
            onClick={() =>
              run(async () => {
                const r = await api<{
                  faces: number[];
                  reachable: boolean;
                  reason: string;
                }>("/api/route", {
                  layout: store.getSnapshot().layout,
                  start: parse(start),
                  end: parse(end),
                });
                store.patch({
                  route: r.faces,
                  preview: { ...s.preview, navigation: true },
                });
                setResult(
                  `${r.reachable ? "Connected" : "No route"} · ${r.reason}`,
                );
              })
            }
          >
            Check route
          </Button>
        </div>
      </Modal>
    );
  return (
    <Modal title="Shell entrance patches" onClose={onClose} wide>
      <p className="hint mb-4">
        Import a reviewed sector survey. Select facade meshes and separate
        collision actors carefully; a shared actor can extend into the street.
      </p>
      <label className="btn cursor-pointer">
        Import sector survey
        <input
          className="sr-only"
          type="file"
          accept=".json"
          onChange={(e) =>
            run(async () => {
              const file = e.target.files?.[0];
              if (!file) return;
              if (file.size > 512000) throw new Error("Survey exceeds 512 KB");
              const d = JSON.parse(await file.text());
              if (
                !d.selection ||
                !Array.isArray(d.candidates) ||
                d.candidates.length > 1000
              )
                throw new Error("Expected a Building Lab sector survey");
              setSurvey(d);
              setSelected([]);
            })
          }
        />
      </label>
      <p className="hint mt-4">
        {survey?.selection.path ||
          `${l.retrofit?.sectors.length || 0} existing sector patches`}
      </p>
      <div className="my-4 max-h-72 space-y-3 overflow-y-auto">
        {survey?.candidates.map((c, i) => (
          <Toggle
            key={i}
            label={`#${c.index} ${c.type}${c.actor !== undefined ? ` · actor ${c.actor}` : c.render_instance !== undefined ? ` · instance ${c.render_instance}` : ""}`}
            checked={selected.includes(i)}
            onChange={(v) =>
              setSelected(
                v ? [...selected, i] : selected.filter((n) => n !== i),
              )
            }
          />
        ))}
      </div>
      {error && (
        <p role="alert" className="text-red-300">
          {error}
        </p>
      )}
      <div className="dialog-actions">
        <Button
          onClick={() =>
            store.mutate((d) => {
              d.retrofit = { sectors: [] };
            }, "Shell patches cleared")
          }
        >
          Clear patches
        </Button>
        <Button
          primary
          disabled={!survey || !selected.length}
          onClick={async () => {
            if (!survey) return;
            const grouped = new Map<number, Record<string, unknown>>();
            for (const i of selected) {
              const c = survey.candidates[i];
              const node = grouped.get(c.index) || {
                index: c.index,
                type: c.type,
              };
              if (c.actor !== undefined) {
                node.expectedActors = c.expectedActors;
                node.actorDeletions = [
                  ...((node.actorDeletions as number[]) || []),
                  c.actor,
                ];
              }
              if (c.render_instance !== undefined) {
                node.expectedInstances = c.expectedInstances;
                node.instanceDeletions = [
                  ...((node.instanceDeletions as number[]) || []),
                  c.render_instance,
                ];
              }
              grouped.set(c.index, node);
            }
            const selection = {
              ...survey.selection,
              nodeDeletions: [...grouped.values()],
            };
            if (
              await store.mutate((d: Layout) => {
                d.retrofit ||= { sectors: [] };
                d.retrofit.sectors = [
                  ...d.retrofit.sectors.filter(
                    (p) => p.path !== selection.path,
                  ),
                  selection,
                ];
              }, "Survey selections applied")
            )
              onClose();
          }}
        >
          Apply selections
        </Button>
      </div>
    </Modal>
  );
}
