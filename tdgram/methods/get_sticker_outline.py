from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import Outline
from .base import BaseMethod


@dataclass(kw_only=True)
class GetStickerOutline(BaseMethod):
    """
    Returns outline of a sticker; this is an offline request. Returns a 404 error if the outline isn't known
    """

    __type__: Literal["getStickerOutline"] = "getStickerOutline"
    __returning_type__ = Outline

    sticker_file_id: int
    """File identifier of the sticker"""
    for_animated_emoji: bool
    """Pass true to get the outline scaled for animated emoji"""
    for_clicked_animated_emoji_message: bool
    """Pass true to get the outline scaled for clicked animated emoji message"""
