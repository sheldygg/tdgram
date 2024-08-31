from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetChatTheme(BaseMethod):
    """
    Changes the chat theme. Supported only in private and secret chats
    """

    __type__: Literal["setChatTheme"] = "setChatTheme"
    __returning_type__ = Ok

    chat_id: int
    """Chat identifier"""
    theme_name: str
    """Name of the new chat theme; pass an empty string to return the default theme"""
