from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from ..types import InputFile, MaskPosition, Ok
from .base import BaseMethod


@dataclass(kw_only=True)
class SetStickerMaskPosition(BaseMethod):
    """
    Changes the mask position of a mask sticker. The sticker must belong to a mask sticker set that is owned by the current user
    """

    __type__: Literal["setStickerMaskPosition"] = "setStickerMaskPosition"
    __returning_type__ = Ok

    sticker: InputFile
    """Sticker"""
    mask_position: MaskPosition | None = None
    """Position where the mask is placed; pass null to remove mask position"""
