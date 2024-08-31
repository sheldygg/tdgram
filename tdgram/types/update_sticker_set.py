from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StickerSet


@dataclass(kw_only=True)
class UpdateStickerSet(BaseType):
    """
    A sticker set has changed
    """

    __type__: Literal["updateStickerSet"] = "updateStickerSet"

    sticker_set: StickerSet
    """The sticker set"""
