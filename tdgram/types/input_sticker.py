from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import InputFile, MaskPosition, StickerFormat


@dataclass(kw_only=True)
class InputSticker(BaseType):
    """
    A sticker to be added to a sticker set
    """

    __type__: Literal["inputSticker"] = "inputSticker"

    sticker: InputFile
    """File with the sticker; must fit in a 512x512 square. For WEBP stickers the file must be in WEBP or PNG format, which will be converted to WEBP server-side."""
    format: StickerFormat
    """Format of the sticker"""
    emojis: str
    """String with 1-20 emoji corresponding to the sticker"""
    mask_position: MaskPosition | None = None
    """Position where the mask is placed; pass null if not specified"""
    keywords: list[str]
    """List of up to 20 keywords with total length up to 64 characters, which can be used to find the sticker"""
