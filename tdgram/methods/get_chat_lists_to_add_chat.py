from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatLists
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatListsToAddChat(BaseMethod):
    """
    Returns chat lists to which the chat can be added. This is an offline request
    """

    __type__: Literal["getChatListsToAddChat"] = "getChatListsToAddChat"
    __returning_type__ = ChatLists

    chat_id: int
    """Chat identifier"""
