from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatStatisticsObjectTypeMessage(BaseType):
    """
    Describes a message sent in the chat
    """

    __type__: Literal["chatStatisticsObjectTypeMessage"] = "chatStatisticsObjectTypeMessage"

    message_id: int
    """Message identifier"""
