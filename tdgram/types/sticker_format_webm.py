from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class StickerFormatWebm(BaseType):
    """
    The sticker is a video in WEBM format
    """

    __type__: Literal["stickerFormatWebm"] = "stickerFormatWebm"
