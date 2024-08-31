from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import (
        Birthdate,
        BlockList,
        BotInfo,
        BusinessInfo,
        ChatPhoto,
        FormattedText,
        PremiumPaymentOption,
    )


@dataclass(kw_only=True)
class UserFullInfo(BaseType):
    """
    Contains full information about a user
    """

    __type__: Literal["userFullInfo"] = "userFullInfo"

    personal_photo: ChatPhoto | None = None
    """User profile photo set by the current user for the contact; may be null. If null and user.profile_photo is null, then the photo is empty; otherwise, it is unknown."""
    photo: ChatPhoto | None = None
    """User profile photo; may be null. If null and user.profile_photo is null, then the photo is empty; otherwise, it is unknown."""
    public_photo: ChatPhoto | None = None
    """User profile photo visible if the main photo is hidden by privacy settings; may be null. If null and user.profile_photo is null, then the photo is empty; otherwise, it is unknown."""
    block_list: BlockList | None = None
    """Block list to which the user is added; may be null if none"""
    can_be_called: bool
    """True, if the user can be called"""
    supports_video_calls: bool
    """True, if a video call can be created with the user"""
    has_private_calls: bool
    """True, if the user can't be called due to their privacy settings"""
    has_private_forwards: bool
    """True, if the user can't be linked in forwarded messages due to their privacy settings"""
    has_restricted_voice_and_video_note_messages: bool
    """True, if voice and video notes can't be sent or forwarded to the user"""
    has_posted_to_profile_stories: bool
    """True, if the user has posted to profile stories"""
    has_sponsored_messages_enabled: bool
    """True, if the user always enabled sponsored messages; known only for the current user"""
    need_phone_number_privacy_exception: bool
    """True, if the current user needs to explicitly allow to share their phone number with the user when the method addContact is used"""
    set_chat_background: bool
    """True, if the user set chat background for both chat users and it wasn't reverted yet"""
    bio: FormattedText | None = None
    """A short user bio; may be null for bots"""
    birthdate: Birthdate | None = None
    """Birthdate of the user; may be null if unknown"""
    personal_chat_id: int
    """Identifier of the personal chat of the user; 0 if none"""
    premium_gift_options: list[PremiumPaymentOption]
    """The list of available options for gifting Telegram Premium to the user"""
    group_in_common_count: int
    """Number of group chats where both the other user and the current user are a member; 0 for the current user"""
    business_info: BusinessInfo | None = None
    """Information about business settings for Telegram Business accounts; may be null if none"""
    bot_info: BotInfo | None = None
    """For bots, information about the bot; may be null if the user isn't a bot"""
