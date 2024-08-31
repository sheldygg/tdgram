from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateChatOnlineMemberCount(BaseType):
    """
    The number of online group members has changed. This update with non-zero number of online group members is sent only for currently opened chats.
    """

    __type__: Literal["updateChatOnlineMemberCount"] = "updateChatOnlineMemberCount"

    chat_id: int
    """Identifier of the chat"""
    online_member_count: int
    """New number of online members in the chat, or 0 if unknown"""
