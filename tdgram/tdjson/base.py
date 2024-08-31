import abc
import json

from typing import Callable, Any

from adaptix import Retort, name_mapping

from ..methods.base import BaseMethod, TDLibType
from ..types import BaseType

_JsonLoads = Callable[..., Any]
_JsonDumps = Callable[..., bytes]

base_retort = Retort(
    strict_coercion=False,
    recipe=[
        name_mapping(
            map={"__type__": "@type"}
        )
    ]
)


def json_loads_default(message: str) -> dict:
    return json.loads(message)


def json_dumps_default(message: dict) -> bytes:
    return json.dumps(message).encode()


class BaseTDJsonClient(abc.ABC):
    @abc.abstractmethod
    async def receive(self) -> BaseType | None: ...

    @abc.abstractmethod
    async def send(self, message: BaseMethod[TDLibType]) -> None: ...

    @abc.abstractmethod
    async def execute(self, message: BaseMethod[TDLibType]) -> BaseType | None: ...

    @abc.abstractmethod
    async def request(self, method: BaseMethod[TDLibType], timeout: float = 10.0) -> BaseType | None: ...
