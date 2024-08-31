from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Emojis, StickerType
from .base import BaseMethod


@dataclass(kw_only=True)
class GetAllStickerEmojis(BaseMethod):
    """
    Returns unique emoji that correspond to stickers to be found by the getStickers(sticker_type, query, 1000000, chat_id)
    """

    __type__: Literal["getAllStickerEmojis"] = "getAllStickerEmojis"
    __returning_type__ = Emojis

    sticker_type: StickerType
    """Type of the stickers to search for"""
    query: str
    """Search query"""
    chat_id: int
    """Chat identifier for which to find stickers"""
    return_only_main_emoji: bool
    """Pass true if only main emoji for each found sticker must be included in the result"""
