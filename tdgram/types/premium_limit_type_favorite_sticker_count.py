from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class PremiumLimitTypeFavoriteStickerCount(BaseType):
    """
    The maximum number of favorite stickers
    """

    __type__: Literal["premiumLimitTypeFavoriteStickerCount"] = (
        "premiumLimitTypeFavoriteStickerCount"
    )
