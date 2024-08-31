from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Stickers
from .base import BaseMethod


@dataclass(kw_only=True)
class GetDefaultBackgroundCustomEmojiStickers(BaseMethod):
    """
    Returns default list of custom emoji stickers for reply background
    """

    __type__: Literal["getDefaultBackgroundCustomEmojiStickers"] = (
        "getDefaultBackgroundCustomEmojiStickers"
    )
    __returning_type__ = Stickers
