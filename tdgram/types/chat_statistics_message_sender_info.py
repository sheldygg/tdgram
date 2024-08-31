from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatStatisticsMessageSenderInfo(BaseType):
    """
    Contains statistics about messages sent by a user
    """

    __type__: Literal["chatStatisticsMessageSenderInfo"] = "chatStatisticsMessageSenderInfo"

    user_id: int
    """User identifier"""
    sent_message_count: int
    """Number of sent messages"""
    average_character_count: int
    """Average number of characters in sent messages; 0 if unknown"""
