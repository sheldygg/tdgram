from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatInviteLink
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatInviteLink(BaseMethod):
    """
    Returns information about an invite link. Requires administrator privileges and can_invite_users right in the chat to get own links and owner privileges to get other links
    """

    __type__: Literal["getChatInviteLink"] = "getChatInviteLink"
    __returning_type__ = ChatInviteLink

    chat_id: int
    """Chat identifier"""
    invite_link: str
    """Invite link to get"""
