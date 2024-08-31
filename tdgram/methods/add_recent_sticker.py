from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputFile, Stickers
from .base import BaseMethod


@dataclass(kw_only=True)
class AddRecentSticker(BaseMethod):
    """
    Manually adds a new sticker to the list of recently used stickers. The new sticker is added to the top of the list. If the sticker was already in the list, it is removed from the list first.
    """

    __type__: Literal["addRecentSticker"] = "addRecentSticker"
    __returning_type__ = Stickers

    is_attached: bool
    """Pass true to add the sticker to the list of stickers recently attached to photo or video files; pass false to add the sticker to the list of recently sent stickers"""
    sticker: InputFile
    """Sticker file to add"""
