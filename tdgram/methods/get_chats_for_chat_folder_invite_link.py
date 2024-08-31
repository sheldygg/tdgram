from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chats
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatsForChatFolderInviteLink(BaseMethod):
    """
    Returns identifiers of chats from a chat folder, suitable for adding to a chat folder invite link
    """

    __type__: Literal["getChatsForChatFolderInviteLink"] = "getChatsForChatFolderInviteLink"
    __returning_type__ = Chats

    chat_folder_id: int
    """Chat folder identifier"""
