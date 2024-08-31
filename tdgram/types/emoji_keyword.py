from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class EmojiKeyword(BaseType):
    """
    Represents an emoji with its keyword
    """

    __type__: Literal["emojiKeyword"] = "emojiKeyword"

    emoji: str
    """The emoji"""
    keyword: str
    """The keyword"""
