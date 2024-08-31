from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class EmojiCategorySourcePremium(BaseType):
    """
    The category contains premium stickers that must be found by getPremiumStickers
    """

    __type__: Literal["emojiCategorySourcePremium"] = "emojiCategorySourcePremium"
