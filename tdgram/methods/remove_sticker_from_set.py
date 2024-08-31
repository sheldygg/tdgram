from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputFile, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class RemoveStickerFromSet(BaseMethod):
    """
    Removes a sticker from the set to which it belongs. The sticker set must be owned by the current user
    """

    __type__: Literal["removeStickerFromSet"] = "removeStickerFromSet"
    __returning_type__ = Ok

    sticker: InputFile
    """Sticker to remove from the set"""
