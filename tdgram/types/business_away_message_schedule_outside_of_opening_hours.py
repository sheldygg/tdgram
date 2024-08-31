from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BusinessAwayMessageScheduleOutsideOfOpeningHours(BaseType):
    """
    Send away messages outside of the business opening hours
    """

    __type__: Literal["businessAwayMessageScheduleOutsideOfOpeningHours"] = (
        "businessAwayMessageScheduleOutsideOfOpeningHours"
    )
