from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentPremiumGiveaway(BaseType):
    """
    A message with a Telegram Premium giveaway
    """

    __type__: Literal["pushMessageContentPremiumGiveaway"] = "pushMessageContentPremiumGiveaway"

    winner_count: int
    """Number of users which will receive Telegram Premium subscription gift codes; 0 for pinned message"""
    month_count: int
    """Number of months the Telegram Premium subscription will be active after code activation; 0 for pinned message"""
    is_pinned: bool
    """True, if the message is a pinned message with the specified content"""
