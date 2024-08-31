from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .base import BaseType


@dataclass(kw_only=True)
class ThumbnailFormatPng(BaseType):
    """
    The thumbnail is in PNG format. It will be used only for background patterns
    """

    __type__: Literal["thumbnailFormatPng"] = "thumbnailFormatPng"
