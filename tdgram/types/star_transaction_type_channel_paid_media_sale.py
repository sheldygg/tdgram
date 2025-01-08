from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PaidMedia


@dataclass(kw_only=True)
class StarTransactionTypeChannelPaidMediaSale(BaseType):
    """
    The transaction is a sale of paid media by the channel chat; for channel chats only
    """

    __type__: Literal["starTransactionTypeChannelPaidMediaSale"] = (
        "starTransactionTypeChannelPaidMediaSale"
    )

    user_id: int
    """Identifier of the user that bought the media"""
    message_id: int
    """Identifier of the corresponding message with paid media; can be 0 or an identifier of a deleted message"""
    media: list[PaidMedia]
    """The bought media"""
