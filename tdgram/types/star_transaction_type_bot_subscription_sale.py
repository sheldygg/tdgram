from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import AffiliateInfo, ProductInfo


@dataclass(kw_only=True)
class StarTransactionTypeBotSubscriptionSale(BaseType):
    """
    The transaction is a sale of a subscription by the bot; for bots only
    """

    __type__: Literal["starTransactionTypeBotSubscriptionSale"] = (
        "starTransactionTypeBotSubscriptionSale"
    )

    user_id: int
    """Identifier of the user that bought the subscription"""
    subscription_period: int
    """The number of seconds between consecutive Telegram Star debitings"""
    product_info: ProductInfo
    """Information about the bought subscription"""
    invoice_payload: bytes
    """Invoice payload"""
    affiliate: AffiliateInfo | None = None
    """Information about the affiliate which received commission from the transaction; may be null if none"""
