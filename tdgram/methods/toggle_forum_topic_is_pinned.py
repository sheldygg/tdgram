from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleForumTopicIsPinned(BaseMethod):
    """
    Changes the pinned state of a forum topic; requires can_manage_topics right in the supergroup. There can be up to getOption('pinned_forum_topic_count_max') pinned forum topics
    """

    __type__: Literal["toggleForumTopicIsPinned"] = "toggleForumTopicIsPinned"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    message_thread_id: int
    """Message thread identifier of the forum topic"""
    is_pinned: bool
    """Pass true to pin the topic; pass false to unpin it"""
