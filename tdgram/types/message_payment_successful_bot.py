from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import OrderInfo


@dataclass(kw_only=True)
class MessagePaymentSuccessfulBot(BaseType):
    """
    A payment has been completed; for bots only
    """

    __type__: Literal["messagePaymentSuccessfulBot"] = "messagePaymentSuccessfulBot"

    currency: str
    """Currency for price of the product"""
    total_amount: int
    """Total price for the product, in the smallest units of the currency"""
    is_recurring: bool
    """True, if this is a recurring payment"""
    is_first_recurring: bool
    """True, if this is the first recurring payment"""
    invoice_payload: bytes
    """Invoice payload"""
    shipping_option_id: str | None = None
    """Identifier of the shipping option chosen by the user; may be empty if not applicable"""
    order_info: OrderInfo | None = None
    """Information about the order; may be null"""
    telegram_payment_charge_id: str
    """Telegram payment identifier"""
    provider_payment_charge_id: str
    """Provider payment identifier"""
