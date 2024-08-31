from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chats
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchRecentlyFoundChats(BaseMethod):
    """
    Searches for the specified query in the title and username of up to 50 recently found chats; this is an offline request
    """

    __type__: Literal["searchRecentlyFoundChats"] = "searchRecentlyFoundChats"
    __returning_type__ = Chats

    query: str
    """Query to search for"""
    limit: int
    """The maximum number of chats to be returned"""
