from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FoundStories
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchPublicStoriesByTag(BaseMethod):
    """
    Searches for public stories containing the given hashtag or cashtag. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit
    """

    __type__: Literal["searchPublicStoriesByTag"] = "searchPublicStoriesByTag"
    __returning_type__ = FoundStories

    story_sender_chat_id: int
    """Identifier of the chat that posted the stories to search for; pass 0 to search stories in all chats"""
    tag: str
    """Hashtag or cashtag to search for"""
    offset: str
    """Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results"""
    limit: int
    """The maximum number of stories to be returned; up to 100. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit"""
