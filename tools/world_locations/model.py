"""Small, dependency-free geometry and identity primitives."""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import math
from typing import Any, Iterable, Mapping


def unwrap(value: Any) -> Any:
    """Unwrap WolvenKit scalar wrappers without touching ordinary objects."""
    while isinstance(value, Mapping) and "$value" in value:
        value = value["$value"]
    return value


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def stable_id(prefix: str, *parts: Any) -> str:
    payload = canonical_json(parts).encode("utf-8")
    return f"{prefix}_{hashlib.sha256(payload).hexdigest()[:32]}"


def _number(value: Any, default: float = 0.0) -> float:
    try:
        return float(unwrap(value))
    except (TypeError, ValueError):
        return default


@dataclass(frozen=True, slots=True)
class Vec3:
    x: float
    y: float
    z: float

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any] | None) -> "Vec3":
        value = value or {}
        return cls(
            _number(value.get("X", value.get("x"))),
            _number(value.get("Y", value.get("y"))),
            _number(value.get("Z", value.get("z"))),
        )

    def __add__(self, other: "Vec3") -> "Vec3":
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vec3") -> "Vec3":
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar: float) -> "Vec3":
        return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)

    def dot(self, other: "Vec3") -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def length(self) -> float:
        return math.sqrt(self.dot(self))

    def horizontal_length(self) -> float:
        return math.hypot(self.x, self.y)

    def normalized(self, *, horizontal: bool = False) -> "Vec3":
        length = self.horizontal_length() if horizontal else self.length()
        if length <= 1e-9:
            return Vec3(0.0, 1.0, 0.0)
        if horizontal:
            return Vec3(self.x / length, self.y / length, 0.0)
        return self * (1.0 / length)

    def distance_2d(self, other: "Vec3") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)

    def as_dict(self) -> dict[str, float]:
        return {"x": self.x, "y": self.y, "z": self.z}


@dataclass(frozen=True, slots=True)
class Quaternion:
    i: float = 0.0
    j: float = 0.0
    k: float = 0.0
    r: float = 1.0

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any] | None) -> "Quaternion":
        value = value or {}
        return cls(
            _number(value.get("i", value.get("I"))),
            _number(value.get("j", value.get("J"))),
            _number(value.get("k", value.get("K"))),
            _number(value.get("r", value.get("R")), 1.0),
        ).normalized()

    def normalized(self) -> "Quaternion":
        magnitude = math.sqrt(self.i**2 + self.j**2 + self.k**2 + self.r**2)
        if magnitude <= 1e-12:
            return Quaternion()
        return Quaternion(
            self.i / magnitude,
            self.j / magnitude,
            self.k / magnitude,
            self.r / magnitude,
        )

    def rotate(self, vector: Vec3) -> Vec3:
        # q * v * q^-1, expanded to avoid allocating intermediate quaternions.
        qx, qy, qz, qw = self.i, self.j, self.k, self.r
        tx = 2.0 * (qy * vector.z - qz * vector.y)
        ty = 2.0 * (qz * vector.x - qx * vector.z)
        tz = 2.0 * (qx * vector.y - qy * vector.x)
        return Vec3(
            vector.x + qw * tx + (qy * tz - qz * ty),
            vector.y + qw * ty + (qz * tx - qx * tz),
            vector.z + qw * tz + (qx * ty - qy * tx),
        )


@dataclass(frozen=True, slots=True)
class Bounds:
    minimum: Vec3
    maximum: Vec3

    @classmethod
    def from_mapping(cls, value: Mapping[str, Any] | None) -> "Bounds | None":
        if not value:
            return None
        minimum = value.get("Min", value.get("min"))
        maximum = value.get("Max", value.get("max"))
        if not isinstance(minimum, Mapping) or not isinstance(maximum, Mapping):
            return None
        return cls(Vec3.from_mapping(minimum), Vec3.from_mapping(maximum))

    def half_extent_along(self, local_axis: Vec3) -> float | None:
        extents = Vec3(
            abs(self.maximum.x - self.minimum.x) * 0.5,
            abs(self.maximum.y - self.minimum.y) * 0.5,
            abs(self.maximum.z - self.minimum.z) * 0.5,
        )
        if max(extents.x, extents.y, extents.z) <= 1e-4:
            return None
        axis = local_axis.normalized()
        return (
            abs(axis.x) * extents.x + abs(axis.y) * extents.y + abs(axis.z) * extents.z
        )


LOCAL_AXES: dict[str, Vec3] = {
    "+x": Vec3(1.0, 0.0, 0.0),
    "-x": Vec3(-1.0, 0.0, 0.0),
    "+y": Vec3(0.0, 1.0, 0.0),
    "-y": Vec3(0.0, -1.0, 0.0),
}


def rotate_z(vector: Vec3, degrees: float) -> Vec3:
    radians = math.radians(degrees)
    cosine, sine = math.cos(radians), math.sin(radians)
    return Vec3(
        vector.x * cosine - vector.y * sine,
        vector.x * sine + vector.y * cosine,
        vector.z,
    )


def outward_vector(
    rotation: Quaternion,
    local_axis: str = "+y",
    yaw_correction_degrees: float = 0.0,
) -> Vec3:
    try:
        axis = LOCAL_AXES[local_axis.lower()]
    except KeyError as error:
        raise ValueError(f"unsupported local axis: {local_axis}") from error
    return rotate_z(rotation.rotate(axis), yaw_correction_degrees).normalized(
        horizontal=True
    )


def game_yaw_degrees(forward: Vec3) -> float:
    """Return a CET yaw where identity/+Y is zero degrees."""
    normalized = forward.normalized(horizontal=True)
    return math.degrees(math.atan2(-normalized.x, normalized.y)) % 360.0


def polyline_length(points: Iterable[Vec3]) -> float:
    values = list(points)
    return sum((right - left).length() for left, right in zip(values, values[1:]))


def interpolate_polyline(points: list[Vec3], distance: float) -> tuple[Vec3, Vec3]:
    if not points:
        raise ValueError("cannot interpolate an empty polyline")
    if len(points) == 1:
        return points[0], Vec3(0.0, 1.0, 0.0)
    remaining = max(0.0, distance)
    for left, right in zip(points, points[1:]):
        delta = right - left
        length = delta.length()
        if length <= 1e-9:
            continue
        if remaining <= length:
            return left + delta * (remaining / length), delta.normalized(
                horizontal=True
            )
        remaining -= length
    tangent = (points[-1] - points[-2]).normalized(horizontal=True)
    return points[-1], tangent


def closest_point_on_segment_2d(
    point: Vec3, left: Vec3, right: Vec3
) -> tuple[Vec3, float]:
    dx, dy = right.x - left.x, right.y - left.y
    denominator = dx * dx + dy * dy
    if denominator <= 1e-12:
        closest = left
    else:
        fraction = ((point.x - left.x) * dx + (point.y - left.y) * dy) / denominator
        fraction = max(0.0, min(1.0, fraction))
        closest = Vec3(
            left.x + fraction * dx,
            left.y + fraction * dy,
            left.z + fraction * (right.z - left.z),
        )
    return closest, point.distance_2d(closest)


def morton_key_2d(x: float, y: float, *, cell_size: float = 64.0) -> int:
    """Spatially coherent deterministic ordering for capture destinations."""
    ix = max(0, min(0xFFFF, int(math.floor(x / cell_size)) + 0x8000))
    iy = max(0, min(0xFFFF, int(math.floor(y / cell_size)) + 0x8000))

    def spread(value: int) -> int:
        value &= 0xFFFF
        value = (value | (value << 8)) & 0x00FF00FF
        value = (value | (value << 4)) & 0x0F0F0F0F
        value = (value | (value << 2)) & 0x33333333
        return (value | (value << 1)) & 0x55555555

    return spread(ix) | (spread(iy) << 1)
