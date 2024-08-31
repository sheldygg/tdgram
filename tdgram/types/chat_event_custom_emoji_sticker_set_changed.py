from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatEventCustomEmojiStickerSetChanged(BaseType):
    """
    The supergroup sticker set with allowed custom emoji was changed
    """

    __type__: Literal["chatEventCustomEmojiStickerSetChanged"] = (
        "chatEventCustomEmojiStickerSetChanged"
    )

    old_sticker_set_id: int
    """Previous identifier of the chat sticker set; 0 if none"""
    new_sticker_set_id: int
    """New identifier of the chat sticker set; 0 if none"""
