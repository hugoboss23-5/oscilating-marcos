"""
Marcos Nucleus (Invariant Core)

Rules:
- Deterministic
- No side effects on import
- Explicit state transitions only
"""

class Nucleus:
    def __init__(self):
        self.state = {}

    def inspect(self):
        return dict(self.state)

    def apply(self, event: dict):
        if not isinstance(event, dict):
            raise ValueError("event must be dict")
        # deterministic merge
        for k, v in event.items():
            self.state[k] = v
        return self.inspect()
