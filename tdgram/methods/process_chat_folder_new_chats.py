from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ProcessChatFolderNewChats(BaseMethod):
    """
    Process new chats added to a shareable chat folder by its owner
    """

    __type__: Literal["processChatFolderNewChats"] = "processChatFolderNewChats"
    __returning_type__ = Ok

    chat_folder_id: int
    """Chat folder identifier"""
    added_chat_ids: list[int]
    """Identifiers of the new chats, which are added to the chat folder. The chats are automatically joined if they aren't joined yet"""
