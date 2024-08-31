from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ForumTopic


@dataclass(kw_only=True)
class ForumTopics(BaseType):
    """
    Describes a list of forum topics
    """

    __type__: Literal["forumTopics"] = "forumTopics"

    total_count: int
    """Approximate total number of forum topics found"""
    topics: list[ForumTopic]
    """List of forum topics"""
    next_offset_date: int
    """Offset date for the next getForumTopics request"""
    next_offset_message_id: int
    """Offset message identifier for the next getForumTopics request"""
    next_offset_message_thread_id: int
    """Offset message thread identifier for the next getForumTopics request"""
