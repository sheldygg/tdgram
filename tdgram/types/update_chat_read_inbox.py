from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateChatReadInbox(BaseType):
    """
    Incoming messages were read or the number of unread messages has been changed
    """

    __type__: Literal["updateChatReadInbox"] = "updateChatReadInbox"

    chat_id: int
    """Chat identifier"""
    last_read_inbox_message_id: int
    """Identifier of the last read incoming message"""
    unread_count: int
    """The number of unread messages left in the chat"""
