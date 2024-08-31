from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import (
    FormattedText,
    InputStoryAreas,
    InputStoryContent,
    Story,
    StoryFullId,
    StoryPrivacySettings,
)
from .base import BaseMethod


@dataclass(kw_only=True)
class SendStory(BaseMethod):
    """
    Sends a new story to a chat; requires can_post_stories right for supergroup and channel chats. Returns a temporary story
    """

    __type__: Literal["sendStory"] = "sendStory"
    __returning_type__ = Story

    chat_id: int
    """Identifier of the chat that will post the story. Pass Saved Messages chat identifier when posting a story on behalf of the current user"""
    content: InputStoryContent
    """Content of the story"""
    areas: InputStoryAreas | None = None
    """Clickable rectangle areas to be shown on the story media; pass null if none"""
    caption: FormattedText | None = None
    """Story caption; pass null to use an empty caption; 0-getOption('story_caption_length_max') characters; can have entities only if getOption('can_use_text_entities_in_story_caption')"""
    privacy_settings: StoryPrivacySettings
    """The privacy settings for the story; ignored for stories sent to supergroup and channel chats"""
    active_period: int
    """Period after which the story is moved to archive, in seconds; must be one of 6 * 3600, 12 * 3600, 86400, or 2 * 86400 for Telegram Premium users, and 86400 otherwise"""
    from_story_full_id: StoryFullId | None = None
    """Full identifier of the original story, which content was used to create the story; pass null if the story isn't repost of another story"""
    is_posted_to_chat_page: bool
    """Pass true to keep the story accessible after expiration"""
    protect_content: bool
    """Pass true if the content of the story must be protected from forwarding and screenshotting"""
