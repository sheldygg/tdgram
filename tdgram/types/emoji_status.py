from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class EmojiStatus(BaseType):
    """
    Describes a custom emoji to be shown instead of the Telegram Premium badge
    """

    __type__: Literal["emojiStatus"] = "emojiStatus"

    custom_emoji_id: int
    """Identifier of the custom emoji in stickerFormatTgs format"""
    expiration_date: int
    """Point in time (Unix timestamp) when the status will expire; 0 if never"""
