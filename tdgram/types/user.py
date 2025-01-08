from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import EmojiStatus, ProfilePhoto, Usernames, UserStatus, UserType, VerificationStatus


@dataclass(kw_only=True)
class User(BaseType):
    """
    Represents a user
    """

    __type__: Literal["user"] = "user"

    id: int
    """User identifier"""
    first_name: str
    """First name of the user"""
    last_name: str
    """Last name of the user"""
    usernames: Usernames | None = None
    """Usernames of the user; may be null"""
    phone_number: str
    """Phone number of the user"""
    status: UserStatus
    """Current online status of the user"""
    profile_photo: ProfilePhoto | None = None
    """Profile photo of the user; may be null"""
    accent_color_id: int
    """Identifier of the accent color for name, and backgrounds of profile photo, reply header, and link preview"""
    background_custom_emoji_id: int
    """Identifier of a custom emoji to be shown on the reply header and link preview background; 0 if none"""
    profile_accent_color_id: int
    """Identifier of the accent color for the user's profile; -1 if none"""
    profile_background_custom_emoji_id: int
    """Identifier of a custom emoji to be shown on the background of the user's profile; 0 if none"""
    emoji_status: EmojiStatus | None = None
    """Emoji status to be shown instead of the default Telegram Premium badge; may be null"""
    is_contact: bool
    """The user is a contact of the current user"""
    is_mutual_contact: bool
    """The user is a contact of the current user and the current user is a contact of the user"""
    is_close_friend: bool
    """The user is a close friend of the current user; implies that the user is a contact"""
    verification_status: VerificationStatus | None = None
    """Information about verification status of the user; may be null if none"""
    is_premium: bool
    """True, if the user is a Telegram Premium user"""
    is_support: bool
    """True, if the user is Telegram support account"""
    restriction_reason: str | None = None
    """If non-empty, it contains a human-readable description of the reason why access to this user must be restricted"""
    has_active_stories: bool
    """True, if the user has non-expired stories available to the current user"""
    has_unread_active_stories: bool
    """True, if the user has unread non-expired stories available to the current user"""
    restricts_new_chats: bool
    """True, if the user may restrict new chats with non-contacts. Use canSendMessageToUser to check whether the current user can message the user or try to create a chat with them"""
    have_access: bool
    """If false, the user is inaccessible, and the only information known about the user is inside this class. Identifier of the user can't be passed to any method"""
    type: UserType
    """Type of the user"""
    language_code: str
    """IETF language tag of the user's language; only available to bots"""
    added_to_attachment_menu: bool
    """True, if the user added the current bot to attachment menu; only available to bots"""
