from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import StickerSets
from .base import BaseMethod


@dataclass(kw_only=True)
class GetOwnedStickerSets(BaseMethod):
    """
    Returns sticker sets owned by the current user
    """

    __type__: Literal["getOwnedStickerSets"] = "getOwnedStickerSets"
    __returning_type__ = StickerSets

    offset_sticker_set_id: int
    """Identifier of the sticker set from which to return owned sticker sets; use 0 to get results from the beginning"""
    limit: int
    """The maximum number of sticker sets to be returned; must be positive and can't be greater than 100. For optimal performance, the number of returned objects is chosen by TDLib and can be smaller than the specified limit"""
