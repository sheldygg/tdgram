from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessagePremiumGiveawayCreated(BaseType):
    """
    A Telegram Premium giveaway was created for the chat. Use telegramPaymentPurposePremiumGiveaway or storePaymentPurposePremiumGiveaway to create a giveaway
    """

    __type__: Literal["messagePremiumGiveawayCreated"] = "messagePremiumGiveawayCreated"
