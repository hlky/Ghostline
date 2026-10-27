import { useEffect, useRef, useState } from "react";
import { Focus } from "lucide-react";
import { BuildingViewer } from "../../viewer.js";
import { createPlanAdapter } from "../plan-adapter.js";
import type { EditorState, LibraryAsset } from "../types";
import type { EditorStore } from "../store";
import { Button, Toggle } from "./primitives";
export function Plan({
  state,
  store,
}: {
  state: EditorState;
  store: EditorStore;
}) {
  const svg = useRef<SVGSVGElement>(null),
    adapter = useRef<ReturnType<typeof createPlanAdapter> | null>(null);
  useEffect(() => {
    if (!svg.current || !state.scene) return;
    adapter.current = createPlanAdapter(svg.current, state, {
      mutate: store.mutate,
      message: store.message,
      select: (patch: Partial<EditorState>) =>
        store.patch({
          ...patch,
          tab: patch.selectedModule ? "objects" : "build",
        }),
      tool: store.tool,
    });
    adapter.current.fit();
    return () => {
      adapter.current?.destroy();
      adapter.current = null;
    };
  }, [!!state.scene]);
  useEffect(() => {
    if (state.scene) adapter.current?.update(state);
  }, [state]);
  useEffect(() => {
    adapter.current?.fit();
  }, [state.fitVersion, state.level, state.view]);
  return (
    <section className="canvas-pane">
      <div className="pane-toolbar">
        <span className="eyebrow">Floor plan</span>
        <div className="flex items-center gap-3">
          <Toggle
            label="Room labels"
            checked={state.preview.zones}
            onChange={(zones) =>
              store.patch({ preview: { ...state.preview, zones } })
            }
          />
          <Button title="Fit plan" onClick={() => adapter.current?.fit()}>
            <Focus size={15} />
          </Button>
        </div>
      </div>
      <svg
        ref={svg}
        id="plan"
        className={`plan-canvas ${state.tool === "room" ? "room-tool" : ""}`}
        role="img"
        aria-label="Building floor plan. Draw rooms or select objects; use inspector fields for exact placement."
        viewBox="-6 -15 27 24"
      >
        <defs>
          <pattern id="grid" width="3" height="3" patternUnits="userSpaceOnUse">
            <path
              d="M 3 0 L 0 0 0 3"
              fill="none"
              stroke="#35414b"
              strokeWidth=".025"
            />
          </pattern>
          <pattern
            id="subgrid"
            width="1"
            height="1"
            patternUnits="userSpaceOnUse"
          >
            <circle cx="0" cy="0" r=".025" fill="#3d4e59" />
          </pattern>
        </defs>
        <g id="plan-content" />
        <g id="draft" />
      </svg>
      <div className="canvas-caption">
        3 m room grid · 5 cm partition snap · scroll to zoom
      </div>
    </section>
  );
}
export function Geometry({
  state,
  store,
}: {
  state: EditorState;
  store: EditorStore;
}) {
  const host = useRef<HTMLDivElement>(null),
    viewer = useRef<BuildingViewer | null>(null);
  const [status, setStatus] = useState("Loading geometry…");
  useEffect(() => {
    if (!host.current) return;
    viewer.current = new BuildingViewer(host.current, setStatus);
    return () => {
      viewer.current?.dispose();
      viewer.current = null;
    };
  }, []);
  useEffect(() => {
    if (state.scene)
      viewer.current?.update(state.scene, {
        ...state.preview,
        level: state.level,
        route: state.route,
      });
  }, [state.scene, state.preview, state.level, state.route]);
  useEffect(() => {
    viewer.current?.resize();
    viewer.current?.fit();
  }, [state.fitVersion, state.level, state.view]);
  return (
    <section className="canvas-pane">
      <div className="pane-toolbar">
        <span className="eyebrow">3D preview</span>
        <div className="flex flex-wrap items-center gap-3">
          {(["cutaway", "roof", "collision", "navigation"] as const).map(
            (key) => (
              <Toggle
                key={key}
                label={
                  key === "navigation"
                    ? "Routes"
                    : key[0].toUpperCase() + key.slice(1)
                }
                checked={state.preview[key]}
                onChange={(v) =>
                  store.patch({ preview: { ...state.preview, [key]: v } })
                }
              />
            ),
          )}
          <Button title="Frame building" onClick={() => viewer.current?.fit()}>
            <Focus size={15} />
          </Button>
        </div>
      </div>
      <div ref={host} className="three-host" />
      <div className="canvas-caption" role="status">
        {status}
      </div>
    </section>
  );
}
export function AssetPreview({ asset }: { asset: LibraryAsset | null }) {
  const host = useRef<HTMLDivElement>(null),
    viewer = useRef<BuildingViewer | null>(null);
  const [status, setStatus] = useState(
    "Select a module to preview its geometry",
  );
  useEffect(() => {
    if (!host.current) return;
    viewer.current = new BuildingViewer(host.current, setStatus);
    return () => viewer.current?.dispose();
  }, []);
  useEffect(() => {
    if (asset?.status === "prepared") viewer.current?.preview(asset);
  }, [asset]);
  return (
    <>
      <div
        ref={host}
        className="h-56 w-full overflow-hidden rounded-lg border border-line bg-surface"
      />
      <p className="hint mt-2" role="status">
        {status}
      </p>
    </>
  );
}
