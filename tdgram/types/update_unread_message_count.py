from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatList


@dataclass(kw_only=True)
class UpdateUnreadMessageCount(BaseType):
    """
    Number of unread messages in a chat list has changed. This update is sent only if the message database is used
    """

    __type__: Literal["updateUnreadMessageCount"] = "updateUnreadMessageCount"

    chat_list: ChatList
    """The chat list with changed number of unread messages"""
    unread_count: int
    """Total number of unread messages"""
    unread_unmuted_count: int
    """Total number of unread messages in unmuted chats"""
