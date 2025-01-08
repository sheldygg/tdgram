from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageGiveawayCreated(BaseType):
    """
    A giveaway was created for the chat. Use telegramPaymentPurposePremiumGiveaway, storePaymentPurposePremiumGiveaway, telegramPaymentPurposeStarGiveaway, or storePaymentPurposeStarGiveaway to create a giveaway
    """

    __type__: Literal["messageGiveawayCreated"] = "messageGiveawayCreated"

    star_count: int
    """Number of Telegram Stars that will be shared by winners of the giveaway; 0 for Telegram Premium giveaways"""
