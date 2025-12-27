"""
CLI Runner

- Loads a scenario file (JSON list of events)
- Runs bonds deterministically
- Applies mode -> nucleus
- Outputs final state + full trace (JSON)

Usage:
python cli.py scenario.json
"""

import json
import sys
from copy import deepcopy

from core.nucleus import Nucleus
from core.modes import YinMode, YangMode
from bonds.bond import BondIO
from bonds.trace_bond import TraceBond
from bonds.mode_selector_bond import ModeSelectorBond
from bonds.policy_bond import PolicyBond
from bonds.state_persistence_bond import StatePersistenceBond


def main(path: str):
    with open(path, "r", encoding="utf-8") as f:
        events = json.load(f)

    nucleus = Nucleus()
    trace = []

    mode_selector = ModeSelectorBond(default_mode="yin")
    policy = PolicyBond(forbidden_keys=["_forbidden"])
    tracer_pre = TraceBond(step_name="pre")
    tracer_post = TraceBond(step_name="post")

    for ev in events:
        io = BondIO(event=deepcopy(ev), state=nucleus.inspect(), trace=trace)

        io = policy.apply(io)
        io = mode_selector.apply(io)
        io = tracer_pre.apply(io)

        mode = YinMode() if io.event["_resolved_mode"] == "yin" else YangMode()
        processed = mode.process(io.event)
        new_state = nucleus.apply(processed)

        io = BondIO(event=processed, state=new_state, trace=io.trace)
        io = tracer_post.apply(io)

        trace = io.trace

    out = {
        "final_state": nucleus.inspect(),
        "trace": trace,
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python cli.py <scenario.json>")
    main(sys.argv[1])
