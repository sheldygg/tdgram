from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ForumTopicInfo


@dataclass(kw_only=True)
class ChatEventForumTopicEdited(BaseType):
    """
    A forum topic was edited
    """

    __type__: Literal["chatEventForumTopicEdited"] = "chatEventForumTopicEdited"

    old_topic_info: ForumTopicInfo
    """Old information about the topic"""
    new_topic_info: ForumTopicInfo
    """New information about the topic"""
