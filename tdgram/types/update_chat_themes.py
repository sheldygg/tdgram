from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ChatTheme


@dataclass(kw_only=True)
class UpdateChatThemes(BaseType):
    """
    The list of available chat themes has changed
    """

    __type__: Literal["updateChatThemes"] = "updateChatThemes"

    chat_themes: list[ChatTheme]
    """The new list of chat themes"""
