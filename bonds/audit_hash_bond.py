"""
AuditHashBond

Cryptographic audit trail.
Invariant: each step produces a deterministic hash chained to the previous step.

Hash input (ordered, deterministic):
- step_index
- event
- state
- previous_hash
"""

import json
import hashlib
from bonds.bond import Bond, BondIO


class AuditHashBond(Bond):
    name = "audit_hash"

    def apply(self, io: BondIO) -> BondIO:
        prev_hash = None
        if io.trace:
            prev_hash = io.trace[-1].get("audit_hash")

        payload = {
            "step_index": len(io.trace),
            "event": io.event,
            "state": io.state,
            "previous_hash": prev_hash,
        }

        blob = json.dumps(payload, sort_keys=True, separators=(",", ":"))
        audit_hash = hashlib.sha256(blob.encode("utf-8")).hexdigest()

        new_trace = list(io.trace)
        new_trace.append({"bond": self.name, "audit_hash": audit_hash})
        return BondIO(event=io.event, state=io.state, trace=new_trace)
