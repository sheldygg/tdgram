from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateChatTheme(BaseType):
    """
    The chat theme was changed
    """

    __type__: Literal["updateChatTheme"] = "updateChatTheme"

    chat_id: int
    """Chat identifier"""
    theme_name: str | None = None
    """The new name of the chat theme; may be empty if theme was reset to default"""
