from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class DeleteSavedMessagesTopicHistory(BaseMethod):
    """
    Deletes all messages in a Saved Messages topic
    """

    __type__: Literal["deleteSavedMessagesTopicHistory"] = "deleteSavedMessagesTopicHistory"
    __returning_type__ = Ok

    saved_messages_topic_id: int
    """Identifier of Saved Messages topic which messages will be deleted"""
