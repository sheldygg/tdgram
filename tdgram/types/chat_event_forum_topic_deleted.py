from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ForumTopicInfo


@dataclass(kw_only=True)
class ChatEventForumTopicDeleted(BaseType):
    """
    A forum topic was deleted
    """

    __type__: Literal["chatEventForumTopicDeleted"] = "chatEventForumTopicDeleted"

    topic_info: ForumTopicInfo
    """Information about the topic"""
