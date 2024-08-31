from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StickerTypeRegular(BaseType):
    """
    The sticker is a regular sticker
    """

    __type__: Literal["stickerTypeRegular"] = "stickerTypeRegular"
