from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Emojis, InputFile
from .base import BaseMethod


@dataclass(kw_only=True)
class GetStickerEmojis(BaseMethod):
    """
    Returns emoji corresponding to a sticker. The list is only for informational purposes, because a sticker is always sent with a fixed emoji from the corresponding Sticker object
    """

    __type__: Literal["getStickerEmojis"] = "getStickerEmojis"
    __returning_type__ = Emojis

    sticker: InputFile
    """Sticker file identifier"""
