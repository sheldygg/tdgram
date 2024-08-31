from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Messages
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatScheduledMessages(BaseMethod):
    """
    Returns all scheduled messages in a chat. The messages are returned in reverse chronological order (i.e., in order of decreasing message_id)
    """

    __type__: Literal["getChatScheduledMessages"] = "getChatScheduledMessages"
    __returning_type__ = Messages

    chat_id: int
    """Chat identifier"""
