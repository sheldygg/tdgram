from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import ChatAdministrators
from .base import BaseMethod


@dataclass(kw_only=True)
class GetChatAdministrators(BaseMethod):
    """
    Returns a list of administrators of the chat with their custom titles
    """

    __type__: Literal["getChatAdministrators"] = "getChatAdministrators"
    __returning_type__ = ChatAdministrators

    chat_id: int
    """Chat identifier"""
