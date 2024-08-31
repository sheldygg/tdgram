from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Message
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatPinnedMessage(BaseMethod):
    """
    Returns information about a newest pinned message in the chat
    """

    __type__: Literal["getChatPinnedMessage"] = "getChatPinnedMessage"
    __returning_type__ = Message

    chat_id: int
    """Identifier of the chat the message belongs to"""
