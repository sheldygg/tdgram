from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Invoice, OrderInfo, ShippingOption


@dataclass(kw_only=True)
class PaymentReceiptTypeRegular(BaseType):
    """
    The payment was done using a third-party payment provider
    """

    __type__: Literal["paymentReceiptTypeRegular"] = "paymentReceiptTypeRegular"

    payment_provider_user_id: int
    """User identifier of the payment provider bot"""
    invoice: Invoice
    """Information about the invoice"""
    order_info: OrderInfo | None = None
    """Order information; may be null"""
    shipping_option: ShippingOption | None = None
    """Chosen shipping option; may be null"""
    credentials_title: str
    """Title of the saved credentials chosen by the buyer"""
    tip_amount: int
    """The amount of tip chosen by the buyer in the smallest units of the currency"""
