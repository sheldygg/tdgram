from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TimeZone(BaseType):
    """
    Describes a time zone
    """

    __type__: Literal["timeZone"] = "timeZone"

    id: str
    """Unique time zone identifier"""
    name: str
    """Time zone name"""
    utc_time_offset: int
    """Current UTC time offset for the time zone"""
