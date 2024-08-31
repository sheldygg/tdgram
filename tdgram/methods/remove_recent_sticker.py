from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputFile, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RemoveRecentSticker(BaseMethod):
    """
    Removes a sticker from the list of recently used stickers
    """

    __type__: Literal["removeRecentSticker"] = "removeRecentSticker"
    __returning_type__ = Ok

    is_attached: bool
    """Pass true to remove the sticker from the list of stickers recently attached to photo or video files; pass false to remove the sticker from the list of recently sent stickers"""
    sticker: InputFile
    """Sticker file to delete"""
