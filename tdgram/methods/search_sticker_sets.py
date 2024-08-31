from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import StickerSets, StickerType
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchStickerSets(BaseMethod):
    """
    Searches for sticker sets by looking for specified query in their title and name. Excludes installed sticker sets from the results
    """

    __type__: Literal["searchStickerSets"] = "searchStickerSets"
    __returning_type__ = StickerSets

    sticker_type: StickerType
    """Type of the sticker sets to return"""
    query: str
    """Query to search for"""
