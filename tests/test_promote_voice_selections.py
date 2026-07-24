import tempfile
import unittest
import wave
from pathlib import Path

from tools.promote_voice_selections import REFERENCE_KEY, validate


def wav(path: Path) -> None:
    with wave.open(str(path), "wb") as stream:
        stream.setnchannels(1)
        stream.setsampwidth(2)
        stream.setframerate(24000)
        stream.writeframes(b"\0\0" * 24)


class PromoteVoiceSelectionsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        self.cinder = root / "cinder.wav"
        self.v = root / "v.wav"
        wav(self.cinder)
        wav(self.v)
        self.manifest = {
            "spoken_lines": [
                {"key": "cinder_line", "speaker": "Cinder"},
                {"key": "v_line", "speaker": "V"},
            ]
        }
        self.rows = [
            {
                "selected": "x",
                "line_key": REFERENCE_KEY,
                "design": "design-a",
                "speaker": "Cinder",
                "file": str(self.cinder),
            },
            {
                "selected": "x",
                "line_key": "cinder_line",
                "design": "design-a",
                "speaker": "Cinder",
                "file": str(self.cinder),
            },
            {
                "selected": "x",
                "line_key": "v_line",
                "design": "v-original-embed",
                "speaker": "V",
                "file": str(self.v),
            },
        ]

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_accepts_complete_consistent_selection(self) -> None:
        design, choices = validate(self.manifest, self.rows)
        self.assertEqual("design-a", design)
        self.assertEqual({"cinder_line", "v_line"}, set(choices))

    def test_rejects_cinder_take_from_other_design(self) -> None:
        self.rows[1]["design"] = "design-b"
        with self.assertRaisesRegex(ValueError, "not selected design"):
            validate(self.manifest, self.rows)

    def test_rejects_missing_line(self) -> None:
        self.rows[2]["selected"] = ""
        with self.assertRaisesRegex(ValueError, "v_line; found 0"):
            validate(self.manifest, self.rows)

    def test_infers_design_when_reference_is_not_marked(self) -> None:
        self.rows[0]["selected"] = ""
        design, _ = validate(self.manifest, self.rows)
        self.assertEqual("design-a", design)


if __name__ == "__main__":
    unittest.main()
