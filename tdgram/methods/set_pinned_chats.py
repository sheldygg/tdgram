from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatList, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetPinnedChats(BaseMethod):
    """
    Changes the order of pinned chats
    """

    __type__: Literal["setPinnedChats"] = "setPinnedChats"
    __returning_type__ = Ok

    chat_list: ChatList
    """Chat list in which to change the order of pinned chats"""
    chat_ids: list[int]
    """The new list of pinned chats"""
