from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import StickerSets, StickerType
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchInstalledStickerSets(BaseMethod):
    """
    Searches for installed sticker sets by looking for specified query in their title and name
    """

    __type__: Literal["searchInstalledStickerSets"] = "searchInstalledStickerSets"
    __returning_type__ = StickerSets

    sticker_type: StickerType
    """Type of the sticker sets to search for"""
    query: str
    """Query to search for"""
    limit: int
    """The maximum number of sticker sets to return"""
