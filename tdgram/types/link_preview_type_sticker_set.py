from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import Sticker


@dataclass(kw_only=True)
class LinkPreviewTypeStickerSet(BaseType):
    """
    The link is a link to a sticker set
    """

    __type__: Literal["linkPreviewTypeStickerSet"] = "linkPreviewTypeStickerSet"

    stickers: list[Sticker]
    """Up to 4 stickers from the sticker set"""
