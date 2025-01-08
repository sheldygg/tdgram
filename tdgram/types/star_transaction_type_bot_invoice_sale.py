from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import AffiliateInfo, ProductInfo


@dataclass(kw_only=True)
class StarTransactionTypeBotInvoiceSale(BaseType):
    """
    The transaction is a sale of a product by the bot; for bots only
    """

    __type__: Literal["starTransactionTypeBotInvoiceSale"] = "starTransactionTypeBotInvoiceSale"

    user_id: int
    """Identifier of the user that bought the product"""
    product_info: ProductInfo
    """Information about the bought product"""
    invoice_payload: bytes
    """Invoice payload"""
    affiliate: AffiliateInfo | None = None
    """Information about the affiliate which received commission from the transaction; may be null if none"""
