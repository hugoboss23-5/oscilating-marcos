from bonds.bond import BondIO
from bonds.trace_bond import TraceBond

def test_trace_bond_appends_entry():
    io0 = BondIO(event={"k": 1}, state={"s": 2}, trace=[])
    b = TraceBond(step_name="after_mode")
    io1 = b.apply(io0)

    assert io0.trace == []
    assert len(io1.trace) == 1
    e = io1.trace[0]
    assert e["bond"] == "trace"
    assert e["step"] == "after_mode"
    assert e["before_event"] == {"k": 1}
    assert e["after_event"] == {"k": 1}
    assert e["before_state"] == {"s": 2}
    assert e["after_state"] == {"s": 2}
