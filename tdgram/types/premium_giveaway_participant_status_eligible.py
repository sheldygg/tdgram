from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumGiveawayParticipantStatusEligible(BaseType):
    """
    The user is eligible for the giveaway
    """

    __type__: Literal["premiumGiveawayParticipantStatusEligible"] = (
        "premiumGiveawayParticipantStatusEligible"
    )
