from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Count
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatSimilarChatCount(BaseMethod):
    """
    Returns approximate number of chats similar to the given chat
    """

    __type__: Literal["getChatSimilarChatCount"] = "getChatSimilarChatCount"
    __returning_type__ = Count

    chat_id: int
    """Identifier of the target chat; must be an identifier of a channel chat"""
    return_local: bool
    """Pass true to get the number of chats without sending network requests, or -1 if the number of chats is unknown locally"""
