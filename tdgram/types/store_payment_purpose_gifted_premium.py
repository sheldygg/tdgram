from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StorePaymentPurposeGiftedPremium(BaseType):
    """
    The user gifting Telegram Premium to another user
    """

    __type__: Literal["storePaymentPurposeGiftedPremium"] = "storePaymentPurposeGiftedPremium"

    user_id: int
    """Identifier of the user to which Telegram Premium is gifted"""
    currency: str
    """ISO 4217 currency code of the payment currency"""
    amount: int
    """Paid amount, in the smallest units of the currency"""
