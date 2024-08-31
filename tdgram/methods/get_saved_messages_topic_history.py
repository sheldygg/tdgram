from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Messages
from .base import BaseMethod


@dataclass(kw_only=True)
class GetSavedMessagesTopicHistory(BaseMethod):
    """
    Returns messages in a Saved Messages topic. The messages are returned in reverse chronological order (i.e., in order of decreasing message_id)
    """

    __type__: Literal["getSavedMessagesTopicHistory"] = "getSavedMessagesTopicHistory"
    __returning_type__ = Messages

    saved_messages_topic_id: int
    """Identifier of Saved Messages topic which messages will be fetched"""
    from_message_id: int
    """Identifier of the message starting from which messages must be fetched; use 0 to get results from the last message"""
    offset: int
    """Specify 0 to get results from exactly the message from_message_id or a negative offset up to 99 to get additionally some newer messages"""
    limit: int
    """The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than or equal to -offset."""
