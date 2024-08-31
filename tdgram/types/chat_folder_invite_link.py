from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatFolderInviteLink(BaseType):
    """
    Contains a chat folder invite link
    """

    __type__: Literal["chatFolderInviteLink"] = "chatFolderInviteLink"

    invite_link: str
    """The chat folder invite link"""
    name: str
    """Name of the link"""
    chat_ids: list[int]
    """Identifiers of chats, included in the link"""
