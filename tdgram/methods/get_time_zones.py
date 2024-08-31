from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import TimeZones
from .base import BaseMethod


@dataclass(kw_only=True)
class GetTimeZones(BaseMethod):
    """
    Returns the list of supported time zones
    """

    __type__: Literal["getTimeZones"] = "getTimeZones"
    __returning_type__ = TimeZones
