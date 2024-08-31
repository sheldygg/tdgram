from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RemoveRecentlyFoundChat(BaseMethod):
    """
    Removes a chat from the list of recently found chats
    """

    __type__: Literal["removeRecentlyFoundChat"] = "removeRecentlyFoundChat"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat to be removed"""
