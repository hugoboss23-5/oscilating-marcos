"""
Marcos Processing Modes (Regulatory)

Modes are pure functions that transform events
before they reach the nucleus. No side effects.
"""

class Mode:
    name = "base"

    def process(self, event: dict) -> dict:
        if not isinstance(event, dict):
            raise ValueError("event must be dict")
        return dict(event)


class YinMode(Mode):
    name = "yin"

    def process(self, event: dict) -> dict:
        # attenuate: drop keys with None values
        return {k: v for k, v in event.items() if v is not None}


class YangMode(Mode):
    name = "yang"

    def process(self, event: dict) -> dict:
        # amplify: pass through unchanged (explicit)
        return dict(event)
