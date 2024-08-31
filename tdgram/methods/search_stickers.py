from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Stickers, StickerType
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchStickers(BaseMethod):
    """
    Searches for stickers from public sticker sets that correspond to any of the given emoji
    """

    __type__: Literal["searchStickers"] = "searchStickers"
    __returning_type__ = Stickers

    sticker_type: StickerType
    """Type of the stickers to return"""
    emojis: str
    """Space-separated list of emojis to search for; must be non-empty"""
    limit: int
    """The maximum number of stickers to be returned; 0-100"""
