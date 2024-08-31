from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StickerTypeMask(BaseType):
    """
    The sticker is a mask in WEBP format to be placed on photos or videos
    """

    __type__: Literal["stickerTypeMask"] = "stickerTypeMask"
