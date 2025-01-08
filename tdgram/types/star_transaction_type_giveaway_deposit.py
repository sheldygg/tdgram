from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StarTransactionTypeGiveawayDeposit(BaseType):
    """
    The transaction is a deposit of Telegram Stars from a giveaway; for regular users only
    """

    __type__: Literal["starTransactionTypeGiveawayDeposit"] = "starTransactionTypeGiveawayDeposit"

    chat_id: int
    """Identifier of a supergroup or a channel chat that created the giveaway"""
    giveaway_message_id: int
    """Identifier of the message with the giveaway; can be 0 or an identifier of a deleted message"""
