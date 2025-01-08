from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StarTransactionTypeChannelPaidReactionReceive(BaseType):
    """
    The transaction is a receiving of a paid reaction to a message by the channel chat; for channel chats only
    """

    __type__: Literal["starTransactionTypeChannelPaidReactionReceive"] = (
        "starTransactionTypeChannelPaidReactionReceive"
    )

    user_id: int
    """Identifier of the user that added the paid reaction"""
    message_id: int
    """Identifier of the reacted message; can be 0 or an identifier of a deleted message"""
