from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Gift


@dataclass(kw_only=True)
class StarTransactionTypeGiftPurchase(BaseType):
    """
    The transaction is a purchase of a regular gift to another user; for regular users and bots only
    """

    __type__: Literal["starTransactionTypeGiftPurchase"] = "starTransactionTypeGiftPurchase"

    user_id: int
    """Identifier of the user that received the gift"""
    gift: Gift
    """The gift"""
