import os
import tempfile
from bonds.bond import BondIO
from bonds.state_persistence_bond import StatePersistenceBond


def test_save_and_load_state():
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "state.json")

        io0 = BondIO(event={}, state={"a": 1}, trace=[])
        saver = StatePersistenceBond(path=path, mode="save")
        saver.apply(io0)

        io1 = BondIO(event={}, state={}, trace=[])
        loader = StatePersistenceBond(path=path, mode="load")
        out = loader.apply(io1)

        assert out.state == {"a": 1}
