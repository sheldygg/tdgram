import asyncio

from typing import TypeVar, Generic
from abc import abstractmethod, ABC
from dataclasses import dataclass, field

from ..types import BaseType, Error
from ..exceptions import TDLibError, TDLibTimeout

TDLibType = TypeVar("TDLibType", bound=BaseType)


class BaseMethod(ABC, Generic[TDLibType]):
    @property
    @abstractmethod
    def __type__(self) -> str:
        pass

    @property
    @abstractmethod
    def __returning_type__(self) -> BaseType:
        pass


@dataclass
class Request:
    method: BaseMethod
    method_raw: dict
    event: asyncio.Event = field(default_factory=asyncio.Event)
    response: BaseType | None = None

    async def wait(self, timeout: float = 10.0):
        try:
            await asyncio.wait_for(self.event.wait(), timeout)

            if isinstance(self.response, Error):
                raise TDLibError(self.response.code, self.response.message)

        except asyncio.TimeoutError as e:
            raise TDLibTimeout from e

    def set_response(self, response: BaseType):
        self.response = response
        self.event.set()
