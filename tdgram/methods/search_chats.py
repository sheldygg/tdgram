from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chats
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchChats(BaseMethod):
    """
    Searches for the specified query in the title and username of already known chats; this is an offline request. Returns chats in the order seen in the main chat list
    """

    __type__: Literal["searchChats"] = "searchChats"
    __returning_type__ = Chats

    query: str
    """Query to search for. If the query is empty, returns up to 50 recently found chats"""
    limit: int
    """The maximum number of chats to be returned"""
