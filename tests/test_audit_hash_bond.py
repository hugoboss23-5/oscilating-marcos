import copy
from bonds.bond import BondIO
from bonds.audit_hash_bond import AuditHashBond


def test_audit_hash_deterministic():
    io = BondIO(event={"a": 1}, state={"x": 2}, trace=[])
    b = AuditHashBond()

    out1 = b.apply(copy.deepcopy(io))
    out2 = b.apply(copy.deepcopy(io))

    assert out1.trace[-1]["audit_hash"] == out2.trace[-1]["audit_hash"]


def test_audit_hash_chain_changes():
    b = AuditHashBond()

    io1 = BondIO(event={"a": 1}, state={"x": 2}, trace=[])
    out1 = b.apply(io1)

    io2 = BondIO(event={"a": 2}, state={"x": 2}, trace=out1.trace)
    out2 = b.apply(io2)

    assert out1.trace[-1]["audit_hash"] != out2.trace[-1]["audit_hash"]
