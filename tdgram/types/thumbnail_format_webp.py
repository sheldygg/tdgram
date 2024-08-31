from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ThumbnailFormatWebp(BaseType):
    """
    The thumbnail is in WEBP format. It will be used only for some stickers and sticker sets
    """

    __type__: Literal["thumbnailFormatWebp"] = "thumbnailFormatWebp"
