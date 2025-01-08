from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import (
        ChatInviteLinkSubscriptionInfo,
        ChatPhotoInfo,
        InviteLinkChatType,
        VerificationStatus,
    )


@dataclass(kw_only=True)
class ChatInviteLinkInfo(BaseType):
    """
    Contains information about a chat invite link
    """

    __type__: Literal["chatInviteLinkInfo"] = "chatInviteLinkInfo"

    chat_id: int
    """Chat identifier of the invite link; 0 if the user has no access to the chat before joining"""
    accessible_for: int
    """If non-zero, the amount of time for which read access to the chat will remain available, in seconds"""
    type: InviteLinkChatType
    """Type of the chat"""
    title: str
    """Title of the chat"""
    photo: ChatPhotoInfo | None = None
    """Chat photo; may be null"""
    accent_color_id: int
    """Identifier of the accent color for chat title and background of chat photo"""
    description: str
    """Chat description"""
    member_count: int
    """Number of members in the chat"""
    member_user_ids: list[int]
    """User identifiers of some chat members that may be known to the current user"""
    subscription_info: ChatInviteLinkSubscriptionInfo | None = None
    """Information about subscription plan that must be paid by the user to use the link; may be null if the link doesn't require subscription"""
    creates_join_request: bool
    """True, if the link only creates join request"""
    is_public: bool
    """True, if the chat is a public supergroup or channel, i.e. it has a username or it is a location-based supergroup"""
    verification_status: VerificationStatus | None = None
    """Information about verification status of the chat; may be null if none"""
