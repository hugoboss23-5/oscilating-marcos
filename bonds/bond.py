"""
Bond Interface (explicit I/O only)

A Bond is a deterministic transformer that can:
- read input event/state/trace
- return updated event/state/trace
No hidden side effects unless explicitly encoded in outputs.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, TypedDict


class TraceEntry(TypedDict, total=False):
    bond: str
    step: str
    before_event: Dict[str, Any]
    after_event: Dict[str, Any]
    before_state: Dict[str, Any]
    after_state: Dict[str, Any]
    note: str


@dataclass(frozen=True)
class BondIO:
    event: Dict[str, Any]
    state: Dict[str, Any]
    trace: List[TraceEntry] = field(default_factory=list)


class Bond:
    name: str = "bond"

    def apply(self, io: BondIO) -> BondIO:
        raise NotImplementedError("Bond.apply must be implemented")
