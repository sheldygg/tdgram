from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteChatFolderInviteLink(BaseMethod):
    """
    Deletes an invite link for a chat folder
    """

    __type__: Literal["deleteChatFolderInviteLink"] = "deleteChatFolderInviteLink"
    __returning_type__ = Ok

    chat_folder_id: int
    """Chat folder identifier"""
    invite_link: str
    """Invite link to be deleted"""
