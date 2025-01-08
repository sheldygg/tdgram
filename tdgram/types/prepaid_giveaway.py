from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import GiveawayPrize


@dataclass(kw_only=True)
class PrepaidGiveaway(BaseType):
    """
    Describes a prepaid giveaway
    """

    __type__: Literal["prepaidGiveaway"] = "prepaidGiveaway"

    id: int
    """Unique identifier of the prepaid giveaway"""
    winner_count: int
    """Number of users which will receive giveaway prize"""
    prize: GiveawayPrize
    """Prize of the giveaway"""
    boost_count: int
    """The number of boosts received by the chat from the giveaway; for Telegram Star giveaways only"""
    payment_date: int
    """Point in time (Unix timestamp) when the giveaway was paid"""
