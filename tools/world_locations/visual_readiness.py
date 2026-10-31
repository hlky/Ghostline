"""Temporal scene settling and learned, engine-labelled loading-screen signatures."""
from __future__ import annotations

import base64
import json
from pathlib import Path
from typing import Any

import numpy as np
from PIL import Image


class FrameReadiness:
    def __init__(self, *, threshold: float = 0.04, template_path: Path | None = None):
        self.threshold = threshold
        self.template_path = template_path
        self.templates: list[np.ndarray] = []
        self.previous: np.ndarray | None = None
        self.changed = False
        if template_path and template_path.is_file():
            try:
                raw = json.loads(template_path.read_text())
                if raw.get("schema_version") == 1:
                    self.templates = [np.frombuffer(base64.b64decode(t, validate=True), dtype=np.uint8).reshape(36,64).copy() for t in raw.get("templates", [])[:24]]
            except (OSError, ValueError, KeyError):
                self.templates = []

    @staticmethod
    def signature(bgr: Any) -> np.ndarray:
        # Spatial structure, not an all-one-colour test. No source pixels are changed.
        return np.asarray(Image.fromarray(bgr.mean(axis=2).astype(np.uint8)).resize((64,36)), dtype=np.uint8)

    def observe(self, bgr: Any, *, loading_confirmed: bool = False) -> tuple[bool, str | None]:
        current = self.signature(bgr)
        if loading_confirmed:
            # Do not learn blank fades: a legitimate dark room can look identical.
            if current.std() >= 12 and not any(np.abs(current.astype(float)-t).mean()/255 < 0.02 for t in self.templates):
                self.templates = [*self.templates[-23:], current.copy()]
                self.changed = True
            self.previous = None
            return False, "engine_loading"
        if any(np.abs(current.astype(float)-t).mean()/255 < 0.02 for t in self.templates):
            self.previous = None
            return False, "known_loading_screen"
        previous, self.previous = self.previous, current
        if previous is None:
            return False, "first_frame"
        delta = np.abs(current.astype(float)-previous)/255
        tiles = delta.reshape(6,6,8,8).mean(axis=(1,3))
        # Median tile change tolerates people/traffic crossing part of a scene.
        if float(np.median(tiles)) > self.threshold:
            return False, "scene_changing"
        return True, None

    def save(self) -> None:
        if not self.changed or self.template_path is None:
            return
        from .protocol import atomic_write_json
        atomic_write_json(self.template_path, {"schema_version": 1, "templates": [base64.b64encode(t.tobytes()).decode("ascii") for t in self.templates]})
