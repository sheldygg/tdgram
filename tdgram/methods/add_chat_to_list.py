from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatList, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class AddChatToList(BaseMethod):
    """
    Adds a chat to a chat list. A chat can't be simultaneously in Main and Archive chat lists, so it is automatically removed from another one if needed
    """

    __type__: Literal["addChatToList"] = "addChatToList"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    chat_list: ChatList
    """The chat list. Use getChatListsToAddChat to get suitable chat lists"""
