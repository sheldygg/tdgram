from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import StickerSet
from .base import BaseMethod


@dataclass(kw_only=True)
class GetStickerSet(BaseMethod):
    """
    Returns information about a sticker set by its identifier
    """

    __type__: Literal["getStickerSet"] = "getStickerSet"
    __returning_type__ = StickerSet

    set_id: int
    """Identifier of the sticker set"""
