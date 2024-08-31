from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BusinessOpeningHours, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetBusinessOpeningHours(BaseMethod):
    """
    Changes the business opening hours of the current user. Requires Telegram Business subscription
    """

    __type__: Literal["setBusinessOpeningHours"] = "setBusinessOpeningHours"
    __returning_type__ = Ok

    opening_hours: BusinessOpeningHours | None = None
    """The new opening hours of the business; pass null to remove the opening hours; up to 28 time intervals can be specified"""
