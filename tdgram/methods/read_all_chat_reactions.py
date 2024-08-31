from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ReadAllChatReactions(BaseMethod):
    """
    Marks all reactions in a chat or a forum topic as read
    """

    __type__: Literal["readAllChatReactions"] = "readAllChatReactions"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
