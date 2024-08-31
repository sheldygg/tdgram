from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ThumbnailFormatTgs(BaseType):
    """
    The thumbnail is in TGS format. It will be used only for sticker sets
    """

    __type__: Literal["thumbnailFormatTgs"] = "thumbnailFormatTgs"
