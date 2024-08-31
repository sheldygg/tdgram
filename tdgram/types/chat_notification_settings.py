from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatNotificationSettings(BaseType):
    """
    Contains information about notification settings for a chat or a forum topic
    """

    __type__: Literal["chatNotificationSettings"] = "chatNotificationSettings"

    use_default_mute_for: bool
    """If true, the value for the relevant type of chat or the forum chat is used instead of mute_for"""
    mute_for: int
    """Time left before notifications will be unmuted, in seconds"""
    use_default_sound: bool
    """If true, the value for the relevant type of chat or the forum chat is used instead of sound_id"""
    sound_id: int
    """Identifier of the notification sound to be played for messages; 0 if sound is disabled"""
    use_default_show_preview: bool
    """If true, the value for the relevant type of chat or the forum chat is used instead of show_preview"""
    show_preview: bool
    """True, if message content must be displayed in notifications"""
    use_default_mute_stories: bool
    """If true, the value for the relevant type of chat is used instead of mute_stories"""
    mute_stories: bool
    """True, if story notifications are disabled for the chat"""
    use_default_story_sound: bool
    """If true, the value for the relevant type of chat is used instead of story_sound_id"""
    story_sound_id: int
    """Identifier of the notification sound to be played for stories; 0 if sound is disabled"""
    use_default_show_story_sender: bool
    """If true, the value for the relevant type of chat is used instead of show_story_sender"""
    show_story_sender: bool
    """True, if the sender of stories must be displayed in notifications"""
    use_default_disable_pinned_message_notifications: bool
    """If true, the value for the relevant type of chat or the forum chat is used instead of disable_pinned_message_notifications"""
    disable_pinned_message_notifications: bool
    """If true, notifications for incoming pinned messages will be created as for an ordinary unread message"""
    use_default_disable_mention_notifications: bool
    """If true, the value for the relevant type of chat or the forum chat is used instead of disable_mention_notifications"""
    disable_mention_notifications: bool
    """If true, notifications for messages with mentions will be created as for an ordinary unread message"""
