from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StarSubscriptionPricing


@dataclass(kw_only=True)
class ChatInviteLink(BaseType):
    """
    Contains a chat invite link
    """

    __type__: Literal["chatInviteLink"] = "chatInviteLink"

    invite_link: str
    """Chat invite link"""
    name: str
    """Name of the link"""
    creator_user_id: int
    """User identifier of an administrator created the link"""
    date: int
    """Point in time (Unix timestamp) when the link was created"""
    edit_date: int
    """Point in time (Unix timestamp) when the link was last edited; 0 if never or unknown"""
    expiration_date: int
    """Point in time (Unix timestamp) when the link will expire; 0 if never"""
    subscription_pricing: StarSubscriptionPricing | None = None
    """Information about subscription plan that is applied to the users joining the chat by the link; may be null if the link doesn't require subscription"""
    member_limit: int
    """The maximum number of members, which can join the chat using the link simultaneously; 0 if not limited. Always 0 if the link requires approval"""
    member_count: int
    """Number of chat members, which joined the chat using the link"""
    expired_member_count: int
    """Number of chat members, which joined the chat using the link, but have already left because of expired subscription; for subscription links only"""
    pending_join_request_count: int
    """Number of pending join requests created using this link"""
    creates_join_request: bool
    """True, if the link only creates join request. If true, total number of joining members will be unlimited"""
    is_primary: bool
    """True, if the link is primary. Primary invite link can't have name, expiration date, or usage limit. There is exactly one primary invite link for each administrator with can_invite_users right at a given time"""
    is_revoked: bool
    """True, if the link was revoked"""
