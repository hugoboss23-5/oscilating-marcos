from bonds.scenario_validator_bond import ScenarioValidatorBond


def test_valid_scenario_passes():
    scenario = [{"a": 1}, {"b": None}, {"_mode": "yang", "c": 2}]
    v = ScenarioValidatorBond(forbidden_keys={"_forbidden"})
    v.validate(scenario)


def test_invalid_non_list():
    v = ScenarioValidatorBond()
    try:
        v.validate({"a": 1})
        assert False
    except ValueError:
        pass


def test_invalid_event_type():
    v = ScenarioValidatorBond()
    try:
        v.validate([{"a": 1}, 3])
        assert False
    except ValueError:
        pass


def test_forbidden_key_rejected():
    v = ScenarioValidatorBond(forbidden_keys={"_bad"})
    try:
        v.validate([{"_bad": 1}])
        assert False
    except ValueError:
        pass
