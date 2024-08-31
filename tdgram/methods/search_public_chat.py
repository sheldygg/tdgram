from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Chat
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchPublicChat(BaseMethod):
    """
    Searches a public chat by its username. Currently, only private chats, supergroups and channels can be public. Returns the chat if found; otherwise, an error is returned
    """

    __type__: Literal["searchPublicChat"] = "searchPublicChat"
    __returning_type__ = Chat

    username: str
    """Username to be resolved"""
