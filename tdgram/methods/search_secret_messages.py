from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FoundMessages, SearchMessagesFilter
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchSecretMessages(BaseMethod):
    """
    Searches for messages in secret chats. Returns the results in reverse chronological order. For optimal performance, the number of returned messages is chosen by TDLib
    """

    __type__: Literal["searchSecretMessages"] = "searchSecretMessages"
    __returning_type__ = FoundMessages

    chat_id: int
    """Identifier of the chat in which to search. Specify 0 to search in all secret chats"""
    query: str
    """Query to search for. If empty, searchChatMessages must be used instead"""
    offset: str
    """Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results"""
    limit: int
    """The maximum number of messages to be returned; up to 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit"""
    filter: SearchMessagesFilter | None = None
    """Additional filter for messages to search; pass null to search for all messages"""
