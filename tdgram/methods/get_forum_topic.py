from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ForumTopic
from .base import BaseMethod


@dataclass(kw_only=True)
class GetForumTopic(BaseMethod):
    """
    Returns information about a forum topic
    """

    __type__: Literal["getForumTopic"] = "getForumTopic"
    __returning_type__ = ForumTopic

    chat_id: int
    """Identifier of the chat"""
    message_thread_id: int
    """Message thread identifier of the forum topic"""
