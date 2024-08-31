from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ScopeNotificationSettings(BaseType):
    """
    Contains information about notification settings for several chats
    """

    __type__: Literal["scopeNotificationSettings"] = "scopeNotificationSettings"

    mute_for: int
    """Time left before notifications will be unmuted, in seconds"""
    sound_id: int
    """Identifier of the notification sound to be played; 0 if sound is disabled"""
    show_preview: bool
    """True, if message content must be displayed in notifications"""
    use_default_mute_stories: bool
    """If true, story notifications are received only for the first 5 chats from topChatCategoryUsers regardless of the value of mute_stories"""
    mute_stories: bool
    """True, if story notifications are disabled"""
    story_sound_id: int
    """Identifier of the notification sound to be played for stories; 0 if sound is disabled"""
    show_story_sender: bool
    """True, if the sender of stories must be displayed in notifications"""
    disable_pinned_message_notifications: bool
    """True, if notifications for incoming pinned messages will be created as for an ordinary unread message"""
    disable_mention_notifications: bool
    """True, if notifications for messages with mentions will be created as for an ordinary unread message"""
