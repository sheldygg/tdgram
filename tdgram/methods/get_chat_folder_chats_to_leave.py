from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chats
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatFolderChatsToLeave(BaseMethod):
    """
    Returns identifiers of pinned or always included chats from a chat folder, which are suggested to be left when the chat folder is deleted
    """

    __type__: Literal["getChatFolderChatsToLeave"] = "getChatFolderChatsToLeave"
    __returning_type__ = Chats

    chat_folder_id: int
    """Chat folder identifier"""
