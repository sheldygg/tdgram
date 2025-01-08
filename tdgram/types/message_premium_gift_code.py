from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import FormattedText, MessageSender, Sticker


@dataclass(kw_only=True)
class MessagePremiumGiftCode(BaseType):
    """
    A Telegram Premium gift code was created for the user
    """

    __type__: Literal["messagePremiumGiftCode"] = "messagePremiumGiftCode"

    creator_id: MessageSender | None = None
    """Identifier of a chat or a user that created the gift code; may be null if unknown"""
    text: FormattedText
    """Message added to the gift"""
    is_from_giveaway: bool
    """True, if the gift code was created for a giveaway"""
    is_unclaimed: bool
    """True, if the winner for the corresponding Telegram Premium subscription wasn't chosen"""
    currency: str
    """Currency for the paid amount; empty if unknown"""
    amount: int
    """The paid amount, in the smallest units of the currency; 0 if unknown"""
    cryptocurrency: str | None = None
    """Cryptocurrency used to pay for the gift; may be empty if none or unknown"""
    cryptocurrency_amount: int
    """The paid amount, in the smallest units of the cryptocurrency; 0 if unknown"""
    month_count: int
    """Number of months the Telegram Premium subscription will be active after code activation"""
    sticker: Sticker | None = None
    """A sticker to be shown in the message; may be null if unknown"""
    code: str
    """The gift code"""
