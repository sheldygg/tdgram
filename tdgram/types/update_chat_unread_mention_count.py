from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateChatUnreadMentionCount(BaseType):
    """
    The chat unread_mention_count has changed
    """

    __type__: Literal["updateChatUnreadMentionCount"] = "updateChatUnreadMentionCount"

    chat_id: int
    """Chat identifier"""
    unread_mention_count: int
    """The number of unread mention messages left in the chat"""
