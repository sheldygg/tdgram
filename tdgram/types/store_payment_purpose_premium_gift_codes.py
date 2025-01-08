from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText


@dataclass(kw_only=True)
class StorePaymentPurposePremiumGiftCodes(BaseType):
    """
    The user creating Telegram Premium gift codes for other users
    """

    __type__: Literal["storePaymentPurposePremiumGiftCodes"] = (
        "storePaymentPurposePremiumGiftCodes"
    )

    boosted_chat_id: int
    """Identifier of the supergroup or channel chat, which will be automatically boosted by the users for duration of the Premium subscription and which is administered by the user; 0 if none"""
    currency: str
    """ISO 4217 currency code of the payment currency"""
    amount: int
    """Paid amount, in the smallest units of the currency"""
    user_ids: list[int]
    """Identifiers of the users which can activate the gift codes"""
    text: FormattedText
    """Text to show along with the gift codes; 0-getOption('gift_text_length_max') characters. Only Bold, Italic, Underline, Strikethrough, Spoiler, and CustomEmoji entities are allowed"""
