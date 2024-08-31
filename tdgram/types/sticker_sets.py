from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StickerSetInfo


@dataclass(kw_only=True)
class StickerSets(BaseType):
    """
    Represents a list of sticker sets
    """

    __type__: Literal["stickerSets"] = "stickerSets"

    total_count: int
    """Approximate total number of sticker sets found"""
    sets: list[StickerSetInfo]
    """List of sticker sets"""
