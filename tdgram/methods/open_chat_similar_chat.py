from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class OpenChatSimilarChat(BaseMethod):
    """
    Informs TDLib that a chat was opened from the list of similar chats. The method is independent of openChat and closeChat methods
    """

    __type__: Literal["openChatSimilarChat"] = "openChatSimilarChat"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the original chat, which similar chats were requested"""
    opened_chat_id: int
    """Identifier of the opened chat"""
