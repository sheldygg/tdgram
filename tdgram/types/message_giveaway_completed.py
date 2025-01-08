from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageGiveawayCompleted(BaseType):
    """
    A giveaway without public winners has been completed for the chat
    """

    __type__: Literal["messageGiveawayCompleted"] = "messageGiveawayCompleted"

    giveaway_message_id: int
    """Identifier of the message with the giveaway; can be 0 if the message was deleted"""
    winner_count: int
    """Number of winners in the giveaway"""
    is_star_giveaway: bool
    """True, if the giveaway is a Telegram Star giveaway"""
    unclaimed_prize_count: int
    """Number of undistributed prizes; for Telegram Premium giveaways only"""
