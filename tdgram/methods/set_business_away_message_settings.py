from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import BusinessAwayMessageSettings, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetBusinessAwayMessageSettings(BaseMethod):
    """
    Changes the business away message settings of the current user. Requires Telegram Business subscription
    """

    __type__: Literal["setBusinessAwayMessageSettings"] = "setBusinessAwayMessageSettings"
    __returning_type__ = Ok

    away_message_settings: BusinessAwayMessageSettings | None = None
    """The new settings for the away message of the business; pass null to disable the away message"""
