from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class GiveawayParticipantStatusAdministrator(BaseType):
    """
    The user can't participate in the giveaway, because they are an administrator in one of the chats that created the giveaway
    """

    __type__: Literal["giveawayParticipantStatusAdministrator"] = (
        "giveawayParticipantStatusAdministrator"
    )

    chat_id: int
    """Identifier of the chat administered by the user"""
