from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ForumTopicInfo


@dataclass(kw_only=True)
class ChatEventForumTopicToggleIsHidden(BaseType):
    """
    The General forum topic was hidden or unhidden
    """

    __type__: Literal["chatEventForumTopicToggleIsHidden"] = "chatEventForumTopicToggleIsHidden"

    topic_info: ForumTopicInfo
    """New information about the topic"""
