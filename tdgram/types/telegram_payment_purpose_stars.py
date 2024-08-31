from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TelegramPaymentPurposeStars(BaseType):
    """
    The user buying Telegram Stars
    """

    __type__: Literal["telegramPaymentPurposeStars"] = "telegramPaymentPurposeStars"

    currency: str
    """ISO 4217 currency code of the payment currency"""
    amount: int
    """Paid amount, in the smallest units of the currency"""
    star_count: int
    """Number of bought Telegram Stars"""
