from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumGiveawayParticipantStatusAlreadyWasMember(BaseType):
    """
    The user can't participate in the giveaway, because they have already been member of the chat
    """

    __type__: Literal["premiumGiveawayParticipantStatusAlreadyWasMember"] = (
        "premiumGiveawayParticipantStatusAlreadyWasMember"
    )

    joined_chat_date: int
    """Point in time (Unix timestamp) when the user joined the chat"""
