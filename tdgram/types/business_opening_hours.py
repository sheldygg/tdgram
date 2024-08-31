from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import BusinessOpeningHoursInterval


@dataclass(kw_only=True)
class BusinessOpeningHours(BaseType):
    """
    Describes opening hours of a business
    """

    __type__: Literal["businessOpeningHours"] = "businessOpeningHours"

    time_zone_id: str
    """Unique time zone identifier"""
    opening_hours: list[BusinessOpeningHoursInterval]
    """Intervals of the time when the business is open"""
