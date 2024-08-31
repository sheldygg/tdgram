from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class EmojiCategoryTypeChatPhoto(BaseType):
    """
    The category must be used for chat photo emoji selection
    """

    __type__: Literal["emojiCategoryTypeChatPhoto"] = "emojiCategoryTypeChatPhoto"
