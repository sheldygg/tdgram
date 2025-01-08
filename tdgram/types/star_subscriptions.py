from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StarAmount, StarSubscription


@dataclass(kw_only=True)
class StarSubscriptions(BaseType):
    """
    Represents a list of Telegram Star subscriptions
    """

    __type__: Literal["starSubscriptions"] = "starSubscriptions"

    star_amount: StarAmount
    """The amount of owned Telegram Stars"""
    subscriptions: list[StarSubscription]
    """List of subscriptions for Telegram Stars"""
    required_star_count: int
    """The number of Telegram Stars required to buy to extend subscriptions expiring soon"""
    next_offset: str
    """The offset for the next request. If empty, then there are no more results"""
