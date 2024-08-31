from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class EmojiCategorySourceSearch(BaseType):
    """
    The category contains a list of similar emoji to search for in getStickers and searchStickers for stickers,
    """

    __type__: Literal["emojiCategorySourceSearch"] = "emojiCategorySourceSearch"

    emojis: list[str]
    """List of emojis to search for"""
