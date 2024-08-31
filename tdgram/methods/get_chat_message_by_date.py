from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Message
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatMessageByDate(BaseMethod):
    """
    Returns the last message sent in a chat no later than the specified date
    """

    __type__: Literal["getChatMessageByDate"] = "getChatMessageByDate"
    __returning_type__ = Message

    chat_id: int
    """Chat identifier"""
    date: int
    """Point in time (Unix timestamp) relative to which to search for messages"""
