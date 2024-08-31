from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumGiveawayInfoCompleted(BaseType):
    """
    Describes a completed giveaway
    """

    __type__: Literal["premiumGiveawayInfoCompleted"] = "premiumGiveawayInfoCompleted"

    creation_date: int
    """Point in time (Unix timestamp) when the giveaway was created"""
    actual_winners_selection_date: int
    """Point in time (Unix timestamp) when the winners were selected. May be bigger than winners selection date specified in parameters of the giveaway"""
    was_refunded: bool
    """True, if the giveaway was canceled and was fully refunded"""
    winner_count: int
    """Number of winners in the giveaway"""
    activation_count: int
    """Number of winners, which activated their gift codes"""
    gift_code: str
    """Telegram Premium gift code that was received by the current user; empty if the user isn't a winner in the giveaway"""
