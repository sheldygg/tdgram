from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import LabeledPricePart


@dataclass(kw_only=True)
class Invoice(BaseType):
    """
    Product invoice
    """

    __type__: Literal["invoice"] = "invoice"

    currency: str
    """ISO 4217 currency code"""
    price_parts: list[LabeledPricePart]
    """A list of objects used to calculate the total price of the product"""
    max_tip_amount: int
    """The maximum allowed amount of tip in the smallest units of the currency"""
    suggested_tip_amounts: list[int]
    """Suggested amounts of tip in the smallest units of the currency"""
    recurring_payment_terms_of_service_url: str | None = None
    """An HTTP URL with terms of service for recurring payments. If non-empty, the invoice payment will result in recurring payments and the user must accept the terms of service before allowed to pay"""
    terms_of_service_url: str | None = None
    """An HTTP URL with terms of service for non-recurring payments. If non-empty, then the user must accept the terms of service before allowed to pay"""
    is_test: bool
    """True, if the payment is a test payment"""
    need_name: bool
    """True, if the user's name is needed for payment"""
    need_phone_number: bool
    """True, if the user's phone number is needed for payment"""
    need_email_address: bool
    """True, if the user's email address is needed for payment"""
    need_shipping_address: bool
    """True, if the user's shipping address is needed for payment"""
    send_phone_number_to_provider: bool
    """True, if the user's phone number will be sent to the provider"""
    send_email_address_to_provider: bool
    """True, if the user's email address will be sent to the provider"""
    is_flexible: bool
    """True, if the total price depends on the shipping method"""
