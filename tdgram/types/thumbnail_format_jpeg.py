from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ThumbnailFormatJpeg(BaseType):
    """
    The thumbnail is in JPEG format
    """

    __type__: Literal["thumbnailFormatJpeg"] = "thumbnailFormatJpeg"
