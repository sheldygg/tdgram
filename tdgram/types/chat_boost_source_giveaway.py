from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatBoostSourceGiveaway(BaseType):
    """
    The chat created a giveaway
    """

    __type__: Literal["chatBoostSourceGiveaway"] = "chatBoostSourceGiveaway"

    user_id: int
    """Identifier of a user that won in the giveaway; 0 if none"""
    gift_code: str
    """The created Telegram Premium gift code if it was used by the user or can be claimed by the current user; an empty string otherwise; for Telegram Premium giveways only"""
    star_count: int
    """Number of Telegram Stars distributed among winners of the giveaway"""
    giveaway_message_id: int
    """Identifier of the corresponding giveaway message; can be an identifier of a deleted message"""
    is_unclaimed: bool
    """True, if the winner for the corresponding giveaway prize wasn't chosen, because there were not enough participants"""
