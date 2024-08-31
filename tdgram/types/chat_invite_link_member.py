from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatInviteLinkMember(BaseType):
    """
    Describes a chat member joined a chat via an invite link
    """

    __type__: Literal["chatInviteLinkMember"] = "chatInviteLinkMember"

    user_id: int
    """User identifier"""
    joined_chat_date: int
    """Point in time (Unix timestamp) when the user joined the chat"""
    via_chat_folder_invite_link: bool
    """True, if the user has joined the chat using an invite link for a chat folder"""
    approver_user_id: int
    """User identifier of the chat administrator, approved user join request"""
