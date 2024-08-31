from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import ClosedVectorPath, Sticker, StickerType, Thumbnail


@dataclass(kw_only=True)
class StickerSetInfo(BaseType):
    """
    Represents short information about a sticker set
    """

    __type__: Literal["stickerSetInfo"] = "stickerSetInfo"

    id: int
    """Identifier of the sticker set"""
    title: str
    """Title of the sticker set"""
    name: str
    """Name of the sticker set"""
    thumbnail: Thumbnail | None = None
    """Sticker set thumbnail in WEBP, TGS, or WEBM format with width and height 100; may be null. The file can be downloaded only before the thumbnail is changed"""
    thumbnail_outline: list[ClosedVectorPath] | None = None
    """Sticker set thumbnail's outline represented as a list of closed vector paths; may be empty. The coordinate system origin is in the upper-left corner"""
    is_owned: bool
    """True, if the sticker set is owned by the current user"""
    is_installed: bool
    """True, if the sticker set has been installed by the current user"""
    is_archived: bool
    """True, if the sticker set has been archived. A sticker set can't be installed and archived simultaneously"""
    is_official: bool
    """True, if the sticker set is official"""
    sticker_type: StickerType
    """Type of the stickers in the set"""
    needs_repainting: bool
    """True, if stickers in the sticker set are custom emoji that must be repainted; for custom emoji sticker sets only"""
    is_allowed_as_chat_emoji_status: bool
    """True, if stickers in the sticker set are custom emoji that can be used as chat emoji status; for custom emoji sticker sets only"""
    is_viewed: bool
    """True for already viewed trending sticker sets"""
    size: int
    """Total number of stickers in the set"""
    covers: list[Sticker]
    """Up to the first 5 stickers from the set, depending on the context. If the application needs more stickers the full sticker set needs to be requested"""
