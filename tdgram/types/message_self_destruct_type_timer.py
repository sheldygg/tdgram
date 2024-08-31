from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageSelfDestructTypeTimer(BaseType):
    """
    The message will be self-destructed in the specified time after its content was opened
    """

    __type__: Literal["messageSelfDestructTypeTimer"] = "messageSelfDestructTypeTimer"

    self_destruct_time: int
    """The message's self-destruct time, in seconds; must be between 0 and 60 in private chats"""
