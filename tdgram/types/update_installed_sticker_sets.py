from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import StickerType


@dataclass(kw_only=True)
class UpdateInstalledStickerSets(BaseType):
    """
    The list of installed sticker sets was updated
    """

    __type__: Literal["updateInstalledStickerSets"] = "updateInstalledStickerSets"

    sticker_type: StickerType
    """Type of the affected stickers"""
    sticker_set_ids: list[int]
    """The new list of installed ordinary sticker sets"""
