import * as THREE from "three";
import { GLTFLoader } from "three/addons/loaders/GLTFLoader.js";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";

const SHAPE_NAMES = ["eyes", "nose", "mouth", "jaw", "ears"];
const MAX_PREVIEW_MODELS = 24;

export class CharacterViewer {
  constructor(container, statusElement) {
    this.container = container;
    this.statusElement = statusElement;
    this.loader = new GLTFLoader();
    this.textureLoader = new THREE.TextureLoader();
    this.models = new THREE.Group();
    this.morphMeshes = [];
    this.shapes = {};
    this.mapping = {};
    this.wireframe = false;
    this.hairVisible = true;
    this.loadToken = 0;

    this.scene = new THREE.Scene();
    this.scene.background = new THREE.Color(0x050b0d);
    this.scene.add(this.models);

    this.camera = new THREE.PerspectiveCamera(34, 1, 0.001, 100);
    this.camera.position.set(0, 0, 1);

    this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false });
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    this.renderer.outputColorSpace = THREE.SRGBColorSpace;
    this.renderer.toneMapping = THREE.ACESFilmicToneMapping;
    this.renderer.toneMappingExposure = 1;
    this.container.append(this.renderer.domElement);

    this.controls = new OrbitControls(this.camera, this.renderer.domElement);
    this.controls.enableDamping = true;
    this.controls.dampingFactor = 0.075;
    this.controls.minDistance = 0.08;
    this.controls.maxDistance = 8;

    const environment = new RoomEnvironment();
    const pmrem = new THREE.PMREMGenerator(this.renderer);
    this.environmentTarget = pmrem.fromScene(environment);
    this.scene.environment = this.environmentTarget.texture;
    this.scene.environmentIntensity = 0.35;
    environment.dispose();
    pmrem.dispose();
    this.fill = new THREE.HemisphereLight(0xffffff, 0x34303a, 0.6);
    this.key = new THREE.DirectionalLight(0xfff1e5, 2.5);
    this.key.position.set(2, 3, -4);
    this.rim = new THREE.DirectionalLight(0xdce8ff, 1);
    this.rim.position.set(-3, 1, 2);
    this.scene.add(this.fill, this.key, this.rim);

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
      for (const material of Array.isArray(node.material) ? node.material : [node.material]) {
        if (!material) continue;
        for (const value of Object.values(material)) if (value?.isTexture) value.dispose();
        material.dispose();
      }
    });
  }

  clearModels() {
    for (const child of [...this.models.children]) {
      this.disposeModel(child);
      this.models.remove(child);
    }
    this.morphMeshes = [];
  }

  setLighting(mode) {
    const night = mode === "night";
    this.key.color.set(night ? 0xffc9ac : 0xfff1e5);
    this.rim.color.set(night ? 0x22d9e0 : 0xdce8ff);
    this.rim.intensity = night ? 2.5 : 1;
    this.fill.intensity = night ? 0.3 : 0.6;
  }

  async materialFor(entry, model, baseUrl) {
    const data = entry?.Data || {};
    const shader = entry?.MaterialTemplate || "";
    const skin = shader.includes("skin");
    const decal = shader.includes("mesh_decal");
    const hair = shader.includes("hair.mt");
    const eye = shader.includes("eye_gradient");
    const material = new THREE.MeshPhysicalMaterial({
      color: hair ? "#17131a" : entry ? "#ffffff" : model.color || "#d6a08a",
      roughness: skin ? 0.65 : 0.5,
      metalness: 0,
      side: THREE.DoubleSide,
      wireframe: this.wireframe,
      clearcoat: eye ? 1 : skin ? 0.08 : 0,
      clearcoatRoughness: 0.45,
      envMapIntensity: 0.5,
    });
    if (shader.includes("eye_shadow")) {
      // RED's screen-space wetness shader is represented by the iris clearcoat.
      material.transparent = true;
      material.opacity = 0;
      material.depthWrite = false;
      return material;
    }
    if (decal) {
      material.transparent = true;
      material.depthWrite = false;
      material.polygonOffset = true;
      material.polygonOffsetFactor = -1;
      material.polygonOffsetUnits = -1;
    }
    const mapFields = {
      map: data.Albedo || data.DiffuseTexture || data.BaseColor || data.BaseColorTexture,
      normalMap: data.Normal || data.NormalTexture,
      roughnessMap: data.Roughness || data.RoughnessTexture,
      alphaMap: data.Strand_Alpha || data.Alpha || data.AlphaTexture || data.Opacity || data.MaskTexture,
    };
    try {
      for (const [field, path] of Object.entries(mapFields)) {
        if (typeof path !== "string" || !path.endsWith(".png")) continue;
        const texture = await this.textureLoader.loadAsync(new URL(path, baseUrl).href);
        if (field === "normalMap" || field === "roughnessMap") {
          // RED normal maps store XY (BC5); roughness is in R rather than glTF's G.
          const canvas = document.createElement("canvas");
          canvas.width = texture.image.width;
          canvas.height = texture.image.height;
          const context = canvas.getContext("2d");
          context.drawImage(texture.image, 0, 0);
          const pixels = context.getImageData(0, 0, canvas.width, canvas.height);
          for (let i = 0; i < pixels.data.length; i += 4) {
            if (field === "roughnessMap") {
              pixels.data[i + 1] = pixels.data[i];
            } else {
              const x = pixels.data[i] / 127.5 - 1;
              const y = pixels.data[i + 1] / 127.5 - 1;
              pixels.data[i + 2] = Math.round((Math.sqrt(Math.max(0, 1 - x*x - y*y)) + 1) * 127.5);
            }
          }
          context.putImageData(pixels, 0, 0);
          texture.image = canvas;
          texture.needsUpdate = true;
        }
        texture.flipY = false;
        texture.wrapS = THREE.RepeatWrapping;
        texture.wrapT = THREE.RepeatWrapping;
        texture.colorSpace = field === "map" ? THREE.SRGBColorSpace : THREE.NoColorSpace;
        texture.anisotropy = Math.min(this.renderer.capabilities.getMaxAnisotropy(), 8);
        material[field] = texture;
      }
      if (material.normalMap) material.normalScale.set(decal ? 0.2 : 0.65, decal ? -0.2 : -0.65);
      if (material.alphaMap || entry?.EnableMask || hair) {
        material.alphaTest = 0.25;
      }
      const tint = data.DiffuseColor || data.AlbedoColor;
      if (tint?.Red != null) material.color.setRGB(tint.Red / 255, tint.Green / 255, tint.Blue / 255, THREE.SRGBColorSpace);
      return material;
    } catch (error) {
      for (const value of Object.values(material)) if (value?.isTexture) value.dispose();
      material.dispose();
      throw error;
    }
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
        // Track the scene before texture loads so a failed load disposes it too.
        loaded.push({ scene: gltf.scene, morphMeshes });
        const nodes = [];
        gltf.scene.traverse((node) => {
          if (node.isMesh) nodes.push(node);
        });
        for (const node of nodes) {
          const index = Number(node.name.match(/submesh_(\d+)/)?.[1] || 0);
          if (model.chunk_mask && !(BigInt(model.chunk_mask) & (1n << BigInt(index)))) node.visible = false;
          const prior = node.material;
          node.material = await this.materialFor(model.materials?.[index], model, new URL(manifestUrl, window.location.href));
          if (Array.isArray(prior)) prior.forEach((material) => material.dispose());
          else prior?.dispose();
          if (node.morphTargetDictionary && node.morphTargetInfluences) morphMeshes.push(node);
        }
      }
    } catch (error) {
      loaded.forEach((entry) => this.disposeModel(entry.scene));
      throw error;
    }
    if (token !== this.loadToken) {
      loaded.forEach((entry) => this.disposeModel(entry.scene));
      return;
    }
    this.clearModels();
    loaded.forEach((model) => {
      this.models.add(model.scene);
      this.morphMeshes.push(...model.morphMeshes);
    });
    this.setHairVisible(this.hairVisible);
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
    this.setStatus(`${loaded.length} layers · ${targetCount} morph targets${manifest.material_quality ? " · Game textures / PBR preview" : " · Neutral geometry"}`);
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
    const head = this.models.children.find((model) => model.userData.previewModel?.component === "h0_head");
    const box = new THREE.Box3().setFromObject(head || this.models);
    if (box.isEmpty()) {
      this.camera.position.set(0, 0, 1);
      this.controls.target.set(0, 0, 0);
      return;
    }
    const center = box.getCenter(new THREE.Vector3());
    const size = box.getSize(new THREE.Vector3());
    const halfFov = Math.tan(THREE.MathUtils.degToRad(this.camera.fov / 2));
    const distance = Math.max(size.y / 2 / halfFov, size.x / 2 / halfFov / this.camera.aspect, size.z) * 1.15;
    this.controls.target.copy(center);
    this.camera.position.set(center.x, center.y, center.z - distance);
    this.camera.near = Math.max(distance / 1000, 0.0001);
    this.camera.far = Math.max(distance * 20, 10);
    this.camera.updateProjectionMatrix();
    this.controls.update();
  }

  setViewAngle(angle) {
    const distance = this.camera.position.distanceTo(this.controls.target);
    this.camera.position.copy(this.controls.target).add(new THREE.Vector3(
      Math.sin(angle) * distance, 0, -Math.cos(angle) * distance,
    ));
    this.controls.update();
  }

  setHairVisible(visible) {
    this.hairVisible = visible;
    for (const model of this.models.children) {
      if (model.userData.previewModel?.role === "hair") model.visible = visible;
    }
  }
}
