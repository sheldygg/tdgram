from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatList


@dataclass(kw_only=True)
class UpdateUnreadChatCount(BaseType):
    """
    Number of unread chats, i.e. with unread messages or marked as unread, has changed. This update is sent only if the message database is used
    """

    __type__: Literal["updateUnreadChatCount"] = "updateUnreadChatCount"

    chat_list: ChatList
    """The chat list with changed number of unread messages"""
    total_count: int
    """Approximate total number of chats in the chat list"""
    unread_count: int
    """Total number of unread chats"""
    unread_unmuted_count: int
    """Total number of unread unmuted chats"""
    marked_as_unread_count: int
    """Total number of chats marked as unread"""
    marked_as_unread_unmuted_count: int
    """Total number of unmuted chats marked as unread"""
