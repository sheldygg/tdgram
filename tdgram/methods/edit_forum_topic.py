from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class EditForumTopic(BaseMethod):
    """
    Edits title and icon of a topic in a forum supergroup chat; requires can_manage_topics right in the supergroup unless the user is creator of the topic
    """

    __type__: Literal["editForumTopic"] = "editForumTopic"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat"""
    message_thread_id: int
    """Message thread identifier of the forum topic"""
    name: str
    """New name of the topic; 0-128 characters. If empty, the previous topic name is kept"""
    edit_icon_custom_emoji: bool
    """Pass true to edit the icon of the topic. Icon of the General topic can't be edited"""
    icon_custom_emoji_id: int
    """Identifier of the new custom emoji for topic icon; pass 0 to remove the custom emoji. Ignored if edit_icon_custom_emoji is false. Telegram Premium users can use any custom emoji, other users can use only a custom emoji returned by getForumTopicDefaultIcons"""
