from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateChatUnreadReactionCount(BaseType):
    """
    The chat unread_reaction_count has changed
    """

    __type__: Literal["updateChatUnreadReactionCount"] = "updateChatUnreadReactionCount"

    chat_id: int
    """Chat identifier"""
    unread_reaction_count: int
    """The number of messages with unread reactions left in the chat"""
