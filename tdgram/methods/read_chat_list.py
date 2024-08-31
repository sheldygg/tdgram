from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatList, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ReadChatList(BaseMethod):
    """
    Traverse all chats in a chat list and marks all messages in the chats as read
    """

    __type__: Literal["readChatList"] = "readChatList"
    __returning_type__ = Ok

    chat_list: ChatList
    """Chat list in which to mark all chats as read"""
