from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import StickerSets
from .base import BaseMethod


@dataclass(kw_only=True)
class GetAttachedStickerSets(BaseMethod):
    """
    Returns a list of sticker sets attached to a file, including regular, mask, and emoji sticker sets. Currently, only animations, photos, and videos can have attached sticker sets
    """

    __type__: Literal["getAttachedStickerSets"] = "getAttachedStickerSets"
    __returning_type__ = StickerSets

    file_id: int
    """File identifier"""
