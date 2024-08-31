from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ForumTopicInfo


@dataclass(kw_only=True)
class ChatEventForumTopicCreated(BaseType):
    """
    A new forum topic was created
    """

    __type__: Literal["chatEventForumTopicCreated"] = "chatEventForumTopicCreated"

    topic_info: ForumTopicInfo
    """Information about the topic"""
