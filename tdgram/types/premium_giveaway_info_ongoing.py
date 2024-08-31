from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import PremiumGiveawayParticipantStatus


@dataclass(kw_only=True)
class PremiumGiveawayInfoOngoing(BaseType):
    """
    Describes an ongoing giveaway
    """

    __type__: Literal["premiumGiveawayInfoOngoing"] = "premiumGiveawayInfoOngoing"

    creation_date: int
    """Point in time (Unix timestamp) when the giveaway was created"""
    status: PremiumGiveawayParticipantStatus
    """Status of the current user in the giveaway"""
    is_ended: bool
    """True, if the giveaway has ended and results are being prepared"""
