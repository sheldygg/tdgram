from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StarGiveawayWinnerOption


@dataclass(kw_only=True)
class StarGiveawayPaymentOption(BaseType):
    """
    Describes an option for creating Telegram Star giveaway. Use telegramPaymentPurposeStarGiveaway for out-of-store payments
    """

    __type__: Literal["starGiveawayPaymentOption"] = "starGiveawayPaymentOption"

    currency: str
    """ISO 4217 currency code for the payment"""
    amount: int
    """The amount to pay, in the smallest units of the currency"""
    star_count: int
    """Number of Telegram Stars that will be distributed among winners"""
    store_product_id: str | None = None
    """Identifier of the store product associated with the option; may be empty if none"""
    yearly_boost_count: int
    """Number of times the chat will be boosted for one year if the option is chosen"""
    winner_options: list[StarGiveawayWinnerOption]
    """Allowed options for the number of giveaway winners"""
    is_default: bool
    """True, if the option must be chosen by default"""
    is_additional: bool
    """True, if the option must be shown only in the full list of payment options"""
