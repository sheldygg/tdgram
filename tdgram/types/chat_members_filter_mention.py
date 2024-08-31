from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatMembersFilterMention(BaseType):
    """
    Returns users which can be mentioned in the chat
    """

    __type__: Literal["chatMembersFilterMention"] = "chatMembersFilterMention"

    message_thread_id: int
    """If non-zero, the identifier of the current message thread"""
