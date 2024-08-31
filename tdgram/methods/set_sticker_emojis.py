from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputFile, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetStickerEmojis(BaseMethod):
    """
    Changes the list of emojis corresponding to a sticker. The sticker must belong to a regular or custom emoji sticker set that is owned by the current user
    """

    __type__: Literal["setStickerEmojis"] = "setStickerEmojis"
    __returning_type__ = Ok

    sticker: InputFile
    """Sticker"""
    emojis: str
    """New string with 1-20 emoji corresponding to the sticker"""
