from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageOriginChat(BaseType):
    """
    The message was originally sent on behalf of a chat
    """

    __type__: Literal["messageOriginChat"] = "messageOriginChat"

    sender_chat_id: int
    """Identifier of the chat that originally sent the message"""
    author_signature: str
    """For messages originally sent by an anonymous chat administrator, original message author signature"""
