from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chats
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatFolderNewChats(BaseMethod):
    """
    Returns new chats added to a shareable chat folder by its owner. The method must be called at most once in getOption('chat_folder_new_chats_update_period') for the given chat folder
    """

    __type__: Literal["getChatFolderNewChats"] = "getChatFolderNewChats"
    __returning_type__ = Chats

    chat_folder_id: int
    """Chat folder identifier"""
