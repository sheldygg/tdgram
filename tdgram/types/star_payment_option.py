from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StarPaymentOption(BaseType):
    """
    Describes an option for buying Telegram Stars. Use telegramPaymentPurposeStars for out-of-store payments
    """

    __type__: Literal["starPaymentOption"] = "starPaymentOption"

    currency: str
    """ISO 4217 currency code for the payment"""
    amount: int
    """The amount to pay, in the smallest units of the currency"""
    star_count: int
    """Number of Telegram Stars that will be purchased"""
    store_product_id: str | None = None
    """Identifier of the store product associated with the option; may be empty if none"""
    is_additional: bool
    """True, if the option must be shown only in the full list of payment options"""
