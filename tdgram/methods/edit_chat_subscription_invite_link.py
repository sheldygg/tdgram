from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatInviteLink
from .base import BaseMethod


@dataclass(kw_only=True)
class EditChatSubscriptionInviteLink(BaseMethod):
    """
    Edits a subscription invite link for a channel chat. Requires can_invite_users right in the chat for own links and owner privileges for other links
    """

    __type__: Literal["editChatSubscriptionInviteLink"] = "editChatSubscriptionInviteLink"
    __returning_type__ = ChatInviteLink

    chat_id: int
    """Chat identifier"""
    invite_link: str
    """Invite link to be edited"""
    name: str
    """Invite link name; 0-32 characters"""
