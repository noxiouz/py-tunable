from tunable import MutableTunable, MutableTunableMap

def test_muyable_tunable():
    t = MutableTunable(lambda: 1)
    assert t() == 1

def test_mutable_map():
    d = {"a": 1, "b": 2}
    m = MutableTunableMap(d, deep_copy=True)
    t = m["a"]
    assert t() == d["a"]
    m["a"] = 3
    assert t() == 3

def test_mutable_null():
    m = MutableTunableMap({})
    t = m['a']
    assert t() is None