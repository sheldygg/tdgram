from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Stickers, StickerType
from .base import BaseMethod


@dataclass(kw_only=True)
class SearchStickers(BaseMethod):
    """
    Searches for stickers from public sticker sets that correspond to any of the given emoji
    """

    __type__: Literal["searchStickers"] = "searchStickers"
    __returning_type__ = Stickers

    sticker_type: StickerType
    """Type of the stickers to return"""
    emojis: str
    """Space-separated list of emojis to search for"""
    query: str | None = None
    """Query to search for; may be empty to search for emoji only"""
    input_language_codes: list[str] | None = None
    """List of possible IETF language tags of the user's input language; may be empty if unknown"""
    offset: int
    """The offset from which to return the stickers; must be non-negative"""
    limit: int
    """The maximum number of stickers to be returned; 0-100"""
