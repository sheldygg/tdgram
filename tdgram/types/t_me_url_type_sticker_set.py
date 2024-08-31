from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class TMeUrlTypeStickerSet(BaseType):
    """
    A URL linking to a sticker set
    """

    __type__: Literal["tMeUrlTypeStickerSet"] = "tMeUrlTypeStickerSet"

    sticker_set_id: int
    """Identifier of the sticker set"""
