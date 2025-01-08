from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InternalLinkType


@dataclass(kw_only=True)
class PremiumPaymentOption(BaseType):
    """
    Describes an option for buying Telegram Premium to a user
    """

    __type__: Literal["premiumPaymentOption"] = "premiumPaymentOption"

    currency: str
    """ISO 4217 currency code for Telegram Premium subscription payment"""
    amount: int
    """The amount to pay, in the smallest units of the currency"""
    discount_percentage: int
    """The discount associated with this option, as a percentage"""
    month_count: int
    """Number of months the Telegram Premium subscription will be active. Use getPremiumInfoSticker to get the sticker to be used as representation of the Telegram Premium subscription"""
    store_product_id: str
    """Identifier of the store product associated with the option"""
    payment_link: InternalLinkType | None = None
    """An internal link to be opened for buying Telegram Premium to the user if store payment isn't possible; may be null if direct payment isn't available"""
