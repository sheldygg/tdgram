from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import StickerSet
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchStickerSet(BaseMethod):
    """
    Searches for a sticker set by its name
    """

    __type__: Literal["searchStickerSet"] = "searchStickerSet"
    __returning_type__ = StickerSet

    name: str
    """Name of the sticker set"""
