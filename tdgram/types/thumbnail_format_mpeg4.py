from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ThumbnailFormatMpeg4(BaseType):
    """
    The thumbnail is in MPEG4 format. It will be used only for some animations and videos
    """

    __type__: Literal["thumbnailFormatMpeg4"] = "thumbnailFormatMpeg4"
