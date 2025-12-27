from bonds.bond import BondIO
from bonds.mode_selector_bond import ModeSelectorBond


def test_mode_selector_default():
    io = BondIO(event={}, state={}, trace=[])
    b = ModeSelectorBond(default_mode="yin")
    out = b.apply(io)
    assert out.event["_resolved_mode"] == "yin"


def test_mode_selector_override():
    io = BondIO(event={"_mode": "yang"}, state={}, trace=[])
    b = ModeSelectorBond(default_mode="yin")
    out = b.apply(io)
    assert out.event["_resolved_mode"] == "yang"
