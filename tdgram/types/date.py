from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class Date(BaseType):
    """
    Represents a date according to the Gregorian calendar
    """

    __type__: Literal["date"] = "date"

    day: int
    """Day of the month; 1-31"""
    month: int
    """Month; 1-12"""
    year: int
    """Year; 1-9999"""
