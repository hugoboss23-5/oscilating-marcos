"""
ModeSelectorBond

Deterministically selects mode (yin/yang) based on explicit input.
Rules:
- If event contains key "_mode", it must be "yin" or "yang"
- Otherwise, fall back to provided default_mode
- Does NOT mutate nucleus; only annotates event
"""

from copy import deepcopy
from bonds.bond import Bond, BondIO


class ModeSelectorBond(Bond):
    name = "mode_selector"

    def __init__(self, default_mode: str):
        if default_mode not in ("yin", "yang"):
            raise ValueError("default_mode must be 'yin' or 'yang'")
        self.default_mode = default_mode

    def apply(self, io: BondIO) -> BondIO:
        event = deepcopy(io.event)
        mode = event.get("_mode", self.default_mode)
        if mode not in ("yin", "yang"):
            raise ValueError("invalid mode")
        event["_resolved_mode"] = mode
        return BondIO(event=event, state=io.state, trace=io.trace)
