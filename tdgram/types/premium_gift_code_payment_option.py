from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Sticker


@dataclass(kw_only=True)
class PremiumGiftCodePaymentOption(BaseType):
    """
    Describes an option for creating Telegram Premium gift codes or Telegram Premium giveaway. Use telegramPaymentPurposePremiumGiftCodes or telegramPaymentPurposePremiumGiveaway for out-of-store payments
    """

    __type__: Literal["premiumGiftCodePaymentOption"] = "premiumGiftCodePaymentOption"

    currency: str
    """ISO 4217 currency code for Telegram Premium gift code payment"""
    amount: int
    """The amount to pay, in the smallest units of the currency"""
    discount_percentage: int
    """The discount associated with this option, as a percentage"""
    winner_count: int
    """Number of users which will be able to activate the gift codes"""
    month_count: int
    """Number of months the Telegram Premium subscription will be active"""
    store_product_id: str | None = None
    """Identifier of the store product associated with the option; may be empty if none"""
    store_product_quantity: int
    """Number of times the store product must be paid"""
    sticker: Sticker | None = None
    """A sticker to be shown along with the gift code; may be null if unknown"""
