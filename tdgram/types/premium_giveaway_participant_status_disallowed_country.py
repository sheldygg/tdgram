from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumGiveawayParticipantStatusDisallowedCountry(BaseType):
    """
    The user can't participate in the giveaway, because they phone number is from a disallowed country
    """

    __type__: Literal["premiumGiveawayParticipantStatusDisallowedCountry"] = (
        "premiumGiveawayParticipantStatusDisallowedCountry"
    )

    user_country_code: str
    """A two-letter ISO 3166-1 alpha-2 country code of the user's country"""
