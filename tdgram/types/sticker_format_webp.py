from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StickerFormatWebp(BaseType):
    """
    The sticker is an image in WEBP format
    """

    __type__: Literal["stickerFormatWebp"] = "stickerFormatWebp"
