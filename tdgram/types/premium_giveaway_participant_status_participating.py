from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumGiveawayParticipantStatusParticipating(BaseType):
    """
    The user participates in the giveaway
    """

    __type__: Literal["premiumGiveawayParticipantStatusParticipating"] = (
        "premiumGiveawayParticipantStatusParticipating"
    )
