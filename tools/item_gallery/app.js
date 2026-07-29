const byId = (id) => document.getElementById(id);
const filters = byId("filters");
const grid = byId("items");
const status = byId("status");
const template = byId("item-template");
let requestToken = 0;
let debounce;
let currentPage = 1;
const pageSize = 48;

const sourceRow = (label, value) => {
  const fragment = document.createDocumentFragment();
  const term = document.createElement("dt");
  const detail = document.createElement("dd");
  term.textContent = label;
  detail.textContent = value || "—";
  fragment.append(term, detail);
  return fragment;
};

function populateSelect(select, rows, valueKey, countKey, allLabel, labelFor = (value) => value) {
  select.replaceChildren(new Option(allLabel, ""));
  for (const row of rows) {
    const value = row[valueKey];
    select.append(new Option(`${labelFor(value)} · ${row[countKey]}`, value));
  }
}

async function bootstrap() {
  const response = await fetch("/api/summary", { cache: "no-store" });
  if (!response.ok) throw new Error(`Summary failed: ${response.status}`);
  const summary = await response.json();
  const values = [
    ["Items", summary.items],
    ["Variants", summary.variants],
    ["Rendered", summary.rendered],
  ];
  const stats = byId("stats").querySelectorAll("div");
  values.forEach(([label, value], index) => {
    stats[index].querySelector("dt").textContent = label;
    stats[index].querySelector("dd").textContent = value ?? "—";
  });
  populateSelect(byId("slot"), summary.slots, "slot", "count", "All slots");
  populateSelect(
    byId("frame"),
    summary.frames,
    "frame",
    "count",
    "All body types",
    (value) => ({ pma: "Male (PMA)", pwa: "Female (PWA)" })[value] || value,
  );
  populateSelect(byId("tag"), summary.tags, "tag", "count", "All tags");
}

function cardFor(item) {
  const card = template.content.firstElementChild.cloneNode(true);
  const setView = (imageSelector, placeholderSelector, url, label) => {
    const image = card.querySelector(imageSelector);
    const placeholder = card.querySelector(placeholderSelector);
    if (url) {
      image.src = url;
      image.alt = `${item.title}, ${item.frame} ${label.toLowerCase()} render`;
      image.hidden = false;
      placeholder.hidden = true;
      return;
    }
    image.hidden = true;
    placeholder.hidden = false;
  };
  setView(
    ".hero-view",
    ".hero-placeholder",
    item.view_urls?.hero || item.image_url,
    "Front",
  );
  setView(".back-view", ".back-placeholder", item.view_urls?.back, "Back");
  card.querySelector(".frame").textContent = item.frame.toUpperCase();
  card.querySelector(".slot").textContent = item.slot.replaceAll("_", " ");
  card.querySelector("h2").textContent = item.title;
  card.querySelector(".description").textContent =
    item.description || "No localized description is present in the installed database.";
  const tags = card.querySelector(".tags");
  for (const value of item.tags.slice(0, 7)) {
    const tag = document.createElement("button");
    tag.type = "button";
    tag.textContent = value;
    tag.addEventListener("click", () => {
      byId("tag").value = value;
      loadItems();
    });
    tags.append(tag);
  }
  const source = card.querySelector(".source");
  source.append(
    sourceRow("Record", item.record_id),
    sourceRow("Appearance", item.app_appearance),
    sourceRow("Mesh skin", item.mesh_appearance),
    sourceRow("Mesh", item.primary_mesh),
    sourceRow("Expansion", item.expansion.replaceAll("_", " ")),
  );
  return card;
}

async function loadItems() {
  const token = ++requestToken;
  const data = new FormData(filters);
  const params = new URLSearchParams();
  for (const [key, value] of data.entries()) if (value) params.set(key, value);
  params.set("limit", String(pageSize));
  params.set("offset", String((currentPage - 1) * pageSize));
  status.textContent = "Querying equipment graph…";
  const response = await fetch(`/api/items?${params}`, { cache: "no-store" });
  if (!response.ok) throw new Error(`Item query failed: ${response.status}`);
  const result = await response.json();
  if (token !== requestToken) return;
  const pageCount = Math.max(1, Math.ceil(result.total / pageSize));
  if (currentPage > pageCount) {
    currentPage = pageCount;
    return loadItems();
  }
  grid.replaceChildren(...result.items.map(cardFor));
  const first = result.total ? result.offset + 1 : 0;
  const last = result.offset + result.items.length;
  status.textContent = `Showing ${first}–${last} of ${result.total} variants`;
  byId("page-status").textContent = `Page ${currentPage} of ${pageCount}`;
  byId("previous").disabled = currentPage <= 1;
  byId("next").disabled = currentPage >= pageCount;
}

filters.addEventListener("input", (event) => {
  clearTimeout(debounce);
  currentPage = 1;
  debounce = setTimeout(loadItems, event.target.type === "search" ? 180 : 0);
});
byId("clear").addEventListener("click", () => {
  filters.reset();
  currentPage = 1;
  loadItems();
});
byId("previous").addEventListener("click", () => {
  if (currentPage <= 1) return;
  currentPage -= 1;
  loadItems();
  window.scrollTo({ top: filters.offsetTop, behavior: "smooth" });
});
byId("next").addEventListener("click", () => {
  currentPage += 1;
  loadItems();
  window.scrollTo({ top: filters.offsetTop, behavior: "smooth" });
});

try {
  await bootstrap();
  await loadItems();
} catch (error) {
  status.textContent = error.message;
  status.classList.add("error");
}
