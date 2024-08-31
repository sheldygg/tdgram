from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteForumTopic(BaseMethod):
    """
    Deletes all messages in a forum topic; requires can_delete_messages administrator right in the supergroup unless the user is creator of the topic, the topic has no messages from other users and has at most 11 messages
    """

    __type__: Literal["deleteForumTopic"] = "deleteForumTopic"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat"""
    message_thread_id: int
    """Message thread identifier of the forum topic"""
