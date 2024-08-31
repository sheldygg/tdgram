from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import TimeZone


@dataclass(kw_only=True)
class TimeZones(BaseType):
    """
    Contains a list of time zones
    """

    __type__: Literal["timeZones"] = "timeZones"

    time_zones: list[TimeZone]
    """A list of time zones"""
