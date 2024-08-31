from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PaymentReceiptType, ProductInfo


@dataclass(kw_only=True)
class PaymentReceipt(BaseType):
    """
    Contains information about a successful payment
    """

    __type__: Literal["paymentReceipt"] = "paymentReceipt"

    product_info: ProductInfo
    """Information about the product"""
    date: int
    """Point in time (Unix timestamp) when the payment was made"""
    seller_bot_user_id: int
    """User identifier of the seller bot"""
    type: PaymentReceiptType
    """Type of the payment receipt"""
