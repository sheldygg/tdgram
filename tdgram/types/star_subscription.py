from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StarSubscriptionPricing


@dataclass(kw_only=True)
class StarSubscription(BaseType):
    """
    Contains information about subscription to a channel chat paid in Telegram Stars
    """

    __type__: Literal["starSubscription"] = "starSubscription"

    id: str
    """Unique identifier of the subscription"""
    chat_id: int
    """Identifier of the channel chat that is subscribed"""
    expiration_date: int
    """Point in time (Unix timestamp) when the subscription will expire or expired"""
    can_reuse: bool
    """True, if the subscription is active and the user can use the method reuseStarSubscription to join the subscribed chat again"""
    is_canceled: bool
    """True, if the subscription was canceled"""
    is_expiring: bool
    """True, if the subscription expires soon and there are no enough Telegram Stars on the user's balance to extend it"""
    invite_link: str | None = None
    """The invite link that can be used to renew the subscription if it has been expired; may be empty, if the link isn't available anymore"""
    pricing: StarSubscriptionPricing
    """The subscription plan"""
