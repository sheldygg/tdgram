from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputSticker, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class AddStickerToSet(BaseMethod):
    """
    Adds a new sticker to a set
    """

    __type__: Literal["addStickerToSet"] = "addStickerToSet"
    __returning_type__ = Ok

    user_id: int
    """Sticker set owner; ignored for regular users"""
    name: str
    """Sticker set name. The sticker set must be owned by the current user, and contain less than 200 stickers for custom emoji sticker sets and less than 120 otherwise"""
    sticker: InputSticker
    """Sticker to add to the set"""
