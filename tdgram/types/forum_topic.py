from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatNotificationSettings, DraftMessage, ForumTopicInfo, Message


@dataclass(kw_only=True)
class ForumTopic(BaseType):
    """
    Describes a forum topic
    """

    __type__: Literal["forumTopic"] = "forumTopic"

    info: ForumTopicInfo
    """Basic information about the topic"""
    last_message: Message | None = None
    """Last message in the topic; may be null if unknown"""
    is_pinned: bool
    """True, if the topic is pinned in the topic list"""
    unread_count: int
    """Number of unread messages in the topic"""
    last_read_inbox_message_id: int
    """Identifier of the last read incoming message"""
    last_read_outbox_message_id: int
    """Identifier of the last read outgoing message"""
    unread_mention_count: int
    """Number of unread messages with a mention/reply in the topic"""
    unread_reaction_count: int
    """Number of messages with unread reactions in the topic"""
    notification_settings: ChatNotificationSettings
    """Notification settings for the topic"""
    draft_message: DraftMessage | None = None
    """A draft of a message in the topic; may be null if none"""
