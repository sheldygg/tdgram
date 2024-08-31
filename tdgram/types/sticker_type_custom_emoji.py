from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StickerTypeCustomEmoji(BaseType):
    """
    The sticker is a custom emoji to be used inside message text and caption
    """

    __type__: Literal["stickerTypeCustomEmoji"] = "stickerTypeCustomEmoji"
