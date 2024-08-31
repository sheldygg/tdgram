from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteSavedMessagesTopicMessagesByDate(BaseMethod):
    """
    Deletes all messages between the specified dates in a Saved Messages topic. Messages sent in the last 30 seconds will not be deleted
    """

    __type__: Literal["deleteSavedMessagesTopicMessagesByDate"] = (
        "deleteSavedMessagesTopicMessagesByDate"
    )
    __returning_type__ = Ok

    saved_messages_topic_id: int
    """Identifier of Saved Messages topic which messages will be deleted"""
    min_date: int
    """The minimum date of the messages to delete"""
    max_date: int
    """The maximum date of the messages to delete"""
