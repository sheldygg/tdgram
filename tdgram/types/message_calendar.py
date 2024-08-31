from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MessageCalendarDay


@dataclass(kw_only=True)
class MessageCalendar(BaseType):
    """
    Contains information about found messages, split by days according to the option 'utc_time_offset'
    """

    __type__: Literal["messageCalendar"] = "messageCalendar"

    total_count: int
    """Total number of found messages"""
    days: list[MessageCalendarDay]
    """Information about messages sent"""
