from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatFolderInviteLinkInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class CheckChatFolderInviteLink(BaseMethod):
    """
    Checks the validity of an invite link for a chat folder and returns information about the corresponding chat folder
    """

    __type__: Literal["checkChatFolderInviteLink"] = "checkChatFolderInviteLink"
    __returning_type__ = ChatFolderInviteLinkInfo

    invite_link: str
    """Invite link to be checked"""
