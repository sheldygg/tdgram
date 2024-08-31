from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import EmojiCategorySource, Sticker


@dataclass(kw_only=True)
class EmojiCategory(BaseType):
    """
    Describes an emoji category
    """

    __type__: Literal["emojiCategory"] = "emojiCategory"

    name: str
    """Name of the category"""
    icon: Sticker
    """Custom emoji sticker, which represents icon of the category"""
    source: EmojiCategorySource
    """Source of stickers for the emoji category"""
    is_greeting: bool
    """True, if the category must be shown first when choosing a sticker for the start page"""
