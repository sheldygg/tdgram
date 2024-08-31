from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BusinessAwayMessageScheduleAlways(BaseType):
    """
    Send away messages always
    """

    __type__: Literal["businessAwayMessageScheduleAlways"] = "businessAwayMessageScheduleAlways"
