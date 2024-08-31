from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Message
from .base import BaseMethod


@dataclass(kw_only=True)
class GetRepliedMessage(BaseMethod):
    """
    Returns information about a non-bundled message that is replied by a given message. Also, returns the pinned message, the game message, the invoice message,
    """

    __type__: Literal["getRepliedMessage"] = "getRepliedMessage"
    __returning_type__ = Message

    chat_id: int
    """Identifier of the chat the message belongs to"""
    message_id: int
    """Identifier of the reply message"""
