from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, PremiumGiveawayParameters
from .base import BaseMethod


@dataclass(kw_only=True)
class LaunchPrepaidPremiumGiveaway(BaseMethod):
    """
    Launches a prepaid Telegram Premium giveaway
    """

    __type__: Literal["launchPrepaidPremiumGiveaway"] = "launchPrepaidPremiumGiveaway"
    __returning_type__ = Ok

    giveaway_id: int
    """Unique identifier of the prepaid giveaway"""
    parameters: PremiumGiveawayParameters
    """Giveaway parameters"""
