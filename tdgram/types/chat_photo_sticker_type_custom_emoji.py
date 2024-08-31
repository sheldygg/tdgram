from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatPhotoStickerTypeCustomEmoji(BaseType):
    """
    Information about the custom emoji, which was used to create the chat photo
    """

    __type__: Literal["chatPhotoStickerTypeCustomEmoji"] = "chatPhotoStickerTypeCustomEmoji"

    custom_emoji_id: int
    """Identifier of the custom emoji"""
