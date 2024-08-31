from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageReadDateRead(BaseType):
    """
    Contains read date of the message
    """

    __type__: Literal["messageReadDateRead"] = "messageReadDateRead"

    read_date: int
    """Point in time (Unix timestamp) when the message was read by the other user"""
