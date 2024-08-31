from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatInviteLinkInfo
from .base import BaseMethod


@dataclass(kw_only=True)
class CheckChatInviteLink(BaseMethod):
    """
    Checks the validity of an invite link for a chat and returns information about the corresponding chat
    """

    __type__: Literal["checkChatInviteLink"] = "checkChatInviteLink"
    __returning_type__ = ChatInviteLinkInfo

    invite_link: str
    """Invite link to be checked"""
