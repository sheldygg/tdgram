from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Stickers
from .base import BaseMethod


@dataclass(kw_only=True)
class GetCustomEmojiStickers(BaseMethod):
    """
    Returns the list of custom emoji stickers by their identifiers. Stickers are returned in arbitrary order. Only found stickers are returned
    """

    __type__: Literal["getCustomEmojiStickers"] = "getCustomEmojiStickers"
    __returning_type__ = Stickers

    custom_emoji_ids: list[int]
    """Identifiers of custom emoji stickers. At most 200 custom emoji stickers can be received simultaneously"""
