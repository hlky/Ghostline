import { CharacterViewer } from "/viewer.js";

const state = {
  manifest: null,
  catalog: null,
  frameProfile: null,
  headPreviewUrl: null,
  fullPreviewUrl: null,
  assetIndex: null,
  assetResults: [],
  assetSummary: {},
  assetPreviews: new Map(),
};
const shapeNames = ["eyes", "nose", "mouth", "jaw", "ears"];

const byId = (id) => document.getElementById(id);

function setResult(value, isError = false) {
  const output = byId("result");
  output.textContent = typeof value === "string" ? value : JSON.stringify(value, null, 2);
  output.classList.toggle("error", isError);
}

function fieldValue(id) { return byId(id).value.trim(); }

function currentShapes() {
  return Object.fromEntries(shapeNames.map((name) => {
    const raw = byId(`shape-${name}`)?.value ?? "";
    return [name, raw === "" ? null : Number(raw)];
  }));
}

function updateAssetSummary(summary = {}) {
  const total = summary.total ?? 0;
  const clothing = summary.by_category?.clothing ?? 0;
  const previewable = summary.by_resource_type?.mesh ?? 0;
  byId("asset-index-summary").textContent = total
    ? `${total.toLocaleString()} assets · ${clothing.toLocaleString()} clothing records · ${previewable.toLocaleString()} previewable meshes`
    : "No generated index yet";
}

function renderAssets(data) {
  updateAssetSummary(data.summary);
  const rows = data.assets || [];
  state.assetResults = rows;
  state.assetSummary = data.summary || {};
  const results = byId("asset-results");
  if (!rows.length) {
    results.replaceChildren(Object.assign(document.createElement("p"), { textContent: "No matching assets." }));
    return;
  }
  results.replaceChildren(...rows.map((asset) => {
    const row = document.createElement("article");
    row.className = "asset-row";
    const copy = document.createElement("div");
    const title = document.createElement("strong");
    title.textContent = asset.family || asset.depot_path.split("\\").at(-1);
    const path = document.createElement("code");
    path.textContent = asset.depot_path;
    const meta = document.createElement("div");
    meta.className = "asset-meta";
    [asset.slot, asset.role, ...(asset.frame_tokens || []), asset.expansion]
      .filter(Boolean)
      .forEach((value) => {
        const chip = document.createElement("span");
        chip.textContent = value;
        meta.append(chip);
      });
    copy.append(title, path, meta);
    row.append(copy);
    const actions = document.createElement("div");
    actions.className = "asset-actions";
    if (asset.previewable) {
      const button = document.createElement("button");
      button.type = "button";
      button.textContent = "Preview mesh";
      button.addEventListener("click", () => previewAsset(asset.depot_path, button));
      actions.append(button);
    }
    const preview = state.assetPreviews.get(asset.depot_path);
    if (preview) {
      const available = preview.mesh_appearances || [];
      if (available.length) {
        const appearance = document.createElement("select");
        appearance.className = "asset-appearance";
        appearance.setAttribute("aria-label", `Mesh appearance for ${asset.family || asset.depot_path}`);
        for (const name of available) {
          const option = document.createElement("option");
          option.value = name;
          option.textContent = name;
          appearance.append(option);
        }
        const manifestCategory = preview.assignment?.manifest_category;
        const selected = state.manifest.appearance.indexed_overrides?.[manifestCategory];
        if (selected?.depot_path === asset.depot_path && available.includes(selected.mesh_appearance)) {
          appearance.value = selected.mesh_appearance;
        } else if (available.includes(preview.selectedAppearance)) {
          appearance.value = preview.selectedAppearance;
        }
        appearance.addEventListener("change", () => { preview.selectedAppearance = appearance.value; });
        actions.append(appearance);
        if (preview.assignment?.supported) {
          const use = document.createElement("button");
          use.type = "button";
          use.className = "primary";
          use.textContent = "Use in outfit";
          use.addEventListener("click", () => assignAsset(asset.depot_path, appearance.value, use));
          actions.append(use);
        }
      }
      if (!preview.assignment?.supported || !available.length) {
        const note = document.createElement("small");
        note.className = "asset-assignment-note";
        note.textContent = available.length
          ? (preview.assignment?.reasons || ["This mesh is preview-only."]).join(" · ")
          : "No selectable mesh appearances were found.";
        actions.append(note);
      }
    }
    row.append(actions);
    return row;
  }));
}

async function loadAssets() {
  if (!state.assetIndex?.available) {
    updateAssetSummary();
    return;
  }
  const parameters = new URLSearchParams({
    query: fieldValue("asset-query"),
    category: fieldValue("asset-category"),
    slot: fieldValue("asset-slot"),
    frame: fieldValue("asset-frame"),
    limit: "80",
  });
  const response = await fetch(`/api/assets?${parameters}`, { cache: "no-store" });
  const data = await response.json();
  if (!response.ok) throw new Error(data.error || `Asset search failed: ${response.status}`);
  renderAssets(data);
}

async function previewAsset(depotPath, button) {
  button.disabled = true;
  viewer.setStatus("Extracting selected mesh…");
  try {
    const result = await post("/api/assets/preview", { depot_path: depotPath });
    state.assetPreviews.set(result.source, result);
    await viewer.load(result.preview_url);
    renderAssets({ summary: state.assetSummary, assets: state.assetResults });
    setResult(result);
  } catch (error) {
    viewer.setStatus(String(error), true);
    setResult(String(error), true);
  } finally {
    button.disabled = false;
  }
}

async function assignAsset(depotPath, meshAppearance, button) {
  button.disabled = true;
  try {
    const result = await post("/api/assets/assign", {
      depot_path: depotPath,
      mesh_appearance: meshAppearance,
    });
    const category = result.manifest_category;
    const curated = byId(`catalog-${category}`);
    if (curated) {
      curated.value = result.anchor_option;
      curated.dispatchEvent(new Event("change"));
    }
    state.manifest.appearance.selections[category] = result.anchor_option;
    state.manifest.appearance.indexed_overrides[category] = result.override;
    state.fullPreviewUrl = null;
    renderSelectedOverrides();
    renderAssets({ summary: state.assetSummary, assets: state.assetResults });
    setResult(result);
  } catch (error) {
    setResult(String(error), true);
  } finally {
    button.disabled = false;
  }
}

function renderSelectedOverrides() {
  const container = byId("selected-overrides");
  const overrides = state.manifest.appearance.indexed_overrides || {};
  const entries = Object.entries(overrides);
  if (!entries.length) {
    container.replaceChildren(Object.assign(document.createElement("p"), {
      textContent: "No indexed clothing selected; curated template bundles are active.",
    }));
    return;
  }
  container.replaceChildren(...entries.map(([categoryId, override]) => {
    const row = document.createElement("article");
    row.className = "selected-override-row";
    const copy = document.createElement("div");
    const title = document.createElement("strong");
    title.textContent = `${state.catalog.categories[categoryId]?.label || categoryId} · ${override.mesh_appearance}`;
    const path = document.createElement("code");
    path.textContent = override.depot_path;
    copy.append(title, path);
    const remove = document.createElement("button");
    remove.type = "button";
    remove.textContent = "Remove";
    remove.addEventListener("click", () => {
      delete state.manifest.appearance.indexed_overrides[categoryId];
      state.fullPreviewUrl = null;
      renderSelectedOverrides();
      renderAssets({ summary: state.assetSummary, assets: state.assetResults });
    });
    row.append(copy, remove);
    return row;
  }));
}

function collectManifest() {
  const manifest = structuredClone(state.manifest);
  manifest.id = fieldValue("character-id");
  manifest.display_name = fieldValue("display-name");
  manifest.namespace = fieldValue("namespace");
  manifest.tweak.record = fieldValue("tweak-record");
  manifest.tweak.voice_tag = fieldValue("voice-tag");
  manifest.tweak.affiliation = fieldValue("affiliation");
  manifest.localization.female_variant = manifest.display_name;
  manifest.head.shapes = currentShapes();
  for (const category of Object.keys(state.catalog.categories)) {
    manifest.appearance.selections[category] = byId(`catalog-${category}`).value;
  }
  return manifest;
}

function requireFrameProfile(data) {
  const profile = data?.frame_profile;
  if (!profile
      || !["pma", "pwa"].includes(profile.player_token)
      || !Number.isInteger(profile.head_shape_max)) {
    throw new Error(
      "Character creator server is older than this UI. Restart tools/character_ui.py and reload the page.",
    );
  }
  return profile;
}

function render(data) {
  const frameProfile = requireFrameProfile(data);
  state.manifest = data.manifest;
  state.catalog = data.catalog;
  state.frameProfile = frameProfile;
  state.assetIndex = data.asset_index;
  state.headPreviewUrl = data.preview_url;
  state.fullPreviewUrl = data.full_preview_url;
  state.manifest.appearance.indexed_overrides ||= {};
  byId("character-id").value = state.manifest.id;
  byId("display-name").value = state.manifest.display_name;
  byId("character-frame").value = state.manifest.frame;
  byId("namespace").value = state.manifest.namespace;
  byId("tweak-record").value = state.manifest.tweak.record;
  byId("voice-tag").value = state.manifest.tweak.voice_tag;
  byId("affiliation").value = state.manifest.tweak.affiliation;
  byId("output-base").textContent = data.output_base;
  byId("asset-frame").value = frameProfile.player_token;
  const unresolved = frameProfile.unresolved_documented_values || [];
  byId("shape-range-hint").textContent = unresolved.length
    ? `This frame supports creator values 1–${frameProfile.head_shape_max}. Documented value ${unresolved.join(", ")} has no matching morph target for this profile. Empty values preserve the current head and block regeneration.`
    : `This frame supports creator values 1–${frameProfile.head_shape_max}. Empty values preserve the current head and block regeneration.`;

  const shapes = byId("shape-fields");
  shapes.replaceChildren(...shapeNames.map((name) => {
    const label = document.createElement("label");
    label.textContent = name;
    const input = document.createElement("input");
    input.type = "number";
    input.min = "1";
    input.max = String(frameProfile.head_shape_max);
    input.id = `shape-${name}`;
    input.value = state.manifest.head.shapes[name] ?? "";
    input.addEventListener("input", () => viewer.setShapes(currentShapes()));
    label.append(input);
    return label;
  }));

  const catalog = byId("catalog-fields");
  catalog.replaceChildren(...Object.entries(state.catalog.categories).map(([categoryId, category]) => {
    const wrapper = document.createElement("div");
    const label = document.createElement("label");
    label.textContent = category.label;
    const select = document.createElement("select");
    select.id = `catalog-${categoryId}`;
    const description = document.createElement("p");
    description.className = "option-description";
    for (const [optionId, option] of Object.entries(category.options)) {
      const node = document.createElement("option");
      node.value = optionId;
      node.textContent = option.label;
      select.append(node);
    }
    select.value = state.manifest.appearance.selections[categoryId];
    const updateDescription = () => {
      description.textContent = category.options[select.value]?.description || "";
    };
    select.addEventListener("change", () => {
      state.manifest.appearance.selections[categoryId] = select.value;
      state.fullPreviewUrl = null;
      if (state.manifest.appearance.indexed_overrides[categoryId]) {
        delete state.manifest.appearance.indexed_overrides[categoryId];
        renderSelectedOverrides();
        renderAssets({ summary: state.assetSummary, assets: state.assetResults });
      }
      updateDescription();
    });
    updateDescription();
    label.append(select);
    wrapper.append(label, description);
    return wrapper;
  }));

  renderSelectedOverrides();

  byId("connection").textContent = data.validation.ok ? "Engine ready" : "Needs attention";
  setResult(data.validation, !data.validation.ok);
  viewer.setShapes(currentShapes());
  if (data.preview_url) {
    viewer.load(data.preview_url).catch((error) => viewer.setStatus(String(error), true));
  }
  updateAssetSummary(data.asset_index?.summary);
  loadAssets().catch((error) => setResult(String(error), true));
}

async function post(route, extra = {}) {
  const response = await fetch(route, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ manifest: collectManifest(), ...extra }),
  });
  const result = await response.json();
  setResult(result, !response.ok);
  if (!response.ok) throw new Error(result.error || `Request failed: ${response.status}`);
  return result;
}

async function action(name) {
  const buttons = [...document.querySelectorAll("button")];
  buttons.forEach((button) => { button.disabled = true; });
  try {
    if (name === "download") {
      const blob = new Blob([JSON.stringify(collectManifest(), null, 2) + "\n"], { type: "application/json" });
      const link = document.createElement("a");
      link.href = URL.createObjectURL(blob);
      link.download = `${collectManifest().id}.character.json`;
      link.click();
      URL.revokeObjectURL(link.href);
      return;
    }
    const routes = {
      validate: "/api/validate",
      generate: "/api/generate",
      "head-plan": "/api/head/plan",
      "head-build": "/api/head/build",
    };
    if (name === "preview-prepare") {
      const result = await post("/api/preview/prepare", {
        include_all_head_parts: byId("preview-all-parts").checked,
      });
      state.headPreviewUrl = result.preview_url;
      await viewer.load(result.preview_url);
      return;
    }
    if (name === "preview-full") {
      viewer.setStatus("Assembling full character…");
      const result = await post("/api/preview/full");
      state.headPreviewUrl = `/preview/${collectManifest().id}/preview/preview-manifest.json`;
      state.fullPreviewUrl = result.preview_url;
      await viewer.load(result.preview_url);
      return;
    }
    if (name === "asset-index") {
      const result = await post("/api/assets/index");
      state.assetIndex = { available: true, summary: result.summary };
      updateAssetSummary(result.summary);
      await loadAssets();
      return;
    }
    await post(routes[name]);
  } catch (error) {
    setResult(String(error), true);
  } finally {
    buttons.forEach((button) => { button.disabled = false; });
  }
}

document.querySelectorAll("button[data-action]").forEach((button) => {
  button.addEventListener("click", () => action(button.dataset.action));
});

const viewer = new CharacterViewer(byId("character-viewport"), byId("viewport-status"));
byId("viewport-reset").addEventListener("click", () => viewer.resetView());
byId("viewport-head").addEventListener("click", () => {
  if (state.headPreviewUrl) viewer.load(state.headPreviewUrl).catch((error) => viewer.setStatus(String(error), true));
  else viewer.setStatus("Prepare the live head preview first", true);
});
byId("viewport-full").addEventListener("click", () => {
  if (state.fullPreviewUrl) {
    viewer.load(state.fullPreviewUrl).catch((error) => viewer.setStatus(String(error), true));
  } else {
    viewer.setStatus("Prepare the full-character preview first", true);
  }
});
byId("viewport-wireframe").addEventListener("click", (event) => {
  const enabled = event.currentTarget.getAttribute("aria-pressed") !== "true";
  event.currentTarget.setAttribute("aria-pressed", String(enabled));
  viewer.setWireframe(enabled);
});

let assetSearchTimer;
for (const id of ["asset-query", "asset-category", "asset-slot", "asset-frame"]) {
  byId(id).addEventListener(id === "asset-query" ? "input" : "change", () => {
    window.clearTimeout(assetSearchTimer);
    assetSearchTimer = window.setTimeout(() => loadAssets().catch((error) => setResult(String(error), true)), 180);
  });
}

fetch("/api/bootstrap")
  .then((response) => response.json())
  .then(render)
  .catch((error) => {
    byId("connection").textContent = String(error).includes("Restart tools/character_ui.py")
      ? "Restart required"
      : "Offline";
    setResult(String(error), true);
  });
