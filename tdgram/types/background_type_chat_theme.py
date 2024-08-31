from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class BackgroundTypeChatTheme(BaseType):
    """
    A background from a chat theme; can be used only as a chat background in channels
    """

    __type__: Literal["backgroundTypeChatTheme"] = "backgroundTypeChatTheme"

    theme_name: str
    """Name of the chat theme"""
