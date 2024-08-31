from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class AddChatFolderByInviteLink(BaseMethod):
    """
    Adds a chat folder by an invite link
    """

    __type__: Literal["addChatFolderByInviteLink"] = "addChatFolderByInviteLink"
    __returning_type__ = Ok

    invite_link: str
    """Invite link for the chat folder"""
    chat_ids: list[int]
    """Identifiers of the chats added to the chat folder. The chats are automatically joined if they aren't joined yet"""
