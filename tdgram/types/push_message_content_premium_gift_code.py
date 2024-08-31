from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentPremiumGiftCode(BaseType):
    """
    A message with a Telegram Premium gift code created for the user
    """

    __type__: Literal["pushMessageContentPremiumGiftCode"] = "pushMessageContentPremiumGiftCode"

    month_count: int
    """Number of months the Telegram Premium subscription will be active after code activation"""
