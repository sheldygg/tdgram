from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatList, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class LoadChats(BaseMethod):
    """
    Loads more chats from a chat list. The loaded chats and their positions in the chat list will be sent through updates. Chats are sorted by the pair (chat.position.order, chat.id) in descending order. Returns a 404 error if all chats have been loaded
    """

    __type__: Literal["loadChats"] = "loadChats"
    __returning_type__ = Ok

    chat_list: ChatList | None = None
    """The chat list in which to load chats; pass null to load chats from the main chat list"""
    limit: int
    """The maximum number of chats to be loaded. For optimal performance, the number of loaded chats is chosen by TDLib and can be smaller than the specified limit, even if the end of the list is not reached"""
