"""
TraceBond

Appends a trace entry describing the transition that already occurred.
It does NOT perform the transition; it only records.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict

from bonds.bond import Bond, BondIO, TraceEntry


class TraceBond(Bond):
    name = "trace"

    def __init__(self, step_name: str):
        self.step_name = step_name

    def apply(self, io: BondIO) -> BondIO:
        entry: TraceEntry = {
            "bond": self.name,
            "step": self.step_name,
            "before_event": deepcopy(io.event),
            "after_event": deepcopy(io.event),
            "before_state": deepcopy(io.state),
            "after_state": deepcopy(io.state),
        }
        new_trace = list(io.trace) + [entry]
        return BondIO(event=io.event, state=io.state, trace=new_trace)
