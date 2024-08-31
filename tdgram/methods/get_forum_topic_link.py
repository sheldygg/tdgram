from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import MessageLink
from .base import BaseMethod


@dataclass(kw_only=True)
class GetForumTopicLink(BaseMethod):
    """
    Returns an HTTPS link to a topic in a forum chat. This is an offline request
    """

    __type__: Literal["getForumTopicLink"] = "getForumTopicLink"
    __returning_type__ = MessageLink

    chat_id: int
    """Identifier of the chat"""
    message_thread_id: int
    """Message thread identifier of the forum topic"""
