from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputSticker, StickerSet, StickerType
from .base import BaseMethod


@dataclass(kw_only=True)
class CreateNewStickerSet(BaseMethod):
    """
    Creates a new sticker set. Returns the newly created sticker set
    """

    __type__: Literal["createNewStickerSet"] = "createNewStickerSet"
    __returning_type__ = StickerSet

    user_id: int
    """Sticker set owner; ignored for regular users"""
    title: str
    """Sticker set title; 1-64 characters"""
    name: str
    """Sticker set name. Can contain only English letters, digits and underscores. Must end with *'_by_<bot username>'* (*<bot_username>* is case insensitive) for bots; 0-64 characters."""
    sticker_type: StickerType
    """Type of the stickers in the set"""
    needs_repainting: bool
    """Pass true if stickers in the sticker set must be repainted; for custom emoji sticker sets only"""
    stickers: list[InputSticker]
    """List of stickers to be added to the set; 1-200 stickers for custom emoji sticker sets, and 1-120 stickers otherwise. For TGS stickers, uploadStickerFile must be used before the sticker is shown"""
    source: str | None = None
    """Source of the sticker set; may be empty if unknown"""
