from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatInviteLinkMember, ChatInviteLinkMembers
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatInviteLinkMembers(BaseMethod):
    """
    Returns chat members joined a chat via an invite link. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
    """

    __type__: Literal["getChatInviteLinkMembers"] = "getChatInviteLinkMembers"
    __returning_type__ = ChatInviteLinkMembers

    chat_id: int
    """Chat identifier"""
    invite_link: str
    """Invite link for which to return chat members"""
    only_with_expired_subscription: bool
    """Pass true if the link is a subscription link and only members with expired subscription must be returned"""
    offset_member: ChatInviteLinkMember | None = None
    """A chat member from which to return next chat members; pass null to get results from the beginning"""
    limit: int
    """The maximum number of chat members to return; up to 100"""
