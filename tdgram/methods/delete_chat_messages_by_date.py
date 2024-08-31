from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteChatMessagesByDate(BaseMethod):
    """
    Deletes all messages between the specified dates in a chat. Supported only for private chats and basic groups. Messages sent in the last 30 seconds will not be deleted
    """

    __type__: Literal["deleteChatMessagesByDate"] = "deleteChatMessagesByDate"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    min_date: int
    """The minimum date of the messages to delete"""
    max_date: int
    """The maximum date of the messages to delete"""
    revoke: bool
    """Pass true to delete chat messages for all users; private chats only"""
