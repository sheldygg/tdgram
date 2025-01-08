from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import File, StickerFormat, StickerFullType, Thumbnail


@dataclass(kw_only=True)
class Sticker(BaseType):
    """
    Describes a sticker
    """

    __type__: Literal["sticker"] = "sticker"

    id: int
    """Unique sticker identifier within the set; 0 if none"""
    set_id: int
    """Identifier of the sticker set to which the sticker belongs; 0 if none"""
    width: int
    """Sticker width; as defined by the sender"""
    height: int
    """Sticker height; as defined by the sender"""
    emoji: str
    """Emoji corresponding to the sticker"""
    format: StickerFormat
    """Sticker format"""
    full_type: StickerFullType
    """Sticker's full type"""
    thumbnail: Thumbnail | None = None
    """Sticker thumbnail in WEBP or JPEG format; may be null"""
    sticker: File
    """File containing the sticker"""
