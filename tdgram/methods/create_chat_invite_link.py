from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatInviteLink
from .base import BaseMethod


@dataclass(kw_only=True)
class CreateChatInviteLink(BaseMethod):
    """
    Creates a new invite link for a chat. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right in the chat
    """

    __type__: Literal["createChatInviteLink"] = "createChatInviteLink"
    __returning_type__ = ChatInviteLink

    chat_id: int
    """Chat identifier"""
    name: str
    """Invite link name; 0-32 characters"""
    expiration_date: int
    """Point in time (Unix timestamp) when the link will expire; pass 0 if never"""
    member_limit: int
    """The maximum number of chat members that can join the chat via the link simultaneously; 0-99999; pass 0 if not limited"""
    creates_join_request: bool
    """Pass true if users joining the chat via the link need to be approved by chat administrators. In this case, member_limit must be 0"""
