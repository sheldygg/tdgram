from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PremiumGiveawayParameters, Sticker


@dataclass(kw_only=True)
class MessagePremiumGiveaway(BaseType):
    """
    A Telegram Premium giveaway
    """

    __type__: Literal["messagePremiumGiveaway"] = "messagePremiumGiveaway"

    parameters: PremiumGiveawayParameters
    """Giveaway parameters"""
    winner_count: int
    """Number of users which will receive Telegram Premium subscription gift codes"""
    month_count: int
    """Number of months the Telegram Premium subscription will be active after code activation"""
    sticker: Sticker | None = None
    """A sticker to be shown in the message; may be null if unknown"""
