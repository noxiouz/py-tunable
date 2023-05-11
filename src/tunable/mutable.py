import copy
import threading

from .protocols import Tunable, T
from typing import Any, Callable, Generic, Optional

class MutableTunable(Generic[T]):
    def __init__(self, cb: Callable[..., T]) -> None:
        self.cb = cb
    
    def __call__(self) -> Optional[T]:
        return self.cb()


class MutableTunableMap:
    """A mutable version of TunableMap."""
    def __init__(self, value: dict[str, Any], deep_copy=False) -> None:
        self.value = copy.deepcopy(value) if deep_copy else value

    def __getitem__(self, key: str) -> Tunable[Any]:
        return MutableTunable(lambda: self.value.get(key))

    def __setitem__(self, key: str, value: Any) -> None:
        self.value[key] = value


class TSMutableMap:
    def __init__(self, map: MutableTunableMap, lock: threading.Lock) -> None:
        self.map = map
        self.lock = lock
    
    def __getitem__(self, key: str) -> Tunable[Any]:
        def cb():
            with self.lock:
                return self.map.value[key]
        return MutableTunable(cb)
    
    def __setitem__(self, key: str, value: Any) -> None:
        with self.lock:
            self.map[key] = value