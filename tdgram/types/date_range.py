from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class DateRange(BaseType):
    """
    Represents a date range
    """

    __type__: Literal["dateRange"] = "dateRange"

    start_date: int
    """Point in time (Unix timestamp) at which the date range begins"""
    end_date: int
    """Point in time (Unix timestamp) at which the date range ends"""
