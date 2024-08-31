from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TelegramPaymentPurposePremiumGiftCodes(BaseType):
    """
    The user creating Telegram Premium gift codes for other users
    """

    __type__: Literal["telegramPaymentPurposePremiumGiftCodes"] = (
        "telegramPaymentPurposePremiumGiftCodes"
    )

    boosted_chat_id: int
    """Identifier of the supergroup or channel chat, which will be automatically boosted by the users for duration of the Premium subscription and which is administered by the user; 0 if none"""
    currency: str
    """ISO 4217 currency code of the payment currency"""
    amount: int
    """Paid amount, in the smallest units of the currency"""
    user_ids: list[int]
    """Identifiers of the users which can activate the gift codes"""
    month_count: int
    """Number of months the Telegram Premium subscription will be active for the users"""
