from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StarSubscriptionPricing


@dataclass(kw_only=True)
class ChatInviteLinkSubscriptionInfo(BaseType):
    """
    Contains information about subscription plan that must be paid by the user to use a chat invite link
    """

    __type__: Literal["chatInviteLinkSubscriptionInfo"] = "chatInviteLinkSubscriptionInfo"

    pricing: StarSubscriptionPricing
    """Information about subscription plan that must be paid by the user to use the link"""
    can_reuse: bool
    """True, if the user has already paid for the subscription and can use joinChatByInviteLink to join the subscribed chat again"""
    form_id: int
    """Identifier of the payment form to use for subscription payment; 0 if the subscription can't be paid"""
