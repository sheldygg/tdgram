from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BusinessAwayMessageScheduleCustom(BaseType):
    """
    Send away messages only in the specified time span
    """

    __type__: Literal["businessAwayMessageScheduleCustom"] = "businessAwayMessageScheduleCustom"

    start_date: int
    """Point in time (Unix timestamp) when the away messages will start to be sent"""
    end_date: int
    """Point in time (Unix timestamp) when the away messages will stop to be sent"""
