from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class AddRecentlyFoundChat(BaseMethod):
    """
    Adds a chat to the list of recently found chats. The chat is added to the beginning of the list. If the chat is already in the list, it will be removed from the list first
    """

    __type__: Literal["addRecentlyFoundChat"] = "addRecentlyFoundChat"
    __returning_type__ = Ok

    chat_id: int
    """Identifier of the chat to add"""
