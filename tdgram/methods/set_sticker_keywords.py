from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputFile, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetStickerKeywords(BaseMethod):
    """
    Changes the list of keywords of a sticker. The sticker must belong to a regular or custom emoji sticker set that is owned by the current user
    """

    __type__: Literal["setStickerKeywords"] = "setStickerKeywords"
    __returning_type__ = Ok

    sticker: InputFile
    """Sticker"""
    keywords: list[str]
    """List of up to 20 keywords with total length up to 64 characters, which can be used to find the sticker"""
