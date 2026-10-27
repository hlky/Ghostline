"""Keep human caption reviews tied to the exact caption and preview evidence."""
import json
from pathlib import Path
import sys
import tempfile
import threading
import unittest
from functools import partial
from http.server import ThreadingHTTPServer
from urllib.error import HTTPError
from urllib.request import Request, urlopen

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from workspot_caption_review import Handler, ReviewStore, build, digest


class CaptionReviewTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.key = "a" * 20
        media = self.root / "previews" / self.key
        media.mkdir(parents=True)
        (media / "preview.mp4").write_bytes(b"video")
        (media / "contact.png").write_bytes(b"contact")
        self.row = {"id": self.key, "status": "captioned", "input_identity": "caption",
                    "input": {"media_sha256": {name: digest(media / name) for name in ("preview.mp4", "contact.png")},
                              "context": {"workspots": [{"workspot_path": "base/test.workspot", "source_sha256": "source"}]}},
                    "raw_response": "</script><script>alert(1)</script>"}
        (self.root / "caption-results").mkdir()
        (self.root / "caption-results/captions.jsonl").write_text(json.dumps(self.row) + "\n", encoding="utf-8")
        (self.root / "catalog.json").write_text(json.dumps({"workspots": [{"depot_path": "base/test.workspot", "source": {"binary_sha256": "source"}}]}))
        self.path = self.root / "reviews.json"
        self.store = ReviewStore(self.path, {self.key: self.row}, self.root)

    def test_build_escapes_model_content_and_rejects_changed_media(self):
        rows, page = build(self.root)
        html = page.read_text(encoding="utf-8")
        self.assertIn('"raw_response": "\\u003c/script>', html)
        self.assertNotIn('</script><script>alert(1)', html)
        self.assertEqual(set(rows), {self.key})
        (self.root / "previews" / self.key / "preview.mp4").write_bytes(b"changed")
        with self.assertRaisesRegex(ValueError, "Media changed"):
            build(self.root)

    def test_review_is_durable_and_cannot_promote_runtime_verification(self):
        record = self.store.save(self.key, {"input_identity": "caption", "decision": "approved", "notes": "Hand position checked"})
        self.assertEqual(ReviewStore(self.path, {self.key: self.row}, self.root).read()["reviews"][self.key], record)
        self.assertIn("not engine runtime verification", record["scope"])
        self.assertEqual(record["workspot_sources"][0]["sha256"], "source")
        with self.assertRaisesRegex(ValueError, "Unknown review"):
            self.store.save(self.key, {"input_identity": "caption", "decision": "runtime_verified"})

    def test_stale_identity_or_media_cannot_overwrite_review(self):
        self.store.save(self.key, {"input_identity": "caption", "decision": "needs_fix"})
        before = self.path.read_bytes()
        with self.assertRaisesRegex(ValueError, "Caption changed"):
            self.store.save(self.key, {"input_identity": "old", "decision": "approved"})
        (self.root / "previews" / self.key / "contact.png").write_bytes(b"changed")
        with self.assertRaisesRegex(ValueError, "Preview changed"):
            self.store.save(self.key, {"input_identity": "caption", "decision": "approved"})
        self.assertEqual(self.path.read_bytes(), before)

    def test_local_api_persists_and_rejects_cross_origin_requests(self):
        server = ThreadingHTTPServer(("127.0.0.1", 0), partial(Handler, directory=self.root, store=self.store))
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        base = f"http://127.0.0.1:{server.server_port}"
        try:
            body = json.dumps({"input_identity": "caption", "decision": "rejected", "notes": "Wrong action"}).encode()
            request = Request(base + "/api/caption-reviews/" + self.key, data=body,
                              headers={"Content-Type": "application/json", "Origin": base})
            with urlopen(request) as response:
                self.assertEqual(json.load(response)["decision"], "rejected")
            with urlopen(base + "/api/caption-reviews") as response:
                self.assertEqual(json.load(response)["reviews"][self.key]["notes"], "Wrong action")
            request.add_header("Origin", "https://example.com")
            with self.assertRaises(HTTPError) as error:
                urlopen(request)
            self.assertEqual(error.exception.code, 403)
        finally:
            server.shutdown()
            server.server_close()
            thread.join()


if __name__ == "__main__":
    unittest.main()
