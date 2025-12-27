from bonds.bond import BondIO
from bonds.policy_bond import PolicyBond


def test_policy_allows_valid_event():
    io = BondIO(event={"a": 1}, state={}, trace=[])
    b = PolicyBond(forbidden_keys=["_forbidden"])
    out = b.apply(io)
    assert out.event == {"a": 1}


def test_policy_rejects_forbidden_key():
    io = BondIO(event={"_forbidden": 1}, state={}, trace=[])
    b = PolicyBond(forbidden_keys=["_forbidden"])
    try:
        b.apply(io)
        assert False, "expected ValueError"
    except ValueError:
        pass


def test_policy_rejects_reserved_internal_keys():
    io = BondIO(event={"_resolved_mode": "yin"}, state={}, trace=[])
    b = PolicyBond(forbidden_keys=["_resolved_mode"])
    try:
        b.apply(io)
        assert False, "expected ValueError"
    except ValueError:
        pass
