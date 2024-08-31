from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetCustomEmojiStickerSetThumbnail(BaseMethod):
    """
    Sets a custom emoji sticker set thumbnail
    """

    __type__: Literal["setCustomEmojiStickerSetThumbnail"] = "setCustomEmojiStickerSetThumbnail"
    __returning_type__ = Ok

    name: str
    """Sticker set name. The sticker set must be owned by the current user"""
    custom_emoji_id: int
    """Identifier of the custom emoji from the sticker set, which will be set as sticker set thumbnail; pass 0 to remove the sticker set thumbnail"""
