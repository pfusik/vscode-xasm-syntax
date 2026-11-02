import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1] / "extension/templates/project"


@unittest.skipUnless(sys.platform.startswith("linux"), "Linux launch configurations")
class LinuxLaunchTests(unittest.TestCase):
    def test_detached_launchers_without_node(self):
        launch = json.loads((PROJECT / ".vscode/launch.json").read_text(encoding="utf-8"))
        configs = {entry["name"]: entry for entry in launch["configurations"]}
        expected_tasks = {
            "Build & Run (detached)": "build & run (atari800 prelaunch)",
            "Run only (detached)": "run (atari800 prelaunch)",
        }
        with tempfile.TemporaryDirectory(prefix="xasm project ") as folder:
            for name, task in expected_tasks.items():
                with self.subTest(name=name):
                    config = {**configs[name], **configs[name]["linux"]}
                    self.assertEqual(config["preLaunchTask"], task)
                    # The prelaunch task owns the emulator. The launcher should exit on its own.
                    subprocess.run(
                        [config["runtimeExecutable"], *config.get("args", [])],
                        cwd=folder,
                        env={"PATH": folder},
                        stdin=subprocess.DEVNULL,
                        check=True,
                        timeout=5,
                    )
