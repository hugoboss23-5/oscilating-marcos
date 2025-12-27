import json
import copy
from runner import run_scenario

def test_replay_determinism_byte_identical():
    scenario = [
        {"a": 1},
        {"b": None},
        {"_mode": "yang", "c": 2},
    ]

    out1 = run_scenario(
        copy.deepcopy(scenario),
        forbidden_keys=["_forbidden", "_resolved_mode"],
    )
    out2 = run_scenario(
        copy.deepcopy(scenario),
        forbidden_keys=["_forbidden", "_resolved_mode"],
    )

    # Strict equality: structure + values must match
    assert out1 == out2

    # Byte-level check for serialized output
    b1 = json.dumps(out1, sort_keys=True)
    b2 = json.dumps(out2, sort_keys=True)
    assert b1 == b2
