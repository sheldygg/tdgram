from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ToggleForumTopicIsClosed(BaseMethod):
    """
    Toggles whether a topic is closed in a forum supergroup chat; requires can_manage_topics right in the supergroup unless the user is creator of the topic
    """

    __type__: Literal["toggleForumTopicIsClosed"] = "toggleForumTopicIsClosed"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat"""
    message_thread_id: int
    """Message thread identifier of the forum topic"""
    is_closed: bool
    """Pass true to close the topic; pass false to reopen it"""
