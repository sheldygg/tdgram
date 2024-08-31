from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Message


@dataclass(kw_only=True)
class MessageCalendarDay(BaseType):
    """
    Contains information about found messages sent on a specific day
    """

    __type__: Literal["messageCalendarDay"] = "messageCalendarDay"

    total_count: int
    """Total number of found messages sent on the day"""
    message: Message
    """First message sent on the day"""
