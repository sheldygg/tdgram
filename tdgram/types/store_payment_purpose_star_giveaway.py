from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import GiveawayParameters


@dataclass(kw_only=True)
class StorePaymentPurposeStarGiveaway(BaseType):
    """
    The user creating a Telegram Star giveaway
    """

    __type__: Literal["storePaymentPurposeStarGiveaway"] = "storePaymentPurposeStarGiveaway"

    parameters: GiveawayParameters
    """Giveaway parameters"""
    currency: str
    """ISO 4217 currency code of the payment currency"""
    amount: int
    """Paid amount, in the smallest units of the currency"""
    winner_count: int
    """The number of users to receive Telegram Stars"""
    star_count: int
    """The number of Telegram Stars to be distributed through the giveaway"""
