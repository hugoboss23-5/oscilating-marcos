import json
import subprocess
import sys
import tempfile
import os


def test_cli_end_to_end():
    scenario = [
        {"a": 1},
        {"b": None},
        {"_mode": "yang", "c": 2},
    ]

    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "scenario.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(scenario, f)

        out = subprocess.check_output(
            [sys.executable, "cli.py", path],
            cwd=os.path.dirname(__file__) + "/..",
        )
        data = json.loads(out.decode("utf-8"))

        assert data["final_state"]["a"] == 1
        assert data["final_state"]["c"] == 2
        assert isinstance(data["trace"], list)
        assert len(data["trace"]) > 0
