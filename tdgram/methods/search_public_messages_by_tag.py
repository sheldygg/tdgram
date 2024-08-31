from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import FoundMessages
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchPublicMessagesByTag(BaseMethod):
    """
    Searches for public channel posts containing the given hashtag or cashtag. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
    """

    __type__: Literal["searchPublicMessagesByTag"] = "searchPublicMessagesByTag"
    __returning_type__ = FoundMessages

    tag: str
    """Hashtag or cashtag to search for"""
    offset: str
    """Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results"""
    limit: int
    """The maximum number of messages to be returned; up to 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit"""
