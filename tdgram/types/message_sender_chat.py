from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageSenderChat(BaseType):
    """
    The message was sent on behalf of a chat
    """

    __type__: Literal["messageSenderChat"] = "messageSenderChat"

    chat_id: int
    """Identifier of the chat that sent the message"""
