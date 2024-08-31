from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import EmojiCategory


@dataclass(kw_only=True)
class EmojiCategories(BaseType):
    """
    Represents a list of emoji categories
    """

    __type__: Literal["emojiCategories"] = "emojiCategories"

    categories: list[EmojiCategory]
    """List of categories"""
