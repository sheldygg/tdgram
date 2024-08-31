from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class EmojiCategoryTypeRegularStickers(BaseType):
    """
    The category must be used by default for regular sticker selection. It may contain greeting emoji category and premium stickers
    """

    __type__: Literal["emojiCategoryTypeRegularStickers"] = "emojiCategoryTypeRegularStickers"
