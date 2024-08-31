from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PaymentFormType, ProductInfo


@dataclass(kw_only=True)
class PaymentForm(BaseType):
    """
    Contains information about an invoice payment form
    """

    __type__: Literal["paymentForm"] = "paymentForm"

    id: int
    """The payment form identifier"""
    type: PaymentFormType
    """Type of the payment form"""
    seller_bot_user_id: int
    """User identifier of the seller bot"""
    product_info: ProductInfo
    """Information about the product"""
