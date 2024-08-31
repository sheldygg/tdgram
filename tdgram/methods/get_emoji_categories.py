from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import EmojiCategories, EmojiCategoryType
from .base import BaseMethod


@dataclass(kw_only=True)
class GetEmojiCategories(BaseMethod):
    """
    Returns available emoji categories
    """

    __type__: Literal["getEmojiCategories"] = "getEmojiCategories"
    __returning_type__ = EmojiCategories

    type: EmojiCategoryType | None = None
    """Type of emoji categories to return; pass null to get default emoji categories"""
