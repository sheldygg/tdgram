from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PrepaidPremiumGiveaway(BaseType):
    """
    Describes a prepaid Telegram Premium giveaway
    """

    __type__: Literal["prepaidPremiumGiveaway"] = "prepaidPremiumGiveaway"

    id: int
    """Unique identifier of the prepaid giveaway"""
    winner_count: int
    """Number of users which will receive Telegram Premium subscription gift codes"""
    month_count: int
    """Number of months the Telegram Premium subscription will be active after code activation"""
    payment_date: int
    """Point in time (Unix timestamp) when the giveaway was paid"""
