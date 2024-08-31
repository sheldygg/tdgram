from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import CheckChatUsernameResult
from .base import BaseMethod


@dataclass(kw_only=True)
class CheckChatUsername(BaseMethod):
    """
    Checks whether a username can be set for a chat
    """

    __type__: Literal["checkChatUsername"] = "checkChatUsername"
    __returning_type__ = CheckChatUsernameResult

    chat_id: int
    """Chat identifier; must be identifier of a supergroup chat, or a channel chat, or a private chat with self, or 0 if the chat is being created"""
    username: str
    """Username to be checked"""
