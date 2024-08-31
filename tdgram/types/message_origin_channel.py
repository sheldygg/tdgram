from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageOriginChannel(BaseType):
    """
    The message was originally a post in a channel
    """

    __type__: Literal["messageOriginChannel"] = "messageOriginChannel"

    chat_id: int
    """Identifier of the channel chat to which the message was originally sent"""
    message_id: int
    """Message identifier of the original message"""
    author_signature: str
    """Original post author signature"""
