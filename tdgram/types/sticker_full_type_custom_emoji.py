from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StickerFullTypeCustomEmoji(BaseType):
    """
    The sticker is a custom emoji to be used inside message text and caption. Currently, only Telegram Premium users can use custom emoji
    """

    __type__: Literal["stickerFullTypeCustomEmoji"] = "stickerFullTypeCustomEmoji"

    custom_emoji_id: int
    """Identifier of the custom emoji"""
    needs_repainting: bool
    """True, if the sticker must be repainted to a text color in messages, the color of the Telegram Premium badge in emoji status, white color on chat photos, or another appropriate color in other places"""
