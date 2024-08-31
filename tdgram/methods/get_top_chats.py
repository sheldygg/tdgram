from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chats, TopChatCategory
from .base import BaseMethod


@dataclass(kw_only=True)
class GetTopChats(BaseMethod):
    """
    Returns a list of frequently used chats
    """

    __type__: Literal["getTopChats"] = "getTopChats"
    __returning_type__ = Chats

    category: TopChatCategory
    """Category of chats to be returned"""
    limit: int
    """The maximum number of chats to be returned; up to 30"""
