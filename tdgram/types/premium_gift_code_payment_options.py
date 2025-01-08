from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PremiumGiftCodePaymentOption


@dataclass(kw_only=True)
class PremiumGiftCodePaymentOptions(BaseType):
    """
    Contains a list of options for creating Telegram Premium gift codes or Telegram Premium giveaway
    """

    __type__: Literal["premiumGiftCodePaymentOptions"] = "premiumGiftCodePaymentOptions"

    options: list[PremiumGiftCodePaymentOption]
    """The list of options"""
