from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import StickerSets, StickerType
from .base import BaseMethod


@dataclass(kw_only=True)
class GetArchivedStickerSets(BaseMethod):
    """
    Returns a list of archived sticker sets
    """

    __type__: Literal["getArchivedStickerSets"] = "getArchivedStickerSets"
    __returning_type__ = StickerSets

    sticker_type: StickerType
    """Type of the sticker sets to return"""
    offset_sticker_set_id: int
    """Identifier of the sticker set from which to return the result; use 0 to get results from the beginning"""
    limit: int
    """The maximum number of sticker sets to return; up to 100"""
