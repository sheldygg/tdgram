from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputFile, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class AddFavoriteSticker(BaseMethod):
    """
    Adds a new sticker to the list of favorite stickers. The new sticker is added to the top of the list. If the sticker was already in the list, it is removed from the list first.
    """

    __type__: Literal["addFavoriteSticker"] = "addFavoriteSticker"
    __returning_type__ = Ok

    sticker: InputFile
    """Sticker file to add"""
