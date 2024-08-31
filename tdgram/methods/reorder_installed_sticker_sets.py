from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok, StickerType
from .base import BaseMethod


@dataclass(kw_only=True)
class ReorderInstalledStickerSets(BaseMethod):
    """
    Changes the order of installed sticker sets
    """

    __type__: Literal["reorderInstalledStickerSets"] = "reorderInstalledStickerSets"
    __returning_type__ = Ok

    sticker_type: StickerType
    """Type of the sticker sets to reorder"""
    sticker_set_ids: list[int]
    """Identifiers of installed sticker sets in the new correct order"""
