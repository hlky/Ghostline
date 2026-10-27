// Imperative SVG canvas adapter. React owns surrounding UI and state.
import { clearDoor, wallSpan, drawWall } from "../wall-controls.js";
export function createPlanAdapter(element, initial, actions) {
  let state = initial;
  const events = new AbortController();
  const listen = (type, handler, options = {}) =>
    element.addEventListener(type, handler, {
      ...options,
      signal: events.signal,
    });
  const svgNS = "http://www.w3.org/2000/svg";
  const uid = (prefix) =>
    `${prefix}_${crypto.randomUUID().replaceAll("-", "").slice(0, 8)}`;
  const $ = (id) =>
    id === "plan"
      ? element
      : id === "plan-content" || id === "draft"
        ? element.querySelector("#" + id)
        : {
            checked:
              id === "plan-zones"
                ? state.preview.zones
                : state.preview.navigation,
          };
  const mutate = actions.mutate;
  const message = actions.message;
  const render = () => {
    actions.select({
      selected: state.selected,
      selectedModule: state.selectedModule,
      door: state.door,
      wall: state.wall,
    });
    renderPlan();
  };
  const setTool = (tool) => actions.tool(tool);
  const library = {
    get selected() {
      return state.pendingModule;
    },
    get appearance() {
      return state.pendingAppearance;
    },
  };
  function svg(name, attributes, parent, text) {
    const node = document.createElementNS(svgNS, name);
    for (const [key, value] of Object.entries(attributes))
      node.setAttribute(key, value);
    if (text !== undefined) node.textContent = text;
    parent.appendChild(node);
    return node;
  }

  function moduleFootprint(instance) {
    const { min: lo, max: hi } = instance.bounds,
      a = (instance.yaw * Math.PI) / 180;
    return [
      [lo[0], lo[1]],
      [hi[0], lo[1]],
      [hi[0], hi[1]],
      [lo[0], hi[1]],
    ].map(([x, y]) => [
      instance.position[0] + x * Math.cos(a) - y * Math.sin(a),
      instance.position[1] + x * Math.sin(a) + y * Math.cos(a),
    ]);
  }

  function renderPlan() {
    const content = $("plan-content");
    content.replaceChildren();
    svg(
      "rect",
      { x: -200, y: -200, width: 400, height: 400, fill: "url(#subgrid)" },
      content,
    );
    svg(
      "rect",
      { x: -200, y: -200, width: 400, height: 400, fill: "url(#grid)" },
      content,
    );
    svg(
      "path",
      {
        d: "M -100 0 H 100 M 0 -100 V 100",
        stroke: "#46605a",
        "stroke-width": 0.035,
        opacity: 0.6,
        "pointer-events": "none",
      },
      content,
    );
    const zones = $("plan-zones").checked;
    const rooms = state.layout.rooms.filter(
      (room) => room.level === state.level,
    );
    for (const room of (state.layout.shell_rooms || []).filter(
      (room) => (room.level || 0) === state.level,
    )) {
      const [x, y, z] = room.position;
      const measured = state.scene.shell_rooms.find((r) => r.id === room.id);
      svg(
        "polygon",
        {
          points: measured.outline.map((p) => `${p[0]},${-p[1]}`).join(" "),
          class: "room-shape",
          ...(!zones ? { style: "stroke:none" } : {}),
          "pointer-events": "none",
        },
        content,
      );
      if (room.label === false || !zones) continue;
      svg(
        "text",
        { x: x + room.width / 2, y: -y - room.depth / 2, class: "room-label" },
        content,
        room.name || room.id,
      );
      const area = measured.footprints.reduce(
        (a, b) => a + (b[2] - b[0]) * (b[3] - b[1]),
        0,
      );
      svg(
        "text",
        {
          x: x + room.width / 2,
          y: -y - room.depth / 2 + 0.6,
          class: "room-dimension",
        },
        content,
        `${area.toFixed(1)} m² · Z ${z} m`,
      );
    }
    for (const room of rooms) {
      svg(
        "rect",
        {
          x: room.x,
          y: -room.y - room.depth,
          width: room.width,
          height: room.depth,
          class: `room-shape${state.selected === room.id ? " selected" : ""}`,
          ...(!zones && state.selected !== room.id
            ? { style: "stroke:none" }
            : {}),
          "data-room": room.id,
        },
        content,
      );
      if (!zones) continue;
      svg(
        "text",
        {
          x: room.x + room.width / 2,
          y: -room.y - room.depth / 2 - 0.1,
          class: "room-label",
        },
        content,
        room.name,
      );
      svg(
        "text",
        {
          x: room.x + room.width / 2,
          y: -room.y - room.depth / 2 + 0.5,
          class: "room-dimension",
        },
        content,
        `${room.width} × ${room.depth} m · ${room.width * room.depth} m²`,
      );
    }
    for (const edge of state.scene.edges.filter(
      (edge) => edge.level === state.level,
    )) {
      const x = edge.x,
        y = -edge.y,
        dx = edge.axis === "x" ? 3 : 0,
        dy = edge.axis === "y" ? -3 : 0;
      const line = (from, to, cls = "wall-line") =>
        svg(
          "line",
          {
            x1: x + dx * from,
            y1: y + dy * from,
            x2: x + dx * to,
            y2: y + dy * to,
            class: cls + (edge.shared ? " shared" : ""),
          },
          content,
        );
      if (!edge.opening) line(0, 1);
      if (["doorway", "door_auto", "door_manual"].includes(edge.opening)) {
        line(0, 0.25);
        line(0.75, 1);
        const a = [x + dx * 0.25, y + dy * 0.25],
          b = [x + dx * 0.75, y + dy * 0.75];
        svg(
          "line",
          {
            x1: a[0],
            y1: a[1],
            x2: b[0],
            y2: b[1],
            class: "door-mark",
            "stroke-dasharray": ".13 .1",
          },
          content,
        );
        const nx = edge.axis === "y" ? 0.2 : 0,
          ny = edge.axis === "x" ? -0.2 : 0;
        svg(
          "line",
          {
            x1: a[0] + nx,
            y1: a[1] + ny,
            x2: b[0] + nx,
            y2: b[1] + ny,
            class: "door-mark",
          },
          content,
        );
      }
      if (edge.opening === "passage" && zones) {
        line(0, 1, "door-mark");
      }
      if (
        [
          "doorway",
          "passage",
          "door_auto",
          "door_manual",
          "select",
          "wall",
        ].includes(state.tool)
      ) {
        svg(
          "line",
          {
            x1: x,
            y1: y,
            x2: x + dx,
            y2: y + dy,
            class: "edge-hit",
            "data-edge": edge.id,
          },
          content,
        );
      }
    }
    for (const solid of state.scene.solids.filter(
      (s) =>
        s.level === state.level &&
        s.role === "wall" &&
        s.id.startsWith("shell:"),
    )) {
      const z = state.level * state.scene.kit.storey_height + 1;
      if (
        solid.center[2] - solid.size[2] / 2 > z ||
        solid.center[2] + solid.size[2] / 2 < z
      )
        continue;
      const a = (solid.yaw * Math.PI) / 180,
        dx = (Math.cos(a) * solid.size[0]) / 2,
        dy = (Math.sin(a) * solid.size[0]) / 2;
      svg(
        "line",
        {
          x1: solid.center[0] - dx,
          y1: -solid.center[1] + dy,
          x2: solid.center[0] + dx,
          y2: -solid.center[1] - dy,
          class: "wall-line",
        },
        content,
      );
      if (state.tool === "wall") {
        const parts = solid.id.split(":");
        const key =
          parts[1] === "liner"
            ? `liner:${parts[2]}`
            : `shell:${parts[1]}:${parts[2]}`;
        svg(
          "line",
          {
            x1: solid.center[0] - dx,
            y1: -solid.center[1] + dy,
            x2: solid.center[0] + dx,
            y2: -solid.center[1] - dy,
            class: "edge-hit",
            "data-wall": key,
          },
          content,
        );
      }
    }
    if (["wall", "partition"].includes(state.tool)) {
      for (const [index, wall] of (state.layout.shell_liners || []).entries()) {
        if (!wall.disabled || (wall.level || 0) !== state.level) continue;
        svg(
          "line",
          {
            x1: wall.start[0],
            y1: -wall.start[1],
            x2: wall.end[0],
            y2: -wall.end[1],
            class: "door-mark",
            "stroke-dasharray": ".12 .12",
          },
          content,
        );
        svg(
          "line",
          {
            x1: wall.start[0],
            y1: -wall.start[1],
            x2: wall.end[0],
            y2: -wall.end[1],
            class: "edge-hit",
            "data-wall": "liner:" + index,
          },
          content,
        );
      }
      if (state.wallStart)
        svg(
          "circle",
          {
            cx: state.wallStart.x,
            cy: -state.wallStart.y,
            r: 0.18,
            fill: "#c6df91",
          },
          content,
        );
    }
    if (state.tool === "wall" && state.wall) {
      let span = wallSpan(state.layout, state.wall);
      if (state.wall.startsWith("edge:")) {
        const edge = state.scene.edges.find(
          (e) => e.id === state.wall.slice(5),
        );
        if (edge)
          span = {
            start: [edge.x, edge.y],
            end: [
              edge.x + (edge.axis === "x" ? 3 : 0),
              edge.y + (edge.axis === "y" ? 3 : 0),
            ],
          };
      }
      if (span)
        svg(
          "line",
          {
            x1: span.start[0],
            y1: -span.start[1],
            x2: span.end[0],
            y2: -span.end[1],
            stroke: "#c6df91",
            "stroke-width": 0.13,
            "pointer-events": "none",
          },
          content,
        );
    }
    for (const door of (state.scene.shell_doors || []).filter(
      (d) => d.level === state.level,
    )) {
      const [x0, y0, x1, y1] = door.gate;
      const horizontal = x1 - x0 > y1 - y0;
      svg(
        "line",
        {
          x1: horizontal ? x0 : (x0 + x1) / 2,
          x2: horizontal ? x1 : (x0 + x1) / 2,
          y1: horizontal ? -(y0 + y1) / 2 : -y0,
          y2: horizontal ? -(y0 + y1) / 2 : -y1,
          class: "door-mark",
          "stroke-dasharray": ".13 .1",
        },
        content,
      );
    }
    for (const stair of state.scene.stairs.filter(
      (s) => s.level === state.level || s.level + 1 === state.level,
    )) {
      if (stair.type === "return") {
        svg(
          "rect",
          {
            x: stair.x,
            y: -stair.y - stair.run,
            width: stair.width,
            height: stair.run + stair.landing,
            class: "stair-outline",
          },
          content,
        );
        for (const x of [stair.x, stair.x + stair.width - stair.flight_width]) {
          for (let y = 0; y <= stair.run; y += 0.3)
            svg(
              "line",
              {
                x1: x,
                x2: x + stair.flight_width,
                y1: -stair.y - y,
                y2: -stair.y - y,
                class: "stair-tread",
              },
              content,
            );
        }
        svg(
          "text",
          {
            x: stair.x + stair.width / 2,
            y: -stair.y + stair.landing / 2,
            class: "room-dimension",
          },
          content,
          "TURN",
        );
        continue;
      }
      if (stair.axis === "x") {
        svg(
          "rect",
          {
            x: stair.x,
            y: -stair.y,
            width: stair.run,
            height: stair.width,
            class: "stair-outline",
          },
          content,
        );
        for (let v = 0; v < stair.run; v += 0.45)
          svg(
            "line",
            {
              x1: stair.x + v,
              x2: stair.x + v,
              y1: -stair.y,
              y2: -stair.y + stair.width,
              class: "stair-tread",
            },
            content,
          );
        svg(
          "text",
          {
            x: stair.x + stair.run / 2,
            y: -stair.y + stair.width / 2,
            class: "room-label",
          },
          content,
          "STAIRS →",
        );
        continue;
      }
      svg(
        "rect",
        {
          x: stair.x,
          y: -stair.y - stair.run,
          width: stair.width,
          height: stair.run,
          class: "stair-outline",
        },
        content,
      );
      for (let y = 0; y < stair.run; y += 0.45)
        svg(
          "line",
          {
            x1: stair.x,
            x2: stair.x + stair.width,
            y1: -stair.y - y,
            y2: -stair.y - y,
            class: "stair-tread",
          },
          content,
        );
      svg(
        "text",
        {
          x: stair.x + stair.width / 2,
          y: -stair.y - stair.run / 2,
          class: "room-label",
        },
        content,
        "STAIRS ↑",
      );
    }
    if ($("nav-preview").checked)
      for (const [
        index,
        triangle,
      ] of state.scene.navigation.triangles.entries()) {
        if (
          !triangle.some(
            (p) =>
              Math.abs(p[2] - state.level * state.scene.kit.storey_height) <
              0.05,
          )
        )
          continue;
        svg(
          "polygon",
          {
            points: triangle.map((p) => `${p[0]},${-p[1]}`).join(" "),
            class: state.route.includes(index)
              ? "nav-face route-face"
              : "nav-face",
          },
          content,
        );
      }
    if ($("nav-preview").checked)
      for (const link of state.scene.navigation.links.filter(
        (link) => link.area === 12,
      )) {
        const [a, b] = link.endpoints;
        svg(
          "line",
          { x1: a[0], y1: -a[1], x2: b[0], y2: -b[1], class: "entrance-link" },
          content,
        );
      }
    const selected = rooms.find((room) => room.id === state.selected);
    if (selected && state.tool === "select") {
      svg(
        "circle",
        {
          cx: selected.x + selected.width,
          cy: -selected.y - selected.depth,
          r: 0.21,
          class: "resize-handle",
          "data-resize": selected.id,
        },
        content,
      );
    }
    for (const instance of state.scene.instances.filter(
      (i) => i.kind === "module" && i.level === state.level,
    )) {
      const points = moduleFootprint(instance)
        .map(([x, y]) => `${x},${-y}`)
        .join(" ");
      const id = instance.id.slice(7);
      svg(
        "polygon",
        {
          points,
          class:
            "module-outline" +
            (instance.reference_only ? " shell-reference" : "") +
            (id === state.selectedModule ? " selected" : ""),
          "data-module": id,
        },
        content,
      );
    }
    // Keep entrance selection above the retained shell footprints.
    for (const door of (state.scene.shell_doors || []).filter(
      (d) => d.level === state.level,
    )) {
      const [x0, y0, x1, y1] = door.gate;
      svg(
        "rect",
        {
          x: x0,
          y: -y1,
          width: x1 - x0,
          height: y1 - y0,
          fill: "transparent",
          "pointer-events": "all",
          "data-door": door.id,
          role: "button",
          "aria-label": "Select " + door.id + " door",
        },
        content,
      );
    }
    for (const w of (state.scene.workstations || []).filter(
      (w) => w.level === state.level,
    )) {
      const [x, y] = w.actor.position;
      svg(
        "circle",
        { cx: x, cy: -y, r: 0.18, fill: "#d8e6a4", "pointer-events": "none" },
        content,
      );
      svg(
        "text",
        {
          x: x + 0.25,
          y: -y,
          class: "room-dimension",
          "pointer-events": "none",
        },
        content,
        "Worker seat",
      );
    }
  }

  function planPoint(event, step = 3) {
    const point = $("plan").createSVGPoint();
    point.x = event.clientX;
    point.y = event.clientY;
    const local = point.matrixTransform($("plan").getScreenCTM().inverse());
    return {
      x: Math.round(local.x / step) * step,
      y: Math.round(-local.y / step) * step,
    };
  }

  function draftRoom(drag, point) {
    if (drag.mode === "room")
      return {
        x: Math.min(drag.start.x, point.x),
        y: Math.min(drag.start.y, point.y),
        width: Math.max(3, Math.abs(point.x - drag.start.x)),
        depth: Math.max(3, Math.abs(point.y - drag.start.y)),
      };
    const room = state.layout.rooms.find((room) => room.id === drag.id);
    if (drag.mode === "resize")
      return {
        x: room.x,
        y: room.y,
        width: Math.max(3, point.x - room.x),
        depth: Math.max(3, point.y - room.y),
      };
    return {
      ...room,
      x: room.x + point.x - drag.start.x,
      y: room.y + point.y - drag.start.y,
    };
  }

  listen("pointerdown", (event) => {
    if (event.button !== 0 || !state.layout) return;
    if (state.tool === "module" && library.selected) {
      const point = planPoint(event),
        level = state.level,
        id = uid("module"),
        record = library.selected,
        appearance = library.appearance;
      state.selectedModule = id;
      mutate((layout) => {
        layout.modules ||= [];
        layout.modules.push({
          id,
          asset: record.id,
          source_sha256:
            record.source_content_sha256 || record.source_json_sha256,
          geometry_sha256: record.preview_sha256,
          appearance,
          position: [point.x, point.y, level * state.scene.kit.storey_height],
          yaw: 0,
          level,
          anchor: "base-center",
          collision: "none",
        });
      }, "Vanilla module placed").then(() => setTool("select"));
      return;
    }
    if (["wall", "partition"].includes(state.tool)) {
      const hit =
        state.tool === "wall" &&
        event.target.closest("[data-wall], [data-edge]");
      if (hit) {
        state.wall = hit.dataset.wall || "edge:" + hit.dataset.edge;
        state.wallStart = null;
        render();

        return;
      }
      const point = planPoint(event, 0.05);
      if (!state.wallStart) {
        state.wallStart = point;
        message("Wall start selected. Click the other end.");
        renderPlan();
        return;
      }
      const start = state.wallStart,
        level = state.level;
      if (Math.abs(point.x - start.x) > Math.abs(point.y - start.y))
        point.y = start.y;
      else point.x = start.x;
      state.wallStart = null;
      mutate((layout) => {
        state.wall = drawWall(
          layout,
          start,
          point,
          level,
          Math.min(3.5, state.scene.kit.storey_height - 0.2),
          state.scene.kit.storey_height,
        );
      }, "Partition added").then(() => setTool("wall"));
      return;
    }
    const shellDoor = event.target.closest("[data-door]");
    if (shellDoor && state.tool === "select") {
      state.door = shellDoor.dataset.door;
      render();
      return;
    }
    const moduleTarget = event.target.closest("[data-module]");
    if (moduleTarget && state.tool === "select") {
      state.selectedModule = moduleTarget.dataset.module;
      state.selected = null;
      render();
      return;
    }
    const edge = event.target.closest("[data-edge]");
    if (
      edge &&
      ["doorway", "passage", "door_auto", "door_manual"].includes(state.tool)
    ) {
      const identity = edge.dataset.edge,
        tool = state.tool;
      state.door = identity;
      mutate((layout) => {
        if (layout.openings[identity] === tool)
          delete layout.openings[identity];
        else layout.openings[identity] = tool;
        if (!["door_auto", "door_manual"].includes(layout.openings[identity])) {
          clearDoor(layout, identity);
        }
      }, "Wall opening updated");
      return;
    }
    if (
      edge &&
      state.tool === "select" &&
      state.scene.doors.some((door) => door.id === edge.dataset.edge)
    ) {
      state.door = edge.dataset.edge;
      render();
      return;
    }
    const point = planPoint(event);
    if (state.tool === "stair") {
      const level = state.level;
      mutate((layout) => {
        layout.stairs ||= [];
        layout.stairs.push({
          id: uid("stair"),
          level,
          x: point.x,
          y: point.y,
          width: 3,
          run: 9,
        });
      }, "Stair flight added");
      return;
    }
    if (state.tool === "room") state.drag = { mode: "room", start: point };
    else if (state.tool === "select") {
      const resize = event.target.closest("[data-resize]");
      const room = event.target.closest("[data-room]");
      if (resize || room) {
        state.selected = resize?.dataset.resize || room.dataset.room;
        state.drag = {
          mode: resize ? "resize" : "move",
          id: state.selected,
          start: point,
        };
        render();
      } else {
        state.selected = null;
        render();
      }
    }
    if (state.drag) $("plan").setPointerCapture(event.pointerId);
  });

  listen("pointermove", (event) => {
    if (!state.drag) return;
    const room = draftRoom(state.drag, planPoint(event));
    $("draft").replaceChildren();
    svg(
      "rect",
      {
        x: room.x,
        y: -room.y - room.depth,
        width: room.width,
        height: room.depth,
        class: "ghost-room",
      },
      $("draft"),
    );
    svg(
      "text",
      {
        x: room.x + room.width / 2,
        y: -room.y - room.depth / 2,
        class: "room-label",
      },
      $("draft"),
      `${room.width} × ${room.depth} m`,
    );
  });

  listen("pointerup", (event) => {
    if (!state.drag) return;
    const drag = state.drag,
      point = planPoint(event),
      room = draftRoom(drag, point);
    state.drag = null;
    $("draft").replaceChildren();
    if (drag.mode === "room") {
      const id = uid("room"),
        level = state.level;
      mutate((layout) => {
        layout.rooms.push({
          id,
          name: `Room ${layout.rooms.length + 1}`,
          level,
          ...room,
        });
      }, "Room added").then(() => {
        if (state.layout.rooms.some((room) => room.id === id)) {
          state.selected = id;
          setTool("select");
          render();
        }
      });
    } else if (
      drag.mode === "resize" ||
      point.x !== drag.start.x ||
      point.y !== drag.start.y
    ) {
      mutate(
        (layout) =>
          Object.assign(
            layout.rooms.find((room) => room.id === drag.id),
            room,
          ),
        drag.mode === "resize" ? "Room resized" : "Room moved",
      );
    }
  });
  listen("pointercancel", () => {
    state.drag = null;
    $("draft").replaceChildren();
  });

  listen(
    "wheel",
    (event) => {
      event.preventDefault();
      const box = $("plan").viewBox.baseVal;
      const factor = event.deltaY > 0 ? 1.12 : 0.89;
      const width = Math.max(9, Math.min(150, box.width * factor));
      const height = (width * box.height) / box.width;
      $("plan").setAttribute(
        "viewBox",
        `${box.x + (box.width - width) / 2} ${box.y + (box.height - height) / 2} ${width} ${height}`,
      );
    },
    { passive: false },
  );

  function fitPlan() {
    const rooms = state.layout.rooms.filter(
      (room) => room.level === state.level,
    );
    const points = rooms.flatMap((r) => [
      [r.x, r.y],
      [r.x + r.width, r.y + r.depth],
    ]);
    points.push(
      ...state.scene.instances
        .filter((i) => i.kind === "module" && i.level === state.level)
        .flatMap(moduleFootprint),
    );
    const minX = points.length ? Math.min(...points.map((p) => p[0])) : 0;
    const minY = points.length ? Math.min(...points.map((p) => p[1])) : 0;
    const maxX = points.length ? Math.max(...points.map((p) => p[0])) : 12;
    const maxY = points.length ? Math.max(...points.map((p) => p[1])) : 9;
    const ratio = $("plan").clientWidth / Math.max($("plan").clientHeight, 1);
    const width = Math.max(maxX - minX + 9, (maxY - minY + 9) * ratio);
    const height = width / ratio;
    const cx = (minX + maxX) / 2,
      cy = (minY + maxY) / 2;
    $("plan").setAttribute(
      "viewBox",
      `${cx - width / 2} ${-cy - height / 2} ${width} ${height}`,
    );
  }

  return {
    update(next) {
      state = next;
      renderPlan();
    },
    fit: fitPlan,
    destroy() {
      events.abort();
    },
  };
}
