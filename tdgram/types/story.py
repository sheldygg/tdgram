from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import (
        FormattedText,
        MessageSender,
        ReactionType,
        StoryArea,
        StoryContent,
        StoryInteractionInfo,
        StoryPrivacySettings,
        StoryRepostInfo,
    )


@dataclass(kw_only=True)
class Story(BaseType):
    """
    Represents a story
    """

    __type__: Literal["story"] = "story"

    id: int
    """Unique story identifier among stories of the given sender"""
    sender_chat_id: int
    """Identifier of the chat that posted the story"""
    sender_id: MessageSender | None = None
    """Identifier of the sender of the story; may be null if the story is posted on behalf of the sender_chat_id"""
    date: int
    """Point in time (Unix timestamp) when the story was published"""
    is_being_sent: bool
    """True, if the story is being sent by the current user"""
    is_being_edited: bool
    """True, if the story is being edited by the current user"""
    is_edited: bool
    """True, if the story was edited"""
    is_posted_to_chat_page: bool
    """True, if the story is saved in the sender's profile and will be available there after expiration"""
    is_visible_only_for_self: bool
    """True, if the story is visible only for the current user"""
    can_be_deleted: bool
    """True, if the story can be deleted"""
    can_be_edited: bool
    """True, if the story can be edited"""
    can_be_forwarded: bool
    """True, if the story can be forwarded as a message. Otherwise, screenshots and saving of the story content must be also forbidden"""
    can_be_replied: bool
    """True, if the story can be replied in the chat with the story sender"""
    can_toggle_is_posted_to_chat_page: bool
    """True, if the story's is_posted_to_chat_page value can be changed"""
    can_get_statistics: bool
    """True, if the story statistics are available through getStoryStatistics"""
    can_get_interactions: bool
    """True, if interactions with the story can be received through getStoryInteractions"""
    has_expired_viewers: bool
    """True, if users viewed the story can't be received, because the story has expired more than getOption('story_viewers_expiration_delay') seconds ago"""
    repost_info: StoryRepostInfo | None = None
    """Information about the original story; may be null if the story wasn't reposted"""
    interaction_info: StoryInteractionInfo | None = None
    """Information about interactions with the story; may be null if the story isn't owned or there were no interactions"""
    chosen_reaction_type: ReactionType | None = None
    """Type of the chosen reaction; may be null if none"""
    privacy_settings: StoryPrivacySettings
    """Privacy rules affecting story visibility; may be approximate for non-owned stories"""
    content: StoryContent
    """Content of the story"""
    areas: list[StoryArea]
    """Clickable areas to be shown on the story content"""
    caption: FormattedText
    """Caption of the story"""
