import { useEffect, useState } from "react";
import { Search, ChevronLeft, ChevronRight, MousePointer2 } from "lucide-react";
import { api, pretty } from "../api";
import type { EditorStore } from "../store";
import type { LibraryAsset } from "../types";
import { Button, Modal, Select } from "./primitives";
import { AssetPreview } from "./Canvas";
interface Results {
  assets: LibraryAsset[];
  offset: number;
  total: number;
}
export function Library({
  store,
  onClose,
}: {
  store: EditorStore;
  onClose: () => void;
}) {
  const [query, setQuery] = useState(""),
    [role, setRole] = useState(""),
    [family, setFamily] = useState(""),
    [offset, setOffset] = useState(0),
    [result, setResult] = useState<Results>({
      assets: [],
      total: 0,
      offset: 0,
    }),
    [families, setFamilies] = useState<
      { name: string; path: string; prepared: number; assets: number }[]
    >([]),
    [asset, setAsset] = useState<LibraryAsset | null>(null),
    [appearance, setAppearance] = useState(""),
    [loading, setLoading] = useState(true),
    [error, setError] = useState("");
  useEffect(() => {
    const c = new AbortController();
    api<{ families: typeof families }>(
      "/api/library-families",
      undefined,
      c.signal,
    )
      .then((r) => setFamilies(r.families))
      .catch((e) => {
        if (e.name !== "AbortError") setError(String(e));
      });
    return () => c.abort();
  }, []);
  useEffect(() => {
    const c = new AbortController();
    setLoading(true);
    const timer = setTimeout(() => {
      api<Results>(
        "/api/library?" +
          new URLSearchParams({
            q: query,
            family,
            role,
            offset: String(offset),
          }),
        undefined,
        c.signal,
      )
        .then((r) => {
          setResult(r);
          setError("");
          setLoading(false);
        })
        .catch((e) => {
          if (e.name !== "AbortError") {
            setError(String(e));
            setLoading(false);
          }
        });
    }, 160);
    return () => {
      clearTimeout(timer);
      c.abort();
    };
  }, [query, family, role, offset]);
  function filter(fn: () => void) {
    setOffset(0);
    fn();
  }
  const dims = asset?.geometry?.dimensions || asset?.bounds?.dimensions;
  return (
    <Modal title="Module library" wide onClose={onClose}>
      <p className="hint mb-4">
        Measured game geometry, at its original size. Search for architecture,
        furniture or equipment.
      </p>
      <div className="mb-4 grid grid-cols-[1.4fr_1fr_1fr] gap-3">
        <label className="field">
          <span>Search modules</span>
          <div className="relative">
            <Search
              className="absolute left-3 top-3 text-slate-500"
              size={15}
            />
            <input
              className="!pl-9"
              type="search"
              autoFocus
              data-autofocus
              placeholder="Desk, cabinet, corridor…"
              value={query}
              onChange={(e) => filter(() => setQuery(e.target.value))}
            />
          </div>
        </label>
        <Select
          label="Module family"
          value={family}
          onChange={(v) => filter(() => setFamily(v))}
          options={[
            { value: "", label: "All families" },
            ...families.map((f) => ({
              value: f.path,
              label: `${pretty(f.name)} (${f.prepared})`,
            })),
          ]}
        />
        <Select
          label="Module type"
          value={role}
          onChange={(v) => filter(() => setRole(v))}
          options={[
            { value: "", label: "All types" },
            ...[
              "furniture",
              "equipment",
              "wall",
              "doorway",
              "floor",
              "ceiling",
              "stairs",
              "railing",
              "window",
              "roof",
              "structure",
              "trim",
              "specialist",
            ].map((v) => ({ value: v, label: pretty(v) })),
          ]}
        />
      </div>
      <div className="library-grid">
        <div className="flex min-h-0 flex-col">
          <div
            className="min-h-0 flex-1 overflow-y-auto pr-2"
            aria-busy={loading}
          >
            <div className="grid grid-cols-2 gap-2">
              {result.assets.map((item) => (
                <button
                  key={item.id}
                  aria-pressed={item.id === asset?.id}
                  className={`asset-card ${item.id === asset?.id ? "selected" : ""}`}
                  onClick={() => {
                    setAsset(item);
                    setAppearance(item.appearances?.[0] || "default");
                  }}
                >
                  <span className="mb-2 inline-block rounded bg-white/5 px-2 py-1 text-[10px] uppercase tracking-wider text-accent">
                    {item.role}
                  </span>
                  <strong className="block text-xs font-medium leading-5">
                    {pretty(item.name)}
                  </strong>
                  <span className="mt-2 block text-xs text-slate-400">
                    {(item.geometry?.dimensions || item.bounds?.dimensions)
                      ?.map((v) => v.toFixed(2))
                      .join(" × ")}{" "}
                    m
                  </span>
                  <span className="mt-1 block text-[10px] text-slate-500">
                    {item.status === "prepared"
                      ? "Ready to place"
                      : item.status}
                  </span>
                </button>
              ))}
            </div>
            {!loading && !result.assets.length && (
              <div className="py-16 text-center">
                <p>No matching modules</p>
                <p className="hint mt-2">
                  Try a broader name or clear the family filter.
                </p>
                <Button
                  className="mt-4"
                  onClick={() => {
                    setQuery("");
                    setFamily("");
                    setRole("");
                  }}
                >
                  Clear filters
                </Button>
              </div>
            )}
          </div>
          <div className="mt-3 flex items-center justify-between border-t border-line pt-3">
            <Button
              title="Previous page"
              disabled={offset === 0 || loading}
              onClick={() => setOffset(Math.max(0, offset - 48))}
            >
              <ChevronLeft size={16} />
            </Button>
            <span role="status" className="hint">
              {loading
                ? "Searching…"
                : `${result.total ? offset + 1 : 0}–${Math.min(offset + 48, result.total)} of ${result.total.toLocaleString()}`}
            </span>
            <Button
              title="Next page"
              disabled={offset + 48 >= result.total || loading}
              onClick={() => setOffset(offset + 48)}
            >
              <ChevronRight size={16} />
            </Button>
          </div>
        </div>
        <div className="min-w-0 overflow-y-auto rounded-lg border border-line bg-surface p-4">
          <AssetPreview asset={asset} />
          {asset ? (
            <>
              <h3 className="mt-4 font-medium">{pretty(asset.name)}</h3>
              <p className="hint mt-2">
                {dims?.map((v) => v.toFixed(3)).join(" × ")} m
              </p>
              <Select
                label="Appearance"
                value={appearance}
                onChange={setAppearance}
                options={(asset.appearances || []).map((v) => ({
                  value: v,
                  label: pretty(v),
                }))}
              />
              <details className="mb-3">
                <summary>Source resource</summary>
                <p className="code-panel mt-2">{asset.path}</p>
              </details>
              {(asset.error || asset.preview_error) && (
                <p role="alert" className="text-sm text-red-300">
                  {asset.error || asset.preview_error}
                </p>
              )}
              <Button
                primary
                className="w-full"
                disabled={asset.status !== "prepared" || loading}
                onClick={() => {
                  store.patch({
                    pendingModule: asset,
                    pendingAppearance: appearance,
                  });
                  store.tool("module");
                  store.message(
                    `Click the plan to place ${pretty(asset.name)}`,
                  );
                  onClose();
                }}
              >
                <MousePointer2 size={15} />
                Place on plan
              </Button>
              <p className="hint mt-3">
                Visual mesh only. Collision and interactive devices are authored
                separately.
              </p>
            </>
          ) : (
            <div className="py-6">
              <h3 className="font-medium">Select a module</h3>
              <p className="hint mt-2">
                Inspect its real dimensions and preview before placing it.
              </p>
            </div>
          )}
        </div>
      </div>
      {error && (
        <p role="alert" className="mt-3 text-red-300">
          {error}
        </p>
      )}
    </Modal>
  );
}
