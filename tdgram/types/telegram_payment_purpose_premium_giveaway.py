from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import GiveawayParameters


@dataclass(kw_only=True)
class TelegramPaymentPurposePremiumGiveaway(BaseType):
    """
    The user creating a Telegram Premium giveaway
    """

    __type__: Literal["telegramPaymentPurposePremiumGiveaway"] = (
        "telegramPaymentPurposePremiumGiveaway"
    )

    parameters: GiveawayParameters
    """Giveaway parameters"""
    currency: str
    """ISO 4217 currency code of the payment currency"""
    amount: int
    """Paid amount, in the smallest units of the currency"""
    winner_count: int
    """Number of users which will be able to activate the gift codes"""
    month_count: int
    """Number of months the Telegram Premium subscription will be active for the users"""
