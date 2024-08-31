from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatInviteLinks
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatInviteLinks(BaseMethod):
    """
    Returns invite links for a chat created by specified administrator. Requires administrator privileges and can_invite_users right in the chat to get own links and owner privileges to get other links
    """

    __type__: Literal["getChatInviteLinks"] = "getChatInviteLinks"
    __returning_type__ = ChatInviteLinks

    chat_id: int
    """Chat identifier"""
    creator_user_id: int
    """User identifier of a chat administrator. Must be an identifier of the current user for non-owner"""
    is_revoked: bool
    """Pass true if revoked links needs to be returned instead of active or expired"""
    offset_date: int
    """Creation date of an invite link starting after which to return invite links; use 0 to get results from the beginning"""
    offset_invite_link: str
    """Invite link starting after which to return invite links; use empty string to get results from the beginning"""
    limit: int
    """The maximum number of invite links to return; up to 100"""
