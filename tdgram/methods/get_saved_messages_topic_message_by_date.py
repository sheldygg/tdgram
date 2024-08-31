from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Message
from .base import BaseMethod


@dataclass(kw_only=True)
class GetSavedMessagesTopicMessageByDate(BaseMethod):
    """
    Returns the last message sent in a Saved Messages topic no later than the specified date
    """

    __type__: Literal["getSavedMessagesTopicMessageByDate"] = "getSavedMessagesTopicMessageByDate"
    __returning_type__ = Message

    saved_messages_topic_id: int
    """Identifier of Saved Messages topic which message will be returned"""
    date: int
    """Point in time (Unix timestamp) relative to which to search for messages"""
