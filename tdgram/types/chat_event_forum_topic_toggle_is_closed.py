from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ForumTopicInfo


@dataclass(kw_only=True)
class ChatEventForumTopicToggleIsClosed(BaseType):
    """
    A forum topic was closed or reopened
    """

    __type__: Literal["chatEventForumTopicToggleIsClosed"] = "chatEventForumTopicToggleIsClosed"

    topic_info: ForumTopicInfo
    """New information about the topic"""
