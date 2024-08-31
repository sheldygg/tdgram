from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chats
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchChatsOnServer(BaseMethod):
    """
    Searches for the specified query in the title and username of already known chats via request to the server. Returns chats in the order seen in the main chat list
    """

    __type__: Literal["searchChatsOnServer"] = "searchChatsOnServer"
    __returning_type__ = Chats

    query: str
    """Query to search for"""
    limit: int
    """The maximum number of chats to be returned"""
