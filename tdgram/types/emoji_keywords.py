from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import EmojiKeyword


@dataclass(kw_only=True)
class EmojiKeywords(BaseType):
    """
    Represents a list of emojis with their keywords
    """

    __type__: Literal["emojiKeywords"] = "emojiKeywords"

    emoji_keywords: list[EmojiKeyword]
    """List of emojis with their keywords"""
