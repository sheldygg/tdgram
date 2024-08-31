from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputFile, InputSticker, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class ReplaceStickerInSet(BaseMethod):
    """
    Replaces existing sticker in a set. The function is equivalent to removeStickerFromSet, then addStickerToSet, then setStickerPositionInSet
    """

    __type__: Literal["replaceStickerInSet"] = "replaceStickerInSet"
    __returning_type__ = Ok

    user_id: int
    """Sticker set owner; ignored for regular users"""
    name: str
    """Sticker set name. The sticker set must be owned by the current user"""
    old_sticker: InputFile
    """Sticker to remove from the set"""
    new_sticker: InputSticker
    """Sticker to add to the set"""
