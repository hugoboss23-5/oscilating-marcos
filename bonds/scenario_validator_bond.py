"""
ScenarioValidatorBond

Validates an entire scenario BEFORE execution.
Invariant: only valid scenarios may run.

Rules enforced:
- Scenario must be a list
- Each event must be a dict
- Event keys must be strings
- Forbidden keys are rejected
"""

from typing import List, Dict, Any, Set


class ScenarioValidatorBond:
    name = "scenario_validator"

    def __init__(self, forbidden_keys: Set[str] | None = None):
        self.forbidden_keys = set(forbidden_keys or [])

    def validate(self, scenario: List[Dict[str, Any]]) -> None:
        if not isinstance(scenario, list):
            raise ValueError("scenario must be a list")

        for i, event in enumerate(scenario):
            if not isinstance(event, dict):
                raise ValueError(f"event[{i}] must be dict")

            for k in event.keys():
                if not isinstance(k, str):
                    raise ValueError(f"event[{i}] keys must be strings")
                if k in self.forbidden_keys:
                    raise ValueError(f"event[{i}] contains forbidden key: {k}")
