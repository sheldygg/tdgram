from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class EmojiCategoryTypeEmojiStatus(BaseType):
    """
    The category must be used for emoji status selection
    """

    __type__: Literal["emojiCategoryTypeEmojiStatus"] = "emojiCategoryTypeEmojiStatus"
