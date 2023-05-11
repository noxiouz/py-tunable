from tunable import ConstTunable, ConstTunableMap

def test_const_tunable():
    t = ConstTunable(1)
    assert t() == 1

def test_const_tunable_map():
    d = {"a": 1, "b": 2}
    m = ConstTunableMap(d, deep_copy=True)
    for k, v in d.items():
        assert m[k]() == v

    prev = d["a"]
    d["a"] = prev + 1
    assert m["a"]() == prev
