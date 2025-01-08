from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PaidMedia


@dataclass(kw_only=True)
class StarTransactionTypeBotPaidMediaPurchase(BaseType):
    """
    The transaction is a purchase of paid media from a bot or a business account by the current user; for regular users only
    """

    __type__: Literal["starTransactionTypeBotPaidMediaPurchase"] = (
        "starTransactionTypeBotPaidMediaPurchase"
    )

    user_id: int
    """Identifier of the bot or the business account user that sent the paid media"""
    media: list[PaidMedia]
    """The bought media if the transaction wasn't refunded"""
