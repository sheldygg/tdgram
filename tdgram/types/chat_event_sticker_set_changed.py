from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ChatEventStickerSetChanged(BaseType):
    """
    The supergroup sticker set was changed
    """

    __type__: Literal["chatEventStickerSetChanged"] = "chatEventStickerSetChanged"

    old_sticker_set_id: int
    """Previous identifier of the chat sticker set; 0 if none"""
    new_sticker_set_id: int
    """New identifier of the chat sticker set; 0 if none"""
