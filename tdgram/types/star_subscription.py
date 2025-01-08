from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StarSubscriptionPricing, StarSubscriptionType


@dataclass(kw_only=True)
class StarSubscription(BaseType):
    """
    Contains information about subscription to a channel chat, a bot, or a business account that was paid in Telegram Stars
    """

    __type__: Literal["starSubscription"] = "starSubscription"

    id: str
    """Unique identifier of the subscription"""
    chat_id: int
    """Identifier of the chat that is subscribed"""
    expiration_date: int
    """Point in time (Unix timestamp) when the subscription will expire or expired"""
    is_canceled: bool
    """True, if the subscription was canceled"""
    is_expiring: bool
    """True, if the subscription expires soon and there are no enough Telegram Stars on the user's balance to extend it"""
    pricing: StarSubscriptionPricing
    """The subscription plan"""
    type: StarSubscriptionType
    """Type of the subscription"""
