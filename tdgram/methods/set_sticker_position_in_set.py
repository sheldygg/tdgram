from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputFile, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetStickerPositionInSet(BaseMethod):
    """
    Changes the position of a sticker in the set to which it belongs. The sticker set must be owned by the current user
    """

    __type__: Literal["setStickerPositionInSet"] = "setStickerPositionInSet"
    __returning_type__ = Ok

    sticker: InputFile
    """Sticker"""
    position: int
    """New position of the sticker in the set, 0-based"""
