from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import StickerSets, StickerType
from .base import BaseMethod


@dataclass(kw_only=True)
class GetInstalledStickerSets(BaseMethod):
    """
    Returns a list of installed sticker sets
    """

    __type__: Literal["getInstalledStickerSets"] = "getInstalledStickerSets"
    __returning_type__ = StickerSets

    sticker_type: StickerType
    """Type of the sticker sets to return"""
