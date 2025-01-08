from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ProductInfo


@dataclass(kw_only=True)
class StarTransactionTypeBotInvoicePurchase(BaseType):
    """
    The transaction is a purchase of a product from a bot or a business account by the current user; for regular users only
    """

    __type__: Literal["starTransactionTypeBotInvoicePurchase"] = (
        "starTransactionTypeBotInvoicePurchase"
    )

    user_id: int
    """Identifier of the bot or the business account user that created the invoice"""
    product_info: ProductInfo
    """Information about the bought product"""
