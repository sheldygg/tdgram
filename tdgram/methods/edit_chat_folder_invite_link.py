from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatFolderInviteLink
from .base import BaseMethod


@dataclass(kw_only=True)
class EditChatFolderInviteLink(BaseMethod):
    """
    Edits an invite link for a chat folder
    """

    __type__: Literal["editChatFolderInviteLink"] = "editChatFolderInviteLink"
    __returning_type__ = ChatFolderInviteLink

    chat_folder_id: int
    """Chat folder identifier"""
    invite_link: str
    """Invite link to be edited"""
    name: str
    """New name of the link; 0-32 characters"""
    chat_ids: list[int]
    """New identifiers of chats to be accessible by the invite link. Use getChatsForChatFolderInviteLink to get suitable chats. Basic groups will be automatically converted to supergroups before link editing"""
