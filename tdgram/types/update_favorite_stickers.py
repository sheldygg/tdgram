from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class UpdateFavoriteStickers(BaseType):
    """
    The list of favorite stickers was updated
    """

    __type__: Literal["updateFavoriteStickers"] = "updateFavoriteStickers"

    sticker_ids: list[int]
    """The new list of file identifiers of favorite stickers"""
