from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatActiveStories
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatActiveStories(BaseMethod):
    """
    Returns the list of active stories posted by the given chat
    """

    __type__: Literal["getChatActiveStories"] = "getChatActiveStories"
    __returning_type__ = ChatActiveStories

    chat_id: int
    """Chat identifier"""
