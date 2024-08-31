from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputFile, Ok, StickerFormat
from .base import BaseMethod


@dataclass(kw_only=True)
class SetStickerSetThumbnail(BaseMethod):
    """
    Sets a sticker set thumbnail
    """

    __type__: Literal["setStickerSetThumbnail"] = "setStickerSetThumbnail"
    __returning_type__ = Ok

    user_id: int
    """Sticker set owner; ignored for regular users"""
    name: str
    """Sticker set name. The sticker set must be owned by the current user"""
    thumbnail: InputFile | None = None
    """Thumbnail to set; pass null to remove the sticker set thumbnail"""
    format: StickerFormat | None = None
    """Format of the thumbnail; pass null if thumbnail is removed"""
