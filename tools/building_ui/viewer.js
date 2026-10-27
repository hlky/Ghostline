import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

export class BuildingViewer {
  constructor(element, onStatus) {
    this.element = element;
    this.onStatus = onStatus;
    this.scene = new THREE.Scene();
    this.scene.background = new THREE.Color('#161d22');
    this.camera = new THREE.PerspectiveCamera(37, 1, .1, 500);
    this.camera.position.set(23, 22, 23);
    this.renderer = new THREE.WebGLRenderer({ antialias: true });
    this.renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
    this.renderer.shadowMap.enabled = true;
    this.renderer.shadowMap.type = THREE.PCFShadowMap;
    this.renderer.outputColorSpace = THREE.SRGBColorSpace;
    element.appendChild(this.renderer.domElement);
    this.controls = new OrbitControls(this.camera, this.renderer.domElement);
    this.controls.target.set(6, 0, -3);
    this.controls.enableDamping = true;
    this.controls.maxPolarAngle = Math.PI * .49;
    this.controls.minDistance = 3;
    this.controls.maxDistance = 180;
    this.scene.add(new THREE.HemisphereLight('#d4e8ed', '#405050', 2.5));
    const sun = new THREE.DirectionalLight('#fff0dc', 3.0);
    sun.position.set(15, 28, 12);
    sun.castShadow = true;
    Object.assign(sun.shadow.camera, { left: -45, right: 45, top: 45, bottom: -45, far: 120 });
    sun.shadow.mapSize.set(2048, 2048);
    sun.shadow.bias = -.0005;
    sun.shadow.normalBias = .04;
    this.scene.add(sun);
    const ground = new THREE.Mesh(new THREE.PlaneGeometry(220, 220), new THREE.MeshStandardMaterial({ color: '#1b262b', roughness: 1 }));
    ground.rotation.x = -Math.PI / 2;
    ground.position.y = -.24;
    ground.receiveShadow = true;
    this.scene.add(ground);
    this.grid = new THREE.GridHelper(120, 40, '#40534f', '#29383c');
    this.grid.position.y = -.23;
    this.grid.material.transparent = true;
    this.grid.material.opacity = .55;
    this.scene.add(this.grid);
    this.building = new THREE.Group();
    this.scene.add(this.building);
    this.assets = {};
    this.assetSets = {};
    this.pending = new Map();
    this.moduleAssets = {};
    this.moduleErrors = new Set();
    this.moduleRefreshes = new Set();
    this.refreshFrame = null;
    this.loadingKit = null;
    this.loadedKit = null;
    this.materials = {};
    this.sceneData = null;
    this.options = { level: 0, roof: false, cutaway: true, collision: false, navigation: false, route: /** @type {number[]} */ ([]) };
    this.observer = new ResizeObserver(() => this.resize());
    this.observer.observe(element);
    this.resize();
    this.renderer.setAnimationLoop(() => {
      this.controls.update();
      this.renderer.render(this.scene, this.camera);
    });
  }

  async load(catalog = this.sceneData?.kit) {
    if(this.disposed)return;
    if (!catalog) return;
    const id = catalog.id;
    if (!this.assetSets[id]) {
      if (!this.pending.has(id)) {
        const loader = new GLTFLoader();
        this.pending.set(id, Promise.all(['floor','wall','doorway','ceiling'].map(async role=>[role,(await loader.loadAsync(`/assets/${id}/${role}.glb`)).scene])).then(entries=>{this.assetSets[id]=Object.fromEntries(entries);}));
      }
      try { await this.pending.get(id); }
      catch(error){this.onStatus('Geometry cache missing · run prepare-assets');console.error(error);return;}
    }
    if (this.disposed || this.sceneData?.kit.id !== id) return;
    this.assets = this.assetSets[id];this.loadedKit=id;
    this.onStatus(`${catalog.name} · neutral materials · schematic doors`);
    this.update(this.sceneData);
  }

  resize() {
    const width = this.element.clientWidth, height = this.element.clientHeight;
    if (!width || !height) return;
    this.renderer.setSize(width, height, false);
    this.camera.aspect = width / height;
    this.camera.updateProjectionMatrix();
  }

  async moduleAsset(id) {
    if (this.moduleAssets[id]) return this.moduleAssets[id];
    const key='module:'+id;
    if (!this.pending.has(key)) this.pending.set(key,new GLTFLoader().loadAsync(`/library-assets/${id}.glb`).then(gltf=>{
      this.moduleAssets[id]=gltf.scene;return gltf.scene;
    }));
    return this.pending.get(key);
  }

  scheduleUpdate() {
    if (this.disposed || this.refreshFrame !== null) return;
    this.refreshFrame = requestAnimationFrame(() => {
      this.refreshFrame = null;
      if (!this.disposed && this.sceneData) this.update(this.sceneData, this.options);
    });
  }

  requestModule(id) {
    if (this.disposed || this.moduleErrors.has(id) || this.moduleRefreshes.has(id)) return;
    this.moduleRefreshes.add(id);
    this.moduleAsset(id).then(() => {
      this.moduleRefreshes.delete(id);
      this.scheduleUpdate();
    }).catch(error => {
      this.moduleRefreshes.delete(id);
      this.moduleErrors.add(id);
      if (!this.disposed) this.onStatus('Module preview unavailable: ' + error.message);
    });
  }

  async preview(record) {
    const request=this.previewRequest=(this.previewRequest||0)+1;
    this.onStatus('Loading measured vanilla geometry…');
    try {
      const asset=await this.moduleAsset(record.id);
      if(this.disposed || this.previewRequest!==request)return;
      this.building.clear();
      const model=asset.clone(true);
      model.traverse(n=>{if(n.isMesh){n.material=this.material('wall');n.castShadow=true;n.receiveShadow=true;}});
      const bounds=new THREE.Box3().setFromObject(model),center=bounds.getCenter(new THREE.Vector3());
      model.position.set(-center.x,-bounds.min.y,-center.z);this.building.add(model);
      const size=bounds.getSize(new THREE.Vector3()),span=Math.max(size.x,size.y,size.z,1);
      this.camera.far=Math.max(500,span*10);this.camera.updateProjectionMatrix();
      this.controls.maxDistance=Math.max(180,span*8);this.controls.target.set(0,size.y/2,0);
      this.camera.position.copy(this.controls.target).add(new THREE.Vector3(span*1.2,span*.9,span*1.2));
      this.controls.update();this.resize();this.onStatus('Actual mesh · neutral material · original dimensions');
    } catch(error){this.onStatus(error.message);}
  }

  material(role, appearance, reference = false) {
    const key = `${role}:${appearance}:${reference}`;
    if (!this.materials[key]) {
      let color = role === 'floor' ? '#707b77' : '#a5b0a1';
      if (role === 'ceiling') color = '#a6afa1';
      if (appearance?.includes('black')) color = '#485257';
      if (appearance === 'bricks') color = '#988774';
      if (appearance === 'paper_old') color = '#a9a592';
      if (appearance === 'tiles_terracotta') color = '#9b7662';
      if (appearance === 'Wood') color = '#88755b';
      if (appearance === 'carpet') color = '#67766e';
      this.materials[key] = new THREE.MeshStandardMaterial({ color, roughness: .86, metalness: .05, side: THREE.DoubleSide,
        transparent: reference, opacity: reference ? .45 : 1, depthWrite: !reference });
    }
    return this.materials[key];
  }

  update(scene, options = this.options) {
    if(this.disposed)return;
    this.sceneData = scene;
    if (this.loadedKit !== scene.kit.id && this.loadingKit !== scene.kit.id) {
      const id = scene.kit.id;
      this.loadingKit = id;
      this.load(scene.kit).finally(() => { if (this.loadingKit === id) this.loadingKit = null; });
      this.assets=this.assetSets[id]||{};
    }
    this.options = { ...this.options, ...options };
    const { level, roof, cutaway, collision } = this.options;
    // Cached mesh geometry/materials are reused. Dispose only disposable overlays.
    for (const child of [...this.building.children]) {
      child.traverse(node => {
        if (node.userData.disposable) {
          node.geometry?.dispose();
          node.material?.dispose();
        }
      });
      this.building.remove(child);
    }
    const edges = new Map(scene.edges.map(edge => [edge.id, edge]));
    const hidden = edge => cutaway && edge && !edge.shared && ['south', 'east'].includes(edge.side);
    for (const instance of scene.instances) {
      if(instance.reference_only && ((instance.reference_role==='roof'&&!roof) ||
        (cutaway&&['south','east'].includes(instance.reference_side))))continue;
      if ((instance.level !== level && !(instance.kind === 'stair' && instance.level + 1 === level)) || (instance.role === 'ceiling' && (!instance.kind || instance.kind === 'shell') && !roof) || hidden(edges.get(instance.edge))) continue;
      const asset = ['module','device-preview'].includes(instance.kind)?this.moduleAssets[instance.asset]:this.assets[instance.role];
      if(!asset&&['module','device-preview'].includes(instance.kind)&&!this.moduleErrors.has(instance.asset)){
        this.requestModule(instance.asset);
      }
      if (!asset) continue;
      const model = asset.clone(true);
      model.traverse(node => {
        if (node.isMesh) {
          node.material = this.material(instance.role, instance.appearance, !!instance.reference_only);
          node.castShadow = !instance.reference_only;
          node.receiveShadow = true;
        }
      });
      model.position.set(instance.position[0], instance.position[2], -instance.position[1]);
      model.rotation.y = THREE.MathUtils.degToRad(instance.yaw);
      if(instance.local_orientation){const [x,y,z,w]=instance.local_orientation;model.quaternion.set(x,z,-y,w);}
      if (instance.scale) model.scale.set(instance.scale[0],instance.scale[2],instance.scale[1]);
      this.building.add(model);
    }
    if (collision) {
      for (const solid of scene.solids) {
        if ((solid.level !== level && !(solid.role === 'stair' && solid.level + 1 === level)) || (solid.role === 'ceiling' && !roof) || hidden(edges.get(solid.edge))) continue;
        const geometry = new THREE.BoxGeometry(solid.size[0], solid.size[2], solid.size[1]);
        const mesh = new THREE.Mesh(geometry, new THREE.MeshBasicMaterial({ color: '#73d8cf', transparent: true, opacity: .12, depthWrite: false }));
        mesh.position.set(solid.center[0], solid.center[2], -solid.center[1]);
        mesh.rotation.y = THREE.MathUtils.degToRad(solid.yaw);
        mesh.userData.disposable = true;
        this.building.add(mesh);
        const lines = new THREE.LineSegments(new THREE.EdgesGeometry(geometry), new THREE.LineBasicMaterial({ color: '#73d8cf', transparent: true, opacity: .75 }));
        lines.position.copy(mesh.position);
        lines.rotation.copy(mesh.rotation);
        lines.userData.disposable = true;
        this.building.add(lines);
      }
    }
    for (const door of scene.doors || []) {
      if (door.level !== level) continue;
      const material = new THREE.MeshStandardMaterial({color:door.state==='LOCKED'?'#c77770':'#69aeb4',roughness:.6,transparent:true,opacity:.7});
      if (door.appearance.startsWith('doors_double_')) {
        const yaw=THREE.MathUtils.degToRad(door.yaw);
        for (const side of [-1,1]) {
          const offset=side*(door.state==='OPENED'?2.2:.73);
          const leaf=new THREE.Mesh(new THREE.BoxGeometry(1.46,2.38,.08),material);
          leaf.position.set(door.position[0]+offset*Math.cos(yaw),door.position[2]+1.2,-door.position[1]-offset*Math.sin(yaw));
          leaf.rotation.y=yaw;leaf.userData.disposable=true;this.building.add(leaf);
        }
        continue;
      }
      const leaf = new THREE.Mesh(new THREE.BoxGeometry(1.46,2.38,.08),material);
      const yaw=THREE.MathUtils.degToRad(door.yaw);
      const hinged=door.appearance.startsWith('doors_single_hinged_'),open=door.state==='OPENED';
      const angle=yaw+(hinged&&open?Math.PI/2:0),offset=hinged?-.69:(open?.75:-.75);
      leaf.position.set(door.position[0]+offset*Math.cos(angle),door.position[2]+1.2,-door.position[1]-offset*Math.sin(angle));
      leaf.rotation.y=angle;leaf.userData.disposable=true;
      this.building.add(leaf);
    }
    if (this.options.navigation) {
      const base=level*scene.kit.storey_height,selected=new Set(this.options.route||[]);
      for (const [index,triangle] of scene.navigation.triangles.entries()) {
        if (!triangle.some(point=>Math.abs(point[2]-base)<.05))continue;
        const positions=triangle.flatMap(p=>[p[0],p[2]+.035,-p[1]]);
        const geometry=new THREE.BufferGeometry();geometry.setAttribute('position',new THREE.Float32BufferAttribute(positions,3));geometry.computeVertexNormals();
        const mesh=new THREE.Mesh(geometry,new THREE.MeshBasicMaterial({color:selected.has(index)?'#f0d07a':'#55cdbb',side:THREE.DoubleSide,transparent:true,opacity:selected.has(index)?.7:.3,depthWrite:false}));
        mesh.userData.disposable=true;this.building.add(mesh);
        const wire=new THREE.LineSegments(new THREE.EdgesGeometry(geometry),new THREE.LineBasicMaterial({color:'#6ad8c5',transparent:true,opacity:.6}));wire.userData.disposable=true;this.building.add(wire);
      }
    }
    const base = level * scene.kit.storey_height;
    this.grid.position.y = base - .23;
    this.resize();
  }

  dispose() {
    this.disposed=true;
    if (this.refreshFrame !== null) cancelAnimationFrame(this.refreshFrame);
    this.previewRequest=(this.previewRequest||0)+1;
    this.observer.disconnect();
    this.renderer.setAnimationLoop(null);
    this.controls.dispose();
    const geometries=new Set(),materials=new Set();
    for (const material of Object.values(this.materials)) materials.add(material);
    const collect=root=>root?.traverse(node=>{
      if(node.geometry)geometries.add(node.geometry);
      for(const material of (Array.isArray(node.material)?node.material:[node.material]))if(material)materials.add(material);
    });
    collect(this.scene);
    for(const group of Object.values(this.assetSets))for(const asset of Object.values(group))collect(asset);
    for(const asset of Object.values(this.moduleAssets))collect(asset);
    for(const geometry of geometries)geometry.dispose();
    for(const material of materials)material.dispose();
    this.renderer.dispose();
    this.renderer.domElement.remove();
  }

  fit() {
    const rooms = this.sceneData?.layout.rooms.filter(room => room.level === this.options.level) || [];
    const modules=this.sceneData?.instances.filter(i=>i.kind==='module'&&i.level===this.options.level)||[];
    if (!rooms.length||modules.length) {
      const bounds=new THREE.Box3();
      for(const room of rooms){
        bounds.expandByPoint(new THREE.Vector3(room.x,this.options.level*this.sceneData.kit.storey_height,-room.y));
        bounds.expandByPoint(new THREE.Vector3(room.x+room.width,this.options.level*this.sceneData.kit.storey_height+this.sceneData.kit.wall_height,-room.y-room.depth));
      }
      for(const item of modules){
        const a=item.yaw*Math.PI/180;
        for(const x of [item.bounds.min[0],item.bounds.max[0]])for(const y of [item.bounds.min[1],item.bounds.max[1]])for(const z of [item.bounds.min[2],item.bounds.max[2]]){
          bounds.expandByPoint(new THREE.Vector3(item.position[0]+x*Math.cos(a)-y*Math.sin(a),item.position[2]+z,-(item.position[1]+x*Math.sin(a)+y*Math.cos(a))));
        }
      }
      if(bounds.isEmpty())return;
      const center=bounds.getCenter(new THREE.Vector3()),size=Math.max(...bounds.getSize(new THREE.Vector3()).toArray(),3);
      this.camera.far=Math.max(500,size*10);this.camera.updateProjectionMatrix();this.controls.maxDistance=Math.max(180,size*8);
      const vertical=THREE.MathUtils.degToRad(this.camera.fov),horizontal=2*Math.atan(Math.tan(vertical/2)*this.camera.aspect);
      const distance=bounds.getBoundingSphere(new THREE.Sphere()).radius/Math.sin(Math.min(vertical,horizontal)/2)*1.15;
      this.controls.target.copy(center);this.camera.position.copy(center).add(new THREE.Vector3(1,1,1).normalize().multiplyScalar(distance));this.controls.update();return;
    }
    const xmin = Math.min(...rooms.map(r => r.x)), xmax = Math.max(...rooms.map(r => r.x + r.width));
    const ymin = Math.min(...rooms.map(r => r.y)), ymax = Math.max(...rooms.map(r => r.y + r.depth));
    const center = new THREE.Vector3((xmin + xmax) / 2, this.options.level * this.sceneData.kit.storey_height + 1.1, -(ymin + ymax) / 2);
    const size = Math.max(xmax - xmin, ymax - ymin, 9);
    this.controls.target.copy(center);
    this.camera.position.copy(center).add(new THREE.Vector3(size * 1.05, size * 1.1, size * 1.25));
    this.controls.update();
  }
}
