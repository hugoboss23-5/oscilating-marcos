"""
Deterministic Runner

Composes:
- PolicyBond
- ModeSelectorBond
- TraceBond (pre/post)
- Core (Mode -> Nucleus)

No side effects beyond explicit I/O.
"""

from copy import deepcopy
from typing import List, Dict, Any

from core.nucleus import Nucleus
from core.modes import YinMode, YangMode
from bonds.bond import BondIO
from bonds.mode_selector_bond import ModeSelectorBond
from bonds.policy_bond import PolicyBond
from bonds.trace_bond import TraceBond
from bonds.scenario_validator_bond import ScenarioValidatorBond


def run_scenario(
    events: List[Dict[str, Any]],
    *,
    default_mode: str = "yin",
    forbidden_keys=None,
) -> Dict[str, Any]:
    # preflight scenario validation
    ScenarioValidatorBond(forbidden_keys=forbidden_keys or []).validate(events)

    nucleus = Nucleus()
    trace = []

    policy = PolicyBond(forbidden_keys=forbidden_keys or [])
    mode_selector = ModeSelectorBond(default_mode=default_mode)
    tracer_pre = TraceBond(step_name="pre")
    tracer_post = TraceBond(step_name="post")

    for ev in events:
        io = BondIO(event=deepcopy(ev), state=nucleus.inspect(), trace=trace)

        io = policy.apply(io)
        io = mode_selector.apply(io)
        io = tracer_pre.apply(io)

        # strip meta keys before nucleus
        event_for_nucleus = {
            k: v for k, v in io.event.items()
            if k not in ("_mode", "_resolved_mode")
        }

        mode = YinMode() if io.event.get("_resolved_mode", default_mode) == "yin" else YangMode()
        processed = mode.process(event_for_nucleus)
        new_state = nucleus.apply(processed)

        io = BondIO(event=processed, state=new_state, trace=io.trace)
        io = tracer_post.apply(io)

        trace = io.trace

    return {
        "final_state": nucleus.inspect(),
        "trace": trace,
    }
