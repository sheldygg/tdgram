from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ThumbnailFormatGif(BaseType):
    """
    The thumbnail is in static GIF format. It will be used only for some bot inline query results
    """

    __type__: Literal["thumbnailFormatGif"] = "thumbnailFormatGif"
