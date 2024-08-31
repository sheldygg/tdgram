from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PushMessageContentChatSetTheme(BaseType):
    """
    A chat theme was edited
    """

    __type__: Literal["pushMessageContentChatSetTheme"] = "pushMessageContentChatSetTheme"

    theme_name: str | None = None
    """If non-empty, name of a new theme, set for the chat. Otherwise, the chat theme was reset to the default one"""
