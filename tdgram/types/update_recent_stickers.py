from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateRecentStickers(BaseType):
    """
    The list of recently used stickers was updated
    """

    __type__: Literal["updateRecentStickers"] = "updateRecentStickers"

    is_attached: bool
    """True, if the list of stickers attached to photo or video files was updated; otherwise, the list of sent stickers is updated"""
    sticker_ids: list[int]
    """The new list of file identifiers of recently used stickers"""
