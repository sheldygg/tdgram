from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateChatMessageAutoDeleteTime(BaseType):
    """
    The message auto-delete or self-destruct timer setting for a chat was changed
    """

    __type__: Literal["updateChatMessageAutoDeleteTime"] = "updateChatMessageAutoDeleteTime"

    chat_id: int
    """Chat identifier"""
    message_auto_delete_time: int
    """New value of message_auto_delete_time"""
