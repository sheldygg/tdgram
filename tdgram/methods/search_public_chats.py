from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chats
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchPublicChats(BaseMethod):
    """
    Searches public chats by looking for specified query in their username and title. Currently, only private chats, supergroups and channels can be public. Returns a meaningful number of results.
    """

    __type__: Literal["searchPublicChats"] = "searchPublicChats"
    __returning_type__ = Chats

    query: str
    """Query to search for"""
