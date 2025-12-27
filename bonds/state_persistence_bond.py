"""
StatePersistenceBond

Deterministic save/load of nucleus state.
Rules:
- Explicit mode: "save" or "load"
- Explicit file path provided at init
- No implicit filesystem access
"""

import json
from copy import deepcopy
from bonds.bond import Bond, BondIO


class StatePersistenceBond(Bond):
    name = "state_persistence"

    def __init__(self, path: str, mode: str):
        if mode not in ("save", "load"):
            raise ValueError("mode must be 'save' or 'load'")
        self.path = path
        self.mode = mode

    def apply(self, io: BondIO) -> BondIO:
        if self.mode == "save":
            with open(self.path, "w", encoding="utf-8") as f:
                json.dump(io.state, f, sort_keys=True)
            return io

        # load
        with open(self.path, "r", encoding="utf-8") as f:
            state = json.load(f)
        return BondIO(event=io.event, state=deepcopy(state), trace=io.trace)
