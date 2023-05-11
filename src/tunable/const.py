import copy
from typing import Any, Generic, Optional, TypeVar

T = TypeVar("T")

class ConstTunable(Generic[T]):
    """A tunable that is constant."""
    def __init__(self, value: T) -> None:
        self.value = value

    def __call__(self) -> Optional[T]:
        return self.value

class ConstTunableMap:
    """A tunable map that is constant."""
    def __init__(self, value: dict[str, Any], deep_copy=False) -> None:
        self.value = copy.deepcopy(value) if deep_copy else value

    def __getitem__(self, key: str) -> ConstTunable[Any]:
        return ConstTunable(self.value[key])