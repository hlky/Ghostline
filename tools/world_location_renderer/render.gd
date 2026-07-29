extends Node3D

var scene_path := ""
var report_path := ""
var camera: Camera3D


func argument_value(name: String) -> String:
	var arguments := OS.get_cmdline_user_args()
	for index in range(arguments.size() - 1):
		if arguments[index] == name:
			return arguments[index + 1]
	return ""


func fail(message: String) -> void:
	printerr("GHOSTLINE_DIRECT_ERROR " + message)
	get_tree().quit(2)


func read_document(path: String) -> Variant:
	if not FileAccess.file_exists(path):
		return null
	return JSON.parse_string(FileAccess.get_file_as_string(path))


func matrix_transform(values: Array) -> Transform3D:
	if values.size() != 16:
		return Transform3D.IDENTITY
	var basis := Basis(
		Vector3(float(values[0]), float(values[4]), float(values[8])),
		Vector3(float(values[1]), float(values[5]), float(values[9])),
		Vector3(float(values[2]), float(values[6]), float(values[10]))
	)
	return Transform3D(
		basis,
		Vector3(float(values[3]), float(values[7]), float(values[11]))
	)


func collect_meshes(node: Node, parent_transform: Transform3D, result: Array) -> void:
	var current := parent_transform
	if node is Node3D:
		current = parent_transform * (node as Node3D).transform
	if node is MeshInstance3D:
		var source := node as MeshInstance3D
		if source.mesh != null:
			var overrides: Array[Material] = []
			for surface in range(source.mesh.get_surface_count()):
				overrides.append(source.get_surface_override_material(surface))
			result.append({
				"mesh": source.mesh,
				"transform": current,
				"material_override": source.material_override,
				"surface_overrides": overrides,
			})
	for child in node.get_children():
		collect_meshes(child, current, result)


func instantiate_batch(batch: Dictionary, batch_index: int) -> int:
	var asset_path := str(batch.get("asset", ""))
	var transforms: Array = batch.get("transforms", [])
	if asset_path.is_empty() or transforms.is_empty():
		return 0
	var document := GLTFDocument.new()
	var state := GLTFState.new()
	var error := document.append_from_file(asset_path, state)
	if error != OK:
		printerr("GHOSTLINE_DIRECT_ASSET_ERROR %s error=%d" % [asset_path, error])
		return 0
	var generated := document.generate_scene(state)
	if generated == null:
		printerr("GHOSTLINE_DIRECT_ASSET_ERROR %s generate_scene_failed" % asset_path)
		return 0
	var mesh_parts: Array = []
	collect_meshes(generated, Transform3D.IDENTITY, mesh_parts)
	for part_index in range(mesh_parts.size()):
		var part: Dictionary = mesh_parts[part_index]
		var multimesh := MultiMesh.new()
		multimesh.transform_format = MultiMesh.TRANSFORM_3D
		multimesh.mesh = part["mesh"]
		multimesh.instance_count = transforms.size()
		for instance_index in range(transforms.size()):
			multimesh.set_instance_transform(
				instance_index,
				matrix_transform(transforms[instance_index]) * part["transform"]
			)
		var instance := MultiMeshInstance3D.new()
		instance.name = "Batch_%d_Part_%d" % [batch_index, part_index]
		instance.multimesh = multimesh
		instance.material_override = part["material_override"]
		var overrides: Array = part["surface_overrides"]
		for surface in range(overrides.size()):
			if overrides[surface] != null:
				instance.set_surface_override_material(surface, overrides[surface])
		add_child(instance)
	generated.free()
	return mesh_parts.size()


func configure_world() -> void:
	var world_environment := WorldEnvironment.new()
	var environment := Environment.new()
	var sky_material := ProceduralSkyMaterial.new()
	sky_material.sky_top_color = Color(0.055, 0.105, 0.18, 1.0)
	sky_material.sky_horizon_color = Color(0.48, 0.62, 0.76, 1.0)
	sky_material.ground_horizon_color = Color(0.34, 0.31, 0.27, 1.0)
	sky_material.ground_bottom_color = Color(0.075, 0.065, 0.055, 1.0)
	sky_material.sun_angle_max = 18.0
	var sky := Sky.new()
	sky.sky_material = sky_material
	environment.background_mode = Environment.BG_SKY
	environment.sky = sky
	environment.ambient_light_source = Environment.AMBIENT_SOURCE_SKY
	environment.reflected_light_source = Environment.REFLECTION_SOURCE_SKY
	environment.ambient_light_energy = 0.8
	environment.tonemap_mode = Environment.TONE_MAPPER_FILMIC
	environment.tonemap_exposure = 1.05
	environment.ssao_enabled = true
	environment.ssao_radius = 2.0
	environment.ssao_intensity = 1.2
	world_environment.environment = environment
	add_child(world_environment)

	var key_light := DirectionalLight3D.new()
	key_light.rotation_degrees = Vector3(-52.0, -34.0, 0.0)
	key_light.light_color = Color(1.0, 0.94, 0.84, 1.0)
	key_light.light_energy = 1.15
	key_light.shadow_enabled = true
	add_child(key_light)

	camera = Camera3D.new()
	camera.keep_aspect = Camera3D.KEEP_WIDTH
	camera.near = 0.08
	camera.far = 1500.0
	camera.current = true
	add_child(camera)


func write_report(report: Dictionary) -> bool:
	var directory := report_path.get_base_dir()
	if DirAccess.make_dir_recursive_absolute(directory) != OK:
		return false
	var file := FileAccess.open(report_path, FileAccess.WRITE)
	if file == null:
		return false
	file.store_string(JSON.stringify(report, "  ") + "\n")
	file.close()
	return true


func render_views(scene: Dictionary) -> Dictionary:
	var output_root := str(scene.get("output", ""))
	var quality: float = clampf(float(scene.get("image_quality", 90)) / 100.0, 0.0, 1.0)
	var viewpoints: Array = scene.get("viewpoints", [])
	var records: Array = []
	var succeeded := 0
	for index in range(viewpoints.size()):
		var viewpoint: Dictionary = viewpoints[index]
		var coordinates: Array = viewpoint.get("position", [0.0, 0.0, 0.0])
		var direction: Array = viewpoint.get("forward", [1.0, 0.0, 0.0])
		camera.position = Vector3(float(coordinates[0]), float(coordinates[1]), float(coordinates[2]))
		var forward := Vector3(float(direction[0]), float(direction[1]), float(direction[2])).normalized()
		camera.look_at(camera.position + forward, Vector3.UP)
		camera.fov = float(viewpoint.get("horizontal_fov_degrees", 80.0))
		await get_tree().process_frame
		await get_tree().process_frame
		var image := get_viewport().get_texture().get_image()
		var destination := output_root.path_join("views").path_join(str(viewpoint.get("folder", "viewpoint"))).path_join(str(viewpoint.get("direction", "view")) + ".webp")
		DirAccess.make_dir_recursive_absolute(destination.get_base_dir())
		var error := image.save_webp(destination, quality)
		var ok := error == OK
		if ok:
			succeeded += 1
		records.append({
			"viewpoint_id": str(viewpoint.get("id", "")),
			"direction": str(viewpoint.get("direction", "")),
			"yaw_degrees": float(viewpoint.get("yaw_degrees", 0.0)),
			"output": destination,
			"image": {"path": destination},
			"valid": ok,
			"error": error,
			"metadata": viewpoint.get("metadata", {}),
		})
		print("GHOSTLINE_DIRECT_RENDER [%d/%d] %s" % [index + 1, viewpoints.size(), destination])
	return {
		"views": records,
		"total_views": viewpoints.size(),
		"rendered_views": succeeded,
		"failed_views": viewpoints.size() - succeeded,
	}


func _ready() -> void:
	scene_path = argument_value("--scene")
	report_path = argument_value("--report")
	if scene_path.is_empty() or report_path.is_empty():
		fail("--scene and --report are required")
		return
	var parsed: Variant = read_document(scene_path)
	if not parsed is Dictionary:
		fail("could not read scene manifest " + scene_path)
		return
	var scene: Dictionary = parsed
	var resolution := int(scene.get("resolution", 768))
	get_viewport().size = Vector2i(resolution, resolution)
	configure_world()
	var batches: Array = scene.get("batches", [])
	var mesh_parts := 0
	for index in range(batches.size()):
		var batch: Dictionary = batches[index]
		mesh_parts += instantiate_batch(batch, index)
		if index == 0 or (index + 1) % 25 == 0 or index + 1 == batches.size():
			print("GHOSTLINE_DIRECT_ASSEMBLY [%d/%d] mesh_parts=%d" % [index + 1, batches.size(), mesh_parts])
	await get_tree().process_frame
	await get_tree().process_frame
	var render_result := await render_views(scene)
	var report := {
		"schema_version": 1,
		"tile_id": str(scene.get("tile_id", "")),
		"run_id": str(scene.get("run_id", "")),
		"content_fingerprint": str(scene.get("content_fingerprint", "")),
		"scene": scene_path,
		"renderer": {
			"name": "godot-direct-gltf",
			"renderer_fingerprint": str(scene.get("renderer_fingerprint", "")),
			"resolution": int(scene.get("resolution", 0)),
		},
		"loaded_batches": batches.size(),
		"mesh_parts": mesh_parts,
		"views": render_result["views"],
		"total_views": render_result["total_views"],
		"rendered_views": render_result["rendered_views"],
		"failed_views": render_result["failed_views"],
		"missing_assets": scene.get("missing_assets", []),
	}
	if not write_report(report):
		fail("could not write report " + report_path)
		return
	print("GHOSTLINE_DIRECT_DONE rendered=%d failed=%d" % [report["rendered_views"], report["failed_views"]])
	get_tree().quit(0 if report["failed_views"] == 0 else 2)
