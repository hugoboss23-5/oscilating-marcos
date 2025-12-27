def test_runner_end_to_end_pure_state():
    from runner import run_scenario

    out = run_scenario(
        [
            {"a": 1},
            {"b": None},
            {"_mode": "yang", "c": 2},
        ],
        forbidden_keys=["_forbidden", "_resolved_mode"],
    )

    assert out["final_state"] == {"a": 1, "c": 2}
    assert isinstance(out["trace"], list)
    assert len(out["trace"]) >= 6
    assert any(e.get("bond") == "audit_hash" for e in out["trace"])
    for entry in out["trace"]:
        for k in entry.get("after_state", {}).keys():
            assert not k.startswith("_")
