from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class GiveawayPrizePremium(BaseType):
    """
    The giveaway sends Telegram Premium subscriptions to the winners
    """

    __type__: Literal["giveawayPrizePremium"] = "giveawayPrizePremium"

    month_count: int
    """Number of months the Telegram Premium subscription will be active after code activation"""
