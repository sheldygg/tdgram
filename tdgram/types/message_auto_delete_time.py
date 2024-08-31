from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageAutoDeleteTime(BaseType):
    """
    Contains default auto-delete timer setting for new chats
    """

    __type__: Literal["messageAutoDeleteTime"] = "messageAutoDeleteTime"

    time: int
    """Message auto-delete time, in seconds. If 0, then messages aren't deleted automatically"""
