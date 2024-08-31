from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatFolderInviteLinks
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatFolderInviteLinks(BaseMethod):
    """
    Returns invite links created by the current user for a shareable chat folder
    """

    __type__: Literal["getChatFolderInviteLinks"] = "getChatFolderInviteLinks"
    __returning_type__ = ChatFolderInviteLinks

    chat_folder_id: int
    """Chat folder identifier"""
