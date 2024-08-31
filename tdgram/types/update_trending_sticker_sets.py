from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StickerType, TrendingStickerSets


@dataclass(kw_only=True)
class UpdateTrendingStickerSets(BaseType):
    """
    The list of trending sticker sets was updated or some of them were viewed
    """

    __type__: Literal["updateTrendingStickerSets"] = "updateTrendingStickerSets"

    sticker_type: StickerType
    """Type of the affected stickers"""
    sticker_sets: TrendingStickerSets
    """The prefix of the list of trending sticker sets with the newest trending sticker sets"""
