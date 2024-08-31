from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatPhotoStickerTypeRegularOrMask(BaseType):
    """
    Information about the sticker, which was used to create the chat photo
    """

    __type__: Literal["chatPhotoStickerTypeRegularOrMask"] = "chatPhotoStickerTypeRegularOrMask"

    sticker_set_id: int
    """Sticker set identifier"""
    sticker_id: int
    """Identifier of the sticker in the set"""
