from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatFolderInviteLink
from .base import BaseMethod


@dataclass(kw_only=True)
class CreateChatFolderInviteLink(BaseMethod):
    """
    Creates a new invite link for a chat folder. A link can be created for a chat folder if it has only pinned and included chats
    """

    __type__: Literal["createChatFolderInviteLink"] = "createChatFolderInviteLink"
    __returning_type__ = ChatFolderInviteLink

    chat_folder_id: int
    """Chat folder identifier"""
    name: str
    """Name of the link; 0-32 characters"""
    chat_ids: list[int]
    """Identifiers of chats to be accessible by the invite link. Use getChatsForChatFolderInviteLink to get suitable chats. Basic groups will be automatically converted to supergroups before link creation"""
