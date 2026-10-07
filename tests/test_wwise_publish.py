from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


class WwisePublicationTests(unittest.TestCase):
    @unittest.skipUnless(
        shutil.which("pwsh"), "PowerShell 7 is required for Wwise publication checks"
    )
    def test_preflight_and_rollback_without_wwise(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [
                    shutil.which("pwsh"),
                    "-NoProfile",
                    "-File",
                    str(Path(__file__).with_name("wwise_publish_smoke.ps1")),
                    "-Work",
                    directory,
                ],
                capture_output=True,
                text=True,
                timeout=30,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("PASS:", result.stdout)


if __name__ == "__main__":
    unittest.main()
