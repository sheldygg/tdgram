from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BusinessOpeningHoursInterval(BaseType):
    """
    Describes an interval of time when the business is open
    """

    __type__: Literal["businessOpeningHoursInterval"] = "businessOpeningHoursInterval"

    start_minute: int
    """The minute's sequence number in a week, starting on Monday, marking the start of the time interval during which the business is open; 0-7*24*60"""
    end_minute: int
    """The minute's sequence number in a week, starting on Monday, marking the end of the time interval during which the business is open; 1-8*24*60"""
