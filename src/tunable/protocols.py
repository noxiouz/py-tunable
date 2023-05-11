from typing import Any,Protocol, Optional, TypeVar

T = TypeVar("T")

class Tunable(Protocol[T]):
    def __call__(self) -> Optional[T]:
        ...

class TunableMap(Protocol):
    def __getitem__(self, key: str) -> Tunable[Any]:
        ...

