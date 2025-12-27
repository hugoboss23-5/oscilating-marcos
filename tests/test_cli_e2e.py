import json
import subprocess
import sys
import tempfile
import os


def test_cli_end_to_end_state_is_pure_and_traced():
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

        # Final state must be pure (no meta keys)
        assert data["final_state"] == {"a": 1, "c": 2}

        # Trace must exist and show transitions
        assert isinstance(data["trace"], list)
        assert len(data["trace"]) == 6

        # No meta keys leak into after_state entries
        for entry in data["trace"]:
            for k in entry.get("after_state", {}).keys():
                assert not k.startswith("_")
