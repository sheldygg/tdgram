from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class InternalLinkTypePremiumGift(BaseType):
    """
    The link is a link to the screen for gifting Telegram Premium subscriptions to friends via inputInvoiceTelegram with telegramPaymentPurposePremiumGiftCodes payments or in-store purchases
    """

    __type__: Literal["internalLinkTypePremiumGift"] = "internalLinkTypePremiumGift"

    referrer: str
    """Referrer specified in the link"""
