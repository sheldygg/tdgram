from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StarTransactionTypeChannelPaidReactionSend(BaseType):
    """
    The transaction is a sending of a paid reaction to a message in a channel chat by the current user; for regular users only
    """

    __type__: Literal["starTransactionTypeChannelPaidReactionSend"] = (
        "starTransactionTypeChannelPaidReactionSend"
    )

    chat_id: int
    """Identifier of the channel chat"""
    message_id: int
    """Identifier of the reacted message; can be 0 or an identifier of a deleted message"""
