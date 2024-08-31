from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import PremiumGiftCodePaymentOptions
from .base import BaseMethod


@dataclass(kw_only=True)
class GetPremiumGiftCodePaymentOptions(BaseMethod):
    """
    Returns available options for Telegram Premium gift code or giveaway creation
    """

    __type__: Literal["getPremiumGiftCodePaymentOptions"] = "getPremiumGiftCodePaymentOptions"
    __returning_type__ = PremiumGiftCodePaymentOptions

    boosted_chat_id: int
    """Identifier of the supergroup or channel chat, which will be automatically boosted by receivers of the gift codes and which is administered by the user; 0 if none"""
