from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputFile, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RemoveFavoriteSticker(BaseMethod):
    """
    Removes a sticker from the list of favorite stickers
    """

    __type__: Literal["removeFavoriteSticker"] = "removeFavoriteSticker"
    __returning_type__ = Ok

    sticker: InputFile
    """Sticker file to delete from the list"""
