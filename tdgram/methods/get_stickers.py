from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Stickers, StickerType
from .base import BaseMethod


@dataclass(kw_only=True)
class GetStickers(BaseMethod):
    """
    Returns stickers from the installed sticker sets that correspond to any of the given emoji or can be found by sticker-specific keywords. If the query is non-empty, then favorite, recently used or trending stickers may also be returned
    """

    __type__: Literal["getStickers"] = "getStickers"
    __returning_type__ = Stickers

    sticker_type: StickerType
    """Type of the stickers to return"""
    query: str
    """Search query; a space-separated list of emojis or a keyword prefix. If empty, returns all known installed stickers"""
    limit: int
    """The maximum number of stickers to be returned"""
    chat_id: int
    """Chat identifier for which to return stickers. Available custom emoji stickers may be different for different chats"""
