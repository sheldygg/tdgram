from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BusinessLocation, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetBusinessLocation(BaseMethod):
    """
    Changes the business location of the current user. Requires Telegram Business subscription
    """

    __type__: Literal["setBusinessLocation"] = "setBusinessLocation"
    __returning_type__ = Ok

    location: BusinessLocation | None = None
    """The new location of the business; pass null to remove the location"""
