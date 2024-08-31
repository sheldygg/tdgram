from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FoundMessages
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchOutgoingDocumentMessages(BaseMethod):
    """
    Searches for outgoing messages with content of the type messageDocument in all chats except secret chats. Returns the results in reverse chronological order
    """

    __type__: Literal["searchOutgoingDocumentMessages"] = "searchOutgoingDocumentMessages"
    __returning_type__ = FoundMessages

    query: str
    """Query to search for in document file name and message caption"""
    limit: int
    """The maximum number of messages to be returned; up to 100"""
