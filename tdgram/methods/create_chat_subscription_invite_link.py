from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatInviteLink, StarSubscriptionPricing
from .base import BaseMethod


@dataclass(kw_only=True)
class CreateChatSubscriptionInviteLink(BaseMethod):
    """
    Creates a new subscription invite link for a channel chat. Requires can_invite_users right in the chat
    """

    __type__: Literal["createChatSubscriptionInviteLink"] = "createChatSubscriptionInviteLink"
    __returning_type__ = ChatInviteLink

    chat_id: int
    """Chat identifier"""
    name: str
    """Invite link name; 0-32 characters"""
    subscription_pricing: StarSubscriptionPricing
    """Information about subscription plan that will be applied to the users joining the chat via the link."""
