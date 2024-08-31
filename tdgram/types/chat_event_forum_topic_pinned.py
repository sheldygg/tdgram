from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ForumTopicInfo


@dataclass(kw_only=True)
class ChatEventForumTopicPinned(BaseType):
    """
    A pinned forum topic was changed
    """

    __type__: Literal["chatEventForumTopicPinned"] = "chatEventForumTopicPinned"

    old_topic_info: ForumTopicInfo | None = None
    """Information about the old pinned topic; may be null"""
    new_topic_info: ForumTopicInfo | None = None
    """Information about the new pinned topic; may be null"""
