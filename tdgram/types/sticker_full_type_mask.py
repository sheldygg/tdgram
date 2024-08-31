from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

from .base import BaseType

if TYPE_CHECKING:
    from . import MaskPosition


@dataclass(kw_only=True)
class StickerFullTypeMask(BaseType):
    """
    The sticker is a mask in WEBP format to be placed on photos or videos
    """

    __type__: Literal["stickerFullTypeMask"] = "stickerFullTypeMask"

    mask_position: MaskPosition | None = None
    """Position where the mask is placed; may be null"""
