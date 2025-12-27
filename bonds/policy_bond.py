"""
PolicyBond

Deterministic guardrails.
Rules:
- Event must be a dict
- Keys must be strings
- Disallow forbidden keys (explicit list)
- Rejects by raising ValueError (no mutation)
"""

from bonds.bond import Bond, BondIO


class PolicyBond(Bond):
    name = "policy"

    def __init__(self, forbidden_keys=None):
        self.forbidden_keys = set(forbidden_keys or [])

    def apply(self, io: BondIO) -> BondIO:
        if not isinstance(io.event, dict):
            raise ValueError("event must be dict")

        for k in io.event.keys():
            if not isinstance(k, str):
                raise ValueError("event keys must be strings")
            if k in self.forbidden_keys:
                raise ValueError(f"forbidden key: {k}")

        return io
