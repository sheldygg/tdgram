from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ReadAllChatMentions(BaseMethod):
    """
    Marks all mentions in a chat as read
    """

    __type__: Literal["readAllChatMentions"] = "readAllChatMentions"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
