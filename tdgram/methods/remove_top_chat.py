from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, TopChatCategory
from .base import BaseMethod


@dataclass(kw_only=True)
class RemoveTopChat(BaseMethod):
    """
    Removes a chat from the list of frequently used chats. Supported only if the chat info database is enabled
    """

    __type__: Literal["removeTopChat"] = "removeTopChat"
    __returning_type__ = Ok

    category: TopChatCategory
    """Category of frequently used chats"""
    chat_id: int
    """Chat identifier"""
