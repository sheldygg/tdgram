from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class MessageChatSetTheme(BaseType):
    """
    A theme in the chat has been changed
    """

    __type__: Literal["messageChatSetTheme"] = "messageChatSetTheme"

    theme_name: str | None = None
    """If non-empty, name of a new theme, set for the chat. Otherwise, chat theme was reset to the default one"""
