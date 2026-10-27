export type Vec3 = [number, number, number];
export type Tool =
  | "select"
  | "room"
  | "doorway"
  | "passage"
  | "door_auto"
  | "door_manual"
  | "stair"
  | "wall"
  | "partition"
  | "module";
export interface Room {
  id: string;
  name: string;
  level: number;
  x: number;
  y: number;
  width: number;
  depth: number;
  ceiling_height?: number;
}
export interface Module {
  id: string;
  asset: string;
  position: Vec3;
  yaw: number;
  level: number;
  anchor: string;
  collision: string;
  appearance: string;
  reference_only?: boolean;
  source_sha256?: string;
  geometry_sha256?: string;
}
export interface Workstation {
  id: string;
  desk: string;
  chair: string;
  actor: {
    record: string;
    appearance: string;
    active_on_start: boolean;
    offset: Vec3;
    yaw_offset: number;
    workspot: string;
  };
  computer: { offset: Vec3; yaw_offset: number };
}
export interface SectorPatch {
  path: string;
  nodeDeletions: Record<string, unknown>[];
  [key: string]: unknown;
}
export interface Layout {
  schema_version: number;
  id: string;
  name: string;
  kit: string;
  origin: { x: number; y: number; z: number; yaw: number };
  rooms: Room[];
  modules: Module[];
  openings: Record<string, string>;
  stairs: {
    id: string;
    level: number;
    x: number;
    y: number;
    width: number;
    run: number;
  }[];
  wall_appearance: string;
  floor_appearance: string;
  door_states?: Record<string, string>;
  door_devices?: Record<string, unknown>;
  windows?: Record<string, unknown>;
  navigation: {
    radius?: number;
    layer?: number;
    export?: boolean;
    connections?: { id: string; from: number[]; to: number[] }[];
    door_connections?: Record<string, unknown>;
  };
  retrofit?: { sectors: SectorPatch[] };
  workstations?: Workstation[];
  [extension: string]: unknown;
}
export interface Kit {
  id: string;
  name: string;
  storey_height: number;
  wall_height: number;
  wall_appearances: string[];
  floor_appearances: string[];
  [key: string]: unknown;
}
export interface Instance {
  id: string;
  kind: string;
  level: number;
  name: string;
  position: Vec3;
  yaw: number;
  bounds: { min: Vec3; max: Vec3 };
  appearances?: string[];
  reference_only?: boolean;
  [key: string]: unknown;
}
export interface Scene {
  layout: Layout;
  kit: Kit;
  instances: Instance[];
  stats: {
    area: number;
    rooms: number;
    meshes: number;
    colliders: number;
    [key: string]: number;
  };
  warnings: string[];
  removed_openings: string[];
  doors: { id: string; state: string; mode: string }[];
  navigation: {
    radius: number;
    stats: { triangles: number; islands: number };
    triangles: Vec3[][];
    links: unknown[];
  };
  workstations: (Workstation & {
    community: string;
    seat: string;
    computer_ref: string;
    read_fact: string;
    level: number;
  })[];
  [key: string]: unknown;
}
export interface LibraryAsset {
  id: string;
  name: string;
  path: string;
  role: string;
  status: string;
  appearances: string[];
  geometry?: { dimensions: Vec3 };
  bounds?: { dimensions: Vec3 };
  source_content_sha256: string;
  source_json_sha256: string;
  preview_sha256: string;
  preview_error?: string;
  error?: string;
  material_warning?: string;
}
export interface Project {
  scene: Scene;
  files: { id: string; name: string }[];
  kits: Kit[];
  assets_ready: boolean;
  library_summary: { families: number; prepared: number };
}
export interface Preview {
  cutaway: boolean;
  roof: boolean;
  collision: boolean;
  navigation: boolean;
  zones: boolean;
}
export interface EditorState {
  scene: Scene | null;
  layout: Layout | null;
  catalogs: Kit[];
  files: Project["files"];
  selected: string | null;
  selectedModule: string | null;
  door: string | null;
  wall: string | null;
  tool: Tool;
  level: number;
  route: number[];
  preview: Preview;
  view: "plan" | "split" | "three";
  tab: "build" | "objects" | "quest" | "project";
  pendingModule: LibraryAsset | null;
  pendingAppearance: string | null;
  message: string;
  error: boolean;
  busy: boolean;
  dirty: boolean;
  undo: Layout[];
  redo: Layout[];
  fitVersion: number;
  wallStart?: { x: number; y: number } | null;
  drag?: unknown;
}
