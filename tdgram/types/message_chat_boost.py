from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageChatBoost(BaseType):
    """
    The chat was boosted by the sender of the message
    """

    __type__: Literal["messageChatBoost"] = "messageChatBoost"

    boost_count: int
    """Number of times the chat was boosted"""
