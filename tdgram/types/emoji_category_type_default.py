from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class EmojiCategoryTypeDefault(BaseType):
    """
    The category must be used by default (e.g., for custom emoji or animation search)
    """

    __type__: Literal["emojiCategoryTypeDefault"] = "emojiCategoryTypeDefault"
