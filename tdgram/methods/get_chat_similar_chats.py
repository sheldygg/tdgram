from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chats
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatSimilarChats(BaseMethod):
    """
    Returns a list of chats similar to the given chat
    """

    __type__: Literal["getChatSimilarChats"] = "getChatSimilarChats"
    __returning_type__ = Chats

    chat_id: int
    """Identifier of the target chat; must be an identifier of a channel chat"""
