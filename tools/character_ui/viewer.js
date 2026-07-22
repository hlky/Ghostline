import * as THREE from "three";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";

const SHAPE_NAMES = ["eyes", "nose", "mouth", "jaw", "ears"];
const MAX_PREVIEW_MODELS = 16;

export class CharacterViewer {
  constructor(container, statusElement) {
    this.container = container;
    this.statusElement = statusElement;
    this.loader = new GLTFLoader();
    this.models = new THREE.Group();
    this.morphMeshes = [];
    this.shapes = {};
    this.mapping = {};
    this.wireframe = false;
    this.loadToken = 0;

    this.scene = new THREE.Scene();
    this.scene.background = new THREE.Color(0x050b0d);
    this.scene.fog = new THREE.Fog(0x050b0d, 2.5, 7);
    this.scene.add(this.models);

    this.camera = new THREE.PerspectiveCamera(34, 1, 0.001, 100);
    this.camera.position.set(0, 0, 1);

    this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false });
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    this.renderer.outputColorSpace = THREE.SRGBColorSpace;
    this.renderer.toneMapping = THREE.ACESFilmicToneMapping;
    this.renderer.toneMappingExposure = 1.15;
    this.container.append(this.renderer.domElement);

    this.controls = new OrbitControls(this.camera, this.renderer.domElement);
    this.controls.enableDamping = true;
    this.controls.dampingFactor = 0.075;
    this.controls.minDistance = 0.08;
    this.controls.maxDistance = 8;

    this.scene.add(new THREE.HemisphereLight(0xbcecff, 0x23151b, 2.2));
    const key = new THREE.DirectionalLight(0xffe4d2, 4.5);
    key.position.set(2, 3, -4);
    this.scene.add(key);
    const rim = new THREE.DirectionalLight(0x22e9df, 3.2);
    rim.position.set(-3, 1, 2);
    this.scene.add(rim);

    this.resizeObserver = new ResizeObserver(() => this.resize());
    this.resizeObserver.observe(this.container);
    this.resize();
    this.renderer.setAnimationLoop(() => {
      this.controls.update();
      this.renderer.render(this.scene, this.camera);
    });
  }

  setStatus(message, isError = false) {
    this.statusElement.textContent = message;
    this.statusElement.classList.toggle("error", isError);
  }

  resize() {
    const width = Math.max(this.container.clientWidth, 1);
    const height = Math.max(this.container.clientHeight, 1);
    this.camera.aspect = width / height;
    this.camera.updateProjectionMatrix();
    this.renderer.setSize(width, height, false);
  }

  disposeModel(model) {
    model.traverse((node) => {
      if (!node.isMesh) return;
      node.geometry?.dispose();
      if (Array.isArray(node.material)) node.material.forEach((material) => material.dispose());
      else node.material?.dispose();
    });
  }

  clearModels() {
    for (const child of [...this.models.children]) {
      this.disposeModel(child);
      this.models.remove(child);
    }
    this.morphMeshes = [];
  }

  async load(manifestUrl) {
    const token = ++this.loadToken;
    this.setStatus("Loading preview…");
    const response = await fetch(manifestUrl, { cache: "no-store" });
    if (!response.ok) throw new Error(`Preview manifest failed: ${response.status}`);
    const manifest = await response.json();
    if (!Array.isArray(manifest.models) || !manifest.models.length) {
      throw new Error("Preview manifest contains no models");
    }
    if (manifest.models.length > MAX_PREVIEW_MODELS) {
      throw new Error(`Preview is capped at ${MAX_PREVIEW_MODELS} models`);
    }
    const loaded = [];
    try {
      for (const [modelIndex, model] of manifest.models.entries()) {
        this.setStatus(`Loading model ${modelIndex + 1}/${manifest.models.length}…`);
        const url = new URL(model.file, new URL(manifestUrl, window.location.href));
        const gltf = await this.loader.loadAsync(url.href);
        if (token !== this.loadToken) {
          this.disposeModel(gltf.scene);
          loaded.forEach((entry) => this.disposeModel(entry.scene));
          return null;
        }
        const morphMeshes = [];
        gltf.scene.userData.previewModel = model;
        gltf.scene.traverse((node) => {
          if (!node.isMesh) return;
          const prior = node.material;
          node.material = new THREE.MeshStandardMaterial({
            color: model.color || "#d6a08a",
            roughness: 0.72,
            metalness: 0.02,
            side: THREE.DoubleSide,
            wireframe: this.wireframe,
          });
          if (Array.isArray(prior)) prior.forEach((material) => material.dispose());
          else prior?.dispose();
          if (node.morphTargetDictionary && node.morphTargetInfluences) morphMeshes.push(node);
        });
        loaded.push({ scene: gltf.scene, morphMeshes });
      }
    } catch (error) {
      loaded.forEach((entry) => this.disposeModel(entry.scene));
      throw error;
    }
    if (token !== this.loadToken) return;
    this.clearModels();
    loaded.forEach((model) => {
      this.models.add(model.scene);
      this.morphMeshes.push(...model.morphMeshes);
    });
    this.mapping = manifest.morph_mapping || {};
    for (const name of SHAPE_NAMES) {
      if (this.shapes[name] == null) this.shapes[name] = this.mapping[name]?.creator_value ?? null;
    }
    this.applyShapes();
    this.resetView();
    const targetCount = this.morphMeshes.reduce(
      (count, mesh) => count + Object.keys(mesh.morphTargetDictionary || {}).length,
      0,
    );
    this.setStatus(`${loaded.length} model${loaded.length === 1 ? "" : "s"} · ${targetCount} morph targets`);
    return manifest;
  }

  setShapes(shapes) {
    this.shapes = { ...shapes };
    this.applyShapes();
  }

  applyShapes() {
    for (const mesh of this.morphMeshes) {
      mesh.morphTargetInfluences.fill(0);
      for (const name of SHAPE_NAMES) {
        const value = this.shapes[name];
        if (value == null || value === "") continue;
        const target = this.mapping[name]?.targets?.[String(value)];
        const index = target == null ? undefined : mesh.morphTargetDictionary[target];
        if (index !== undefined) mesh.morphTargetInfluences[index] = 1;
      }
    }
  }

  setWireframe(enabled) {
    this.wireframe = enabled;
    this.models.traverse((node) => {
      if (!node.isMesh) return;
      const materials = Array.isArray(node.material) ? node.material : [node.material];
      materials.forEach((material) => {
        material.wireframe = enabled;
        material.needsUpdate = true;
      });
    });
  }

  resetView() {
    const box = new THREE.Box3().setFromObject(this.models);
    if (box.isEmpty()) {
      this.camera.position.set(0, 0, 1);
      this.controls.target.set(0, 0, 0);
      return;
    }
    const center = box.getCenter(new THREE.Vector3());
    const size = box.getSize(new THREE.Vector3());
    const maxDimension = Math.max(size.x, size.y, size.z, 0.01);
    const distance = (maxDimension / (2 * Math.tan(THREE.MathUtils.degToRad(this.camera.fov / 2)))) * 1.25;
    this.controls.target.copy(center);
    this.camera.position.set(center.x, center.y, center.z - distance);
    this.camera.near = Math.max(distance / 1000, 0.0001);
    this.camera.far = Math.max(distance * 20, 10);
    this.camera.updateProjectionMatrix();
    this.controls.update();
  }
}
