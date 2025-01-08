from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PaidMedia


@dataclass(kw_only=True)
class StarTransactionTypeChannelPaidMediaPurchase(BaseType):
    """
    The transaction is a purchase of paid media from a channel by the current user; for regular users only
    """

    __type__: Literal["starTransactionTypeChannelPaidMediaPurchase"] = (
        "starTransactionTypeChannelPaidMediaPurchase"
    )

    chat_id: int
    """Identifier of the channel chat that sent the paid media"""
    message_id: int
    """Identifier of the corresponding message with paid media; can be 0 or an identifier of a deleted message"""
    media: list[PaidMedia]
    """The bought media if the transaction wasn't refunded"""
