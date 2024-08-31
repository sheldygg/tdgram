from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ProductInfo


@dataclass(kw_only=True)
class BotTransactionPurposeInvoicePayment(BaseType):
    """
    User bought a product from the bot
    """

    __type__: Literal["botTransactionPurposeInvoicePayment"] = (
        "botTransactionPurposeInvoicePayment"
    )

    product_info: ProductInfo | None = None
    """Information about the bought product; may be null if not applicable"""
    invoice_payload: bytes
    """Invoice payload; for bots only"""
