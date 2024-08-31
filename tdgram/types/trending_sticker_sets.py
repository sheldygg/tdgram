from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StickerSetInfo


@dataclass(kw_only=True)
class TrendingStickerSets(BaseType):
    """
    Represents a list of trending sticker sets
    """

    __type__: Literal["trendingStickerSets"] = "trendingStickerSets"

    total_count: int
    """Approximate total number of trending sticker sets"""
    sets: list[StickerSetInfo]
    """List of trending sticker sets"""
    is_premium: bool
    """True, if the list contains sticker sets with premium stickers"""
