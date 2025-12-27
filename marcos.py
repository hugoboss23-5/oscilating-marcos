"""
Marcos Entry Point (Deterministic)

Wires:
Mode -> Nucleus

No I/O side effects beyond explicit calls.
"""

from core.nucleus import Nucleus
from core.modes import YinMode, YangMode


class Marcos:
    def __init__(self, mode="yin"):
        self.nucleus = Nucleus()
        if mode == "yin":
            self.mode = YinMode()
        elif mode == "yang":
            self.mode = YangMode()
        else:
            raise ValueError("unknown mode")

    def step(self, event: dict):
        processed = self.mode.process(event)
        return self.nucleus.apply(processed)


if __name__ == "__main__":
    m = Marcos(mode="yin")
    print(m.step({"a": 1, "b": None}))
