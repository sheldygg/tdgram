from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import GiveawayParameters, GiveawayPrize, Sticker


@dataclass(kw_only=True)
class MessageGiveaway(BaseType):
    """
    A giveaway
    """

    __type__: Literal["messageGiveaway"] = "messageGiveaway"

    parameters: GiveawayParameters
    """Giveaway parameters"""
    winner_count: int
    """Number of users which will receive Telegram Premium subscription gift codes"""
    prize: GiveawayPrize
    """Prize of the giveaway"""
    sticker: Sticker | None = None
    """A sticker to be shown in the message; may be null if unknown"""
