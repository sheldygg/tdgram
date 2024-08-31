from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumGiftCodePaymentOption(BaseType):
    """
    Describes an option for creating Telegram Premium gift codes. Use telegramPaymentPurposePremiumGiftCodes for out-of-store payments
    """

    __type__: Literal["premiumGiftCodePaymentOption"] = "premiumGiftCodePaymentOption"

    currency: str
    """ISO 4217 currency code for Telegram Premium gift code payment"""
    amount: int
    """The amount to pay, in the smallest units of the currency"""
    user_count: int
    """Number of users which will be able to activate the gift codes"""
    month_count: int
    """Number of months the Telegram Premium subscription will be active"""
    store_product_id: str | None = None
    """Identifier of the store product associated with the option; may be empty if none"""
    store_product_quantity: int
    """Number of times the store product must be paid"""
