from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ProductInfo


@dataclass(kw_only=True)
class StarTransactionTypeBotSubscriptionPurchase(BaseType):
    """
    The transaction is a purchase of a subscription from a bot or a business account by the current user; for regular users only
    """

    __type__: Literal["starTransactionTypeBotSubscriptionPurchase"] = (
        "starTransactionTypeBotSubscriptionPurchase"
    )

    user_id: int
    """Identifier of the bot or the business account user that created the subscription link"""
    subscription_period: int
    """The number of seconds between consecutive Telegram Star debitings"""
    product_info: ProductInfo
    """Information about the bought subscription"""
