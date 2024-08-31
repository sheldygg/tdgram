from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatInviteLinks
from .base import BaseMethod


@dataclass(kw_only=True)
class RevokeChatInviteLink(BaseMethod):
    """
    Revokes invite link for a chat. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links.
    """

    __type__: Literal["revokeChatInviteLink"] = "revokeChatInviteLink"
    __returning_type__ = ChatInviteLinks

    chat_id: int
    """Chat identifier"""
    invite_link: str
    """Invite link to be revoked"""
