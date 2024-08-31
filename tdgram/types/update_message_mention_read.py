from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateMessageMentionRead(BaseType):
    """
    A message with an unread mention was read
    """

    __type__: Literal["updateMessageMentionRead"] = "updateMessageMentionRead"

    chat_id: int
    """Chat identifier"""
    message_id: int
    """Message identifier"""
    unread_mention_count: int
    """The new number of unread mention messages left in the chat"""
