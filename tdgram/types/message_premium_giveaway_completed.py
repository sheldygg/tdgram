from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessagePremiumGiveawayCompleted(BaseType):
    """
    A Telegram Premium giveaway without public winners has been completed for the chat
    """

    __type__: Literal["messagePremiumGiveawayCompleted"] = "messagePremiumGiveawayCompleted"

    giveaway_message_id: int
    """Identifier of the message with the giveaway; can be 0 if the message was deleted"""
    winner_count: int
    """Number of winners in the giveaway"""
    unclaimed_prize_count: int
    """Number of undistributed prizes"""
