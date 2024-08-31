from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import StickerType, TrendingStickerSets
from .base import BaseMethod


@dataclass(kw_only=True)
class GetTrendingStickerSets(BaseMethod):
    """
    Returns a list of trending sticker sets. For optimal performance, the number of returned sticker sets is chosen by TDLib
    """

    __type__: Literal["getTrendingStickerSets"] = "getTrendingStickerSets"
    __returning_type__ = TrendingStickerSets

    sticker_type: StickerType
    """Type of the sticker sets to return"""
    offset: int
    """The offset from which to return the sticker sets; must be non-negative"""
    limit: int
    """The maximum number of sticker sets to be returned; up to 100. For optimal performance, the number of returned sticker sets is chosen by TDLib and can be smaller than the specified limit, even if the end of the list has not been reached"""
