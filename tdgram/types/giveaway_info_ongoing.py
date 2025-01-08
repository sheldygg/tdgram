from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import GiveawayParticipantStatus


@dataclass(kw_only=True)
class GiveawayInfoOngoing(BaseType):
    """
    Describes an ongoing giveaway
    """

    __type__: Literal["giveawayInfoOngoing"] = "giveawayInfoOngoing"

    creation_date: int
    """Point in time (Unix timestamp) when the giveaway was created"""
    status: GiveawayParticipantStatus
    """Status of the current user in the giveaway"""
    is_ended: bool
    """True, if the giveaway has ended and results are being prepared"""
