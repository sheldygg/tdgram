from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleSavedMessagesTopicIsPinned(BaseMethod):
    """
    Changes the pinned state of a Saved Messages topic. There can be up to getOption('pinned_saved_messages_topic_count_max') pinned topics. The limit can be increased with Telegram Premium
    """

    __type__: Literal["toggleSavedMessagesTopicIsPinned"] = "toggleSavedMessagesTopicIsPinned"
    __returning_type__ = Ok

    saved_messages_topic_id: int
    """Identifier of Saved Messages topic to pin or unpin"""
    is_pinned: bool
    """Pass true to pin the topic; pass false to unpin it"""
