from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatList, Chats
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChats(BaseMethod):
    """
    Returns an ordered list of chats from the beginning of a chat list. For informational purposes only. Use loadChats and updates processing instead to maintain chat lists in a consistent state
    """

    __type__: Literal["getChats"] = "getChats"
    __returning_type__ = Chats

    chat_list: ChatList | None = None
    """The chat list in which to return chats; pass null to get chats from the main chat list"""
    limit: int
    """The maximum number of chats to be returned"""
